from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
import uuid
from namespaces import apply_namespaces, get_namespace
from visualise import visualise_graph

def boxingleavesdate(mydb, cursor, cursorupdate):
    graph = Graph() # graph for the dataset
    docgraph = Graph() # graph for the documentation drawing
    # add namespaces
    graph = apply_namespaces(graph)
    docgraph = apply_namespaces(docgraph)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    # deal with thesaurus concepts
    graph.add((URIRef("http://stcath.measuringbox"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.measuringbox"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.measuringbox"), SKOS.prefLabel, Literal("measuring boxes", lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300055644"), RDF.type, CRM["E55_Type"]))  # height
    graph.add((URIRef("http://vocab.getty.edu/aat/300055644"), SKOS.prefLabel, Literal('height', lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300055647"), RDF.type, CRM["E55_Type"]))  # width
    graph.add((URIRef("http://vocab.getty.edu/aat/300055647"), SKOS.prefLabel, Literal('width', lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300055646"), RDF.type, CRM["E55_Type"]))  # thickness
    graph.add((URIRef("http://vocab.getty.edu/aat/300055646"), SKOS.prefLabel, Literal('thickness', lang="en")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E58_Measurement_Unit"])) # mm
    graph.add((URIRef("http://vocab.getty.edu/aat/300379097"), SKOS.prefLabel, Literal('millimeters', lang="en")))

    doci = 1  # set the desirable db row for the documentation example

    # 1_0_BoxingLeavesDate
    cursor.execute("SELECT mss.cataloguename, mss.msuuid, bld.* FROM 1_0_BoxingLeavesDate bld INNER JOIN MSs mss ON mss.id = bld.msid LIMIT 2")
    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        shelfmark = row["cataloguename"]

        msuuid = URIRef(row["msuuid"], str(STCATH))
        if row["measurementuuid"] is None: # if there is no measurementuuid, make one
            newuuid = str(uuid.uuid4())
            measurementuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET measurementuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else: # else just fetch it
            measurementuuid = URIRef(row["measurementuuid"], str(STCATH))

        # height
        if row["heightuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionhuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET heightuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionhuuid = URIRef(row["heightuuid"], str(STCATH))

        # width
        if row["widthuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionwuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionwuuid = URIRef(row["widthuuid"], str(STCATH))

        # thickness
        if row["thicknessuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensiontuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET thicknessuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensiontuuid = URIRef(row["thicknessuuid"], str(STCATH))

        # boxing status
        if row["boxingstatus"] is not None:
            boxingnote = row["boxingstatus"]
            if row["boxingnotes"] is not None:
                boxingnote = row["boxingstatus"] + " - " + row["boxingnotes"]

        # survey date
        if row["surveyeventuuid"] is None:
            newuuid = str(uuid.uuid4())
            surveyeventuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveyeventuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveyeventuuid = URIRef(row["surveyeventuuid"], str(STCATH))

        if row["surveytimespanuuid"] is None:
            newuuid = str(uuid.uuid4())
            surveytimespanuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET surveytimespanuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            surveytimespanuuid = URIRef(row["surveytimespanuuid"], str(STCATH))

        graph.add((measurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
        graph.add((measurementuuid, RDFS.label, Literal('Measurement of overall dimensions of ' + shelfmark, lang="en")))
        graph.add((measurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript
        graph.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://stcath.measuringbox")))  # measurement used measuring box
        graph.add((dimensionhuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
        graph.add((dimensionhuuid, RDFS.label, Literal('Height of ' + shelfmark, lang="en")))
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionhuuid))  # measurement observes the dimension
        graph.add((dimensionhuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055644")))  # dimension has type height
        graph.add((dimensionhuuid, CRM["P90_has_value"], Literal(str(row["height"]))))  # dimension has value from the db
        graph.add((dimensionhuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
        graph.add((dimensionwuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
        graph.add((dimensionwuuid, RDFS.label, Literal('Width of ' + shelfmark, lang="en")))
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionwuuid))  # measurement observes the dimension
        graph.add((dimensionwuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055647")))  # dimension has type width
        graph.add((dimensionwuuid, CRM["P90_has_value"], Literal(str(row["width"]))))  # dimension has value from the db
        graph.add((dimensionwuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
        graph.add((dimensiontuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
        graph.add((dimensiontuuid, RDFS.label, Literal('Thickness of ' + shelfmark, lang="en")))
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensiontuuid))  # measurement observes the dimension
        graph.add((dimensiontuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055646")))  # dimension has type thickness
        graph.add((dimensiontuuid, CRM["P90_has_value"], Literal(str(row["thickness"]))))  # dimension has value from the db
        graph.add((dimensiontuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
        graph.add((msuuid, CRM["P3_has_note"], Literal(boxingnote)))  # add boxing notes as a note to the manuscript node
        graph.add((surveyeventuuid, RDF.type, CRM["E13_Attribute_Assignment"]))  # rdf type the survey event
        graph.add((surveyeventuuid, RDFS.label, Literal('Survey event for ' + shelfmark, lang="en")))
        graph.add((surveytimespanuuid, RDF.type, CRM["E52_Time-Span"]))  # rdf type the survey event time-span
        graph.add((surveytimespanuuid, RDFS.label, Literal('Time-span of survey event for ' + shelfmark, lang="en")))
        graph.add((surveyeventuuid, CRM["P4_has_time-span"], surveytimespanuuid))  # survey event has time-span
        graph.add((surveyeventuuid, CRM["P9_consists_of"], measurementuuid)) # measurement event is part of survey event

        if row["surveydate"] is not None:
            graph.add((surveytimespanuuid, CRM["P82a_begin_of_the_begin"], Literal(str(row["surveydate"]).replace("00:00:00", "08:00:00").replace(" ", "T"))))
            graph.add((surveytimespanuuid, CRM["P82b_end_of_the_end"], Literal(str(row["surveydate"]).replace("00:00:00", "20:00:00").replace(" ", "T"))))

        if i == doci:
            docgraph.add((URIRef("http://stcath.measuringbox"), RDF.type, CRM["E55_Type"]))
            docgraph.add((URIRef("http://stcath.measuringbox"), SKOS.prefLabel, Literal("measuring boxes", lang="en")))
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055644"), RDF.type, CRM["E55_Type"]))  # height
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055644"), SKOS.prefLabel, Literal('height', lang="en")))
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055647"), RDF.type, CRM["E55_Type"]))  # width
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055647"), SKOS.prefLabel, Literal('width', lang="en")))
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055646"), RDF.type, CRM["E55_Type"]))  # thickness
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300055646"), SKOS.prefLabel, Literal('thickness', lang="en")))
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E58_Measurement_Unit"]))  # mm
            docgraph.add((URIRef("http://vocab.getty.edu/aat/300379097"), SKOS.prefLabel, Literal('millimeters', lang="en")))
            docgraph.add((msuuid, RDF.type, CRM["E22_Man-Made_Object"]))
            docgraph.add((msuuid, RDFS.label, Literal(str(row["cataloguename"]), lang="en")))
            docgraph.add((measurementuuid, RDF.type, CRM["E16_Measurement"]))  # rdf type the measurement
            docgraph.add((measurementuuid, RDFS.label, Literal('Measurement of overall dimensions of ' + shelfmark, lang="en")))
            docgraph.add((measurementuuid, CRM["P39_measured"], msuuid))  # measurement event measured the manuscript
            docgraph.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://stcath.measuringbox")))  # measurement used measuring box
            docgraph.add((dimensionhuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph.add((dimensionhuuid, RDFS.label, Literal('Height of ' + shelfmark, lang="en")))
            docgraph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionhuuid))  # measurement observes the dimension
            docgraph.add((dimensionhuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055644")))  # dimension has type height
            docgraph.add((dimensionhuuid, CRM["P90_has_value"], Literal(str(row["height"]))))  # dimension has value from the db
            docgraph.add((dimensionhuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
            docgraph.add((dimensionwuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph.add((dimensionwuuid, RDFS.label, Literal('Width of ' + shelfmark, lang="en")))
            docgraph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionwuuid))  # measurement observes the dimension
            docgraph.add((dimensionwuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055647")))  # dimension has type width
            docgraph.add((dimensionwuuid, CRM["P90_has_value"], Literal(str(row["width"]))))  # dimension has value from the db
            docgraph.add((dimensionwuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
            docgraph.add((dimensiontuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
            docgraph.add((dimensiontuuid, RDFS.label, Literal('Thickness of ' + shelfmark, lang="en")))
            docgraph.add((measurementuuid, CRM["P40_observed_dimension"], dimensiontuuid))  # measurement observes the dimension
            docgraph.add((dimensiontuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055646")))  # dimension has type thickness
            docgraph.add((dimensiontuuid, CRM["P90_has_value"], Literal(str(row["thickness"]))))  # dimension has value from the db
            docgraph.add((dimensiontuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
            docgraph.add((msuuid, CRM["P3_has_note"], Literal(boxingnote)))  # add boxing notes as a note to the manuscript node
            docgraph.add((surveyeventuuid, RDF.type, CRM["E13_Attribute_Assignment"]))  # rdf type the survey event
            docgraph.add((surveyeventuuid, RDFS.label, Literal('Survey event for ' + shelfmark, lang="en")))
            docgraph.add((surveytimespanuuid, RDF.type, CRM["E52_Time-Span"]))  # rdf type the survey event time-span
            docgraph.add((surveytimespanuuid, RDFS.label, Literal('Time-span of survey event for ' + shelfmark, lang="en")))
            docgraph.add((surveyeventuuid, CRM["P4_has_time-span"], surveytimespanuuid))  # survey event has time-span
            docgraph.add((surveytimespanuuid, CRM["P82a_begin_of_the_begin"], Literal(str(row["surveydate"]).replace("00:00:00", "08:00:00").replace(" ", "T"))))
            docgraph.add((surveytimespanuuid, CRM["P82b_end_of_the_end"], Literal(str(row["surveydate"]).replace("00:00:00", "20:00:00").replace(" ", "T"))))
            docgraph.add((surveyeventuuid, CRM["P9_consists_of"], measurementuuid))  # measurement event is part of survey event

    # documentation drawing
    dot = visualise_graph(docgraph, 'Boxing, leaves, survey date')
    dot.render('boxingleavesdate/1-0-boxingleavesdate.gv', format='svg')

    # serialise the graph
    graph.serialize(destination='boxingleavesdate/1-0-boxingleavesdate.ttl', format='turtle', encoding="utf-8")
    docgraph.serialize(destination='boxingleavesdate/1-0-boxingleavesdate.n3', format='n3', encoding="utf-8")