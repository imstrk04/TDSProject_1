import csv
from datetime import datetime

# List to store users from Sydney
users_in_sydney = []

# Read the CSV file with UTF-8 encoding
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        
        # Check if the user is from Sydney
        if 'sydney' in location:
            try:
                # Parse the created_at field
                created_at = datetime.strptime(row['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                users_in_sydney.append({
                    'login': row['login'],
                    'created_at': created_at
                })
            except ValueError:
                continue  # Skip row if date format is invalid

# Sort users by created_at in ascending order
sorted_users = sorted(users_in_sydney, key=lambda x: x['created_at'])

# Extract the top 5 earliest user logins
top_5_earliest_logins = [user['login'] for user in sorted_users[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_earliest_logins))
