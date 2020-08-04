import mysql.connector
from rdflib import Graph, Namespace, URIRef

# import all table specific scripts
from mss import mss
from boxingleavesdate import boxingleavesdate # 1-0-boaxingleavesdate
from openingcharacteristics import openingcharacteristics # 1-1-openingcharacteristics
from pagemarkers import pagemarkers # 1-2-PageMarkers and PageMarkers
from html import escape

mydb = mysql.connector.connect(
    host="localhost",
    user="stcathpython",
    password="stcathpython",
    database="catherine-no-lists"
)
cursor = mydb.cursor(dictionary=True)
cursorupdate = mydb.cursor(buffered=True)
#namespace = escape("https://data.ligatus.org.uk/stcatherines/ms/")

graph = Graph()
# add Ligatus's namespace
STCATH = Namespace('https://data.ligatus.org.uk/stcatherines/ms/')
graph.bind('stcath', STCATH)
# add CIDOC-CRM's namespace and prefix
CRM = Namespace('http://www.cidoc-crm.org/cidoc-crm/')
graph.bind('crm', CRM)

mss.mss(mydb, cursor, cursorupdate, graph, STCATH, CRM)
#boxingleavesdate.boxingleavesdate(mydb, cursor, cursorupdate, namespace, graph, CRM)
#openingcharacteristics.openingcharacteristics(mydb, cursor, cursorupdate, namespace, graph, CRM)
#pagemarkers.pagemarkers(mydb, cursor, cursorupdate, namespace, graph, CRM)

graph.serialize(destination='output.ttl', format='turtle', encoding="utf-8")