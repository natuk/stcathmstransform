from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

def openingcharacteristics(mydb, cursor, cursorupdate, namespace):
    # 1_1_OpeningCharacteristics
    cursor.execute("SELECT * FROM 1_1_OpeningCharacteristics")
    rows = cursor.fetchall()
    # root for main data
    root = etree.Element("root")
    # root for prototype document for mapping
    prototyperoot = etree.Element("root")

    for row in rows:
        bookelement = etree.Element("book")
        msuuidelement = etree.SubElement(bookelement, "msuuid")
        msuuidelement.text = namespace + row["msuuid"]
        # measurement event
        measurementelement = etree.SubElement(bookelement, "measurement")
        measurementuuidelement = etree.SubElement(measurementelement, "measurementuuid")
        if row["measurementuuid"] is None:
            newuuid = str(uuid.uuid4())
            measurementuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE 1_1_OpeningCharacteristics SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            measurementuuidelement.text = namespace + row["measurementuuid"]
        measurementtoolelement = etree.SubElement(measurementelement, "measurementtool")
        measurementtooltypeuuidelement = etree.SubElement(measurementtoolelement, "measurementtooltypeuuid")
        measurementtooltypeuuidelement.text = escape("http://vocab.getty.edu/aat/300022525")
        measurementtooltypelabelelement = etree.SubElement(measurementtoolelement, "measurementtooltypelabel")
        measurementtooltypelabelelement.text = "protractors"
        # left of centre
        if row["leftofcentre"] is not None:
            leftofcentredimensionelement = etree.SubElement(measurementelement, "dimension")
            leftofcentredimensionuuidelement = etree.SubElement(leftofcentredimensionelement, "dimensionuuid")
            if row["leftofcentreuuid"] is None:
                newuuid = str(uuid.uuid4())
                leftofcentredimensionuuidelement.text = namespace + newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET leftofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                leftofcentredimensionuuidelement.text = namespace + row["leftofcentreuuid"]
            leftofcentredimensionvalueelement = etree.SubElement(leftofcentredimensionelement, "dimensionvalue")
            leftofcentredimensionvalueelement.text = str(row["leftofcentre"])
            leftofcentredimensionunitelement = etree.SubElement(leftofcentredimensionelement, "dimensionunit")
            leftofcentredimensionunituuidelement = etree.SubElement(leftofcentredimensionunitelement, "dimensionunituuid")
            leftofcentredimensionunituuidelement.text = escape("http://stcath.degrees")
            leftofcentredimensionunitlabelelement = etree.SubElement(leftofcentredimensionunitelement, "dimensionunitlabel")
            leftofcentredimensionunitlabelelement.text = "degrees"
            leftofcentredimensiontypeelement = etree.SubElement(leftofcentredimensionelement, "dimensiontype")
            leftofcentredimensiontypeuuidelement = etree.SubElement(leftofcentredimensiontypeelement, "dimensiontypeuuid")
            leftofcentredimensiontypeuuidelement.text = escape("http://stcath.leftofcentre")
            leftofcentredimensiontypelabelelement = etree.SubElement(leftofcentredimensiontypeelement, "dimensiontypelabel")
            leftofcentredimensiontypelabelelement.text = "left of centre"
        # centre
        if row["centre"] is not None:
            centredimensionelement = etree.SubElement(measurementelement, "dimension")
            centredimensionuuidelement = etree.SubElement(centredimensionelement, "dimensionuuid")
            if row["centreuuid"] is None:
                newuuid = str(uuid.uuid4())
                centredimensionuuidelement.text = namespace + newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET centreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                centredimensionuuidelement.text = namespace + row["centreuuid"]
            centredimensionvalueelement = etree.SubElement(centredimensionelement, "dimensionvalue")
            centredimensionvalueelement.text = str(row["centre"])
            centredimensionunitelement = etree.SubElement(centredimensionelement, "dimensionunit")
            centredimensionunituuidelement = etree.SubElement(centredimensionunitelement, "dimensionunituuid")
            centredimensionunituuidelement.text = escape("http://stcath.degrees")
            centredimensionunitlabelelement = etree.SubElement(centredimensionunitelement, "dimensionunitlabel")
            centredimensionunitlabelelement.text = "degrees"
            centredimensiontypeelement = etree.SubElement(centredimensionelement, "dimensiontype")
            centredimensiontypeuuidelement = etree.SubElement(centredimensiontypeelement, "dimensiontypeuuid")
            centredimensiontypeuuidelement.text = escape("http://stcath.centre")
            centredimensiontypelabelelement = etree.SubElement(centredimensiontypeelement, "dimensiontypelabel")
            centredimensiontypelabelelement.text = "centre"
        # right of centre
        if row["rightofcentre"] is not None:
            rightofcentredimensionelement = etree.SubElement(measurementelement, "dimension")
            rightofcentredimensionuuidelement = etree.SubElement(rightofcentredimensionelement, "dimensionuuid")
            if row["rightofcentreuuid"] is None:
                newuuid = str(uuid.uuid4())
                rightofcentredimensionuuidelement.text = namespace + newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET rightofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                rightofcentredimensionuuidelement.text = namespace + row["rightofcentreuuid"]
            rightofcentredimensionvalueelement = etree.SubElement(rightofcentredimensionelement, "dimensionvalue")
            rightofcentredimensionvalueelement.text = str(row["rightofcentre"])
            rightofcentredimensionunitelement = etree.SubElement(rightofcentredimensionelement, "dimensionunit")
            rightofcentredimensionunituuidelement = etree.SubElement(rightofcentredimensionunitelement, "dimensionunituuid")
            rightofcentredimensionunituuidelement.text = escape("http://stcath.degrees")
            rightofcentredimensionunitlabelelement = etree.SubElement(rightofcentredimensionunitelement, "dimensionunitlabel")
            rightofcentredimensionunitlabelelement.text = "degrees"
            rightofcentredimensiontypeelement = etree.SubElement(rightofcentredimensionelement, "dimensiontype")
            rightofcentredimensiontypeuuidelement = etree.SubElement(rightofcentredimensiontypeelement, "dimensiontypeuuid")
            rightofcentredimensiontypeuuidelement.text = escape("http://stcath.rightofcentre")
            rightofcentredimensiontypelabelelement = etree.SubElement(rightofcentredimensiontypeelement, "dimensiontypelabel")
            rightofcentredimensiontypelabelelement.text = "right of centre"
        # right board TODO: provision for -1 (broken/split) -2 (detached) -3 (missing)
        if row["rightboard"] is not None:
            if row["rightboard"] != -1 & row["rightboard"] != -2 & row["rightboard"] !=-3:
                rightboarddimensionelement = etree.SubElement(measurementelement, "dimension")
                rightboarddimensionuuidelement = etree.SubElement(rightboarddimensionelement, "dimensionuuid")
                if row["rightboarduuid"] is None:
                    newuuid = str(uuid.uuid4())
                    rightofcentredimensionuuidelement.text = namespace + newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET rightboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    rightboarddimensionuuidelement.text = namespace + row["rightboarduuid"]
                rightboarddimensionvalueelement = etree.SubElement(rightboarddimensionelement, "dimensionvalue")
                rightboarddimensionvalueelement.text = str(row["rightboard"])
                rightboarddimensionunitelement = etree.SubElement(rightboarddimensionelement, "dimensionunit")
                rightboarddimensionunituuidelement = etree.SubElement(rightboarddimensionunitelement, "dimensionunituuid")
                rightboarddimensionunituuidelement.text = escape("http://stcath.degrees")
                rightboarddimensionunitlabelelement = etree.SubElement(rightboarddimensionunitelement, "dimensionunitlabel")
                rightboarddimensionunitlabelelement.text = "degrees"
                rightboarddimensiontypeelement = etree.SubElement(rightboarddimensionelement, "dimensiontype")
                rightboarddimensiontypeuuidelement = etree.SubElement(rightboarddimensiontypeelement, "dimensiontypeuuid")
                rightboarddimensiontypeuuidelement.text = escape("http://stcath.rightboard")
                rightboarddimensiontypelabelelement = etree.SubElement(rightboarddimensiontypeelement, "dimensiontypelabel")
                rightboarddimensiontypelabelelement.text = "right board"
        # left board
        if row["leftboard"] is not None:
            if row["leftboard"] != -1 & row["leftboard"] != -2 & row["leftboard"] !=-3:
                leftboarddimensionelement = etree.SubElement(measurementelement, "dimension")
                leftboarddimensionuuidelement = etree.SubElement(leftboarddimensionelement, "dimensionuuid")
                if row["leftboarduuid"] is None:
                    newuuid = str(uuid.uuid4())
                    leftofcentredimensionuuidelement.text = namespace + newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET leftboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    leftboarddimensionuuidelement.text = namespace + row["leftboarduuid"]
                leftboarddimensionvalueelement = etree.SubElement(leftboarddimensionelement, "dimensionvalue")
                leftboarddimensionvalueelement.text = str(row["leftboard"])
                leftboarddimensionunitelement = etree.SubElement(leftboarddimensionelement, "dimensionunit")
                leftboarddimensionunituuidelement = etree.SubElement(leftboarddimensionunitelement, "dimensionunituuid")
                leftboarddimensionunituuidelement.text = escape("http://stcath.degrees")
                leftboarddimensionunitlabelelement = etree.SubElement(leftboarddimensionunitelement, "dimensionunitlabel")
                leftboarddimensionunitlabelelement.text = "degrees"
                leftboarddimensiontypeelement = etree.SubElement(leftboarddimensionelement, "dimensiontype")
                leftboarddimensiontypeuuidelement = etree.SubElement(leftboarddimensiontypeelement, "dimensiontypeuuid")
                leftboarddimensiontypeuuidelement.text = escape("http://stcath.leftboard")
                leftboarddimensiontypelabelelement = etree.SubElement(leftboarddimensiontypeelement, "dimensiontypelabel")
                leftboarddimensiontypelabelelement.text = "left board"
        # closed board min thickness
        if row["closedbook"] is not None:
            closedbookelement = etree.SubElement(bookelement, "closedbook")
            closedbookmeasurementelement = etree.SubElement(closedbookelement, "closedbookmeasurement")
            closedbookmeasurementuuidelement = etree.SubElement(closedbookmeasurementelement, "closedbookmeasurementuuid")
            if row["closedbookmeasurementuuid"] is None:
                newuuid = str(uuid.uuid4())
                closedbookmeasurementuuidelement.text = namespace + newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookmeasurementuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookmeasurementuuidelement.text = namespace + row["closedbookmeasurementuuid"]
            closedbookmeasurementtoolelement = etree.SubElement(closedbookmeasurementelement, "closedbookmeasurementtool")
            closedbookmeasurementtooltypeuuidelement = etree.SubElement(closedbookmeasurementtoolelement, "closedbookmeasurementtooltypeuuid")
            closedbookmeasurementtooltypeuuidelement.text = escape("http://vocab.getty.edu/aat/300266529")
            closedbookmeasurementtooltypelabelelement = etree.SubElement(closedbookmeasurementtoolelement, "closedbookmeasurementtooltypelabel")
            closedbookmeasurementtooltypelabelelement.text = "rulers"
            closedbookdimensionelement = etree.SubElement(closedbookmeasurementelement, "closedbookdimension")
            closedbookdimensionuuidelement = etree.SubElement(closedbookdimensionelement, "dimensionuuid")
            if row["closedbookdimensionuuid"] is None:
                newuuid = str(uuid.uuid4())
                closedbookdimensionuuidelement.text = namespace + newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookdimensionuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookdimensionuuidelement.text = namespace + row["closedbookdimensionuuid"]
            closedbookdimensionvalueelement = etree.SubElement(closedbookdimensionelement, "dimensionvalue")
            closedbookdimensionvalueelement.text = str(row["closedbook"])
            closedbookdimensionunitelement = etree.SubElement(closedbookdimensionelement, "dimensionunit")
            closedbookdimensionunituuidelement = etree.SubElement(closedbookdimensionunitelement, "dimensionunituuid")
            closedbookdimensionunituuidelement.text = escape("http://vocab.getty.edu/aat/300379097")
            closedbookdimensionunitlabelelement = etree.SubElement(closedbookdimensionunitelement, "dimensionunitlabel")
            closedbookdimensionunitlabelelement.text = "millimeters"
            closedbookdimensiontypeelement = etree.SubElement(closedbookdimensionelement, "dimensiontype")
            closedbookdimensiontypeuuidelement = etree.SubElement(closedbookdimensiontypeelement, "dimensiontypeuuid")
            closedbookdimensiontypeuuidelement.text = escape("http://stcath.closedbook")
            closedbookdimensiontypelabelelement = etree.SubElement(closedbookdimensiontypeelement, "dimensiontypelabel")
            closedbookdimensiontypelabelelement.text = "closed book thickness"
        # textblockbreaks
        if row["textblockbreaks"] is not None:
            if row["textblockbreaks"] < 10:
                textblockbreakselement = etree.SubElement(bookelement, "textblockbreaks")
                textblockbreaksmeasurementelement = etree.SubElement(textblockbreakselement, "textblockbreaksmeasurement")
                textblockbreaksmeasurementuuidelement = etree.SubElement(textblockbreaksmeasurementelement, "textblockbreaksmeasurementuuid")
                if row["textblockbreaksmeasurementuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksmeasurementuuidelement.text = namespace + newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksmeasurementuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksmeasurementuuidelement.text = namespace + row["textblockbreaksmeasurementuuid"]
                textblockbreaksdimensionelement = etree.SubElement(textblockbreaksmeasurementelement, "textblockbreaksdimension")
                textblockbreaksdimensionuuidelement = etree.SubElement(textblockbreaksdimensionelement, "dimensionuuid")
                if row["textblockbreaksdimensionuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksdimensionuuidelement.text = namespace + newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksdimensionuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksdimensionuuidelement.text = namespace + row["textblockbreaksdimensionuuid"]
                textblockbreaksdimensionvalueelement = etree.SubElement(textblockbreaksdimensionelement, "dimensionvalue")
                textblockbreaksdimensionvalueelement.text = str(row["textblockbreaks"])
                textblockbreaksdimensionunitelement = etree.SubElement(textblockbreaksdimensionelement, "dimensionunit")
                textblockbreaksdimensionunituuidelement = etree.SubElement(textblockbreaksdimensionunitelement, "dimensionunituuid")
                textblockbreaksdimensionunituuidelement.text = escape("http://stcath.textblockbreaks")
                textblockbreaksdimensionunitlabelelement = etree.SubElement(textblockbreaksdimensionunitelement, "dimensionunitlabel")
                textblockbreaksdimensionunitlabelelement.text = "textblock breaks"
                textblockbreaksdimensiontypeelement = etree.SubElement(textblockbreaksdimensionelement, "dimensiontype")
                textblockbreaksdimensiontypeuuidelement = etree.SubElement(textblockbreaksdimensiontypeelement, "dimensiontypeuuid")
                textblockbreaksdimensiontypeuuidelement.text = escape("http://stcath.nooftextblockbreak")
                textblockbreaksdimensiontypelabelelement = etree.SubElement(textblockbreaksdimensiontypeelement, "dimensiontypelabel")
                textblockbreaksdimensiontypelabelelement.text = "number of textblock breaks"
        # add it to root
        root.append(bookelement)

    tree = etree.ElementTree(root)
    tree.write(open('openingcharacteristics/1-1-openingcharacteristics.xml', 'wb'), encoding='utf-8', pretty_print=True)
    prototyperoot = getprototype(root, prototyperoot)
    prototypetree = etree.ElementTree(prototyperoot)
    prototypetree.write(open('openingcharacteristics/1-1-openingcharacteristics-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))