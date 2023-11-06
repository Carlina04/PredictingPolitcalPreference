import pandas as pd

# Read each CSV file
df1 = pd.read_csv('President-PP/marcosPP.csv')
df2 = pd.read_csv('President-PP/pacquiaoPP.csv')
df3 = pd.read_csv('President-PP/robredoPP.csv')
df4 = pd.read_csv('VP-PreProcessed/dutertePP.csv')
df5 = pd.read_csv('VP-PreProcessed/pangilinanPP.csv')

# Combine dataframes into one
combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Write to a new CSV file
combined_df.to_csv('ph_elections.csv', index=False)
