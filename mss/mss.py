from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
from rdflib.tools import rdf2dot
import uuid
from graphviz import Digraph
from namespaces import apply_namespaces, get_namespace
from visualise import visualise_graph

def mss(mydb, cursor, cursorupdate):
    graph = Graph() # graph for the dataset
    docgraph = Graph() # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph = apply_namespaces(docgraph)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    # deal with thesaurus concepts
    graph.add((URIRef("http://w3id.org/lob/concept/4886"), RDF.type, CRM["E55_Type"])) # codex-form books
    graph.add((URIRef("http://w3id.org/lob/concept/4886"), SKOS.prefLabel, Literal("codex-form books", lang="en")))  # codex-form books

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
        graph.add((URIRef(row["collectionuuid"], str(STCATH)), RDF.type, CRM["E78_Collection"]))  # rdf type the collection
        graph.add((URIRef(row["collectionuuid"], str(STCATH)), RDFS.label, Literal(row["collection"]))) # rdf label

    cursor.execute("SELECT * FROM MSs")
    rows = cursor.fetchall()

    doci = 0 # set the desirable db row for the documentation example

    for i, row in enumerate(rows):
        if row["msuuid"] is None: #if there is no msuuid create one
            newuuid = str(uuid.uuid4())
            msuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE MSs SET msuuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            msuuid = URIRef(row["msuuid"], str(STCATH))

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

        for collection in collections:
            if collection[1] == str(row["collection"]):
                collectionuuid = collection[0]
                break

        graph.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))  # rdf type the manuscript
        graph.add((msuuid, RDFS.label, Literal(str(row["cataloguename"]))))
        graph.add((msuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/4886")))  # manuscript is 'codex-form book'
        graph.add((cataloguenameuuid, RDF.type, CRM["E42_Identifier"]))  # rdf type the identifier
        graph.add((cataloguenameuuid, RDFS.label, Literal(row["cataloguename"] + " (shelfmark)")))
        graph.add((msuuid, CRM["P48_has_preferred_identifier"], cataloguenameuuid))  # shelfmark is preferred identifier of the manuscript
        graph.add((URIRef(collectionuuid, str(STCATH)), CRM["P46_is_composed_of"], msuuid))  # manuscript belongs to collection

        # add the same triples to the docgraph if it is the example we have chosen
        if i == doci:
            docgraph.add((URIRef("http://w3id.org/lob/concept/4886"), RDF.type, CRM["E55_Type"]))
            docgraph.add((URIRef("http://w3id.org/lob/concept/4886"), SKOS.prefLabel, Literal("codex-form books", lang="en")))
            docgraph.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph.add((msuuid, RDFS.label, Literal(str(row["cataloguename"]), lang="en")))
            docgraph.add((msuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/4886")))
            docgraph.add((cataloguenameuuid, RDF.type, CRM["E42_Identifier"]))
            docgraph.add((cataloguenameuuid, RDFS.label, Literal(row["cataloguename"] + " (shelfmark)", lang="en")))
            docgraph.add((msuuid, CRM["P48_has_preferred_identifier"], cataloguenameuuid))
            docgraph.add((URIRef(collectionuuid, str(STCATH)), RDF.type, CRM["E78_Collection"]))
            docgraph.add((URIRef(collectionuuid, str(STCATH)), RDFS.label, Literal(row["collection"], lang="en")))
            docgraph.add((URIRef(collectionuuid, str(STCATH)), CRM["P46_is_composed_of"], msuuid))

    # documentation drawing
    dot = visualise_graph(docgraph, 'MSs')
    dot.render('mss/mss.gv',format='svg')

    # serialise the graph
    #graph.serialize(destination='mss/mss.ttl', format='turtle', encoding="utf-8")
    #docgraph.serialize(destination='mss/mss-doc.n3', format='n3', encoding="utf-8")