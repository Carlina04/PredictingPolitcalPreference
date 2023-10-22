import pandas as pd

data = pd.read_csv("P-Labelled/robredoLabel.csv")
data2 = pd.read_csv("President-PP/probredoPP.csv")

data["Cleaned"] = data2["0"]

data.to_csv('President-PP/robredoPP.csv')