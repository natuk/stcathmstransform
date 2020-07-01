from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

def openingcharacteristics(mydb, cursor, cursorupdate):
    # 1_1_OpeningCharacteristics
    cursor.execute("SELECT * FROM 1_1_OpeningCharacteristics")
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
        # measurement event
        measurementelement = etree.SubElement(bookelement, "measurement")
        measurementuuidelement = etree.SubElement(measurementelement, "measurementuuid")
        if row[3] is None:
            newuuid = str(uuid.uuid4())
            measurementuuidelement.text = newuuid
            # update the database
            sql = "UPDATE 1_1_OpeningCharacteristics SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row[0])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            measurementuuidelement.text = row[3]
        measurementtoolelement = etree.SubElement(measurementelement, "measurementtool")
        measurementtooltypeuuidelement = etree.SubElement(measurementtoolelement, "measurementtooltypeuuid")
        measurementtooltypeuuidelement.text = escape("http://vocab.getty.edu/aat/300022525")
        measurementtooltypelabelelement = etree.SubElement(measurementtoolelement, "measurementtooltypelabel")
        measurementtooltypelabelelement.text = "protractors"
        # left of centre
        if row[4] is not None:
            leftofcentredimensionelement = etree.SubElement(measurementelement, "dimension")
            leftofcentredimensionuuidelement = etree.SubElement(leftofcentredimensionelement, "dimensionuuid")
            if row[5] is None:
                newuuid = str(uuid.uuid4())
                leftofcentredimensionuuidelement.text = newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET leftofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row[0])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                leftofcentredimensionuuidelement.text = row[5]
            leftofcentredimensionvalueelement = etree.SubElement(leftofcentredimensionelement, "dimensionvalue")
            leftofcentredimensionvalueelement.text = str(row[4])
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
        if row[6] is not None:
            centredimensionelement = etree.SubElement(measurementelement, "dimension")
            centredimensionuuidelement = etree.SubElement(centredimensionelement, "dimensionuuid")
            if row[7] is None:
                newuuid = str(uuid.uuid4())
                centredimensionuuidelement.text = newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET centreuuid=%s WHERE msid=%s"
                val = (newuuid, row[0])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                centredimensionuuidelement.text = row[7]
            centredimensionvalueelement = etree.SubElement(centredimensionelement, "dimensionvalue")
            centredimensionvalueelement.text = str(row[6])
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
        if row[8] is not None:
            rightofcentredimensionelement = etree.SubElement(measurementelement, "dimension")
            rightofcentredimensionuuidelement = etree.SubElement(rightofcentredimensionelement, "dimensionuuid")
            if row[9] is None:
                newuuid = str(uuid.uuid4())
                rightofcentredimensionuuidelement.text = newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET rightofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row[0])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                rightofcentredimensionuuidelement.text = row[9]
            rightofcentredimensionvalueelement = etree.SubElement(rightofcentredimensionelement, "dimensionvalue")
            rightofcentredimensionvalueelement.text = str(row[8])
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
        if row[10] is not None:
            if row[10] != -1 & row[10] != -2 & row[10] !=-3:
                rightboarddimensionelement = etree.SubElement(measurementelement, "dimension")
                rightboarddimensionuuidelement = etree.SubElement(rightboarddimensionelement, "dimensionuuid")
                if row[11] is None:
                    newuuid = str(uuid.uuid4())
                    rightofcentredimensionuuidelement.text = newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET rightboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row[0])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    rightboarddimensionuuidelement.text = row[11]
                rightboarddimensionvalueelement = etree.SubElement(rightboarddimensionelement, "dimensionvalue")
                rightboarddimensionvalueelement.text = str(row[10])
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
        if row[12] is not None:
            if row[12] != -1 & row[12] != -2 & row[12] !=-3:
                leftboarddimensionelement = etree.SubElement(measurementelement, "dimension")
                leftboarddimensionuuidelement = etree.SubElement(leftboarddimensionelement, "dimensionuuid")
                if row[13] is None:
                    newuuid = str(uuid.uuid4())
                    leftofcentredimensionuuidelement.text = newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET leftboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row[0])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    leftboarddimensionuuidelement.text = row[13]
                leftboarddimensionvalueelement = etree.SubElement(leftboarddimensionelement, "dimensionvalue")
                leftboarddimensionvalueelement.text = str(row[12])
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
        if row[14] is not None:
            closedbookelement = etree.SubElement(bookelement, "closedbook")
            closedbookmeasurementelement = etree.SubElement(closedbookelement, "closedbookmeasurement")
            closedbookmeasurementuuidelement = etree.SubElement(closedbookmeasurementelement, "closedbookmeasurementuuid")
            if row[15] is None:
                newuuid = str(uuid.uuid4())
                closedbookmeasurementuuidelement.text = newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookmeasurementuuid=%s WHERE msid=%s"
                val = (newuuid, row[0])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookmeasurementuuidelement.text = row[15]
            closedbookmeasurementtoolelement = etree.SubElement(closedbookmeasurementelement, "closedbookmeasurementtool")
            closedbookmeasurementtooltypeuuidelement = etree.SubElement(closedbookmeasurementtoolelement, "closedbookmeasurementtooltypeuuid")
            closedbookmeasurementtooltypeuuidelement.text = escape("http://vocab.getty.edu/aat/300266529")
            closedbookmeasurementtooltypelabelelement = etree.SubElement(closedbookmeasurementtoolelement, "closedbookmeasurementtooltypelabel")
            closedbookmeasurementtooltypelabelelement.text = "rulers"
            closedbookdimensionelement = etree.SubElement(closedbookmeasurementelement, "closedbookdimension")
            closedbookdimensionuuidelement = etree.SubElement(closedbookdimensionelement, "dimensionuuid")
            if row[16] is None:
                newuuid = str(uuid.uuid4())
                closedbookdimensionuuidelement.text = newuuid
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookdimensionuuid=%s WHERE msid=%s"
                val = (newuuid, row[0])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookdimensionuuidelement.text = row[16]
            closedbookdimensionvalueelement = etree.SubElement(closedbookdimensionelement, "dimensionvalue")
            closedbookdimensionvalueelement.text = str(row[14])
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
        if row[17] is not None:
            if row[17] < 10:
                textblockbreakselement = etree.SubElement(bookelement, "textblockbreaks")
                textblockbreaksmeasurementelement = etree.SubElement(textblockbreakselement, "textblockbreaksmeasurement")
                textblockbreaksmeasurementuuidelement = etree.SubElement(textblockbreaksmeasurementelement, "textblockbreaksmeasurementuuid")
                if row[18] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksmeasurementuuidelement.text = newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksmeasurementuuid=%s WHERE msid=%s"
                    val = (newuuid, row[0])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksmeasurementuuidelement.text = row[18]
                textblockbreaksdimensionelement = etree.SubElement(textblockbreaksmeasurementelement, "textblockbreaksdimension")
                textblockbreaksdimensionuuidelement = etree.SubElement(textblockbreaksdimensionelement, "dimensionuuid")
                if row[19] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksdimensionuuidelement.text = newuuid
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksdimensionuuid=%s WHERE msid=%s"
                    val = (newuuid, row[0])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksdimensionuuidelement.text = row[19]
                textblockbreaksdimensionvalueelement = etree.SubElement(textblockbreaksdimensionelement, "dimensionvalue")
                textblockbreaksdimensionvalueelement.text = str(row[17])
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
        # add it to the prototype root
        if prototypeneeded:
            prototypeneeded, prototyperoot = getprototype(row, prototypeneeded, prototyperoot, bookelement)

    tree = etree.ElementTree(root)
    tree.write(open('openingcharacteristics/1-1-openingcharacteristics.xml', 'wb'), encoding='utf-8', pretty_print=True)
    prototypetree = etree.ElementTree(prototyperoot)
    prototypetree.write(open('openingcharacteristics/1-1-openingcharacteristics-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))