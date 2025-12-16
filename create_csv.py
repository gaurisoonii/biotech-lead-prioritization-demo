import pandas as pd

# Base lead data (without email & LinkedIn)
data = [
    # HIGH INTENT
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
    },

    #mid range
    {
        "Name": "Dr Ananya Mehta",
        "Title": "Associate Director Toxicology",
        "Company": "BioSyn Labs",
        "Person_Location": "Bangalore",
        "Company_HQ": "Boston",
        "Company_Stage": "Series A",
        "Funded": "Yes",
        "Published_Liver_Paper": "Yes",
        "Conference_Attendee": "No",
        "Uses_InVitro_Tech": "Yes"
    },
    {
        "Name": "Dr Marcus Chen",
        "Title": "Principal Toxicologist",
        "Company": "NovaCure",
        "Person_Location": "Singapore",
        "Company_HQ": "Singapore",
        "Company_Stage": "Series A",
        "Funded": "Yes",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "Yes"
    },
    {
        "Name": "Dr Elena Rossi",
        "Title": "Safety Scientist",
        "Company": "MedPharmX",
        "Person_Location": "Milan",
        "Company_HQ": "Zurich",
        "Company_Stage": "Series A",
        "Funded": "Yes",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "No"
    },
    {
        "Name": "Dr Rahul Verma",
        "Title": "Senior Scientist",
        "Company": "OncoBridge",
        "Person_Location": "Hyderabad",
        "Company_HQ": "San Francisco",
        "Company_Stage": "Seed",
        "Funded": "Yes",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "No",
        "Uses_InVitro_Tech": "Yes"
    },
    {
        "Name": "Dr Sophie Laurent",
        "Title": "Research Scientist",
        "Company": "Cellix Bio",
        "Person_Location": "Paris",
        "Company_HQ": "Paris",
        "Company_Stage": "Seed",
        "Funded": "No",
        "Published_Liver_Paper": "No",
        "Conference_Attendee": "Yes",
        "Uses_InVitro_Tech": "No"
    },

    # LOW INTENT
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
