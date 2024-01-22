import os; os.makedirs("plotting_results", exist_ok=True)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("src/merged_data.csv")

df["Percentage_change"] = (df["Product Price before Discount"]-df["Product Price"])/df["Product Price before Discount"]
#df.fillna(0, inplace=True) - jezeli wypełnimy puste wiersze 0 to uzyskamy od na pytanie 'Które typy produktów sklep lubi przeceniać najbardziej?' Bez tego omawiamy tylko produkty przecenione (nieprzecenione nie są brane w kolejnych obliczeniach)

df=df.groupby("Product Type").agg({"Percentage_change":['mean', 'count']}).reset_index()
df.columns = ['Product_Type', 'Mean_Percentage_change', 'Product_Count']
print(df)
#1.1
sns.barplot(data=df[df["Mean_Percentage_change"]<=0.2].sort_values("Mean_Percentage_change"), x="Product_Type", y="Mean_Percentage_change",
            hue="Product_Type", palette="rocket")
plt.show()
#1.2 dzięki count>10 pokazujemy czy warto wybrać się do tego sklepu na zakupy (gdy count jest np 1, 2, 3... to znaczy ze jest tak mało pdoruktów ze ciezko bedzie cos kupic mimo duzych obnizek)
sns.barplot(data=df[(df["Mean_Percentage_change"]<=0.2) & (df["Product_Count"]>=10)].sort_values("Mean_Percentage_change"), x="Product_Type", y="Mean_Percentage_change",
            hue="Product_Type", palette="rocket")
plt.show()

#2.1
sns.barplot(data=df[df["Mean_Percentage_change"]>=3/10].sort_values("Mean_Percentage_change", ascending=False), x="Product_Type", y="Mean_Percentage_change",
            hue="Product_Type", palette="rocket")
plt.show()
#2.2 same like 1.2
sns.barplot(data=df[(df["Mean_Percentage_change"]>=3/10) & (df["Product_Count"]>=10)].sort_values("Mean_Percentage_change", ascending=False), x="Product_Type", y="Mean_Percentage_change",
            hue="Product_Type", palette="rocket")
plt.show()



