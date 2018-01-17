import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine("sqlite:///Chinook.sqlite")

with engine.connect() as con:
	sd = con.execute("SELECT * FROM Orders")
	apanda  = pd.DataFrame(sd.fetchall())

	apanda.columns = sd.keys()

print(sd.head())  



DF = pd.read_sql_query("SELECT FROM * Orders",engine)