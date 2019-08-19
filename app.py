import pandas
from geopy.geocoders import ArcGIS

df1 = pandas.read_csv("supermarket.csv")
df2 = pandas.read_json("supermarkets.json")

df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)

df4 = pandas.read_csv("supermarkets_commas.txt")  # Comma is the default separator
df5 = pandas.read_csv("supermarkets_semi-colons.txt", sep=";")  # Because the default is a comma

# To add columns, just be like df6.columns = ["ID", "Something"]

# To get value from csv:

df9 = df5.set_index("ID")  # Needs to be saved as a new variable unless you make inplace parameter to True

df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")
df7.set_index("Address")
val = df7.loc["332 Hill Str", "Country"]

another_val = df7.iloc[1:4, 1:4]  # First by rows, then by columns

df7.drop("332 Hill Str", 0)  # If row, 0; if column, then 1

df7.drop(df7.index[0:3], 1)  # Deletes rows
df7.drop(df7.columns[0:3], 1)  # Deletes columns

df7["Continent"] = df7.shape[0] * ["North America"]  # A column called Continent populated with North America
df7["Continent"] = df7["Country"] + "," + " North America"

# In order to add rows, you need to transverse and then add columns. Then re-transverse to normal

df7_t = df7.T
df7_t["My Address"] = ["My City", "My Country", 10, 7, "Shop", "My state", "My continent"]
df7 = df7_t

nom = ArcGIS()
nom.geocode()
