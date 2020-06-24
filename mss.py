import mysql.connector
from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

mydb = mysql.connector.connect(
    host="localhost",
    user="stcathpython",
    password="stcathpython",
    database="catherine-no-lists"
)
cursor = mydb.cursor()
cursorupdate = mydb.cursor(buffered=True)
namespace = "https://data.ligatus.org.uk/stcatherines/ms/"

# MSs
collections = []
# Get collections first
cursor.execute("SELECT DISTINCT collection, collectionuuid FROM MSs")
rows = cursor.fetchall()
for row in rows:
    if row[1] is None: #if there is no uuid in the database create one
        newuuid = str(uuid.uuid4())
        collections.append([newuuid, row[0]])
        #update the database
        sql = "UPDATE MSs SET collectionuuid=%s WHERE collection=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else: #just fetch it
        collections.append([row[1], row[0]])

cursor.execute("SELECT * FROM MSs")
rows = cursor.fetchall()
# root for main data
root = etree.Element("root")
# root for prototype document for mapping
prototyperoot = etree.Element("root")
prototypeneeded = True

for row in rows:
    bookelement = etree.Element("book")
    msuuidelement = etree.SubElement(bookelement, "msuuid")
    if row[1] is None: #if there is no msuuid
        newuuid = str(uuid.uuid4())
        msuuidelement.text = newuuid
        # update the database
        sql = "UPDATE MSs SET msuuid=%s WHERE id=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        msuuidelement.text = row[1]
    cataloguenameelement = etree.SubElement(bookelement, "cataloguename")
    cataloguenameuuidelement = etree.SubElement(cataloguenameelement, "cataloguenameuuid")
    if row[6] is None:
        newuuid = str(uuid.uuid4())
        cataloguenameuuidelement.text = newuuid
        # update the database
        sql = "UPDATE MSs SET cataloguenameuuid=%s WHERE id=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        cataloguenameuuidelement.text = row[6]
    cataloguenametextelement = etree.SubElement(cataloguenameelement, "cataloguenametext")
    cataloguenametextelement.text = escape(str(row[5]))
    localmsidelement = etree.SubElement(bookelement, "localmsid")
    localmsidelement.text = str(row[0])
    collectionelement = etree.SubElement(bookelement, "collection")
    for collection in collections:
        if collection[1] == str(row[2]):
            collectionuuidelement = etree.SubElement(collectionelement, "collectionuuid")
            collectionuuidelement.text = collection[0]
            collectiontextelement = etree.SubElement(collectionelement, "collectiontext")
            collectiontextelement.text = collection[1]
    # add it to root
    root.append(bookelement)
    # add it to the prototype root
    if prototypeneeded:
        prototypeneeded, prototyperoot = getprototype(row, prototypeneeded, prototyperoot, bookelement)


#print(etree.tostring(root, pretty_print=True, encoding="unicode"))
print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
# get prototypical file for modelling