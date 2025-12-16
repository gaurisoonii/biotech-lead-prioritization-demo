import pandas as pd

# Base lead data (without email & LinkedIn)
data = [
    {
        "Name": "Dr Alice Smith",
        "Title": "Director of Toxicology",
        "Company": "BioGenX",
        "Person_Location": "Boston",
        "Company_HQ": "Cambridge",
        "Company_Stage": "Series B",
        "Funded": "Yes",
        "Published_Liver_Paper": "Yes",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "Yes"
    },
    {
        "Name": "Dr Bob Jones",
        "Title": "Senior Scientist",
        "Company": "HealthStart",
        "Person_Location": "Texas",
        "Company_HQ": "San Diego",
        "Company_Stage": "Seed",
        "Funded": "No",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "No",
        "Uses_InVitro_Tech": "No"
    },
    {
        "Name": "Dr Carol White",
        "Title": "Head of Preclinical Safety",
        "Company": "LiverTech",
        "Person_Location": "Remote CO",
        "Company_HQ": "Boston",
        "Company_Stage": "Series A",
        "Funded": "Yes",
        "Published_Liver_Paper": "Yes",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "Yes"
    },
    {
        "Name": "Dr David Brown",
        "Title": "Junior Scientist",
        "Company": "EarlyBio",
        "Person_Location": "New York",
        "Company_HQ": "New York",
        "Company_Stage": "Seed",
        "Funded": "No",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "No",
        "Uses_InVitro_Tech": "No"
    },
    {
        "Name": "Dr Emma Green",
        "Title": "VP Safety Assessment",
        "Company": "OncoNova",
        "Person_Location": "Basel",
        "Company_HQ": "Basel",
        "Company_Stage": "Public",
        "Funded": "Yes",
        "Published_Liver_Paper": "Yes",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "Yes"
    }
]

df = pd.DataFrame(data)

# ---------- AUTO-GENERATION LOGIC ----------

def clean_name(name):
    return name.replace("Dr ", "").lower().replace(" ", ".")

def clean_company(company):
    return company.lower().replace(" ", "")

df["Email"] = df.apply(
    lambda row: f"{clean_name(row['Name'])}@{clean_company(row['Company'])}.com",
    axis=1
)

df["LinkedIn"] = df.apply(
    lambda row: f"https://linkedin.com/in/{clean_name(row['Name'])}",
    axis=1
)

# ------------------------------------------

df.to_csv("leads.csv", index=False)

print("leads.csv file created successfully")
