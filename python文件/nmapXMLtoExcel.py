# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import xlsxwriter
def getResult(filename):
    ip=""
    portMap={}
    os=""
    #filename="result.xml"
    DOMTree =xml.dom.minidom.parse(filename)
    collection =DOMTree.documentElement
    host=collection.getElementsByTagName("host")[0]
    address =host.getElementsByTagName("address")[0]
    ip=address.getAttribute("addr")
    if host.getElementsByTagName("ports").length>0:
        ports=host.getElementsByTagName("port")
        for port in ports:
            service=port.getElementsByTagName("service")[0]
            portMap[port.getAttribute("portid")]=service.getAttribute("name")
    print("****OS****")
    if host.getElementsByTagName("os").length>0:
        nmapOS = host.getElementsByTagName("os")[0]
        osmatch=nmapOS.getElementsByTagName("osmatch")[0]
        osclasses=osmatch.getElementsByTagName("osclass")
        os=osmatch.getAttribute("name")+"("+osmatch.getAttribute("accuracy")+"%)"
    return (ip,portMap,os)