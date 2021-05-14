import pandas as pd
from time import sleep
df = pd.read_csv("C:\\Users\\Karna\\dataset.csv")
for row_i in range(0,len(df)):
   print(df.iloc[row_i])
   #print()
   #sleep(5)
df1 = (df.iloc[row_i])
html=df1.to_html()
text_file = open("index.html","w")
text_file.write(html)
text_file.close()
