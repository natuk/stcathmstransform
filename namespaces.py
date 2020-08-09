from rdflib import Graph, Namespace, URIRef

def apply_namespaces(graph):
    # add Ligatus's namespace
    STCATH = Namespace('https://data.ligatus.org.uk/stcatherines/ms/')
    graph.bind('stcath', STCATH)
    # add CIDOC-CRM's namespace and prefix
    CRM = Namespace('http://www.cidoc-crm.org/cidoc-crm/')
    graph.bind('crm', CRM)

    return graph

def get_namespace(graph, prefix):
    # returns a namespace object is the "prefix" string matches a prefix in the "graph"
    nss = [n for n in graph.namespace_manager.namespaces()]
    for ns in nss:
        if ns[0] == prefix:
            NS = Namespace(ns[1])
            return NS
    return False

def get_prefix_uri(graph, uri):
    # returns the uri with a prefix if the prefix exists in the graph
    nss = [n for n in graph.namespace_manager.namespaces()]
    for ns in nss:
        if str(uri).find(ns[1]) != -1:
            prefix = ns[0]
            uri = str(uri)[len(ns[1]):]
            return prefix + ":" + uri
    return uri
