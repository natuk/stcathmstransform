from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
import uuid
from namespaces import apply_namespaces, get_namespace
from crmviz.visualise import visualise_graph

def openingcharacteristics(mydb, cursor, cursorupdate):
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

    # deal with thesaurus concepts
    graph.add((URIRef("http://vocab.getty.edu/aat/300022525"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300022525"), SKOS.prefLabel, Literal("protractors", lang="en")))
    graph.add((URIRef("http://stcath.leftofcentre"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.leftofcentre"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.leftofcentre"), SKOS.prefLabel, Literal("left of centre (textblock measurement)", lang="en")))
    graph.add((URIRef("http://stcath.centre"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.centre"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.centre"), SKOS.prefLabel, Literal("centre (textblock measurement)", lang="en")))
    graph.add((URIRef("http://stcath.rightofcentre"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.rightofcentre"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.rightofcentre"), SKOS.prefLabel, Literal("right of centre (textblock measurement)", lang="en")))
    graph.add((URIRef("http://stcath.rightboardopeningangle"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.rightboardopeningangle"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.rightboardopeningangle"), SKOS.prefLabel, Literal("right board opening angle", lang="en")))
    graph.add((URIRef("http://stcath.leftboardopeningangle"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.leftboardopeningangle"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.leftboardopeningangle"), SKOS.prefLabel, Literal("left board opening angle", lang="en")))
    graph.add((URIRef("http://stcath.degrees"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.degrees"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.degrees"), SKOS.prefLabel, Literal("degrees (angle measuring units)", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300266529"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300266529"), SKOS.prefLabel, Literal('rulers', lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://vocab.getty.edu/aat/300379097"), SKOS.prefLabel, Literal('millimeters', lang="en")))
    graph.add((URIRef("http://stcath.closedbook"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.closedbook"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.closedbook"), SKOS.prefLabel, Literal('closed book thickness', lang="en")))
    graph.add((URIRef("http://stcath.textblockbreaks"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.textblockbreaks"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.textblockbreaks"), SKOS.prefLabel, Literal('textblock breaks', lang="en")))
    graph.add((URIRef("http://stcath.nooftextblockbreaks"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.nooftextblockbreaks"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.nooftextblockbreaks"), SKOS.prefLabel, Literal('number of textblock breaks', lang="en")))
    graph.add((URIRef("http://stcath.structurebreakdown"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.structurebreakdown"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.structurebreakdown"), SKOS.prefLabel, Literal('structure breakdown (condition)', lang="en")))

    doci1 = 903 # select a row as an example for the documentation graph
    doci2 = 866

    # 1_1_OpeningCharacteristics
    cursor.execute("SELECT mss.msuuid, mss.cataloguename, bld.surveyeventuuid, oc.* FROM `1_1_OpeningCharacteristics` oc INNER JOIN MSs mss ON oc.msid=mss.id INNER JOIN `1_0_BoxingLeavesDate` bld ON bld.msid=mss.id WHERE oc.msid=903 OR oc.msid=866 ORDER BY oc.msid ASC")
    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        shelfmark = row["cataloguename"]
        msuuid = URIRef(row["msuuid"], str(STCATH))
        # measurement event for measuring opening angles
        if row["measurementuuid"] is None:
            newuuid = str(uuid.uuid4())
            measurementuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_1_OpeningCharacteristics SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            measurementuuid = URIRef(row["measurementuuid"], str(STCATH))
        graph.add((measurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
        graph.add((measurementuuid, RDFS.label, Literal('Measurement of textblock opening angles of ' + shelfmark, lang="en")))
        graph.add((measurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
        graph.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300022525")))  # measurement used measuring box
        graph.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], measurementuuid))  # measurement event is part of survey event
        # left of centre
        if row["leftofcentre"] is not None:
            if row["leftofcentreuuid"] is None:
                newuuid = str(uuid.uuid4())
                leftofcentredimensionuuid = URIRef(newuuid, 'stcath')
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET leftofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                leftofcentredimensionuuid = URIRef(row["leftofcentreuuid"], 'stcath')
            graph.add((leftofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            graph.add((leftofcentredimensionuuid, RDFS.label, Literal('Left of centre of ' + shelfmark, lang="en")))
            graph.add((measurementuuid, CRM["P40_observed_dimension"], leftofcentredimensionuuid))  # measurement observes the dimension
            graph.add((leftofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftofcentre")))  # dimension has type left of centre
            graph.add((leftofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["leftofcentre"]))))  # dimension has value from the db
            graph.add((leftofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
        # centre
        if row["centre"] is not None:
            if row["centreuuid"] is None:
                newuuid = str(uuid.uuid4())
                centredimensionuuid = URIRef(newuuid, 'stcath')
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET centreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                centredimensionuuid = URIRef(row["centreuuid"], 'stcath')
            graph.add((centredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            graph.add((centredimensionuuid, RDFS.label, Literal('Centre of ' + shelfmark, lang="en")))
            graph.add((measurementuuid, CRM["P40_observed_dimension"], centredimensionuuid))  # measurement observes the dimension
            graph.add((centredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.centre")))  # dimension has type left of centre
            graph.add((centredimensionuuid, CRM["P90_has_value"], Literal(str(row["centre"]))))  # dimension has value from the db
            graph.add((centredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
        # right of centre
        if row["rightofcentre"] is not None:
            if row["rightofcentreuuid"] is None:
                newuuid = str(uuid.uuid4())
                rightofcentredimensionuuid = URIRef(newuuid, 'stcath')
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET rightofcentreuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                rightofcentredimensionuuid = URIRef(row["rightofcentreuuid"], 'stcath')
            graph.add((rightofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            graph.add((rightofcentredimensionuuid, RDFS.label, Literal('Right of centre of ' + shelfmark, lang="en")))
            graph.add((measurementuuid, CRM["P40_observed_dimension"], rightofcentredimensionuuid))  # measurement observes the dimension
            graph.add((rightofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.rightofcentre")))  # dimension has type right of centre
            graph.add((rightofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["rightofcentre"]))))  # dimension has value from the db
            graph.add((rightofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
        # right board TODO: provision for -1 (broken/split) -2 (detached) -3 (missing)
        if row["rightboard"] is not None:
            if row["rightboard"] != -1 and row["rightboard"] != -2 and row["rightboard"] !=-3:
                if row["rightboarduuid"] is None:
                    newuuid = str(uuid.uuid4())
                    rightboarddimensionuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET rightboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    rightboarddimensionuuid = URIRef(row["rightboarduuid"], 'stcath')
                graph.add((rightboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
                graph.add((rightboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
                graph.add((measurementuuid, CRM["P40_observed_dimension"], rightboarddimensionuuid))  # measurement observes the dimension
                graph.add((rightboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftboardopeningangle")))  # dimension has type right board
                graph.add((rightboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["rightboard"]))))  # dimension has value from the db
                graph.add((rightboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
        # left board
        if row["leftboard"] is not None:
            if row["leftboard"] != -1 and row["leftboard"] != -2 and row["leftboard"] !=-3:
                if row["leftboarduuid"] is None:
                    newuuid = str(uuid.uuid4())
                    leftofcentredimensionuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET leftboarduuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    leftboarddimensionuuid = URIRef(row["leftboarduuid"], 'stcath')
                graph.add((leftboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
                graph.add((leftboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
                graph.add((measurementuuid, CRM["P40_observed_dimension"], leftboarddimensionuuid))  # measurement observes the dimension
                graph.add((leftboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftboardopeningangle")))  # dimension has type left board
                graph.add((leftboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["leftboard"]))))  # dimension has value from the db
                graph.add((leftboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
        # closed board min thickness
        if row["closedbook"] is not None:
            if row["closedbookmeasurementuuid"] is None:
                newuuid = str(uuid.uuid4())
                closedbookmeasurementuuid = URIRef(newuuid, 'stcath')
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookmeasurementuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookmeasurementuuid = URIRef(row["closedbookmeasurementuuid"], 'stcath')
            graph.add((closedbookmeasurementuuid, RDF.type, CRM["E16_Measurement"])) # type the min thickness measurement event
            graph.add((closedbookmeasurementuuid, RDFS.label, Literal('Measurement of minimum thickness of ' + shelfmark, lang="en")))  # label the measurement
            graph.add((closedbookmeasurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript
            graph.add((closedbookmeasurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300266529")))  # measurement used ruler
            graph.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], closedbookmeasurementuuid))  # measurement event is part of survey event
            if row["closedbookdimensionuuid"] is None:
                newuuid = str(uuid.uuid4())
                closedbookdimensionuuid = URIRef(newuuid, 'stcath')
                # update the database
                sql = "UPDATE 1_1_OpeningCharacteristics SET closedbookdimensionuuid=%s WHERE msid=%s"
                val = (newuuid, row["msid"])
                cursorupdate.execute(sql, val)
                mydb.commit()
            else:
                closedbookdimensionuuid = URIRef(row["closedbookdimensionuuid"], 'stcath')
            graph.add((closedbookdimensionuuid, RDF.type, CRM["E54_Dimension"])) # type the dimension
            graph.add((closedbookdimensionuuid, RDFS.label, Literal('Minimum thickness of ' + shelfmark, lang="en"))) # label of minimum thickness dimension
            graph.add((closedbookmeasurementuuid, CRM["P40_observed_dimension"], closedbookdimensionuuid))  # measurement observes the dimension
            graph.add((closedbookdimensionuuid, CRM["P90_has_value"], Literal(str(row["closedbook"]))))
            graph.add((closedbookdimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))
            graph.add((closedbookdimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.closedbook")))

        # textblockbreaks
        if row["textblockbreaks"] is not None and row["textblockbreaks"] > 0:
            if row["textblockbreaks"] < 10: # make it a measurement
                if row["textblockbreaksmeasurementuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksmeasurementuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksmeasurementuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksmeasurementuuid = URIRef(row["textblockbreaksmeasurementuuid"], 'stcath')
                graph.add((textblockbreaksmeasurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
                graph.add((textblockbreaksmeasurementuuid, RDFS.label, Literal('Counting of textblock breaks of ' + shelfmark, lang="en")))
                graph.add((textblockbreaksmeasurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
                graph.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], textblockbreaksmeasurementuuid))  # measurement event is part of survey event
                if row["textblockbreaksdimensionuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksdimensionuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksdimensionuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksdimensionuuid = URIRef(row["textblockbreaksdimensionuuid"], 'stcath')
                graph.add((textblockbreaksdimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
                graph.add((textblockbreaksdimensionuuid, RDFS.label, Literal('Number of textblock breaks of ' + shelfmark, lang="en")))
                graph.add((textblockbreaksmeasurementuuid, CRM["P40_observed_dimension"], textblockbreaksdimensionuuid))
                graph.add((textblockbreaksdimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.nooftextblockbreaks")))  # dimension has type right board
                graph.add((textblockbreaksdimensionuuid, CRM["P90_has_value"], Literal(str(row["textblockbreaks"]))))  # dimension has value from the db
                graph.add((textblockbreaksdimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.textblockbreaks")))  # dimension has unit textblockbreaks
            else:
                if row["textblockbreaksmeasurementuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksconditionassessmentuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksmeasurementuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksconditionassessmentuuid = URIRef(row["textblockbreaksmeasurementuuid"], 'stcath')
                graph.add((textblockbreaksconditionassessmentuuid, RDF.type, CRM["E14_Condition_Assessment"]))  # rdf type the condition assessmnt
                graph.add((textblockbreaksconditionassessmentuuid, RDFS.label, Literal('Assessment of textblock breaks of ' + shelfmark, lang="en")))
                graph.add((textblockbreaksconditionassessmentuuid, CRM["P34_concerned"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
                graph.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], textblockbreaksconditionassessmentuuid))  # measurement event is part of survey event
                if row["textblockbreaksdimensionuuid"] is None:
                    newuuid = str(uuid.uuid4())
                    textblockbreaksconditionuuid = URIRef(newuuid, 'stcath')
                    # update the database
                    sql = "UPDATE 1_1_OpeningCharacteristics SET textblockbreaksdimensionuuid=%s WHERE msid=%s"
                    val = (newuuid, row["msid"])
                    cursorupdate.execute(sql, val)
                    mydb.commit()
                else:
                    textblockbreaksconditionuuid = URIRef(row["textblockbreaksdimensionuuid"], 'stcath')
                graph.add((textblockbreaksconditionuuid, RDF.type, CRM["E3_Condition_State"]))  # rdf type the condition
                graph.add((textblockbreaksconditionuuid, RDFS.label, Literal('Textblock breaks (condition) of ' + shelfmark, lang="en")))
                graph.add((textblockbreaksconditionassessmentuuid, CRM["P35_has_identified"], textblockbreaksconditionuuid))
                graph.add((textblockbreaksconditionuuid, CRM["P2_has_type"], URIRef("http://stcath.structurebreakdown")))  # condition has type

        if row["msid"] == doci1: # create the documentation graph for few textblock breaks and a intact boards
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300022525"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300022525"), SKOS.prefLabel, Literal("protractors", lang="en")))
            docgraph1.add((URIRef("http://stcath.leftofcentre"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.leftofcentre"), SKOS.prefLabel, Literal("left of centre (textblock measurement)", lang="en")))
            docgraph1.add((URIRef("http://stcath.centre"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.centre"), SKOS.prefLabel, Literal("centre (textblock measurement)", lang="en")))
            docgraph1.add((URIRef("http://stcath.rightofcentre"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.rightofcentre"), SKOS.prefLabel, Literal("right of centre (textblock measurement)", lang="en")))
            docgraph1.add((URIRef("http://stcath.rightboardopeningangle"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.rightboardopeningangle"), SKOS.prefLabel, Literal("right board opening angle", lang="en")))
            docgraph1.add((URIRef("http://stcath.leftboardopeningangle"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.leftboardopeningangle"), SKOS.prefLabel, Literal("left board opening angle", lang="en")))
            docgraph1.add((URIRef("http://stcath.degrees"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.degrees"), SKOS.prefLabel, Literal("degrees (angle measuring units)", lang="en")))
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300266529"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300266529"), SKOS.prefLabel, Literal('rulers', lang="en")))
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://vocab.getty.edu/aat/300379097"), SKOS.prefLabel, Literal('millimeters', lang="en")))
            docgraph1.add((URIRef("http://stcath.closedbook"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.closedbook"), SKOS.prefLabel, Literal('closed book thickness', lang="en")))
            docgraph1.add((URIRef("http://stcath.textblockbreaks"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.textblockbreaks"), SKOS.prefLabel, Literal('textblock breaks', lang="en")))
            docgraph1.add((URIRef("http://stcath.nooftextblockbreaks"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.nooftextblockbreaks"), SKOS.prefLabel, Literal('number of textblock breaks', lang="en")))
            docgraph1.add((URIRef("http://stcath.structurebreakdown"), RDF.type, CRM["E55_Type"]))
            docgraph1.add((URIRef("http://stcath.structurebreakdown"), SKOS.prefLabel, Literal('structure breakdown (condition)', lang="en")))
            docgraph1.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph1.add((msuuid, RDFS.label, Literal(shelfmark, lang="en")))
            docgraph1.add((URIRef(row["surveyeventuuid"], 'stcath'), RDF.type, CRM["E13_Attribute_Assignment"]))  # rdf type the survey event
            docgraph1.add((URIRef(row["surveyeventuuid"], 'stcath'), RDFS.label, Literal('Survey event for ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
            docgraph1.add((measurementuuid, RDFS.label, Literal('Measurement of textblock opening angles of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P39_measured"], msuuid)) # measurement event measured the manuscript TODO: point this to the textblock, not the MS
            docgraph1.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300022525")))  # measurement used measuring box
            docgraph1.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], measurementuuid))  # measurement event is part of survey event
            docgraph1.add((leftofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((leftofcentredimensionuuid, RDFS.label, Literal('Left of centre of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P40_observed_dimension"], leftofcentredimensionuuid))  # measurement observes the dimension
            docgraph1.add((leftofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftofcentre")))  # dimension has type left of centre
            docgraph1.add((leftofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["leftofcentre"]))))  # dimension has value from the db
            docgraph1.add((leftofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph1.add((centredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((centredimensionuuid, RDFS.label, Literal('Centre of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P40_observed_dimension"], centredimensionuuid))  # measurement observes the dimension
            docgraph1.add((centredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.centre")))  # dimension has type left of centre
            docgraph1.add((centredimensionuuid, CRM["P90_has_value"], Literal(str(row["centre"]))))  # dimension has value from the db
            docgraph1.add((centredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph1.add((rightofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((rightofcentredimensionuuid, RDFS.label, Literal('Right of centre of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P40_observed_dimension"], rightofcentredimensionuuid))  # measurement observes the dimension
            docgraph1.add((rightofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.rightofcentre")))  # dimension has type right of centre
            docgraph1.add((rightofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["rightofcentre"]))))  # dimension has value from the db
            docgraph1.add((rightofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph1.add((rightboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((rightboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P40_observed_dimension"], rightboarddimensionuuid))  # measurement observes the dimension
            docgraph1.add((rightboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.rightboardopeningangle")))  # dimension has type right board
            docgraph1.add((rightboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["rightboard"]))))  # dimension has value from the db
            docgraph1.add((rightboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph1.add((leftboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((leftboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
            docgraph1.add((measurementuuid, CRM["P40_observed_dimension"], leftboarddimensionuuid))  # measurement observes the dimension
            docgraph1.add((leftboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftboardopeningangle")))  # dimension has type left board
            docgraph1.add((leftboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["leftboard"]))))  # dimension has value from the db
            docgraph1.add((leftboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph1.add((closedbookmeasurementuuid, RDF.type, CRM["E16_Measurement"]))  # type the min thickness measurement event
            docgraph1.add((closedbookmeasurementuuid, RDFS.label, Literal('Measurement of minimum thickness of ' + shelfmark, lang="en")))  # label the measurement
            docgraph1.add((closedbookmeasurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript
            docgraph1.add((closedbookmeasurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300266529")))  # measurement used ruler
            docgraph1.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], closedbookmeasurementuuid))  # measurement event is part of survey event
            docgraph1.add((closedbookdimensionuuid, RDF.type, CRM["E54_Dimension"]))  # type the dimension
            docgraph1.add((closedbookdimensionuuid, RDFS.label, Literal('Minimum thickness of ' + shelfmark, lang="en")))  # label of minimum thickness dimension
            docgraph1.add((closedbookmeasurementuuid, CRM["P40_observed_dimension"], closedbookdimensionuuid))  # measurement observes the dimension
            docgraph1.add((closedbookdimensionuuid, CRM["P90_has_value"], Literal(str(row["closedbook"]))))
            docgraph1.add((closedbookdimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))
            docgraph1.add((closedbookdimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.closedbook")))
            docgraph1.add((textblockbreaksmeasurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
            docgraph1.add((textblockbreaksmeasurementuuid, RDFS.label, Literal('Counting of textblock breaks of ' + shelfmark, lang="en")))
            docgraph1.add((textblockbreaksmeasurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
            docgraph1.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], textblockbreaksmeasurementuuid))  # measurement event is part of survey event
            docgraph1.add((textblockbreaksdimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph1.add((textblockbreaksdimensionuuid, RDFS.label, Literal('Number of textblock breaks of ' + shelfmark, lang="en")))
            docgraph1.add((textblockbreaksmeasurementuuid, CRM["P40_observed_dimension"], textblockbreaksdimensionuuid))
            docgraph1.add((textblockbreaksdimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.nooftextblockbreaks")))  # dimension has type right board
            docgraph1.add((textblockbreaksdimensionuuid, CRM["P90_has_value"], Literal(str(row["textblockbreaks"]))))  # dimension has value from the db
            docgraph1.add((textblockbreaksdimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.textblockbreaks")))  # dimension has unit textblockbreaks

        if row["msid"] == doci2:  # create the documentation graph for few textblock breaks and a intact boards
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300022525"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300022525"), SKOS.prefLabel, Literal("protractors", lang="en")))
            docgraph2.add((URIRef("http://stcath.leftofcentre"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.leftofcentre"), SKOS.prefLabel, Literal("left of centre (textblock measurement)", lang="en")))
            docgraph2.add((URIRef("http://stcath.centre"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.centre"), SKOS.prefLabel, Literal("centre (textblock measurement)", lang="en")))
            docgraph2.add((URIRef("http://stcath.rightofcentre"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.rightofcentre"), SKOS.prefLabel, Literal("right of centre (textblock measurement)", lang="en")))
            docgraph2.add((URIRef("http://stcath.rightboardopeningangle"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.rightboardopeningangle"), SKOS.prefLabel, Literal("right board opening angle", lang="en")))
            docgraph2.add((URIRef("http://stcath.leftboardopeningangle"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.leftboardopeningangle"), SKOS.prefLabel, Literal("left board opening angle", lang="en")))
            docgraph2.add((URIRef("http://stcath.degrees"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.degrees"), SKOS.prefLabel, Literal("degrees (angle measuring units)", lang="en")))
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300266529"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300266529"), SKOS.prefLabel, Literal('rulers', lang="en")))
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://vocab.getty.edu/aat/300379097"), SKOS.prefLabel, Literal('millimeters', lang="en")))
            docgraph2.add((URIRef("http://stcath.closedbook"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.closedbook"), SKOS.prefLabel, Literal('closed book thickness', lang="en")))
            docgraph2.add((URIRef("http://stcath.textblockbreaks"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.textblockbreaks"), SKOS.prefLabel, Literal('textblock breaks', lang="en")))
            docgraph2.add((URIRef("http://stcath.nooftextblockbreaks"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.nooftextblockbreaks"), SKOS.prefLabel, Literal('number of textblock breaks', lang="en")))
            docgraph2.add((URIRef("http://stcath.structurebreakdown"), RDF.type, CRM["E55_Type"]))
            docgraph2.add((URIRef("http://stcath.structurebreakdown"), SKOS.prefLabel, Literal('structure breakdown (condition)', lang="en")))
            docgraph2.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph2.add((msuuid, RDFS.label, Literal(shelfmark, lang="en")))
            docgraph2.add((URIRef(row["surveyeventuuid"], 'stcath'), RDF.type, CRM["E13_Attribute_Assignment"]))  # rdf type the survey event
            docgraph2.add((URIRef(row["surveyeventuuid"], 'stcath'), RDFS.label, Literal('Survey event for ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
            docgraph2.add((measurementuuid, RDFS.label, Literal('Measurement of textblock opening angles of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
            docgraph2.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300022525")))  # measurement used measuring box
            docgraph2.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], measurementuuid))  # measurement event is part of survey event
            docgraph2.add((leftofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph2.add((leftofcentredimensionuuid, RDFS.label, Literal('Left of centre of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P40_observed_dimension"], leftofcentredimensionuuid))  # measurement observes the dimension
            docgraph2.add((leftofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftofcentre")))  # dimension has type left of centre
            docgraph2.add((leftofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["leftofcentre"]))))  # dimension has value from the db
            docgraph2.add((leftofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph2.add((centredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph2.add((centredimensionuuid, RDFS.label, Literal('Centre of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P40_observed_dimension"], centredimensionuuid))  # measurement observes the dimension
            docgraph2.add((centredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.centre")))  # dimension has type left of centre
            docgraph2.add((centredimensionuuid, CRM["P90_has_value"], Literal(str(row["centre"]))))  # dimension has value from the db
            docgraph2.add((centredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph2.add((rightofcentredimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph2.add((rightofcentredimensionuuid, RDFS.label, Literal('Right of centre of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P40_observed_dimension"], rightofcentredimensionuuid))  # measurement observes the dimension
            docgraph2.add((rightofcentredimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.rightofcentre")))  # dimension has type right of centre
            docgraph2.add((rightofcentredimensionuuid, CRM["P90_has_value"], Literal(str(row["rightofcentre"]))))  # dimension has value from the db
            docgraph2.add((rightofcentredimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph2.add((rightboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph2.add((rightboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P40_observed_dimension"], rightboarddimensionuuid))  # measurement observes the dimension
            docgraph2.add((rightboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.rightboardopeningangle")))  # dimension has type right board
            docgraph2.add((rightboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["rightboard"]))))  # dimension has value from the db
            docgraph2.add((rightboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph2.add((leftboarddimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph2.add((leftboarddimensionuuid, RDFS.label, Literal('Right board opening angle of ' + shelfmark, lang="en")))
            docgraph2.add((measurementuuid, CRM["P40_observed_dimension"], leftboarddimensionuuid))  # measurement observes the dimension
            docgraph2.add((leftboarddimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.leftboardopeningangle")))  # dimension has type left board
            docgraph2.add((leftboarddimensionuuid, CRM["P90_has_value"], Literal(str(row["leftboard"]))))  # dimension has value from the db
            docgraph2.add((leftboarddimensionuuid, CRM["P91_has_unit"], URIRef("http://stcath.degrees")))  # dimension has unit degrees
            docgraph2.add((closedbookmeasurementuuid, RDF.type, CRM["E16_Measurement"]))  # type the min thickness measurement event
            docgraph2.add((closedbookmeasurementuuid, RDFS.label, Literal('Measurement of minimum thickness of ' + shelfmark, lang="en")))  # label the measurement
            docgraph2.add((closedbookmeasurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript
            docgraph2.add((closedbookmeasurementuuid, CRM["P125_used_object_of_type"], URIRef("http://vocab.getty.edu/aat/300266529")))  # measurement used ruler
            docgraph2.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], closedbookmeasurementuuid))  # measurement event is part of survey event
            docgraph2.add((closedbookdimensionuuid, RDF.type, CRM["E54_Dimension"]))  # type the dimension
            docgraph2.add((closedbookdimensionuuid, RDFS.label, Literal('Minimum thickness of ' + shelfmark, lang="en")))  # label of minimum thickness dimension
            docgraph2.add((closedbookmeasurementuuid, CRM["P40_observed_dimension"], closedbookdimensionuuid))  # measurement observes the dimension
            docgraph2.add((closedbookdimensionuuid, CRM["P90_has_value"], Literal(str(row["closedbook"]))))
            docgraph2.add((closedbookdimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))
            docgraph2.add((closedbookdimensionuuid, CRM["P2_has_type"], URIRef("http://stcath.closedbook")))
            docgraph2.add((textblockbreaksconditionassessmentuuid, RDF.type, CRM["E14_Condition_Assessment"]))  # rdf type the condition assessmnt
            docgraph2.add((textblockbreaksconditionassessmentuuid, RDFS.label, Literal('Assessment of textblock breaks of ' + shelfmark, lang="en")))
            docgraph2.add((textblockbreaksconditionassessmentuuid, CRM["P34_concerned"], msuuid))  # measurement event measured the manuscript TODO: point this to the textblock, not the MS
            docgraph2.add((URIRef(row["surveyeventuuid"], 'stcath'), CRM["P9_consists_of"], textblockbreaksconditionassessmentuuid))  # measurement event is part of survey event
            docgraph2.add((textblockbreaksconditionuuid, RDF.type, CRM["E3_Condition_State"]))  # rdf type the condition
            docgraph2.add((textblockbreaksconditionuuid, RDFS.label, Literal('Textblock breaks (condition) of ' + shelfmark, lang="en")))
            docgraph2.add((textblockbreaksconditionassessmentuuid, CRM["P35_has_identified"], textblockbreaksconditionuuid))
            docgraph2.add((textblockbreaksconditionuuid, CRM["P2_has_type"], URIRef("http://stcath.structurebreakdown")))  # condition has type

    # documentation drawing
    dot1 = visualise_graph(docgraph1, 'Opening characteristics - textblock breaks counted')
    dot1.render('openingcharacteristics/1-1-openingcharacteristics-1.gv', format='svg')
    dot2 = visualise_graph(docgraph2, 'Opening characteristics - textblock breaks as condition')
    dot2.render('openingcharacteristics/1-1-openingcharacteristics-2.gv', format='svg')

    # serialise the graph
    #graph.serialize(destination='openingcharacteristics/1-1-openingcharacteristics.ttl', format='turtle', encoding="utf-8")
    #docgraph1.serialize(destination='openingcharacteristics/1-1-openingcharacteristics-1.n3', format='n3', encoding="utf-8")