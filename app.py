import streamlit as st
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="3D In-Vitro Lead Qualification Dashboard",
    layout="wide"
)

st.title("3D In-Vitro Lead Qualification Dashboard")
st.caption(
    "Identify, enrich, and rank life-science professionals by likelihood of working with 3D in-vitro models."
)

# -----------------------------
# LOAD CSV
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("leads.csv")

df = load_data()

# -----------------------------
# ENSURE REQUIRED COLUMNS
# -----------------------------
# If Work_Mode not present, infer it
if "Work_Mode" not in df.columns:
    def infer_work_mode(location):
        if "Remote" in str(location):
            return "Remote"
        return "Onsite"

    df["Work_Mode"] = df["Person_Location"].apply(infer_work_mode)

# -----------------------------
# SCORING LOGIC (×5 BUCKETS)
# -----------------------------
def round_to_5(x):
    return int(5 * round(x / 5))


def calculate_score(role, domain, has_3d_signal, company_stage, decision_maker):
    score = 0

    role_scores = {
        "VP": 30,
        "Head": 30,
        "Director": 25,
        "Associate Director": 20,
        "Principal": 15,
        "Senior Scientist": 15,
        "Scientist": 10,
        "Junior": 5
    }
    for key in role_scores:
        if key.lower() in role.lower():
            score += role_scores[key]
            break

    score += {"High": 25, "Medium": 15, "Low": 5}[domain]
    score += {"Strong": 25, "Indirect": 15, "None": 0}[has_3d_signal]
    score += {
        "Public": 10,
        "Series C": 10,
        "Series B": 10,
        "Series A": 5,
        "Seed": 0
    }.get(company_stage, 0)

    if decision_maker:
        score += 10

    # 🔥 THIS LINE FIXES EVERYTHING
    return min(round_to_5(score), 100)


# -----------------------------
# MAP CSV → SCORING SIGNALS
# -----------------------------
def map_domain(row):
    return "High" if row["Published_Liver_Paper"] == "Yes" else "Low"

def map_3d_signal(row):
    if row["Uses_InVitro_Tech"] == "Yes":
        return "Strong"
    elif row["Conference_Attendee"] == "Yes":
        return "Indirect"
    return "None"

def is_decision_maker(title):
    keywords = ["VP", "Head", "Director", "Associate Director"]
    return any(k.lower() in title.lower() for k in keywords)

df["domain"] = df.apply(map_domain, axis=1)
df["has_3d_signal"] = df.apply(map_3d_signal, axis=1)
df["decision_maker"] = df["Title"].apply(is_decision_maker)

# -----------------------------
# CALCULATE SCORES
# -----------------------------
df["probability_score"] = df.apply(
    lambda row: calculate_score(
        role=row["Title"],
        domain=row["domain"],
        has_3d_signal=row["has_3d_signal"],
        company_stage=row["Company_Stage"],
        decision_maker=row["decision_maker"]
    ),
    axis=1
)

df["score_band"] = df["probability_score"].apply(
    lambda x: "🔥 Hot" if x >= 80 else "⚡ Warm" if x >= 50 else "❄️ Cold"
)

df = df.sort_values("probability_score", ascending=False).reset_index(drop=True)
df["rank"] = df.index + 1

# -----------------------------
# KPI SUMMARY
# -----------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Leads", len(df))
col2.metric("Qualified (70+)", len(df[df["probability_score"] >= 70]))
col3.metric("Avg Score", round(df["probability_score"].mean(), 1))
col4.metric("Top Region", df["Company_HQ"].mode()[0])

st.divider()

# -----------------------------
# FILTERS
# -----------------------------
with st.sidebar:
    st.header("Filters")
    min_score = st.slider("Minimum Score", 0, 100, 0)
    role_filter = st.multiselect(
        "Role contains",
        ["VP", "Head", "Director", "Associate", "Principal", "Senior", "Scientist"]
    )
    work_mode_filter = st.multiselect(
        "Work Mode",
        df["Work_Mode"].unique()
    )
    decision_only = st.checkbox("Decision-makers only")

filtered = df[df["probability_score"] >= min_score]

if role_filter:
    filtered = filtered[filtered["Title"].str.contains("|".join(role_filter), case=False)]

if work_mode_filter:
    filtered = filtered[filtered["Work_Mode"].isin(work_mode_filter)]

if decision_only:
    filtered = filtered[filtered["decision_maker"]]

# -----------------------------
# TABLE DISPLAY
# -----------------------------
st.subheader("Ranked Leads")
st.dataframe(
    filtered[[
        "rank",
        "probability_score",
        "score_band",
        "Name",
        "Title",
        "Company",
        "Email",
        "Work_Mode",
        "Person_Location",
        "Company_HQ"
    ]],
    use_container_width=True
)

# -----------------------------
# DOWNLOAD
# -----------------------------
st.download_button(
    "⬇ Download Leads (CSV)",
    filtered.to_csv(index=False),
    file_name="qualified_leads.csv",
    mime="text/csv"
)

st.caption("Demo data • CSV-driven • Explainable rule-based scoring (×5 buckets)")
