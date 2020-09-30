from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
from rdflib.tools import rdf2dot
import uuid
from graphviz import Digraph
from namespaces import apply_namespaces, get_namespace
from crmviz.visualise import visualise_graph

def liftingtabs(mydb, cursor, cursorupdate):

    graph = Graph() # graph for the dataset
    docgraph1 = Graph() # graph for the documentation drawing
    docgraph2 = Graph()  # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph1 = apply_namespaces(docgraph1)
    docgraph2 = apply_namespaces(docgraph2)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    doci1 = 2 # msid with no liftingtabs
    doci2 = 1307 # msid with liftingtabs, pagemarker id: 23

    # deal with thesaurus concepts
    graph.add((URIRef("http://w3id.org/lob/concept/2833"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2833"), SKOS.prefLabel, Literal("board strap markers", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), SKOS.prefLabel, Literal("tanned skin", lang="en")))

    # 1_3_LiftingTabs
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, lt.msid, lt.yesnonk FROM MSs mss INNER JOIN `1_3_LiftingTabs` lt on mss.id=lt.msid")
    rows = cursor.fetchall()

    for row in rows:
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["yesnonk"] == "no":
            graph.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2833")))

        if row["msid"] == doci1:
            docgraph1.add((URIRef("http://w3id.org/lob/concept/2833"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://w3id.org/lob/concept/2833"), SKOS.prefLabel, Literal("board strap markers", lang="en")))
            docgraph1.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2833")))
            docgraph1.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph1.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))
        if row["msid"] == doci2:
            docgraph2.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))

    # LiftingTabs
    cursor.execute("SELECT lt.id, mss.msuuid, mss.cataloguename, lt.msid, lt.partadditionuuid, lt.leftliftingtabuuid, lt.rightliftingtabuuid, lt.location, lt.material, lt.attachment, lt.turnin FROM MSs mss INNER JOIN `LiftingTabs` lt on mss.id=lt.msid")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        # lifting tabs
        locations = row["location"].split(",")
        # TODO: work out how many and which lifting tabs we have and loop through them for the rest of the script -- start here
        if locations[1] == "Both boards" or locations[1] == "Left board":
            if row["leftliftingtabuuid"] is None:
                newuuid = str(uuid.uuid4())
                leftliftingtabuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE LiftingTabs SET leftliftingtabuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                leftliftingtabuuid = URIRef(row["leftliftingtabuuid"], str(STCATH))

            graph.add((leftliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            graph.add((leftliftingtabuuid, RDFS.label, Literal("Left board marker of " + shelfmark, lang="en")))

        if locations[1] == "Both boards" or locations[1] == "Right board":
            if row["rightliftingtabuuid"] is None:
                newuuid = str(uuid.uuid4())
                rightliftingtabuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE LiftingTabs SET rightliftingtabuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                rightliftingtabuuid = URIRef(row["rightliftingtabuuid"], str(STCATH))

            graph.add((rightliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            graph.add((rightliftingtabuuid, RDFS.label, Literal("Right board marker of " + shelfmark, lang="en")))

        if locations[1] == "Both boards" or locations[1] == "Left board" or locations[1] == "Right board":
            if row["partadditionuuid"] is None:
                newuuid = str(uuid.uuid4())
                partadditionuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE LiftingTabs SET partadditionuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                partadditionuuid = URIRef(row["partadditionuuid"], str(STCATH))


            graph.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            graph.add((partadditionuuid, RDFS.label, Literal("Addition of board markers to " + shelfmark, lang="en")))
            graph.add((partadditionuuid, CRM["P110_augmented"], msuuid))
            if locations[1] == "Both boards" or locations[1] == "Left board":
                graph.add((partadditionuuid, CRM["P111_added"], leftliftingtabuuid))
            if locations[1] == "Both boards" or locations[1] == "Right board":
                graph.add((partadditionuuid, CRM["P111_added"], rightliftingtabuuid))

        if row["msid"] == doci2:
            docgraph2.add((leftliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((leftliftingtabuuid, RDFS.label, Literal("Left board marker of " + shelfmark, lang="en")))
            docgraph2.add((rightliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((rightliftingtabuuid, RDFS.label, Literal("Right board marker of " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            docgraph2.add((partadditionuuid, RDFS.label, Literal("Addition of board markers to " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, CRM["P111_added"], leftliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P111_added"], rightliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P110_augmented"], msuuid))

        if locations[1] == "Both boards":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((leftliftingtabuuid, CRM["P55_has_current_location"], ...))
            #graph.add((rightliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass
        elif locations[1] == "Right board":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((rightliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass
        elif locations[1] == "Left board":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((leftliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass

        if row["material"] == "Tanned leather":
            graph.add((leftliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))


    # documentation drawing
    dot1 = visualise_graph(docgraph1, 'MS without board strap markers')
    dot2 = visualise_graph(docgraph2, 'MS with board strap markers')
    dot1.render('liftingtabs/liftingtabs-1.gv', format='svg')
    dot2.render('liftingtabs/liftingtabs-2.gv', format='svg')

    # serialise the graph
    graph.serialize(destination='liftingtabs/liftingtabs.ttl', format='turtle', encoding="utf-8")
    docgraph1.serialize(destination='liftingtabs/liftingtabs-doc-1.n3', format='n3', encoding="utf-8")
    docgraph2.serialize(destination='liftingtabs/liftingtabs-doc-2.n3', format='n3', encoding="utf-8")