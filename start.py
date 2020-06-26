import mysql.connector

# import all table specific scripts
from mss import mss
from boxingleavesdate import boxingleavesdate # 1-0-boaxingleavesdate

mydb = mysql.connector.connect(
    host="localhost",
    user="stcathpython",
    password="stcathpython",
    database="catherine-no-lists"
)
cursor = mydb.cursor()
cursorupdate = mydb.cursor(buffered=True)
namespace = "https://data.ligatus.org.uk/stcatherines/ms/"

mss.mss(mydb, cursor, cursorupdate)
boxingleavesdate.boxingleavesdate(mydb, cursor, cursorupdate)