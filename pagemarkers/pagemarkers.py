from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
from rdflib.tools import rdf2dot
import uuid
from graphviz import Digraph
from namespaces import apply_namespaces, get_namespace
from visualise import visualise_graph

def pagemarkers(mydb, cursor, cursorupdate):

    graph = Graph() # graph for the dataset
    docgraph = Graph() # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph = apply_namespaces(docgraph)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    # deal with thesaurus concepts
    graph.add((URIRef("http://w3id.org/lob/concept/5423"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/5423"), SKOS.prefLabel, Literal("leaf markers", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2945"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2945"), SKOS.prefLabel, Literal("leaf tab markers", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2944"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2944"), SKOS.prefLabel, Literal("leaf string markers", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014585"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014585"), RDFS.label, Literal("wax", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1658"), RDFS.label, Literal("tanned skin", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2468"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2468"), RDFS.label, Literal("silk", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2470"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2470"), RDFS.label, Literal("textile", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1481"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1481"), RDFS.label, Literal("paper", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1197"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1197"), RDFS.label, Literal("alum-tawed skin", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1485"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1485"), RDFS.label, Literal("parchment", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2474"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2474"), RDFS.label, Literal("thread", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014585"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300014585"), RDFS.label, Literal("wax", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/3855"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/3855"), RDFS.label, Literal("solid-coloured paper", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/3165"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/3165"), RDFS.label, Literal("paint (coating)", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/5429"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/5429"), RDFS.label, Literal("adhering", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/2362"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/2362"), RDFS.label, Literal("sewing (techniques)", lang="en")))
    graph.add((URIRef("http://stcath.looped"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.looped"), RDFS.label, Literal("looped", lang="en")))
    graph.add((URIRef("http://w3id.org/lob/concept/1476"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://w3id.org/lob/concept/1476"), RDFS.label, Literal("painting (techniques)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129361"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129361"), RDFS.label, Literal("blue (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127490"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127490"), RDFS.label, Literal("brown (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDFS.label, Literal("gold (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127526"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127526"), RDFS.label, Literal("dark brown", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126272"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126272"), RDFS.label, Literal("deep red", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126225"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300126225"), RDFS.label, Literal("red (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127503"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127503"), RDFS.label, Literal("light brown", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDFS.label, Literal("gold (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127794"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300127794"), RDFS.label, Literal("yellow (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128438"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300128438"), RDFS.label, Literal("green (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129394"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300129394"), RDFS.label, Literal("deep blue", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300311191"), RDFS.label, Literal("gold (color)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300056130"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300056130"), RDFS.label, Literal("color (perceived attribute)", lang="en")))
    graph.add((URIRef("http://stcath.sound"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.sound"), RDFS.label, Literal("sound", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300131111"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300131111"), RDFS.label, Literal("detached (positional attribute) ", lang="en")))
    graph.add((URIRef("http://stcath.brokenoff"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.brokenoff"), RDFS.label, Literal("broken off", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300219449"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300219449"), RDFS.label, Literal("wear", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300379497"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300379497"), RDFS.label, Literal("stains (damage)", lang="en")))
    graph.add((URIRef("http://stcath.missing"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.missing"), RDFS.label, Literal("missing", lang="en")))
    graph.add((URIRef("http://stcath.trimmedforedge"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.trimmedforedge"), RDFS.label, Literal("trimmed foredge", lang="en")))
    graph.add((URIRef("http://stcath.dangling"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.dangling"), RDFS.label, Literal("dangling", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300380188"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300380188"), RDFS.label, Literal("rodent (damage)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300230031"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300230031"), RDFS.label, Literal("insect damage", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300053077"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300053077"), RDFS.label, Literal("abrasion (condition or effect)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300219449"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300219449"), RDFS.label, Literal("wear", lang="en")))
    graph.add((URIRef("http://stcath.dirty"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.dirty"), RDFS.label, Literal("dirty", lang="en")))

    # 1_1_PageMarkers
    cursor.execute("SELECT mss.msuuid, pms.yesnonk FROM MSs mss INNER JOIN `1_2_PageMarkers` pms on mss.id=pms.msid")
    rows = cursor.fetchall()

    for row in rows:
        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["yesnonk"] == "no":
            graph.add((msuuid, CRM["NTP46_is_not_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/5423")))
        elif row["yesnonk"] == "yes":
            graph.add((msuuid, CRM["TP46_is_composed_of_physical_thing_of_type"], URIRef("http://w3id.org/lob/concept/5423")))

    # Pagemarkers
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, pm.id, pm.uuid, pm.type, pm.attachment, pm.partadditionuuid, pm.material FROM PageMarkers pm INNER JOIN MSs mss ON pm.msid=mss.id")
    rows = cursor.fetchall()

    for row in rows:
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        # pagemarker series attachment, type, material
        if row["uuid"] is None:
            newuuid = str(uuid.uuid4())
            pagemarkeruuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE PageMarkers SET uuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            pagemarkeruuid = URIRef(row["uuid"], str(STCATH))

        if row["type"] is not None:
            if bool(row["type"] == "Folded") | bool(row["type"] == "Folded and knotted") | row["type"] == "Straight" | bool(row["type"] == "Platted") | bool(row["type"] == "Tied") | bool(row["type"] == "Twisted thread") | bool(row["type"] == "Thread"):
                graph.add((pagemarkeruuid, RDF.type, CRM["E22_Man-Made_Object"])) # page markers of these types are separate things.
                graph.add((msuuid, CRM["P46_composed_of"], pagemarkeruuid))  # book is composed of page markers
            elif bool(row["type"] == "Wax") | bool(row["type"] == "Painted"):
                graph.add((pagemarkeruuid, RDF.type, CRM["E25_Man-Made_Feature"]))  # page markers of these types are features, i.e. cannot be removed.
                graph.add((msuuid, CRM["P56_bears_feature"], pagemarkeruuid))  # book bears feature page markers
            graph.add((pagemarkeruuid, RDFS.label, Literal("Page-markers of " + shelfmark)))

            if bool(row["type"] == "Folded") | bool(row["type"] == "Folded and knotted"):
                graph.add((pagemarkeruuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2945")))
            if row["type"] == "Straight":
                graph.add((pagemarkeruuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/5423")))
            if bool(row["type"] == "Platted") | bool(row["type"] == "Tied") | bool(row["type"] == "Twisted thread") | bool(row["type"] == "Thread"):
                graph.add((pagemarkeruuid, CRM["P2_has_type"], URIRef("http://w3id.org/lob/concept/2944")))
            if bool(row["type"] == "Wax") | bool(row["type"] == "Painted"):
                # TODO: consider a new type of page marker which is a feature
                pass

        if row["attachment"] is not None:
            if row["partadditionuuid"] is None:
                newuuid = str(uuid.uuid4())
                partadditionuuid = URIRef(newuuid, str(STCATH))
                # update the database
                sql = "UPDATE PageMarkers SET partadditionuuid=%s WHERE id=%s"
                val = (newuuid, row["id"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                partadditionuuid = URIRef(row["partadditionuuid"], str(STCATH))
            graph.add((partadditionuuid, RDF.type, CRM["E79_Part_Addition"])) # type the part addition event
            graph.add((partadditionuuid, RDFS.label, Literal("Addition of pagemarkers to " + shelfmark, lang="en"))) # label
            graph.add((partadditionuuid, CRM["P110_augmented"], msuuid)) # augmented book
            graph.add((partadditionuuid, CRM["P111_added"], pagemarkeruuid)) # added pagemarker
            if bool(row["attachment"] == "Adhesive"):
                partadditiontechniqueuuid = URIRef("http://w3id.org/lob/concept/5429")
            elif bool(row["attachment"] == "Sewn"):
                partadditiontechniqueuuid = URIRef("http://w3id.org/lob/concept/2362")
            elif bool(row["attachment"] == "Looped"):
                partadditiontechniqueuuid = URIRef("http://stcath.looped")
            elif bool(row["attachment"] == "Paint"):
                partadditiontechniqueuuid = URIRef("http://w3id.org/lob/concept/1476")
            graph.add((partadditionuuid, CRM["P32_used_general_technique"], partadditiontechniqueuuid))

        if row["material"] is not None:
            if bool(row["material"] == "Candle wax"):
                materialuuid = URIRef("http://vocab.getty.edu/aat/300014585")
            elif row["material"] == "Tanned leather":
                materialuuid = URIRef("http://w3id.org/lob/concept/1658")
            elif row["material"] == "Silk":
                materialuuid = URIRef("http://w3id.org/lob/concept/2468")
            elif row["material"] == "Textile":
                materialuuid = URIRef("http://w3id.org/lob/concept/2470")
            elif row["material"] == "Paper":
                materialuuid = URIRef("http://w3id.org/lob/concept/1481")
            elif row["material"] == "Tawed leather":
                materialuuid = URIRef("http://w3id.org/lob/concept/1197")
            elif row["material"] == "Parchment":
                materialuuid = URIRef("http://w3id.org/lob/concept/1485")
            elif row["material"] == "Natural thread":
                materialuuid = URIRef("http://w3id.org/lob/concept/2474")
            elif row["material"] == "Wax":
                materialuuid = URIRef("http://vocab.getty.edu/aat/300014585")
            elif row["material"] == "Tinted paper":
                materialuuid = URIRef("http://w3id.org/lob/concept/3855")
            elif row["material"] == "Paint":
                materialuuid = URIRef("http://w3id.org/lob/concept/3165")
            graph.add((pagemarkeruuid, CRM["P45_consists_of"], materialuuid))

    # PageMarkers colour
    cursor.execute("SELECT pm.uuid, pmc.pagemarkercolour FROM PageMarkersColour pmc INNER JOIN PageMarkers pm on pm.id=pmc.pagemarker")
    rows = cursor.fetchall()
    pagemarkeruuid = URIRef(row["uuid"], str(STCATH))
    for row in rows:
        if row["pagemarkercolour"] is not None and row["pagemarkercolour"] != "-":
            if row["pagemarkercolour"] == "Natural":
                graph.add((pagemarkeruuid, CRM["NTP56_does_not_bear_feature_of_type"], URIRef("http://vocab.getty.edu/aat/300056130"))) # pagemarker does not have colour
            if row["pagemarkercolour"] == "Blue":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300129361")
            if row["pagemarkercolour"] == "Brown":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300127490")
            if row["pagemarkercolour"] == "Gold" or row["pagemarkercolour"] == "Gilded" or row["pagemarkercolour"] == "Gilt":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300311191")
            if row["pagemarkercolour"] == "Dark brown":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300127526")
            if row["pagemarkercolour"] == "Deep red":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300126272")
            if row["pagemarkercolour"] == "Red":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300126225")
            if row["pagemarkercolour"] == "Light brown":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300127503")
            if row["pagemarkercolour"] == "Yellow":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300127794")
            if row["pagemarkercolour"] == "Green":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300128438")
            if row["pagemarkercolour"] == "Deep blue":
                colouruuid = URIRef("http://vocab.getty.edu/aat/300129394")
            graph.add((pagemarkeruuid, CRM["P56_bears_feature"], colouruuid))

    # Pagemarker locations
    cursor.execute("SELECT pm.uuid AS pagemarkersetuuid, pml.id, pml.uuid AS pagemarkersubsetuuid, pml.pagemarker, pml.pagemarkerlocation, pml.locationno FROM PageMarkersLocation pml INNER JOIN PageMarkers pm ON pm.id=pml.pagemarker")
    rows = cursor.fetchall()

    for row in rows:
        pagemarkersetuuid = URIRef(row["pagemarkersetuuid"], str(STCATH)) # we should have a uuid for every set of pagemerkers by now
        pagemarkersetlabel = graph.preferredLabel(pagemarkersetuuid, lang="en") # get the pagemarkers set label
        # find the total number of pagemarkers in this set
        sql = "SELECT SUM(locationno) FROM `PageMarkersLocation` WHERE pagemarker=%s"
        val = (row["pagemarker"])
        cursor.execute(sql, val)
        pagemarkersettotal = cursor.fetchall()
        # add the number of parts for it
        graph.add((pagemarkersetuuid, CRM["P57_has_number_of_parts"], Literal(pagemarkersettotal[0]["locationno"])))
        # pagemarker subsets
        if row["pagemarkersubsetuuid"] is None:
            newuuid = str(uuid.uuid4())
            pagemarkersubsetuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE PageMarkersLocation SET uuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            pagemarkersubsetuuid = URIRef(row["pagemarkersubsetuuid"], str(STCATH))
        pmstype = graph.value(pagemarkersetuuid, RDF.type) # find the rdf type of the pagemarker set, we assume that the subset is of the same type
        graph.add((pagemarkersubsetuuid, RDF.type, pmstype))
        graph.add((pagemarkersubsetuuid, RDFS.label, Literal("Subset of'" + pagemarkersetlabel + "' on " + row["pagemarkerlocation"], lang="en")))
        graph.add((pagemarkersetuuid, CRM["P46_is_composed_of"], pagemarkersubsetuuid))
        graph.add((pagemarkersubsetuuid, CRM["P57_has_number_of_parts"], Literal(row["locationno"]))) # specify the pagemarker subset in the specific location
        if row["pagemarkerlocation"] is not None:
            if row["pagemarkerlocation"] == "Foredge":
                # TODO: query the graph to get the URI of the textblock foredge place
                pass
            elif row["pagemarkerlocation"] == "Head":
                # TODO: query the graph to get the URI of the textblock foredge place
                pass
            elif row["pagemarkerlocation"] == "Tail":
                # TODO: query the graph to get the URI of the textblock foredge place
                pass
            # graph.add((pagemarkersubsetuuid, CRM["P53_has_former_or_current_location"], *place*))

    # Pagemarker locations
    cursor.execute("SELECT pm.uuid AS pagemarkersetuuid, pmc.id, pmc.uuid AS pagemarkersubsetuuid, pmc.pagemarker, pmc.condition, pmc.conditionuuid, pmc.conditionno FROM PageMarkersCondition pmc INNER JOIN PageMarkers pm ON pm.id=pmc.pagemarker")
    rows = cursor.fetchall()

    for row in rows:
        pagemarkersetuuid = URIRef(row["pagemarkersetuuid"], str(STCATH)) # we should have a uuid for every set of pagemerkers by now
        pagemarkersetlabel = graph.preferredLabel(pagemarkersetuuid, lang="en") # get the pagemarkers set label
        # pagemarker subsets
        if row["pagemarkersubsetuuid"] is None:
            newuuid = str(uuid.uuid4())
            pagemarkersubsetuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE PageMarkersCondition SET uuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            pagemarkersubsetuuid = URIRef(row["pagemarkersubsetuuid"], str(STCATH))
        pmstype = graph.value(pagemarkersetuuid, RDF.type) # find the rdf type of the pagemarker set, we assume that the subset is of the same type
        graph.add((pagemarkersubsetuuid, RDF.type, pmstype))
        graph.add((pagemarkersubsetuuid, RDFS.label, Literal("Subset of '" + pagemarkersetlabel + "' with condition " + row["condition"], lang="en")))
        graph.add((pagemarkersetuuid, CRM["P46_is_composed_of"], pagemarkersubsetuuid))
        graph.add((pagemarkersubsetuuid, CRM["P57_has_number_of_parts"], Literal(row["conditionno"])))  # specify the pagemarker subset in the specific location
        # subset condition
        if row["conditionuuid"] is None:
            newuuid = str(uuid.uuid4())
            conditionuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE PageMarkersCondition SET conditionuuid=%s WHERE id=%s"
            val = (newuuid, row["id"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            conditionuuid = URIRef(row["conditionuuid"], str(STCATH))
        graph.add((conditionuuid, RDF.type, CRM["E3_Condition_State"]))
        graph.add((conditionuuid, RDFS.label, Literal("Condition of subset of " + pagemarkersetlabel, lang="en")))
        graph.add((pagemarkersubsetuuid, CRM["P44_has_condition"], conditionuuid)) # subset of pagemarkers have a condition
        if row["condition"] is not None:
            if row["condition"] == "Sound":
                conditiontypeuuid = URIRef("http://stcath.sound")
            elif row["condition"] == "Detached":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300131111")
            elif row["condition"] == "Broken off":
                conditiontypeuuid = URIRef("http://stcath.brokenoff")
            elif row["condition"] == "Worn":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300219449")
            elif row["condition"] == "Stained":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300379497")
            elif row["condition"] == "Missing":
                conditiontypeuuid = URIRef("http://stcath.missing")
            elif row["condition"] == "Trimmed foredge":
                conditiontypeuuid = URIRef("http://stcath.trimmedforedge")
            elif row["condition"] == "Dangling":
                conditiontypeuuid = URIRef("http://stcath.dangling")
            elif row["condition"] == "Adhesive remains only":
                conditiontypeuuid = URIRef("http://stcath.missing")
                graph.add((conditionuuid, CRM["P3_has_note"], Literal(row["condition"], lang="en")))
            elif row["condition"] == "Rodent":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300380188")
            elif row["condition"] == "Insect damage":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300230031")
            elif row["condition"] == "Abraded in the fold":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300053077")
                graph.add((conditionuuid, CRM["P3_has_note"], Literal(row["condition"], lang="en")))
            elif row["condition"] == "Worn at foredge":
                conditiontypeuuid = URIRef("http://vocab.getty.edu/aat/300219449")
                graph.add((conditionuuid, CRM["P3_has_note"], Literal(row["condition"], lang="en")))
            elif row["condition"] == "Dirty":
                conditiontypeuuid = URIRef("http://stcath.dirty")
            graph.add((conditionuuid, CRM["P2_has_type"], conditiontypeuuid))

    # documentation drawing
    dot = visualise_graph(docgraph, 'Page-markers')
    dot.render('pagemarkers/pagemarkers.gv',format='svg')

    # serialise the graph
    graph.serialize(destination='pagemarkers/pagemarkers.ttl', format='turtle', encoding="utf-8")
    docgraph.serialize(destination='pagemarkers/pagemarkers-doc.n3', format='n3', encoding="utf-8")