import pandas as pd

df = pd.read_csv("hong_df.csv")
print(df)

import pymysql
from sqlalchemy import create_engine


pymysql.install_as_MySQLdb()
import MySQLdb


engine = create_engine("mysql+mysqldb://root:160813@localhost:3307/sample_db", encoding='utf-8')
conn = engine.connect()

df.to_sql(name='latlon', con=engine, if_exists='append', index=False)
conn.close()