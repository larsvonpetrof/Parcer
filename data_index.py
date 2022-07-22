# Data indexes via Pandas
import pandas as pd
data = pd.read_csv(
    "https://video.ittensive.com/python-advanced/internet-2017.csv", \
                   na_values="NA", 
                  decimal = ",",
                skiprows=1,
                names=["Region", "2017"]#,
#                index_col="Region"
)
#data_indexed = pd.Series(data["2017"].values, index=data["Region"].values)
#print(data_indexed)
#data = data.reset_index()
data.head()

#Find all regions contain "округ"
area_indexes = data[data["Region"].str.contains("округ")].index
print(area_indexes)
