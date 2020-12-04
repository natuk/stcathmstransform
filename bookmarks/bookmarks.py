from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
from rdflib.tools import rdf2dot
import uuid
from graphviz import Digraph
from namespaces import apply_namespaces, get_namespace
from crmviz.visualise import visualise_graph

def bookmarks(mydb, cursor, cursorupdate):

    graph = Graph() # graph for the dataset
    docgraph1 = Graph() # graph for the documentation drawing
    docgraph2 = Graph()  # graph for the documentation drawing
    docgraph3 = Graph()  # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph1 = apply_namespaces(docgraph1)
    docgraph2 = apply_namespaces(docgraph2)
    docgraph3 = apply_namespaces(docgraph3)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    doci1 = 2 # msid with no bookmarks
    doci2 = 1171 # msid with bookmarks, bookmark id: 14
    doci3 = 1173 # msid with loose bookmark, bookmark id: 15

    # deal with thesaurus concepts
    graph.add((URIRef("http://w3id.org/lob/concept/2837"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2837"), RDFS.label, Literal("bookmarks", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/4917"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/4917"), RDFS.label, Literal("compound markers", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2885"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2885"), RDFS.label, Literal("endband string markers", lang="en")))
    graph.add((URIRef("http://stcath.loose"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.loose"), RDFS.label, Literal("loose (bookmarks)", lang="en")))
    graph.add((URIRef("http://stcath.knotted"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.knotted"), RDFS.label, Literal("knotted (bookmark attachment)", lang="en")))
    graph.add((URIRef("http://stcath.frayed"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.frayed"), RDFS.label, Literal("frayed (bookmark attachment)", lang="en")))
    graph.add((URIRef("http://stcath.span1"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.span1"), RDFS.label, Literal("span 1 (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.span2"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.span2"), RDFS.label, Literal("span 2 (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.multiplespan"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.multiplespan"), RDFS.label, Literal("multiple span (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.twistedspan"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.twistedspan"), RDFS.label, Literal("twisted span (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.closedloop"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.closedloop"), RDFS.label, Literal("closed loop (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.twistedclosedloop"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.twistedclosedloop"), RDFS.label, Literal("twisted closed loop (bookmark primary type)", lang="en")))
    graph.add((URIRef("http://stcath.knotteddoublelength"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.knotteddoublelength"), RDFS.label, Literal("knotted double length (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.knottedsinglelength"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.knottedsinglelength"), RDFS.label, Literal("knotted single length (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.hitcheddoublelength"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.hitcheddoublelength"), RDFS.label, Literal("hitched double length (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.sewnsinglelength"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.sewnsinglelength"), RDFS.label, Literal("sewn single length (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.plaited"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.plaited"), RDFS.label, Literal("plaited (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.plied"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.plied"), RDFS.label, Literal("plied (bookmark secondary type)", lang="en")))
    graph.add((URIRef("http://stcath.wound"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.wound"), RDFS.label, Literal("wound (bookmark decoration type)", lang="en")))
    graph.add((URIRef("http://stcath.braided"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.braided"), RDFS.label, Literal("braided (bookmark decoration type)", lang="en")))
    graph.add((URIRef("http://stcath.twisted"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.twisted"), RDFS.label, Literal("twisted (bookmark decoration type)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014058"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014058"), RDFS.label, Literal("synthetic fiber", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), RDFS.label, Literal("tanned skin", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2366"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2366"), RDFS.label, Literal("lacing (techniques)", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2432"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2432"), RDFS.label, Literal("cotton (fiber)", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2468"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2468"), RDFS.label, Literal("silk (fiber)", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2470"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2470"), RDFS.label, Literal("textile", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2474"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2474"), RDFS.label, Literal("thread", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2480"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2480"), RDFS.label, Literal("wood", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2970"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2970"), RDFS.label, Literal("metal thread", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/3002"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/3002"), RDFS.label, Literal("ribbon", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/3129"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/3129"), RDFS.label, Literal("cord", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/3729"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/3729"), RDFS.label, Literal("braided cord", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/4506"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/4506"), RDFS.label, Literal("wool hair", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/4585"), RDF.type, CRM["E57_Material"]))
    graph.add((URIRef("http://w3id.org/lob/concept/4585"), RDFS.label, Literal("linen", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300124707"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300124707"), RDFS.label, Literal("Pink", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126225"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126225"), RDFS.label, Literal("Red", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126734"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126734"), RDFS.label, Literal("Orange", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127490"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127490"), RDFS.label, Literal("Brown", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127794"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127794"), RDFS.label, Literal("Yellow", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128438"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128438"), RDFS.label, Literal("Green", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128475"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128475"), RDFS.label, Literal("Light green", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129361"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129361"), RDFS.label, Literal("Blue", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129405"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129405"), RDFS.label, Literal("Light blue", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129784"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129784"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129784"), RDFS.label, Literal("Off white", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129784"), RDFS.label, Literal("White", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130257"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130257"), RDFS.label, Literal("Purple", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130602"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130602"), RDFS.label, Literal("Violet", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130920"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300130920"), RDFS.label, Literal("Black", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300266267"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300266267"), RDFS.label, Literal("Ochre", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDFS.label, Literal("Gold", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311368"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311368"), RDFS.label, Literal("Silver", lang="en")))

    docgraph1.add((URIRef("http://w3id.org/lob/concept/2837"), RDF.type, CRM["E55_Type"]))
    docgraph1.add((URIRef("http://w3id.org/lob/concept/2837"), RDFS.label, Literal("bookmarks", lang="en")))

    docgraph2.add((URIRef("http://w3id.org/lob/concept/2837"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/2837"), RDFS.label, Literal("bookmarks", lang="en")))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/4917"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/4917"), RDFS.label, Literal("compound markers", lang="en")))
    docgraph2.add((URIRef("http://stcath.knotted"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.knotted"), RDFS.label, Literal("knotted (bookmark attachment)", lang="en")))
    docgraph2.add((URIRef("http://stcath.span1"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.span1"), RDFS.label, Literal("span 1 (bookmark primary type)", lang="en")))
    docgraph2.add((URIRef("http://stcath.knotteddoublelength"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.knotteddoublelength"), RDFS.label, Literal("knotted double length (bookmark secondary type)", lang="en")))
    docgraph2.add((URIRef("http://stcath.wound"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.wound"), RDFS.label, Literal("wound (bookmark decoration type)", lang="en")))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/2468"), RDF.type, CRM["E57_Material"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/2468"), RDFS.label, Literal("silk", lang="en")))

    docgraph3.add((URIRef("http://w3id.org/lob/concept/2837"), RDF.type, CRM["E55_Type"]))
    docgraph3.add((URIRef("http://w3id.org/lob/concept/2837"), RDFS.label, Literal("bookmarks", lang="en")))
    docgraph3.add((URIRef("http://stcath.loose"), RDF.type, CRM["E55_Type"]))
    docgraph3.add((URIRef("http://stcath.loose"), RDFS.label, Literal("loose (bookmarks)", lang="en")))

    # 1_4_Bookmarks
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, bm.msid, bm.yesnonk FROM MSs mss INNER JOIN `1_4_Bookmarks` bm on mss.id=bm.msid")
    rows = cursor.fetchall()

    for row in rows:
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["yesnonk"] == "no":
            graph.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2837")))

        if row["msid"] == doci1:
            docgraph1.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2837")))
            docgraph1.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph1.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))
        if row["msid"] == doci2:
            docgraph2.add((msuuid, CRM["TP46_is_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2837")))
            docgraph2.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))

    # Bookmarks
    cursor.execute("SELECT mss.msuuid, bm.id, bm.msid, mss.cataloguename, bm.partadditionuuid, bm.bookmarkuuid, bm.type, bm.primarytype, bm.secondarytype, bm.primaryattachmenttype, bm.decorationtype FROM `MSs` mss INNER JOIN `Bookmarks` bm ON mss.id=bm.msid")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))

        # bookmark
        if row["bookmarkuuid"] is None:
            newuuid = str(uuid.uuid4())
            bookmarkuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE Bookmarks SET bookmarkuuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            bookmarkuuid = URIRef(row["bookmarkuuid"], str(STCATH))

        graph.add((bookmarkuuid, RDF.type, CRM["E22_Man-Made_Object"]))
        graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2837")))
        graph.add((bookmarkuuid, RDFS.label, Literal("Bookmark of " + shelfmark, lang="en")))

        # type
        if row["type"] == "compound":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/4917")))
        elif row["type"] == "Simple":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2885")))
        elif row["type"] == "Loose":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.loose")))
        # TODO: handle option "-"

        # primary type
        if row["primarytype"] == "1. Span 1":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.span1")))
        elif row["primarytype"] == "2. Span 2":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("https//stcath.span2")))
        elif row["primarytype"] == "3. Multiple span":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.multiplespan")))
        elif row["primarytype"] == "4. Twisted span":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.twistedspan")))
        elif row["primarytype"] == "5. Closed loop":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.closedloop")))
        elif row["primarytype"] == "6. Twisted closed span":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.twistedclosedloop")))
        # TODO: handle "NK" and "-"

        # secondary type
        if row["secondarytype"] == "1. Knotted, double length":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.knotteddoublelength")))
        elif row["secondarytype"] == "2. Knotted, single length":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.knottedsinglelength")))
        elif row["secondarytype"] == "3. Hitched, double length":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.hitcheddoublelength")))
        elif row["secondarytype"] == "4. Sewn, single length":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.sewnsinglelength")))
        elif row["secondarytype"] == "5. Plaited":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.plaited")))
        elif row["secondarytype"] == "6. Plied":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.plied")))
            # TODO: handle "NK"

        # decoration type
        if row["decorationtype"] == "1. Wound":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.wound")))
        elif row["decorationtype"] == "2. Braided":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.braided")))
        elif row["decorationtype"] == "3. Twisted":
            graph.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.twisted")))
        # TODO: handle "NK" and "-"

        if row["type"] != "loose": # loose bookmarks do not have part addition event
            graph.add((msuuid, CRM["P46_is_composed_of"], bookmarkuuid)) # if it not loose, it means it is part of the MS

            # part addition
            if row["partadditionuuid"] is None:
                newuuid = str(uuid.uuid4())
                partadditionuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE Bookmarks SET partadditionuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                partadditionuuid = URIRef(row["partadditionuuid"], str(STCATH))

            graph.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            graph.add((partadditionuuid, RDFS.label, Literal("Addition of bookmark to " + shelfmark, lang="en")))
            graph.add((partadditionuuid, CRM["P110_augmented"], msuuid)) # add to book
            graph.add((partadditionuuid, CRM["P111_added"], bookmarkuuid))  # add bookmark

            if row["primaryattachmenttype"] == "1. Knotted":
                graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.knotted"))) # add attachment technique
            elif row["primaryattachmenttype"] == "2. Frayed":
                graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.frayed"))) # add attachment technique
            #TODO: handle options: "-" and "NK"

        elif row["type"] == "loose": # loose bookmarks are found in the space of the book
            #TODO: sort this out with the CRM 7.0 property "holds or supports"
            pass

        if row["msid"] == doci2:
            docgraph2.add((bookmarkuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2837")))
            docgraph2.add((bookmarkuuid, RDFS.label, Literal("Bookmark of " + shelfmark, lang="en")))
            docgraph2.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/4917")))
            docgraph2.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.span1")))
            docgraph2.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.knotteddoublelength")))
            docgraph2.add((bookmarkuuid, CRM["P2_has_type"], URIRef("http://stcath.wound")))
            docgraph2.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            docgraph2.add((partadditionuuid, RDFS.label, Literal("Addition of bookmark to " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, CRM["P110_augmented"], msuuid))
            docgraph2.add((partadditionuuid, CRM["P111_added"], bookmarkuuid))
            docgraph2.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.knotted")))

        if row["msid"] == doci3:
            # TODO: sort this out with the CRM 7.0 property "holds or supports"
            pass

    # BookmarkMaterials
    cursor.execute("SELECT b.bookmarkuuid, mss.msuuid, mss.id, mss.cataloguename, bm.bookmarkmaterial FROM `MSs` mss INNER JOIN `Bookmarks` b ON mss.id=b.msid INNER JOIN BookmarkMaterials bm ON bm.bookmarkid=b.id")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        bookmarkuuid = URIRef(row["bookmarkuuid"], str(STCATH))
        if row["bookmarkmaterial"] == "Natural thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Silk":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
        elif row["bookmarkmaterial"] == "Silk and thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Linen braid and thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/4585")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3729")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Cord":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3129")))
        elif row["bookmarkmaterial"] == "Braid and thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3729")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Wool":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/4506")))
        elif row["bookmarkmaterial"] == "Wood":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2480")))
        elif row["bookmarkmaterial"] == "Cotton thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2432")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Cotton cord":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2432")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3129")))
        elif row["bookmarkmaterial"] == "Chord":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3129")))
        elif row["bookmarkmaterial"] == "Stub of threads":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Coloured threads":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Silk textile":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
        elif row["bookmarkmaterial"] == "Thread and textile":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
        elif row["bookmarkmaterial"] == "Cord and thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3129")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Metal thread and silk":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2970")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
        elif row["bookmarkmaterial"] == "Textile woven and embroidered":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
        elif row["bookmarkmaterial"] == "Textile":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
        elif row["bookmarkmaterial"] == "Textile, cotton":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2432")))
        elif row["bookmarkmaterial"] == "Silk thread and textile":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
        elif row["bookmarkmaterial"] == "Cord core and silk":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3129")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
        elif row["bookmarkmaterial"] == "Textile ribbon":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2470")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3002")))
        elif row["bookmarkmaterial"] == "silk and metal thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2970")))
        elif row["bookmarkmaterial"] == "Tanned leather":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))
        elif row["bookmarkmaterial"] == "Thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Silk ribbon":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3002")))
        elif row["bookmarkmaterial"] == "Cotton ribbon":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2432")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3002")))
        elif row["bookmarkmaterial"] == "Ribbon":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/3002")))
        elif row["bookmarkmaterial"] == "Silk thread":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2474")))
        elif row["bookmarkmaterial"] == "Synthetic":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://vocab.getty.edu/aat/300014058")))
        elif row["bookmarkmaterial"] == "Lace":
            graph.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://vocab.getty.edu/aat/300132861")))

        if row["id"] == doci2:
            docgraph2.add((bookmarkuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/2468")))

    # BookmarkColours
    cursor.execute("SELECT b.bookmarkuuid, mss.msuuid, mss.id, mss.cataloguename, bk.bookmarkcolour FROM `MSs` mss INNER JOIN `Bookmarks` b ON mss.id=b.msid INNER JOIN BookmarkColours bk ON bk.bookmarkid=b.id")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        bookmarkuuid = URIRef(row["bookmarkuuid"], str(STCATH))
        if row["bookmarkcolour"] == "Blue":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129361")))
        elif row["bookmarkcolour"] == "White":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129784")))
        elif row["bookmarkcolour"] == "Yellow":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300127794")))
        elif row["bookmarkcolour"] == "Green":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300128438")))
        elif row["bookmarkcolour"] == "Natural":
            pass
        elif row["bookmarkcolour"] == "Black":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300130920")))
        elif row["bookmarkcolour"] == "Red":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300126225")))
        elif row["bookmarkcolour"] == "Pink":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300124707")))
        elif row["bookmarkcolour"] == "Off white":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129784")))
        elif row["bookmarkcolour"] == "Brown":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300127490")))
        elif row["bookmarkcolour"] == "Purple":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300130257")))
        elif row["bookmarkcolour"] == "Light blue":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129405")))
        elif row["bookmarkcolour"] == "Orange":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300126734")))
        elif row["bookmarkcolour"] == "Light green":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300128475")))
        elif row["bookmarkcolour"] == "Silver":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300311368")))
        elif row["bookmarkcolour"] == "Violet":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300130602")))
        elif row["bookmarkcolour"] == "Ochre":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300266267")))
        elif row["bookmarkcolour"] == "Gold":
            graph.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300311191")))

        if row["id"] == doci2:
            docgraph2.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129361")))
        if row["id"] == doci3:
            docgraph2.add((bookmarkuuid, CRM["TP56_bears_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300129361")))

    # documentation drawing
    dot1 = visualise_graph(docgraph1, 'MS without bookmarks', "forth")
    dot2 = visualise_graph(docgraph2, 'MS with bookmark', "forth")
    dot3 = visualise_graph(docgraph3, 'MS with loose bookmark', "forth")
    dot1.render('bookmarks/bookmarks-1.gv', format='svg')
    dot2.render('bookmarks/bookmarks-2.gv', format='svg')
    dot3.render('bookmarks/bookmarks-3.gv', format='svg')

    # serialise the graph
    graph.serialize(destination='bookmarks/bookmarks.ttl', format='turtle', encoding="utf-8")
    docgraph1.serialize(destination='bookmarks/bookmarks-doc-1.n3', format='n3', encoding="utf-8")
    docgraph2.serialize(destination='bookmarks/bookmarks-doc-2.n3', format='n3', encoding="utf-8")
    docgraph3.serialize(destination='bookmarks/bookmarks-doc-3.n3', format='n3', encoding="utf-8")