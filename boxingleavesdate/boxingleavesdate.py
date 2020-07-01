from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

def boxingleavesdate(mydb, cursor, cursorupdate):
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
        measurementelement = etree.SubElement(bookelement, "measurement")
        measurementuuidelement = etree.SubElement(measurementelement, "measurementuuid")
        if row[2] is None:
            newuuid = str(uuid.uuid4())
            measurementuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            measurementuuidelement.text = row[2]
        measurementtoolelement = etree.SubElement(measurementelement, "measurementtool")
        measurementtooltypeuuidelement = etree.SubElement(measurementtoolelement, "measurementtooltypeuuid")
        measurementtooltypeuuidelement.text = escape("http://stcath.measuringbox")
        measurementtooltypelabelelement = etree.SubElement(measurementtoolelement, "measurementtooltypelabel")
        measurementtooltypelabelelement.text = "measuring box"
        # height
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row[4] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET heightuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = row[4]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row[3])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055644")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "height"
        # width
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row[6] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = row[6]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row[5])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055647")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "width"
        # thickness
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row[8] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET thicknessuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = row[8]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row[7])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055646")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "thickness"
        # boxing status
        if row[11] is not None:
            boxingnote = row[11]
            if row[12] is not None:
                boxingnote = row[11] + " - " + row[12]
                boxingstatuselement = etree.SubElement(bookelement, "boxingstatusnotes")
                boxingstatuselement.text = escape(boxingnote)

        # survey date
        surveyeventelement = etree.SubElement(bookelement, "surveyevent")
        surveyeventuuidelement = etree.SubElement(surveyeventelement, "surveyeventuuid")
        if row[13] is None:
            newuuid = str(uuid.uuid4())
            surveyeventuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveyeventuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveyeventuuidelement.text = row[13]
        surveytimespanelement = etree.SubElement(surveyeventelement, "surveytimespan")
        surveytimespanuuidelement = etree.SubElement(surveytimespanelement, "surveytimespanuuid")
        if row[14] is None:
            newuuid = str(uuid.uuid4())
            surveytimespanuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveytimespanuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveytimespanuuidelement.text = row[14]
        if row[15] is not None:
            surveytimespannotbeforeelement = etree.SubElement(surveytimespanelement, "surveytimespannotbefore")
            surveytimespannotbeforeelement.text = str(row[15]).replace("00:00:00", "08:00:00").replace(" ", "T")
            surveytimespannotafterelement = etree.SubElement(surveytimespanelement, "surveytimespannotafter")
            surveytimespannotafterelement.text = str(row[15]).replace("00:00:00", "20:00:00").replace(" ", "T")
        # add it to root
        root.append(bookelement)
        # add it to the prototype root
        if prototypeneeded:
            prototypeneeded, prototyperoot = getprototype(row, prototypeneeded, prototyperoot, bookelement)

    tree = etree.ElementTree(root)
    tree.write(open('boxingleavesdate/1-0-boxingleavesdate.xml', 'wb'), encoding='utf-8', pretty_print=True)
    prototypetree = etree.ElementTree(prototyperoot)
    prototypetree.write(open('boxingleavesdate/1-0-boxingleavesdate-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
    # get prototypical file for modelling