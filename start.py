import mysql.connector
from rdflib import Graph, Namespace, URIRef

# import all table specific scripts
from mss import mss
from boxingleavesdate import boxingleavesdate # 1-0-boaxingleavesdate
from openingcharacteristics import openingcharacteristics # 1-1-openingcharacteristics
from pagemarkers import pagemarkers # 1-2-PageMarkers and PageMarkers
from liftingtabs import liftingtabs # 1-3-liftingTabs, LiftingTabs and LiftingTabsCondition
from bookmarks import bookmarks # 1-4-Bookmarks, Bookmarks, BookmarkMaterials, BookmarkColours
from insertedmaterial import insertedmaterial # 1-5-InsertedMaterial

mydb = mysql.connector.connect(
    host="localhost",
    user="stcathpython",
    password="stcathpython",
    database="catherine-no-lists"
)
cursor = mydb.cursor(dictionary=True)
cursorupdate = mydb.cursor(buffered=True)

#mss.mss(mydb, cursor, cursorupdate)
#boxingleavesdate.boxingleavesdate(mydb, cursor, cursorupdate)
#openingcharacteristics.openingcharacteristics(mydb, cursor, cursorupdate)
#pagemarkers.pagemarkers(mydb, cursor, cursorupdate)
#liftingtabs.liftingtabs(mydb, cursor, cursorupdate)
#bookmarks.bookmarks(mydb, cursor, cursorupdate)
insertedmaterial.insertedmaterial(mydb, cursor, cursorupdate)


