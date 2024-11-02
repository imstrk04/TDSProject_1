
import pandas as pd

def top_weekend_repo_creators(repositories_csv_path='repositories.csv'):
    # Load the repositories data into a DataFrame
    df = pd.read_csv(repositories_csv_path)

    # Convert the 'created_at' column to datetime
    df['created_at'] = pd.to_datetime(df['created_at'])

    # Filter for weekend repositories (Saturday and Sunday)
    df['day_of_week'] = df['created_at'].dt.dayofweek  # 0 = Monday, 6 = Sunday
    weekend_repos = df[df['day_of_week'].isin([5, 6])]  # 5 = Saturday, 6 = Sunday

    # Count the number of repositories created by each user
    user_repo_counts = weekend_repos['login'].value_counts()

    # Get the top 5 users with the most weekend repositories
    top_users = user_repo_counts.head(5).index.tolist()

    # Return the top 5 users' logins as a comma-separated string
    return ','.join(top_users)

# Calculate the top users
result = top_weekend_repo_creators()
print(f"Top 5 users who created the most repositories on weekends: {result}")
