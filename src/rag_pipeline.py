from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load LLM
llm = OllamaLLM(model="llama3.2:3b")

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an expert analyst on tech company mergers and acquisitions.

Use the following context from a knowledge graph to answer the question.
If you don't know the answer from the context, say "I don't have enough information."

Context:
{context}

Question: {question}

Answer:
"""
)


def build_vector_store(neo4j_driver):
    """
    Fetch company descriptions from Neo4j and build a FAISS vector store.
    Returns the index, and the list of (name, description) pairs.
    """
    with neo4j_driver.session() as session:
        results = session.run(
            """
            MATCH (c:Company)
            WHERE c.description <> 'Not Available'
            RETURN c.name AS name, c.description AS description
            """
        )
        companies = [(r["name"], r["description"]) for r in results]

    print(f"Building vector store from {len(companies)} company descriptions...")

    descriptions = [desc for _, desc in companies]
    embeddings = embedder.encode(descriptions, show_progress_bar=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    print(f"Vector store built. {index.ntotal} vectors indexed.")
    return index, companies


def retrieve_context(query, index, companies, top_k=5):
    """
    Retrieve top_k most similar companies to the query.
    Returns a formatted context string.
    """
    query_embedding = embedder.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    context_parts = []
    for i in indices[0]:
        name, description = companies[i]
        context_parts.append(f"Company: {name}\nDescription: {description}")

    return "\n\n".join(context_parts)


def answer_question(query, index, companies):
    """
    Full RAG pipeline - retrieve context then generate answer.
    """
    context = retrieve_context(query, index, companies)
    chain = prompt_template | llm
    answer = chain.invoke({"context": context, "question": query})
    return answer, context