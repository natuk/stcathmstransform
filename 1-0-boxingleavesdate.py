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

# 1_0_BoxingLeavesDate
cursor.execute("SELECT * FROM 1_0_BoxingLeavesDate")
rows = cursor.fetchall()
# root for main data
root = etree.Element("root")
# root for prototype document for mapping
prototyperoot = etree.Element("root")
prototypeneeded = True

for row in rows:
    bookelement = etree.Element("book")
    msuuidelement = etree.SubElement(bookelement, "msuuid")
    msuuidelement.text = row[1]
    # height
    dimensionelement = etree.SubElement(bookelement, "dimension")
    dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
    if row[3] is None:
        newuuid = str(uuid.uuid4())
        dimensionuuidelement.text = newuuid
        # update the database
        sql = "UPDATE 1_0_BoxingLeavesDate SET heightuuid=%s WHERE msid=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        dimensionuuidelement.text = row[3]
    dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
    dimensionvalueelement.text = str(row[2])
    dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
    dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
    dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055644")
    dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
    dimensiontypelabelelement.text = "height"
    # width
    dimensionelement = etree.SubElement(bookelement, "dimension")
    dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
    if row[5] is None:
        newuuid = str(uuid.uuid4())
        dimensionuuidelement.text = newuuid
        # update the database
        sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        dimensionuuidelement.text = row[5]
    dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
    dimensionvalueelement.text = str(row[4])
    dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
    dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
    dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055647")
    dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
    dimensiontypelabelelement.text = "width"
    # thickness
    dimensionelement = etree.SubElement(bookelement, "dimension")
    dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
    if row[7] is None:
        newuuid = str(uuid.uuid4())
        dimensionuuidelement.text = newuuid
        # update the database
        sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        dimensionuuidelement.text = row[7]
    dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
    dimensionvalueelement.text = str(row[6])
    dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
    dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
    dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055646")
    dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
    dimensiontypelabelelement.text = "thickness"
    # boxing status
    if row[10] is not None:
        boxingnote = row[10]
        if row[11] is not None:
            boxingnote = row[10] + " - " + row[11]
            boxingstatuselement = etree.SubElement(bookelement, "boxingstatusnotes")
            boxingstatuselement.text = escape(boxingnote)

    # survey date
    surveyeventelement = etree.SubElement(bookelement, "surveyevent")
    surveyeventuuidelement = etree.SubElement(surveyeventelement, "surveyeventuuid")
    if row[12] is None:
        newuuid = str(uuid.uuid4())
        surveyeventuuidelement.text = newuuid
        # update the database
        sql = "UPDATE 1_0_BoxingLeavesDate SET surveyeventuuid=%s WHERE msid=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        surveyeventuuidelement.text = row[12]
    surveytimespanelement = etree.SubElement(surveyeventelement, "surveytimespan")
    surveytimespanuuidelement = etree.SubElement(surveytimespanelement, "surveytimespanuuid")
    if row[13] is None:
        newuuid = str(uuid.uuid4())
        surveytimespanuuidelement.text = newuuid
        # update the database
        sql = "UPDATE 1_0_BoxingLeavesDate SET surveytimespanuuid=%s WHERE msid=%s"
        val = (newuuid, row[0])
        cursorupdate.execute(sql, val)
        mydb.commit()
    else:
        surveytimespanuuidelement.text = row[13]
    #surveytimespannotbeforeelement = etree.SubElement(surveytimespanelement, "surveytimespannotbefore")
    #surveytimespannotbeforeelement.text = row[14]
    # add it to root
    root.append(bookelement)
    # add it to the prototype root
    if prototypeneeded:
        prototypeneeded, prototyperoot = getprototype(row, prototypeneeded, prototyperoot, bookelement)

tree = etree.ElementTree(root)
tree.write(open('1-0-boxingleavesdate.xml', 'wb'), encoding='utf-8', pretty_print=True)
prototypetree = etree.ElementTree(prototyperoot)
prototypetree.write(open('1-0-boxingleavesdate-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
#print(etree.tostring(root, pretty_print=True, encoding="unicode"))
#print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
# get prototypical file for modelling