# Tech M&A Knowledge Graph – Milestone 1

## Project Overview
This project aims to design a knowledge graph representing technology mergers and acquisitions (M&A).  
Milestone 1 focuses on dataset preparation, preprocessing, and conceptual schema design.

---

## Dataset
The project uses a technology M&A dataset consisting of:

- Acquisitions.csv
- Acquiring Tech Companies.csv
- Acquired Tech Companies.csv

- Total records: 1643 acquisition events.

These datasets capture acquisition events and company-level metadata.

---

## Data Preprocessing

The following preprocessing steps were performed:

- Duplicate removal
- Whitespace normalization in company names
- Handling of placeholder and missing values
- Standardization of date formats
- Creation of an enriched `Decade` feature

The cleaned dataset is now structured and ready for graph modeling.

---

## Knowledge Graph Schema

The graph models:

- **Company** as the primary node type
- **ACQUIRED** as a directed relationship between companies

Acquisition details (year, price, status, terms) are stored as relationship properties.

Full schema details are available in:
`docs/schema.md`

---

## Next Steps

In the next milestone:
- Neo4j graph instantiation
- Cypher-based data loading
- Query development and graph validation
