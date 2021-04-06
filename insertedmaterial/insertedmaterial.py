from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
from rdflib.tools import rdf2dot
import uuid
from graphviz import Digraph
from namespaces import apply_namespaces, get_namespace
from crmviz.visualise import visualise_graph

def insertedmaterial(mydb, cursor, cursorupdate):

    graph = Graph() # graph for the dataset
    docgraph1 = Graph() # graph for the documentation drawing
    docgraph2 = Graph()  # graph for the documentation drawing
    docgraph3 = Graph()  # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph1 = apply_namespaces(docgraph1)
    docgraph2 = apply_namespaces(docgraph2)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    doci1 = 2 # msid with no inserted material
    doci2 = 21 # msid with inserted material

    # deal with thesaurus concepts

    # 1_5_InsertedMaterial
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, im.msid, im.yesno, im.insertedmaterial FROM MSs mss INNER JOIN `1_5_InsertedMaterial` im on mss.id=im.msid")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["yesno"] == "no":
            graph.add((msuuid, CRM["NTPXX_does_not_hold_or_support_physical_thing_of_type"], CRM["E18_Physical_Thing"]))
        elif row["yesno"] == "yes":
            graph.add((msuuid, CRM["TPXX_holds_or_supports_physical_thing_of_type"], CRM["E18_Physical_Thing"]))
            graph.add((msuuid, CRM["P3_has_note"], Literal("Inserted material of " + shelfmark + ": " + str(row["insertedmaterial"]), lang="en")))

        if row["msid"] == doci1:
            docgraph1.add((msuuid, CRM["NTPXX_does_not_hold_or_support_physical_thing_of_type"], CRM["E18_Physical_Thing"]))
            docgraph1.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph1.add((CRM["E18_Physical_Thing"], RDF.type, CRM["E55_Type"]))
            docgraph1.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))
        if row["msid"] == doci2:
            docgraph2.add((msuuid, CRM["TPXX_holds_or_supports_physical_thing_of_type"], CRM["E18_Physical_Thing"]))
            docgraph2.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((CRM["E18_Physical_Thing"], RDF.type, CRM["E55_Type"]))
            docgraph2.add((msuuid, RDFS.label, Literal(row["cataloguename"], lang="en")))
            docgraph2.add((msuuid, CRM["P3_has_note"], Literal("Inserted material of " + shelfmark + ": " + row["insertedmaterial"], lang="en")))

    # documentation drawing
    dot1 = visualise_graph(docgraph1, 'MS without inserted material', "forth")
    dot2 = visualise_graph(docgraph2, 'MS with inserted material', "forth")
    dot1.render('insertedmaterial/insertedmaterial-1.gv', format='svg')
    dot2.render('insertedmaterial/insertedmaterial-2.gv', format='svg')

    # serialise the graph
    graph.serialize(destination='insertedmaterial/insertedmaterial.ttl', format='turtle', encoding="utf-8")
    docgraph1.serialize(destination='insertedmaterial/insertedmaterial-doc-1.n3', format='n3', encoding="utf-8")
    docgraph2.serialize(destination='insertedmaterial/insertedmaterial-doc-2.n3', format='n3', encoding="utf-8")