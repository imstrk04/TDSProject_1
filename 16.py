import pandas as pd
from collections import Counter

def find_most_common_surname(users_csv_path='users.csv'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(users_csv_path)

    # Debug: Check the initial structure of the DataFrame
    print("Initial DataFrame:")
    print(df.head())
    
    # Initialize a list to store surnames
    surnames = []

    # Process each user's name
    for name in df['name'].dropna():  # Ignore missing names
        trimmed_name = name.strip()     # Trim whitespace
        if trimmed_name:  # Ensure the name is not empty
            # Split the name by whitespace and get the last word as the surname
            parts = trimmed_name.split()
            surname = parts[-1]  # Last word
            surnames.append(surname)

    # Debug: Check the extracted surnames
    print(f"Extracted surnames (first 10): {surnames[:10]}")  # Show first 10 for inspection

    # Count the occurrences of each surname
    surname_counts = Counter(surnames)

    # Find the maximum count value
    if surname_counts:
        max_count = max(surname_counts.values())
        
        # Get all surnames that have the maximum count
        most_common_surnames = [surname for surname, count in surname_counts.items() if count == max_count]
        
        # Sort the surnames alphabetically
        most_common_surnames.sort()
        
        # Debug: Show the count of each surname
        print("Surname counts:")
        for surname, count in surname_counts.items():
            print(f"{surname}: {count}")

        return ', '.join(most_common_surnames)
    else:
        return "No surnames found."

# Calculate the most common surname
result = find_most_common_surname()
print(f"Most common surname(s): {result}")
