import pandas as pd

# Read the existing CSV file
input_file = 'all_data.csv'  # Replace with your CSV file name
output_file = 'malignant_only_data.csv'  # Output file with only "Malignant" rows

# Load the CSV into a DataFrame
df = pd.read_csv(input_file)

# Filter the DataFrame to keep only rows where 'Type' is 'Malignant'
filtered_df = df[df['Type'] == 'Malignant']

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered CSV file '{output_file}' created successfully.")
