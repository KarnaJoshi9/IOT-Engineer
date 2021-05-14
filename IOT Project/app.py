from flask import Flask , render_template
import pandas as pd
from time import sleep
app=Flask(__name__)
@app.route("/")
def home():
    data = pd.read_csv("C:\\Users\\Karna\\dataset.csv")
    print(data.shape[0])
    for row_i in range(0, data.shape[0]):
        print(data.iloc[row_i])
        print()
        #value_df=df.iloc[0]
        #print("value_data",value_df)
        return render_template("index.html")

app.run(debug=True)
