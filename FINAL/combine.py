import pandas as pd

data = pd.read_csv("Testing/VPs/sottoLabel.csv")
data2 = pd.read_csv("VP/sottoPP.csv")

data["Cleaned"] = data2["0"]

data.to_csv('VP-PreProcessed/sottoPP.csv')