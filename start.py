import mysql.connector

# import all table specific scripts
from mss import mss
from boxingleavesdate import boxingleavesdate # 1-0-boaxingleavesdate
from openingcharacteristics import openingcharacteristics # 1-1-openingcharacteristics
from pagemarkers import pagemarkers # 1-2-PageMarkers and PageMarkers

mydb = mysql.connector.connect(
    host="localhost",
    user="stcathpython",
    password="stcathpython",
    database="catherine-no-lists"
)
cursor = mydb.cursor(dictionary=True)
cursorupdate = mydb.cursor(buffered=True)
namespace = "https://data.ligatus.org.uk/stcatherines/ms/"

mss.mss(mydb, cursor, cursorupdate)
boxingleavesdate.boxingleavesdate(mydb, cursor, cursorupdate)
openingcharacteristics.openingcharacteristics(mydb, cursor, cursorupdate)
pagemarkers.pagemarkers(mydb, cursor, cursorupdate)