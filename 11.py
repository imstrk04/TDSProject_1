
import pandas as pd

def calculate_correlation_projects_wiki(repositories_csv_path='repositories.csv'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(repositories_csv_path)

    # Ensure 'has_projects' and 'has_wiki' are treated as boolean
    df['has_projects'] = df['has_projects'].astype(int)  # 1 for True, 0 for False
    df['has_wiki'] = df['has_wiki'].astype(int)          # 1 for True, 0 for False

    # Calculate the correlation
    correlation = df['has_projects'].corr(df['has_wiki'])

    return round(correlation, 3)

# Calculate the correlation
result = calculate_correlation_projects_wiki()
print(f"Correlation between projects and wiki enabled: {result}")
