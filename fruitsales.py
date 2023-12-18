#Import Pandas
import pandas as pd

#Create Dataframe
fruit_sales = pd.DataFrame({'Apples':[35,41], 'Bananas':[21,34]}, index =['2017 Sales', '2018 Sales'])

#Write to csv file
fruit_sales.to_csv("fruit.csv")
