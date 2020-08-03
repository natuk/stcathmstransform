from lxml import etree as etree

def getprototype(datasetroot, prototyperoot):
    #create the prototyperoot
    #prototyperoot = etree.Element("root")
    #datasetroot = etree.Element("root")
    # loop through child elements or datasetroot
    prototyperoot = loopthroughchildren(datasetroot, prototyperoot)
    return prototyperoot

def loopthroughchildren(datasetelement, prototypeelement):
    datasetelementchildnodes = datasetelement.xpath('child::*')
    prototypeelementchildnodes = prototypeelement.xpath('child::*')
    i = 0
    while i < len(datasetelementchildnodes):
        checkresult = checktag(datasetelementchildnodes[i].tag, prototypeelementchildnodes)
        if checkresult is False: #if there is no corresponding element in the prototype
            newprototypeelement = etree.SubElement(prototypeelement, datasetelementchildnodes[i].tag)
            newprototypeelement.text = datasetelementchildnodes[i].text
            newprototypeelement = loopthroughchildren(datasetelementchildnodes[i], newprototypeelement)
            prototypeelementchildnodes = prototypeelement.xpath('child::*')
        else: #if there is, then get the corresponding prototype element location
            prototypeelementchildnodes[checkresult] = loopthroughchildren(datasetelementchildnodes[i], prototypeelementchildnodes[checkresult])
        i = i + 1
    return prototypeelement

def checktag(tag, elements):
# checks whether an element with the same tag as the 'tag' already exists among 'elements'
    i = 0
    for element in elements:
        if element.tag == tag:
            # it is found
            return i
        i = i + 1
    # it is not found
    return False