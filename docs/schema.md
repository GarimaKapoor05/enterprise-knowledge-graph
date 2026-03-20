# Knowledge Graph Schema – Tech M&A Dataset

## Overview
This schema represents technology company mergers and acquisitions.
The graph models companies as nodes and acquisition events as relationships.
Note: A Person node (founders, board members) is planned for Milestone 2.
---

## Node Types

### 1. Company

Represents both acquiring and acquired technology companies.

**Properties:**
- name (string)
- year_founded (integer)
- market_categories (string)
- country (string)
- city (string)
- description (string)
- homepage (string)
- twitter (string)
- total_funding (integer)
- number_of_employees (string)

---

## Relationship Types

### 1. ACQUIRED

Represents an acquisition event between two companies.

**Direction:**
(Acquiring Company) → (Acquired Company)

**Properties:**
- acquisition_id (string)
- year (integer)
- price (string)
- status (string)
- terms (string)

---

## Graph Structure

(:Company)-[:ACQUIRED {year, price, status}]->(:Company)

---

## Data Source Mapping

| CSV File | Graph Component |
|----------|-----------------|
| Acquisitions.csv | ACQUIRED relationship |
| Acquiring Tech Companies.csv | Company node (acquirer) |
| Acquired Tech Companies.csv | Company node (target) |

---

## Planned Graph Creation (Neo4j Representation)

**The following Cypher structure will be used in the next milestone to instantiate the designed schema in Neo4j.**
```cypher
CREATE (acquirer:Company {name: "Microsoft"})
CREATE (target:Company {name: "LinkedIn"})

CREATE (acquirer)-[:ACQUIRED {
    acquisition_id: "A123",
    year: 2016,
    price: "$26B",
    status: "Completed",
    terms: "Cash"
}]->(target)
```