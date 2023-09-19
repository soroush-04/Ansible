
import pandas as pd

# Load the CSV file into a Pandas DataFrame
input_file = "assignment data.csv"
output_file = "filtered-sales-data.csv"


# Assuming the CSV columns are in the following order: property_id, price, square_feet
df = pd.read_csv(input_file)

print(df.columns.tolist())

# # Calculate the price per square foot and add it as a new column
df['price_per_sqft'] = df['price'] / df['sq__ft']

# Calculate the average price per square foot
average_price_per_sqft = df['price_per_sqft'].mean()

# Filter rows where the property's price per square foot is less than the average
filtered_df = df[df['price_per_sqft'] < average_price_per_sqft]

# Drop the 'price_per_sqft' column if you don't need it in the output
filtered_df = filtered_df.drop(columns=['price_per_sqft'])

# Save the filtered data to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been written to {output_file}")
