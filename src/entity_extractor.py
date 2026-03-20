from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2:3b")

prompt_template = PromptTemplate(
    input_variables=["text"],
    template="""
You are an expert in Named Entity Recognition for business and technology domains.

Extract all companies and their relationships from the text below.
Return ONLY a JSON array, no explanation, no markdown, just raw JSON.

Format:
[
  {{
    "entity1": "Company A",
    "relation": "ACQUIRED",
    "entity2": "Company B"
  }}
]

If no relationships are found, return an empty array: []

Text: {text}
"""
)

def extract_entities(text):
    """
    Extract company entities and relationships from text using Llama3.2.
    Returns a list of dicts with entity1, relation, entity2.
    """
    if not text or text == "Not Available":
        return []

    chain = prompt_template | llm
    result = chain.invoke({"text": text})

    try:
        import json
        # Clean response in case LLM adds extra text
        result = result.strip()
        start = result.find("[")
        end = result.rfind("]") + 1
        json_str = result[start:end]
        return json.loads(json_str)
    except Exception:
        return []
def extract_and_store(graph_builder):
    """
    Fetch company descriptions from Neo4j, extract entities,
    and store any new relationships found back into the graph.
    """
    with graph_builder.driver.session() as session:
        results = session.run(
            "MATCH (c:Company) WHERE c.description <> 'Not Available' RETURN c.name AS name, c.description AS description"
        )
        companies = [(r["name"], r["description"]) for r in results] [:50]

    print(f"Processing {len(companies)} company descriptions...")

    found = 0
    for name, description in companies:
        entities = extract_entities(description)
        for e in entities:
            if e.get("relation") == "ACQUIRED":
                graph_builder.create_acquisition(
                    acquirer=e["entity1"],
                    target=e["entity2"],
                    acquisition_id=f"NER-{e['entity1']}-{e['entity2']}",
                    year=0,
                    price="Unknown",
                    status="NER-Extracted",
                    terms="Unknown"
                )
                found += 1
                print(f"  Extracted: {e['entity1']} → ACQUIRED → {e['entity2']}")

    print(f"\nDone. {found} new relationships extracted and stored.")