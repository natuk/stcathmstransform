from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

def boxingleavesdate(mydb, cursor, cursorupdate, namespace):
    # 1_0_BoxingLeavesDate, namespace
    cursor.execute("SELECT * FROM 1_0_BoxingLeavesDate")
    rows = cursor.fetchall()
    # root for main data
    root = etree.Element("root")
    # root for prototype document for mapping
    prototyperoot = etree.Element("root")

    for row in rows:
        bookelement = etree.Element("book")
        msuuidelement = etree.SubElement(bookelement, "msuuid")
        msuuidelement.text = namespace + row["msuuid"]
        measurementelement = etree.SubElement(bookelement, "measurement")
        measurementuuidelement = etree.SubElement(measurementelement, "measurementuuid")
        if row["measurementuuid"] is None:
            newuuid = str(uuid.uuid4())
            measurementuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            measurementuuidelement.text = namespace + row["measurementuuid"]
        measurementtoolelement = etree.SubElement(measurementelement, "measurementtool")
        measurementtooltypeuuidelement = etree.SubElement(measurementtoolelement, "measurementtooltypeuuid")
        measurementtooltypeuuidelement.text = escape("http://stcath.measuringbox")
        measurementtooltypelabelelement = etree.SubElement(measurementtoolelement, "measurementtooltypelabel")
        measurementtooltypelabelelement.text = "measuring box"
        # height
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row["heightuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET heightuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = namespace + row["heightuuid"]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row["height"])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055644")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "height"
        dimensionunitelement = etree.SubElement(dimensionelement, "dimensionunit")
        dimensionunituuidelement = etree.SubElement(dimensionunitelement, "dimensionunituuid")
        dimensionunituuidelement.text = escape("http://vocab.getty.edu/aat/300379097")
        dimensionunitlabelelement = etree.SubElement(dimensionunitelement, "dimensionunitlabel")
        dimensionunitlabelelement.text = "mm"
        # width
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row["widthuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = namespace + row["widthuuid"]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row["width"])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055647")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "width"
        dimensionunitelement = etree.SubElement(dimensionelement, "dimensionunit")
        dimensionunituuidelement = etree.SubElement(dimensionunitelement, "dimensionunituuid")
        dimensionunituuidelement.text = escape("http://vocab.getty.edu/aat/300379097")
        dimensionunitlabelelement = etree.SubElement(dimensionunitelement, "dimensionunitlabel")
        dimensionunitlabelelement.text = "mm"
        # thickness
        dimensionelement = etree.SubElement(measurementelement, "dimension")
        dimensionuuidelement = etree.SubElement(dimensionelement, "dimensionuuid")
        if row["thicknessuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET thicknessuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuidelement.text = namespace + row["thicknessuuid"]
        dimensionvalueelement = etree.SubElement(dimensionelement, "dimensionvalue")
        dimensionvalueelement.text = str(row["thickness"])
        dimensiontypeelement = etree.SubElement(dimensionelement, "dimensiontype")
        dimensiontypeuuidelement = etree.SubElement(dimensiontypeelement, "dimensiontypeuuid")
        dimensiontypeuuidelement.text = escape("http://vocab.getty.edu/aat/300055646")
        dimensiontypelabelelement = etree.SubElement(dimensiontypeelement, "dimensiontypelabel")
        dimensiontypelabelelement.text = "thickness"
        dimensionunitelement = etree.SubElement(dimensionelement, "dimensionunit")
        dimensionunituuidelement = etree.SubElement(dimensionunitelement, "dimensionunituuid")
        dimensionunituuidelement.text = escape("http://vocab.getty.edu/aat/300379097")
        dimensionunitlabelelement = etree.SubElement(dimensionunitelement, "dimensionunitlabel")
        dimensionunitlabelelement.text = "mm"
        # boxing status
        if row["boxingstatus"] is not None:
            boxingnote = row["boxingstatus"]
            if row["boxingnotes"] is not None:
                boxingnote = row["boxingstatus"] + " - " + row["boxingnotes"]
                boxingstatuselement = etree.SubElement(bookelement, "boxingstatusnotes")
                boxingstatuselement.text = escape(boxingnote)

        # survey date
        surveyeventelement = etree.SubElement(bookelement, "surveyevent")
        surveyeventuuidelement = etree.SubElement(surveyeventelement, "surveyeventuuid")
        if row["surveyeventuuid"] is None:
            newuuid = str(uuid.uuid4())
            surveyeventuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveyeventuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveyeventuuidelement.text = namespace + row["surveyeventuuid"]
        surveytimespanelement = etree.SubElement(surveyeventelement, "surveytimespan")
        surveytimespanuuidelement = etree.SubElement(surveytimespanelement, "surveytimespanuuid")
        if row["surveytimespanuuid"] is None:
            newuuid = str(uuid.uuid4())
            surveytimespanuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveytimespanuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveytimespanuuidelement.text = namespace + row["surveytimespanuuid"]
        if row["surveydate"] is not None:
            surveytimespannotbeforeelement = etree.SubElement(surveytimespanelement, "surveytimespannotbefore")
            surveytimespannotbeforeelement.text = str(row["surveydate"]).replace("00:00:00", "08:00:00").replace(" ", "T")
            surveytimespannotafterelement = etree.SubElement(surveytimespanelement, "surveytimespannotafter")
            surveytimespannotafterelement.text = str(row["surveydate"]).replace("00:00:00", "20:00:00").replace(" ", "T")
        # add it to root
        root.append(bookelement)

    tree = etree.ElementTree(root)
    tree.write(open('boxingleavesdate/1-0-boxingleavesdate.xml', 'wb'), encoding='utf-8', pretty_print=True)
    prototyperoot = getprototype(root, prototyperoot)
    prototypetree = etree.ElementTree(prototyperoot)
    prototypetree.write(open('boxingleavesdate/1-0-boxingleavesdate-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
    # get prototypical file for modelling