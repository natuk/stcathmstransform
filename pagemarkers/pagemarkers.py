from lxml import etree as etree
import uuid
from html import escape
from getprototype import getprototype

def pagemarkers(mydb, cursor, cursorupdate, namespace):
    # 1_1_PageMarkers and PageMarkers
    cursor.execute("SELECT pms.msid, pms.msiduuid, pms.yesnonk, pm.type, pm.attachment, pm.material FROM `1_2_PageMarkers` pms LEFT JOIN `PageMarkers` pm ON pms.msid=pm.msid")
    rows = cursor.fetchall()
    # root for main data
    root = etree.Element("root")
    # root for prototype document for mapping
    prototyperoot = etree.Element("root")

    for row in rows:
        bookelement = etree.Element("book")
        msuuidelement = etree.SubElement(bookelement, "msuuid")
        msuuidelement.text = namespace + row["msiduuid"]
        if row["yesnonk"] == "no":
            nopagemarkerselement = etree.SubElement(bookelement, "nopagemarkers")
            nopagemarkerstypeelement = etree.SubElement(nopagemarkerselement, "nopagemarkerstype")
            nopagemarkerstypeuuidelement = etree.SubElement(nopagemarkerstypeelement, "nopagemarkerstypeuuid")
            nopagemarkerstypeuuidelement.text = escape("http://w3id.org/lob/concept/5423")
            nopagemarkerstypelabelelement = etree.SubElement(nopagemarkerstypeelement, "nopagemarkerstypelabel")
            nopagemarkerstypelabelelement.text = "leaf markers"
        elif row["yesnonk"] == "yes":
            pagemarkerselement = etree.SubElement(bookelement, "pagemarkers")
            pagemarkerstypeelement = etree.SubElement(pagemarkerselement, "pagemarkerstype")
            pagemarkerstypeuuidelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypeuuid")
            pagemarkerstypeuuidelement.text = escape("http://w3id.org/lob/concept/5423")
            pagemarkerstypelabelelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypelabel")
            pagemarkerstypelabelelement.text = "leaf markers"

            if bool(row["type"] == "Folded") | bool(row["type"] == "Folded and knotted"):
                pagemarkerstypeelement = etree.SubElement(pagemarkerselement, "pagemarkerstype")
                pagemarkerstypeuuidelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypeuuid")
                pagemarkerstypeuuidelement.text = escape("http://w3id.org/lob/concept/2945")
                pagemarkerstypelabelelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypelabel")
                pagemarkerstypelabelelement.text = "leaf tab markers"
            if row["type"] == "Straight":
                pagemarkerstypeelement = etree.SubElement(pagemarkerselement, "pagemarkerstype")
                pagemarkerstypeuuidelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypeuuid")
                pagemarkerstypeuuidelement.text = escape("http://w3id.org/lob/concept/5423")
                pagemarkerstypelabelelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypelabel")
                pagemarkerstypelabelelement.text = "leaf markers"
            if bool(row["type"] == "Platted") | bool(row["type"] == "Tied") | bool(row["type"] == "Twisted thread") | bool(row["type"] == "Thread"):
                pagemarkerstypeelement = etree.SubElement(pagemarkerselement, "pagemarkerstype")
                pagemarkerstypeuuidelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypeuuid")
                pagemarkerstypeuuidelement.text = escape("http://w3id.org/lob/concept/2944")
                pagemarkerstypelabelelement = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypelabel")
                pagemarkerstypelabelelement.text = "leaf string markers"
            # TODO: handle "Box", "Wax" and "Painted"
            pagemarkerstypelabel2element = etree.SubElement(pagemarkerstypeelement, "pagemarkerstypelabel")
            pagemarkerstypelabel2element.text = str(row["type"]).lower()

        # add it to root
        root.append(bookelement)

    tree = etree.ElementTree(root)
    tree.write(open('pagemarkers/pagemarkers.xml', 'wb'), encoding='utf-8', pretty_print=True)
    prototyperoot = getprototype(root, prototyperoot)
    prototypetree = etree.ElementTree(prototyperoot)
    prototypetree.write(open('pagemarkers/pagemarkers-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
    # get prototypical file for modelling