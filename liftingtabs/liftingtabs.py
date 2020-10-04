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
    graph.add((URIRef("http://w3id.org/lob/concept/1197"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1197"), SKOS.prefLabel, Literal("tawed skin", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/5429"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/5429"), SKOS.prefLabel, Literal("adhering", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/4045"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/4045"), SKOS.prefLabel, Literal("nailing", lang="en")))
    graph.add((URIRef("http://stcath.overturnin"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.overturnin"), SKOS.prefLabel, Literal("over turn-in attaching", lang="en")))
    graph.add((URIRef("http://stcath.underturnin"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.underturnin"), SKOS.prefLabel, Literal("under turn-in attaching", lang="en")))
    graph.add((URIRef("http://stcath.brokenoff"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.brokenoff"), SKOS.prefLabel, Literal("broken off", lang="en")))
    graph.add((URIRef("http://stcath.brokenandsewn"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.brokenandsewn"), SKOS.prefLabel, Literal("broken and sewn", lang="en")))
    graph.add((URIRef("http://stcath.missing"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.missing"), SKOS.prefLabel, Literal("missing", lang="en")))
    graph.add((URIRef("http://stcath.sound"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.sound"), SKOS.prefLabel, Literal("sound", lang="en")))
    graph.add((URIRef("http://stcath.worn"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.worn"), SKOS.prefLabel, Literal("worn", lang="en")))
    graph.add((URIRef("http://stcath.detached"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.detached"), SKOS.prefLabel, Literal("detached", lang="en")))
    graph.add((URIRef("http://stcath.dangling"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.dangling"), SKOS.prefLabel, Literal("dangling", lang="en")))

    docgraph1.add((URIRef("http://w3id.org/lob/concept/2833"), RDF.type, CRM["E55_Type"]))
    docgraph1.add((URIRef("http://w3id.org/lob/concept/2833"), SKOS.prefLabel, Literal("board strap markers", lang="en")))

    docgraph2.add((URIRef("http://w3id.org/lob/concept/2833"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/2833"), SKOS.prefLabel, Literal("board strap markers", lang="en")))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/1658"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/1658"), SKOS.prefLabel, Literal("tanned skin", lang="en")))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/5429"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://w3id.org/lob/concept/5429"), SKOS.prefLabel, Literal("adhering", lang="en")))
    docgraph2.add((URIRef("http://stcath.underturnin"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.underturnin"), SKOS.prefLabel, Literal("under turn-in attaching", lang="en")))
    docgraph2.add((URIRef("http://stcath.brokenoff"), RDF.type, CRM["E55_Type"]))
    docgraph2.add((URIRef("http://stcath.brokenoff"), SKOS.prefLabel, Literal("broken off", lang="en")))

    # 1_3_LiftingTabs
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, lt.msid, lt.yesnonk FROM MSs mss INNER JOIN `1_3_LiftingTabs` lt on mss.id=lt.msid")
    rows = cursor.fetchall()

    for row in rows:
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["yesnonk"] == "no":
            graph.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/2833")))

        if row["msid"] == doci1:
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
        # TODO: deal with option "Centre, board"
        for location in locations:
            location = location.strip()
            if location == "Left board" or location == "Both boards" or location == "Right board":
                if location == "Left board" or location == "Both boards":
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
                    graph.add((leftliftingtabuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2833")))
                    graph.add((leftliftingtabuuid, RDFS.label, Literal("Left board marker of " + shelfmark, lang="en")))

                    if row["material"] == "Tanned leather":
                        graph.add((leftliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))
                    elif row["material"] == "Tawed leather":
                        graph.add((leftliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1197")))

                if location == "Right board" or location == "Both boards":
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
                    graph.add((rightliftingtabuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2833")))
                    graph.add((rightliftingtabuuid, RDFS.label, Literal("Right board marker of " + shelfmark, lang="en")))

                    if row["material"] == "Tanned leather":
                        graph.add((rightliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))
                    elif row["material"] == "Tawed leather":
                        graph.add((rightliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1197")))

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

                if location == "Both boards" or location == "Left board":
                    graph.add((partadditionuuid, CRM["P111_added"], leftliftingtabuuid))
                if location == "Both boards" or location == "Right board":
                    graph.add((partadditionuuid, CRM["P111_added"], rightliftingtabuuid))
                if row['attachment'] == "Glued":
                    graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://w3id.org/lob/concept/5429")))
                elif row['attachment'] == "Nailed":
                    graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://w3id.org/lob/concept/4045")))
                if row['turnin'] == "Under turn-in":
                    graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.underturnin")))
                elif row['turnin'] == "Over turn-in":
                    graph.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.overturnin")))

        if location == "Both boards":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((leftliftingtabuuid, CRM["P55_has_current_location"], ...))
            #graph.add((rightliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass
        elif location == "Right board":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((rightliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass
        elif location == "Left board":
            # TODO: Mark the location of the lifting tabs when the board foredge place is available
            #graph.add((leftliftingtabuuid, CRM["P55_has_current_location"], ...))
            pass

        if row["msid"] == doci2:
            docgraph2.add((leftliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((leftliftingtabuuid, RDFS.label, Literal("Left board marker of " + shelfmark, lang="en")))
            docgraph2.add((leftliftingtabuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2833")))
            docgraph2.add((rightliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((rightliftingtabuuid, RDFS.label, Literal("Right board marker of " + shelfmark, lang="en")))
            docgraph2.add((rightliftingtabuuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2833")))
            docgraph2.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            docgraph2.add((partadditionuuid, RDFS.label, Literal("Addition of board markers to " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, CRM["P111_added"], leftliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P111_added"], rightliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P110_augmented"], msuuid))
            docgraph2.add((leftliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((leftliftingtabuuid, RDFS.label, Literal("Left board marker of " + shelfmark, lang="en")))
            docgraph2.add((rightliftingtabuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((rightliftingtabuuid, RDFS.label, Literal("Right board marker of " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"]))
            docgraph2.add((partadditionuuid, RDFS.label, Literal("Addition of board markers to " + shelfmark, lang="en")))
            docgraph2.add((partadditionuuid, CRM["P111_added"], leftliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P111_added"], rightliftingtabuuid))
            docgraph2.add((partadditionuuid, CRM["P110_augmented"], msuuid))
            docgraph2.add((leftliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))
            docgraph2.add((rightliftingtabuuid, CRM["P45_consists_of"], URIRef("http://w3id.org/lob/concept/1658")))
            docgraph2.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://w3id.org/lob/concept/5429")))
            docgraph2.add((partadditionuuid, CRM["P32_used_general_technique"], URIRef("http://stcath.underturnin")))

    # LiftingTabsCondition
    cursor.execute("SELECT ltc.id, lt.msid, mss.msuuid, mss.cataloguename, lt.leftliftingtabuuid, lt.rightliftingtabuuid, ltc.condition, ltc.conditionuuid, ltc.leftboard FROM `LiftingTabsCondition` ltc LEFT JOIN `LiftingTabs` lt ON ltc.liftingtabid=lt.id INNER JOIN MSs mss ON mss.id=lt.msid")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row['leftliftingtabuuid'] is not None:
            leftliftingtabuuid = URIRef(row["leftliftingtabuuid"], str(STCATH))
        # elif row['leftliftingtabuuid'] is None:
        #     if row["leftboard"] == 1: # we have a left lifting tab condition but no left lifting tab
        #         print(str(row["msid"]) + ", ")
        if row['rightliftingtabuuid'] is not None:
            rightliftingtabuuid = URIRef(row["rightliftingtabuuid"], str(STCATH))
        # elif row['rightliftingtabuuid'] is None:
        #     if row["leftboard"] == 0: # we have a right lifting tab condition but no right lifting tab
        #         print(str(row["msid"]) + ", ")
        if row["leftboard"] == 1: # this is the left board
            if row["conditionuuid"] is None:
                newuuid = str(uuid.uuid4())
                conditionuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE LiftingTabsCondition SET conditionuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                conditionuuid = URIRef(row["conditionuuid"], str(STCATH))

            graph.add((conditionuuid, RDF.type, CRM["E3_Condition_State"]))
            graph.add((conditionuuid, RDFS.label, Literal("Condition of left board marker of " + shelfmark, lang="en")))
            graph.add((leftliftingtabuuid, CRM["P44_has_condition"], conditionuuid))

            if row["msid"] == doci2:
                docgraph2.add((conditionuuid, RDF.type, CRM["E3_Condition_State"]))
                docgraph2.add((conditionuuid, RDFS.label, Literal("Condition of left board marker of " + shelfmark, lang="en")))
                docgraph2.add((leftliftingtabuuid, CRM["P44_has_condition"], conditionuuid))
                docgraph2.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.brokenoff")))

        elif row["leftboard"] == 0: # this is the right board
            if row["conditionuuid"] is None:
                newuuid = str(uuid.uuid4())
                conditionuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE LiftingTabsCondition SET conditionuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                conditionuuid = URIRef(row["conditionuuid"], str(STCATH))

            graph.add((conditionuuid, RDF.type, CRM["E3_Condition_State"]))
            graph.add((conditionuuid, RDFS.label, Literal("Condition of right board marker of " + shelfmark, lang="en")))
            graph.add((rightliftingtabuuid, CRM["P44_has_condition"], conditionuuid))

            if row["msid"] == doci2:
                docgraph2.add((conditionuuid, RDF.type, CRM["E3_Condition_State"]))
                docgraph2.add((conditionuuid, RDFS.label, Literal("Condition of right board marker of " + shelfmark, lang="en")))
                docgraph2.add((rightliftingtabuuid, CRM["P44_has_condition"], conditionuuid))
                docgraph2.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.brokenoff")))

        if row["condition"] == "Broken off":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.brokenoff")))
        elif row["condition"] == "Broken and Sewn":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.brokenandsewn")))
        elif row["condition"] == "Missing":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.missing")))
        elif row["condition"] == "Sound":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.sound")))
        elif row["condition"] == "Worn":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.worn")))
        elif row["condition"] == "Detached":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.detached")))
        elif row["condition"] == "Dangling":
            graph.add((conditionuuid, CRM["P2_has_type"], URIRef("http://stcath.dangling")))

    # documentation drawing
    dot1 = visualise_graph(docgraph1, 'MS without board strap markers', "forth")
    dot2 = visualise_graph(docgraph2, 'MS with board strap markers', "forth")
    dot1.render('liftingtabs/liftingtabs-1.gv', format='svg')
    dot2.render('liftingtabs/liftingtabs-2.gv', format='svg')

    # serialise the graph
    graph.serialize(destination='liftingtabs/liftingtabs.ttl', format='turtle', encoding="utf-8")
    docgraph1.serialize(destination='liftingtabs/liftingtabs-doc-1.n3', format='n3', encoding="utf-8")
    docgraph2.serialize(destination='liftingtabs/liftingtabs-doc-2.n3', format='n3', encoding="utf-8")