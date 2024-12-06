# import pandas as pd

# # File paths for the two Excel files
# file1 = 'all_data.csv'  # Replace with the path to your first file
# file2 = '2nd_set.csv'  # Replace with the path to your second file

# # Load the Excel files into DataFrames
# data1 = pd.read_excel(file1, sheet_name=None)  # Load all sheets as a dictionary
# data2 = pd.read_excel(file2, sheet_name=None)

# # Create a writer for the combined file
# output_file = 'combined.xlsx'  # Name of the output file
# with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
#     # Write all sheets from the first file
#     for sheet_name, df in data1.items():
#         df.to_excel(writer, sheet_name=f'{sheet_name}_file1', index=False)
    
#     # Write all sheets from the second file
#     for sheet_name, df in data2.items():
#         df.to_excel(writer, sheet_name=f'{sheet_name}_file2', index=False)

# print(f"Data from {file1} and {file2} combined into {output_file}")






import pandas as pd

# File paths for the two CSV files
file1 = r'all_data.csv'
file2 = r'2nd_set.csv'

# Read the CSV files
data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

# Combine the two files into one
combined_data = pd.concat([data1, data2], ignore_index=True)

# Save the combined data to a new CSV file
output_file = r'combined.csv'
combined_data.to_csv(output_file, index=False)

print(f"Data from {file1} and {file2} combined into {output_file}")

