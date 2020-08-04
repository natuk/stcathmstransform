from rdflib import Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
#from lxml import etree as etree
import uuid
#from html import escape
#from getprototype import getprototype

def mss(mydb, cursor, cursorupdate, graph, STCATH, CRM):
    # MSs
    collections = []
    # Get collections first
    cursor.execute("SELECT DISTINCT collection, collectionuuid FROM MSs")
    rows = cursor.fetchall()
    for row in rows:
        if row["collectionuuid"] is None: #if there is no uuid in the database create one
            newuuid = str(uuid.uuid4())
            collections.append([newuuid, row["collection"]])
            #update the database
            sql = "UPDATE MSs SET collectionuuid=%s WHERE collection=%s"
            val = (newuuid, row["collection"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else: #just fetch it
            collections.append([row["collectionuuid"], row["collection"]])

    cursor.execute("SELECT * FROM MSs")
    rows = cursor.fetchall()
    # root for main data
    #root = etree.Element("root")
    # root for prototype document for mapping
    #prototyperoot = etree.Element("root")

    for row in rows:
        #bookelement = etree.Element("book")
        #msuuidelement = etree.SubElement(bookelement, "msuuid")
        if row["msuuid"] is None: #if there is no msuuid
            newuuid = str(uuid.uuid4())
            msuuid = URIRef(newuuid, str(STCATH))
            #msuuidelement.text = namespace + newuuid
            # update the database
            sql = "UPDATE MSs SET msuuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            msuuid = URIRef(row["msuuid"], str(STCATH))
        graph.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
        graph.add((msuuid, RDFS.label, Literal(str(row["cataloguename"]))))
        graph.add((msuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/4886")))
        #cataloguenameelement = etree.SubElement(bookelement, "cataloguename")
        #cataloguenameuuidelement = etree.SubElement(cataloguenameelement, "cataloguenameuuid")
        if row["cataloguenameuuid"] is None:
            newuuid = str(uuid.uuid4())
            cataloguenameuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE MSs SET cataloguenameuuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            cataloguenameuuid = URIRef(row["cataloguenameuuid"], str(STCATH))
        graph.add((cataloguenameuuid, RDF.type, CRM["E42_Identifier"])) # type the identifier
        graph.add((cataloguenameuuid, RDFS.label, Literal(row["cataloguename"] + " (shelfmark)")))
        #cataloguenametextelement = etree.SubElement(cataloguenameelement, "cataloguenametext")
        #cataloguenametextelement.text = escape(str(row["cataloguename"]))
        # type for codex from LoB
        #typeelement = etree.SubElement(bookelement, "type")
        #typeuuidelement = etree.SubElement(typeelement, "typeuuid")
        #typeuuidelement.text = escape("http://w3id.org/lob/concept/4886")
        #typelabelelement = etree.SubElement(typeelement, "typelabel")
        #typelabelelement.text = "codex-form books"
        #localmsidelement = etree.SubElement(bookelement, "localmsid")
        #localmsidelement.text = str(row["id"])
        #collectionelement = etree.SubElement(bookelement, "collection")
        for collection in collections:
            if collection[1] == str(row["collection"]):
                graph.add((URIRef(collection[0], str(STCATH)), RDF.type, CRM["E78_Collection"])) # type the collection
                graph.add((URIRef(collection[0], str(STCATH)), RDFS.label, Literal(collection[1])))
                graph.add((URIRef(collection[0], str(STCATH)), CRM["P46_is_composed_of"], msuuid)) # manuscript belongs to collection
                break
                #collectionuuidelement = etree.SubElement(collectionelement, "collectionuuid")
                #collectionuuidelement.text = namespace.collection[0]
                #collectiontextelement = etree.SubElement(collectionelement, "collectiontext")
                #collectiontextelement.text = collection[1]
        # add it to root
        #root.append(bookelement)

    #tree = etree.ElementTree(root)
    #tree.write(open('mss/mss.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #prototyperoot = getprototype(root, prototyperoot)
    #prototypetree = etree.ElementTree(prototyperoot)
    #prototypetree.write(open('mss/mss-prototype.xml', 'wb'), encoding='utf-8', pretty_print=True)
    #print(etree.tostring(root, pretty_print=True, encoding="unicode"))
    #print(etree.tostring(prototyperoot, pretty_print=True, encoding="unicode"))
    # get prototypical file for modelling