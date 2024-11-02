import pandas as pd

def analyze_email_sharing(users_csv_path='users.csv'):
    # Load the users data into a DataFrame
    df = pd.read_csv(users_csv_path)

    # Calculate the fraction of hireable users with email addresses
    hireable_with_email = df[df['hireable'] == True]['email'].notnull().mean()
    
    # Calculate the fraction of non-hireable users with email addresses
    non_hireable_with_email = df[df['hireable'] != True]['email'].notnull().mean()
    
    # Calculate the difference rounded to 3 decimal places
    difference = round(hireable_with_email - non_hireable_with_email, 3)
    
    # Print debug information
    print(f"Fraction of hireable users with email: {hireable_with_email:.3f}")
    print(f"Fraction of non-hireable users with email: {non_hireable_with_email:.3f}")
    
    return difference

# Calculate the difference
result = analyze_email_sharing()
print(f"\nDifference in email sharing: {result:.3f}")
