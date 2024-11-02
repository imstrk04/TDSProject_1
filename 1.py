

import csv

# List to store users in Sydney
users_in_sydney = []

# Open the CSV file and read the data
with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        
        # Check if the user is from Sydney
        if 'sydney' in location:
            users_in_sydney.append({
                'login': row['login'],
                'followers': int(row['followers'])
            })

# Sort users by followers in descending order
top_users = sorted(users_in_sydney, key=lambda x: x['followers'], reverse=True)

# Get the top 5 users' logins
top_5_logins = [user['login'] for user in top_users[:5]]

# Print result as comma-separated list
print(','.join(top_5_logins))
