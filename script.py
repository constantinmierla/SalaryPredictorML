import pandas as pd

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than a Bachelor’s degree'

# Load and process the data
df = pd.read_csv("survey_results_public.csv")
df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
df = df[df["ConvertedCompYearly"].notnull()]
df = df.dropna()
df = df[df["Employment"] == "Employed, full-time"]
df = df.drop("Employment", axis=1)

country_map = shorten_categories(df.Country.value_counts(), 80)
df['Country'] = df['Country'].map(country_map)
df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
df = df[df["Salary"] <= 250000]
df = df[df["Salary"] >= 10000]
df = df[df['Country'] != 'Other']

df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
df['EdLevel'] = df['EdLevel'].apply(clean_education)

# Save the cleaned data
df.to_csv("cleaned_survey_results.csv", index=False)
print(f"Cleaned data saved with {len(df)} rows and {len(df.columns)} columns")