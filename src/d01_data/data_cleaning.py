import pandas as pd

# Path for datas
survey_path = "./data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx"
data_analyst_path = "./data/01_raw/DataAnalyst.csv"

survey_df = pd.read_excel(survey_path, skiprows=2)

# Get datas only from United State
survey_df = survey_df[survey_df.Country == "United States"]
# Keep only revelant column
survey_df = survey_df[
    ["SalaryUSD",
     "PostalCode",
     "Gender",
     "EmploymentStatus",
     "JobTitle",
     "YearsWithThisTypeOfJob",
     "HowManyCompanies",
     "OtherPeopleOnYourTeam"]
]


# Set "Gender" = "Other" if it is not male or female"
survey_df.loc[~survey_df["Gender"].isin(["Male", "Female"]), "Gender"] = "Other - NA"
    
# Group all DBA jobs
survey_df["JobTitle"] = survey_df["JobTitle"].apply(
    lambda x: "Database Admin" if x.startswith('DBA') else x
)
# Group all Developer jobs
survey_df["JobTitle"] = survey_df["JobTitle"].apply(
    lambda x: "Developer" if x.startswith('Developer') else x
)

#affichage simplifié des valeurs dans HowManyCompanies
survey_df["HowManyCompanies"] = survey_df["HowManyCompanies"].apply(
    lambda x: "1" if str(x).startswith('1') else "2" if str(x).startswith('2') else x
)

# s = number of times each job appears
s = survey_df["JobTitle"].value_counts()

# Set "JobTitle" = "Other" if it appears less than 5 times"
survey_df.loc[survey_df["JobTitle"].isin(s[(s < 5)].index), "JobTitle"] = "Other"



survey_df.to_csv("data/02_intermediate/survey_df.csv")


data_analyst_df = pd.read_csv(data_analyst_path, index_col="Unnamed: 0")
data_analyst_df = data_analyst_df[
    ["Job Title",
     "Salary Estimate",
     "Location"]
]


data_analyst_df.to_csv("data/02_intermediate/data_analyst_df.csv")



