
import pandas as pd
import numpy as np

def analyze_bio_impact(users_csv_path='users.csv'):
    # Read the data
    df = pd.read_csv(users_csv_path)

    # Function to count words in the bio
    def count_words(bio):
        if pd.isna(bio):  # Check for NaN
            return 0
        return len(bio.split())

    # Apply the word count function to the 'bio' column
    df['bio_word_count'] = df['bio'].apply(count_words)

    # Filter out users without bios
    filtered_df = df[df['bio_word_count'] > 0]

    # Ensure there is data for regression
    if len(filtered_df) > 1:
        # Perform linear regression: followers ~ bio_word_count
        slope, _ = np.polyfit(filtered_df['bio_word_count'], filtered_df['followers'], 1)
        
        # Return the slope rounded to 3 decimal places
        return round(slope, 3)
    else:
        print("Insufficient data for regression.")
        return None

# Calculate the regression slope
result = analyze_bio_impact()
if result is not None:
    print(f"Regression slope of followers on bio word count: {result:.3f}")
