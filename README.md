# Biotech Lead Prioritization Agent (Demo)

## Overview
This project is a **working demo** of a lead generation and prioritization system designed for **3D in-vitro models used in therapy design**.

The goal is to help Business Development teams **identify, enrich, and rank high-intent biotech professionals**, so outreach can focus on the most promising leads first.

> **Note:** The data in this demo is **mocked**. The objective is to demonstrate **business logic and ranking methodology**, not live scraping.

---

## What This Demo Shows
- Identification of relevant roles (Toxicology, Preclinical Safety, Safety Assessment)
- Enrichment with scientific, commercial, and technographic signals
- A **0–100 propensity-to-buy score** based on weighted criteria
- Automatic re-ranking of leads
- A searchable, exportable dashboard

---

## Scoring Logic (0–100)
Leads are scored using weighted signals:
- Role seniority (Director / Head / VP)
- Recent scientific publications in liver toxicity
- Company funding stage (Series A/B, Public)
- Use of in-vitro / NAM technologies
- Conference participation
- Presence in major biotech hubs (Boston, Basel, etc.)

Scores are capped at **100** and used to rank leads by priority.

---

## Output
The final output is a **Streamlit dashboard** with:
- Ranked leads table
- Person location vs company HQ split
- Programmatically generated email and LinkedIn fields
- CSV export for BD workflows

---

## Tech Stack
- Python
- Pandas
- Streamlit

---

## Project Structure

Project Structure
internship_gauri/

├── app.py  # Streamlit dashboard

├── create_csv.py    # Mock lead data generator

├── leads.csv        # Sample enriched lead data

└── README.md


---

## How to Run
```bash
pip install pandas streamlit
python create_csv.py
python -m streamlit run app.py


Open in browser:

http://localhost:8501

Production Note

In a production setup, identification and enrichment would be automated using sources such as LinkedIn, PubMed, conference sites, and funding databases.
This demo focuses on demonstrating the decision engine and prioritization logic.

Author

Gauri Soni
