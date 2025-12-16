import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Ranking Demo", layout="wide")

st.title("Biotech Lead Prioritization Dashboard")
st.caption("Demo: Identifying & ranking high-intent leads for 3D in-vitro models")

# Load CSV
df = pd.read_csv("leads.csv")

def calculate_score(row):
    score = 0

    # Role fit
    if any(x in row["Title"] for x in ["Director", "Head", "VP"]):
        score += 30

    # Funding
    if row["Funded"] == "Yes":
        score += 20

    # Scientific intent
    if row["Published_Liver_Paper"] == "Yes":
        score += 40

    # Conference activity
    if row["Conference_Attendee"] == "Yes":
        score += 10

    # Technographic signal
    if row["Uses_InVitro_Tech"] == "Yes":
        score += 15

    # Location hubs
    hubs = ["Boston", "Cambridge", "Basel", "San Diego"]
    if any(hub in row["Company_HQ"] for hub in hubs):
        score += 10

    return min(score, 100)


# Calculate & rank
df["Probability_Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values(by="Probability_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

# Filters
st.subheader("Filters")
location_filter = st.text_input("Filter by location or HQ (optional)")

if location_filter:
    df = df[
        df["Person_Location"].str.contains(location_filter, case=False) |
        df["Company_HQ"].str.contains(location_filter, case=False)
    ]

# Display table
st.subheader("Ranked Leads")
st.dataframe(df, use_container_width=True)

# Download button
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Ranked Leads (CSV)",
    csv,
    "ranked_leads.csv",
    "text/csv",
)
