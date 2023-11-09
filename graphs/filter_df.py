import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("graph.csv")

# Define the nodes you want to keep
desired_nodes = ["F", "G", "X", "E"]

# Filter the DataFrame to keep only the rows with the desired nodes
filtered_df = df[df['Start Node'].isin(desired_nodes) & df['End Node'].isin(desired_nodes)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv("filtered_graph_data.csv", index=False)
