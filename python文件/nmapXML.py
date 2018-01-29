# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
#def makeHtml(filename):
filename=""
general=""
scaninfostr=""
runstatsstr=""
statusstr=""
addressstr=""
portsstr=""
osstr=""
uptimestr=""
tcpsequencestr=""
ipidsequencestr=""
tcptssequencestr=""
hostscriptstr=""
tracestr=""
timesstr=""

filename="result.xml"
DOMTree =xml.dom.minidom.parse(filename)
collection =DOMTree.documentElement
collection.getAttribute("scanner")

general="scanner:<b>"+collection.getAttribute("scanner")+"</b></br>"
general=general+"version:<b>"+collection.getAttribute("version")+"</b></br>"
general=general+"xmloutputversion:<b>"+collection.getAttribute("xmloutputversion")+"</b></br>"
general=general+"instruction:<b>"+collection.getAttribute("args")+"</b></br>"
general=general+"datetime:<b>"+collection.getAttribute("startstr")+"</b></br>"

verbose=collection.getElementsByTagName("verbose")
general=general+"verbose level:<b>"+verbose[0].getAttribute("level")+"</b></br>"
debugging=collection.getElementsByTagName("debugging")
general=general+"debugging level:<b>"+debugging[0].getAttribute("level")+"</b></br>"

scaninfo=collection.getElementsByTagName("scaninfo")

scaninfostr="type:<b>"+scaninfo[0].getAttribute("type")+"</b></br>"
scaninfostr=scaninfostr+"protocol:<b>"+scaninfo[0].getAttribute("protocol")+"</b></br>"
scaninfostr=scaninfostr+"numservices:<b>"+scaninfo[0].getAttribute("numservices")+"</b></br>"
scaninfostr=scaninfostr+"services:<b>"+scaninfo[0].getAttribute("services")+"</b></br>"

print("******details******")
host=collection.getElementsByTagName("host")[0]
status=host.getElementsByTagName("status")[0]
statusstr="state:<b>"+status.getAttribute("state")+"</b></br>"
statusstr=statusstr+"reason:<b>"+status.getAttribute("reason")+"</b></br>"
statusstr=statusstr+"reason_ttl:<b>"+status.getAttribute("reason_ttl")+"</b></br>"
address =host.getElementsByTagName("address")[0]
addressstr="IP:<b>"+address.getAttribute("addr")+"</b></br>"
addressstr=addressstr+"IPtype:<b>"+address.getAttribute("addrtype")+"</b></br>"
if host.getElementsByTagName("ports").length>0:
    portst=host.getElementsByTagName("ports")[0]
    ports=portst.getElementsByTagName("port")
    print("****ports****")
    portsstr=""
    for port in ports:
        portsstr=portsstr+"</br>"
        portsstr = portsstr + "protid:<b>" + port.getAttribute("portid") + "</b></br>"
        portsstr=portsstr+"protocol:<b>"+port.getAttribute("protocol")+"</b></br>"

        state=port.getElementsByTagName("state")[0]
        portsstr = portsstr +"state:<b>"+state.getAttribute("state")+"</b></br>"
        portsstr = portsstr +"reason:<b>" + state.getAttribute("reason")+"</b></br>"
        portsstr = portsstr +"reason_ttl:<b>" + state.getAttribute("reason_ttl")+"</b></br>"

        service=port.getElementsByTagName("service")[0]
        portsstr = portsstr +"name:<b>"+service.getAttribute("name")+"</b></br>"
        portsstr = portsstr +"method:<b>" + service.getAttribute("method")+"</b></br>"
        portsstr = portsstr +"conf:<b>" + service.getAttribute("conf")+"</b></br>"
        portsstr=portsstr+"</br>"
print("****OS****")
if host.getElementsByTagName("os").length>0:
    nmapOS = host.getElementsByTagName("os")[0]
    portused=nmapOS.getElementsByTagName("portused")[0]
    osmatchs=nmapOS.getElementsByTagName("osmatch")
    osstr="state:<b>"+portused.getAttribute("state")+"</b></br>"
    osstr=osstr+"proto:<b>"+portused.getAttribute("proto")+"</b></br>"
    osstr=osstr+"portid:<b>"+portused.getAttribute("portid")+"</b></br>"
    for osmatch in osmatchs:
        osstr = osstr +"</br>"
        osclasses=osmatch.getElementsByTagName("osclass")
        osstr = osstr +"name:<b>"+osmatch.getAttribute("name")+"</b></br>"
        osstr = osstr +"accuracy:<b>" + osmatch.getAttribute("accuracy")+"</b></br>"
        for osclass in osclasses:
            osstr = osstr + "</br>"
            osstr = osstr +"type:<b>"+osclass.getAttribute("type")+"</b></br>"
            osstr = osstr +"vendor:<b>" + osclass.getAttribute("vendor")+"</b></br>"
            osstr = osstr +"osfamily:<b>" + osclass.getAttribute("osfamily")+"</b></br>"
            osstr = osstr +"osgen:<b>" + osclass.getAttribute("osgen")+"</b></br>"
            osstr = osstr +"accuracy:<b>" + osclass.getAttribute("accuracy")+"</b></br>"
        osstr = osstr + "</br>"
if host.getElementsByTagName("uptime")>0:
    uptime=host.getElementsByTagName("uptime")[0]
    print("***uptime***")
    uptimestr="secondes:<b>"+uptime.getAttribute("secondes")+"</b></br>"
    uptimestr=uptimestr+"lastboot:<b>"+uptime.getAttribute("lastboot")+"</b></br>"
print("***tcpsequence***")
if host.getElementsByTagName("tcpsequence")>0:
    tcpsequence=host.getElementsByTagName("tcpsequence")[0]
    tcpsequencestr="index:<b>"+tcpsequence.getAttribute("index")+"</b></br>"
    tcpsequencestr=tcpsequencestr+"difficulty:<b>"+tcpsequence.getAttribute("difficulty")+"</b></br>"
    tcpsequencestr=tcpsequencestr+"values:<b>"+tcpsequence.getAttribute("values")+"</b></br>"
print("***ipidsequence***")
if host.getElementsByTagName("ipidsequence")>0:
    ipidsequence=host.getElementsByTagName("ipidsequence")[0]
    ipidsequencestr="class:<b>"+ipidsequence.getAttribute("class")+"</b></br>"
    ipidsequencestr=ipidsequencestr+"values:<b>"+ipidsequence.getAttribute("values")+"</b></br>"
print("***tcptssequence***")
if host.getElementsByTagName("tcptssequence")>0:
    tcptssequence=host.getElementsByTagName("tcptssequence")[0]
    tcptssequencestr="class:<b>"+tcptssequence.getAttribute("class")+"</b></br>"
    tcptssequencestr=tcptssequencestr+"values:<b>"+tcptssequence.getAttribute("values")+"</b></br>"
if host.getElementsByTagName("hostscript")>0:
    hostscript=host.getElementsByTagName("hostscript")[0]
    scripts=hostscript.getElementsByTagName("scripts")
    print("***hostscript***")

    for script in scripts:
        hostscriptstr="id:<b>" + script.getAttribute("id")+"</b></br>"
        hostscriptstr=hostscriptstr+"output:<b>" + script.getAttribute("output")+"</b></br>"
        hostscriptstr=hostscriptstr+"</br>"
if host.getElementsByTagName("distance")>0:
    distance=host.getElementsByTagName("distance")[0]
    print("***trace***")
    tracestr=""
    tracestr=tracestr+"distance value:<b>"+distance.getAttribute("distance")+"</b></br>"
    trace=host.getElementsByTagName("trace")[0]
    hops=trace.getElementsByTagName("hops")
    tracestr=tracestr+"port:<b>"+trace.getAttribute("port")+"</b></br>"
    tracestr=tracestr+"proto:<b>"+trace.getAttribute("proto")+"</b></br>"
    for hop in hops:
        tracestr = tracestr +"ttl:<b>"+hop.getAttribute("ttl")+"&nbsp;&nbsp;ipaddr:<b>"+hop.getAttribute("ttl")+"&nbsp;&nbsp;rtt:<b>"+hop.getAttribute("rtt")+"</b></br>"
if host.getElementsByTagName("times")>0:
    times=host.getElementsByTagName("times")[0]

    timesstr="srtt:<b>"+times.getAttribute("srtt")+"</b></br>"
    timesstr=timesstr+"rttvar:<b>"+times.getAttribute("rttvar")+"</b></br>"
    timesstr=timesstr+"to:<b>"+times.getAttribute("to")+"</b></br>"
print("****runstats****")
if collection.getElementsByTagName("runstats")>0:
    runstats=collection.getElementsByTagName("runstats")[0]
    finished=runstats.getElementsByTagName("finished")[0]
    runstatsstr="finished timestr:<b>"+finished.getAttribute("timestr")+"</b></br>"
    runstatsstr="summary:<b>"+finished.getAttribute("summary")+"</b></br>"
#hosts=runstats.getElementsByTagName("hosts")[0]
#print("up:<b>"+hosts.getAttribute("up")+"</b>\tdown:<b>"+hosts.getAttribute("down")+"</b>\ttotal:<b>"+hosts.getAttribute("total")+"</b></br>"
#print("state:<b>"+status.getAttribute("state")+"</b></br>"
f = open(filename+'.html','w')
message = """
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="HandheldFriendly" content="True">
        <meta name="MobileOptimized" content="320">
        <meta name="viewport" content="initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>nmapReport</title>
        <link rel="alternate" type="application/rss+xml" title="egrappler.com" href="feed/index.html">
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/prettify.css">
        </head>
        <body>
        <header>
          <div class="container">
            <h2 class="docs-header"> %s</h2>
          </div>
        </header>
        <section>
          <div class="container">
            <ul class="docs-nav" id="menu-left">
              <li><strong>summary</strong></li>
              <li><a href="#general" class=" ">general</a></li>
              <li><a href="#scaninfo" class=" ">scaninfo</a></li>
              <li><a href="#runstats" class=" ">runstats</a></li>
              <li class="separator"></li>
              <li><strong>details</strong></li>
              <li><a href="#status" class=" ">status</a></li>
              <li><a href="#address" class=" ">address</a></li>
              <li><a href="#ports" class=" ">ports</a></li>
              <li><a href="#os" class=" ">os</a></li>
              <li><a href="#uptime" class=" ">uptime</a></li>
              <li><a href="#tcpsequence" class=" ">tcpsequence</a></li>
              <li><a href="#ipidsequence" class=" ">ipidsequence</a></li>
              <li><a href="#tcptssequence" class=" ">tcptssequence</a></li>
              <li><a href="#hostscript" class=" ">hostscript</a></li>
              <li><a href="#trace" class=" ">trace</a></li>
              <li><a href="#times" class=" ">times</a></li>
              
              
            </ul>
            <div class="docs-content">
              <h2> summary</h2>
              <h3 id="general"> general</h3>
              %s
              <h3 id="scaninfo"> scaninfo</h3>
             %s
              <h3 id="runstats"> runstats</h3>
             %s
              <h2> details</h2>
              <h3 id="status"> status</h3>
              %s
              <h3 id="address"> address</h3>
              %s
              <h3 id="ports"> ports</h3>
              %s
              <h3 id="os"> os</h3>
              %s
              <h3 id="uptime"> uptime</h3>
              %s
              <h3 id="tcpsequence"> tcpsequence</h3>
              %s
              <h3 id="ipidsequence"> ipidsequence</h3>
              %s
              <h3 id="tcptssequence"> tcptssequence</h3>
              %s
              <h3 id="hostscript"> hostscript</h3>
              %s
              <h3 id="trace"> trace</h3>
              %s
              <h3 id="times"> times</h3>
              %s
        </section>
        <section class="vibrant centered">
          <div class="container">
            <h4> This Report is end .Go top click<a href="#"> here</a></h4>
          </div>
        </section>
        <script src="js/jquery.min.js"></script> 
         
        <script type="text/javascript" src="js/prettify/prettify.js"></script> 
        <script src="js/layout.js"></script>
         <script src="js/jquery.localscroll-1.2.7.js" type="text/javascript"></script>
         <script src="js/jquery.scrollTo-1.4.3.1.js" type="text/javascript"></script>
        </body>
        </html>
        
        """%(filename,general,scaninfostr,runstatsstr,statusstr,addressstr,portsstr,osstr,uptimestr,tcpsequencestr,ipidsequencestr,tcptssequencestr,hostscriptstr,tracestr,timesstr)

f.write(message)
f.close()