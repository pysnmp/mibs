#
# PySNMP MIB module DLINKSW-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-TRAFFIC-SEGMENT-MIB
# Source digest sha256:374c0590984fd124ff58188d97b76c79b5a28e95e9e7876a86c0313567bace19
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwTrafficSegMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 26))
dlinkSwTrafficSegMIB.setRevisions(('2013-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setRevisionsDescriptions(('This is the first version of the MIB file.',))
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setLastUpdated('2013-03-01 00:00')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwTrafficSegMIB.setDescription('This MIB module defines objects for Traffic Segmentation.')
dTrafficSegNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 0))
dTrafficSegObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 1))
dTrafficSegConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2))
dTrafficSegForwardDomainTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dTrafficSegForwardDomainTable.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardDomainTable.setDescription('A list of specification of forwarding domains for Traffic Segmentation.')
dTrafficSegForwardDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dTrafficSegForwardDomainEntry.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardDomainEntry.setDescription('An entry indicates the setting of forwarding domain on an interface.')
dTrafficSegForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 26, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dTrafficSegForwardPorts.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegForwardPorts.setDescription('This object indicates the forward domain (a set of ports) on the\n            interface.')
dTrafficSegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1))
dTrafficSegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2))
dTrafficSegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 1, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegIfCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegMIBCompliance = dTrafficSegMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegMIBCompliance.setDescription('The compliance statement for entities which implement the \n            DLINKSW-TRAFFIC-SEGMENT-MIB.')
dTrafficSegIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 26, 2, 2, 1)).setObjects(("DLINKSW-TRAFFIC-SEGMENT-MIB", "dTrafficSegForwardPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dTrafficSegIfCfgGroup = dTrafficSegIfCfgGroup.setStatus('current')
if mibBuilder.loadTexts: dTrafficSegIfCfgGroup.setDescription('A collection of objects providing management of the Traffic\n            Segmentation feature.')
mibBuilder.exportSymbols("DLINKSW-TRAFFIC-SEGMENT-MIB", PYSNMP_MODULE_ID=dlinkSwTrafficSegMIB, dTrafficSegConformance=dTrafficSegConformance, dTrafficSegForwardDomainEntry=dTrafficSegForwardDomainEntry, dTrafficSegForwardDomainTable=dTrafficSegForwardDomainTable, dTrafficSegForwardPorts=dTrafficSegForwardPorts, dTrafficSegIfCfgGroup=dTrafficSegIfCfgGroup, dTrafficSegMIBCompliance=dTrafficSegMIBCompliance, dTrafficSegMIBCompliances=dTrafficSegMIBCompliances, dTrafficSegMIBGroups=dTrafficSegMIBGroups, dTrafficSegNotifications=dTrafficSegNotifications, dTrafficSegObjects=dTrafficSegObjects, dlinkSwTrafficSegMIB=dlinkSwTrafficSegMIB)
