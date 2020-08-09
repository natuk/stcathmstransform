from rdflib import Graph, Literal, URIRef
from rdflib.namespace import SKOS, RDF, RDFS
import uuid
from namespaces import apply_namespaces, get_namespace

def boxingleavesdate(mydb, cursor, cursorupdate):
    graph = Graph()
    # add namespaces
    graph = apply_namespaces(graph)
    # get the ones we need here
    STCATH = get_namespace(graph, 'stcath')
    CRM = get_namespace(graph, 'crm')

    # deal with thesaurus concepts
    graph.add((URIRef("http://stcath.measuringbox"), RDF.type, CRM["E55_Type"]))
    graph.add((URIRef("http://stcath.measuringbox"), RDF.type, SKOS.Concept))
    graph.add((URIRef("http://stcath.measuringbox"), SKOS.prefLabel, Literal("measuring boxes")))
    graph.add((URIRef("http://vocab.getty.edu/aat/300055644"), RDF.type, CRM["E55_Type"]))  # height
    graph.add((URIRef("http://vocab.getty.edu/aat/300055647"), RDF.type, CRM["E55_Type"]))  # width
    graph.add((URIRef("http://vocab.getty.edu/aat/300055646"), RDF.type, CRM["E55_Type"]))  # thickness
    graph.add((URIRef("http://vocab.getty.edu/aat/300379097"), RDF.type, CRM["E58_Measurement_Unit"])) # mm

    # 1_0_BoxingLeavesDate
    cursor.execute("SELECT * FROM 1_0_BoxingLeavesDate")
    rows = cursor.fetchall()

    for row in rows:
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
        graph.add((measurementuuid, RDF.type, CRM["E16_Measurement"])) # rdf type the measurement
        graph.add((measurementuuid, CRM["P39_measured"], msuuid)) # measurement event measured the manuscript
        graph.add((measurementuuid, CRM["P125_used_object_of_type"], URIRef("http://stcath.measuringbox"))) # measurement used measuring box
        # height
        if row["heightuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET heightuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuid = URIRef(row["heightuuid"], str(STCATH))
        graph.add((dimensionuuid, RDF.type, CRM["E54_Dimension"])) # rdf type the dimension
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionuuid)) # measurement observes the dimension
        graph.add((dimensionuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055644"))) # dimension has type height
        graph.add((dimensionuuid, CRM["P90_has_value"], Literal(str(row["height"])))) # dimension has value from the db
        graph.add((dimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097"))) # dimension has unit mm
        # width
        if row["widthuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET widthuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuid = URIRef(row["widthuuid"], str(STCATH))
        graph.add((dimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionuuid))  # measurement observes the dimension
        graph.add((dimensionuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055647")))  # dimension has type width
        graph.add((dimensionuuid, CRM["P90_has_value"], Literal(str(row["width"]))))  # dimension has value from the db
        graph.add((dimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
        # thickness
        if row["thicknessuuid"] is None:
            newuuid = str(uuid.uuid4())
            dimensionuuid = URIRef(newuuid, str(STCATH))
            # update the database
            sql = "UPDATE 1_0_BoxingLeavesDate SET thicknessuuid=%s WHERE msid=%s"
            val = (newuuid, row["msid"])
            cursorupdate.execute(sql, val)
            mydb.commit()
        else:
            dimensionuuid = URIRef(row["thicknessuuid"], str(STCATH))
        graph.add((dimensionuuid, RDF.type, CRM["E54_Dimension"]))  # rdf type the dimension
        graph.add((measurementuuid, CRM["P40_observed_dimension"], dimensionuuid))  # measurement observes the dimension
        graph.add((dimensionuuid, CRM["P2_has_type"], URIRef("http://vocab.getty.edu/aat/300055646")))  # dimension has type thickness
        graph.add((dimensionuuid, CRM["P90_has_value"], Literal(str(row["thickness"]))))  # dimension has value from the db
        graph.add((dimensionuuid, CRM["P91_has_unit"], URIRef("http://vocab.getty.edu/aat/300379097")))  # dimension has unit mm
        # boxing status
        if row["boxingstatus"] is not None:
            boxingnote = row["boxingstatus"]
            if row["boxingnotes"] is not None:
                boxingnote = row["boxingstatus"] + " - " + row["boxingnotes"]
            graph.add((msuuid, CRM["P3_has_note"], Literal(boxingnote)))  # add boxing notes as a note to the manuscript node
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
        graph.add((surveyeventuuid, RDF.type, CRM["E13_Attribute_Assignment"])) # rdf type the survey event
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
        graph.add((surveytimespanuuid, RDF.type, CRM["E52_Time-Span"]))  # rdf type the survey event time-span
        graph.add((surveyeventuuid, CRM["P4_has_time-span"], surveytimespanuuid))  # survey event has time-span
        if row["surveydate"] is not None:
            graph.add((surveytimespanuuid, CRM["P82a_begin_of_the_begin"], Literal(str(row["surveydate"]).replace("00:00:00", "08:00:00").replace(" ", "T"))))
            graph.add((surveytimespanuuid, CRM["P82b_end_of_the_end"], Literal(str(row["surveydate"]).replace("00:00:00", "20:00:00").replace(" ", "T"))))

    # serialise the graph
    graph.serialize(destination='boxingleavesdate/1-0-boxingleavesdate.ttl', format='turtle', encoding="utf-8")