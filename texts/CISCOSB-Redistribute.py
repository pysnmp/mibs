#
# PySNMP MIB module CISCOSB-Redistribute (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-Redistribute
# Source digest sha256:8d21eaccf41e5028ce804d26eb3438adbbbd555bc39b3061fd9a527c33c3fd7a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ipSpec, = mibBuilder.importSymbols("CISCOSB-IP", "ipSpec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
class RlRedistSrcProtocol(TextualConvention, Integer32):
    description = 'Source Protocol\n                 this defines the list of sources that redistribute their routes '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rlRedistProtocolConnected", 1), ("rlRedistProtocolStatic", 2), ("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9), ("rlRedistProtocolAll", 10))

class RlRedistDstProtocol(TextualConvention, Integer32):
    description = 'Destination Protocol'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9))

class RlRedistMatchType(TextualConvention, Integer32):
    description = 'Match Type\n                 Bit Map that defines the criteria by which OSPF routes are redistributed into other routing domains.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlRedistMatchTypeNone", 0), ("rlRedistMatchTypeInternal", 1), ("rlRedistMatchTypeExternalOne", 2), ("rlRedistMatchTypeExternalTwo", 3))

class RlRedistMetricType(TextualConvention, Integer32):
    description = 'Metric Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rlRedistMetricTypeNone", 0), ("rlRedistMetricTypeExternalOne", 1), ("rlRedistMetricTypeExternalTwo", 2))

rlRedistribute = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27))
rlRedistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistTable.setStatus('current')
if mibBuilder.loadTexts: rlRedistTable.setDescription('Using a routing protocol to advertise routes that are learned by some other means,\n                 such as by another routing protocol, static routes, or directly connected routes, is called redistribution.\n                 This table is used to configure under which conditions will redistribution occur\n                 and which actions (if any) should be done on redistributed route.')
rlRedistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-Redistribute", "rlRedistDstProtocol"), (0, "CISCOSB-Redistribute", "rlRedistSrcProtocol"), (0, "CISCOSB-Redistribute", "rlRedistDstProcessId"), (0, "CISCOSB-Redistribute", "rlRedistSrcProcessId"), (0, "CISCOSB-Redistribute", "rlRedistMatchType"), (0, "CISCOSB-Redistribute", "rlRedistRoutMapName"))
if mibBuilder.loadTexts: rlRedistEntry.setStatus('current')
if mibBuilder.loadTexts: rlRedistEntry.setDescription('.')
rlRedistDstProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 1), RlRedistDstProtocol()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistDstProtocol.setStatus('current')
if mibBuilder.loadTexts: rlRedistDstProtocol.setDescription('The protocol to which the routes are exported to')
rlRedistSrcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 2), RlRedistSrcProtocol()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistSrcProtocol.setStatus('current')
if mibBuilder.loadTexts: rlRedistSrcProtocol.setDescription('The protocol from which the routes are imported from')
rlRedistDstProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistDstProcessId.setStatus('current')
if mibBuilder.loadTexts: rlRedistDstProcessId.setDescription('Parameter semantic differs according to rlRedistDstProtocol.\n                in OSPF this is an appropriate OSPF process ID to which routes are to be redistributed')
rlRedistSrcProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistSrcProcessId.setStatus('current')
if mibBuilder.loadTexts: rlRedistSrcProcessId.setDescription('Parameter semantic differs according to rlRedistSrcProtocol.\n                 in BGP and EIGRP keyword, this is an autonomous system number, in range 1 to 65535..\n                 in OSPF, this is an appropriate OSPF process ID from which routes are to be redistributed.\n                 0 means no process ID')
rlRedistMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 5), RlRedistMatchType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistMatchType.setStatus('current')
if mibBuilder.loadTexts: rlRedistMatchType.setDescription('Applicable only when rlRedistSrcProtocol is OSPF\n                defines the criteria by which OSPF routes are redistributed into other routing domains.\n                It can be one of the following:\n                rlRedistMatchTypeInternal    - Routes that are internal to a specific autonomous system.\n                rlRedistMatchTypeExternalTwo - Routes that are external to the autonomous system, but are imported into OSPF as Type 2 external route.\n                rlRedistMatchTypeExternalOne - Routes that are external to the autonomous system, but are imported into OSPF as Type 1 external route.')
rlRedistRoutMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlRedistRoutMapName.setStatus('current')
if mibBuilder.loadTexts: rlRedistRoutMapName.setDescription('Specifies the route map that should be interrogated to filter the importation of routes\n                 from this source routing protocol to the current routing protocol.\n                 If not specified, all routes are redistributed. If this keyword is specified, but no route map tags are listed, no routes will be imported.')
rlRedistAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistAsNumber.setStatus('current')
if mibBuilder.loadTexts: rlRedistAsNumber.setDescription('Autonomous system number for the redistributed route. Number in range from 1 to 65535.\n                 0 means no AS number defined')
rlRedistMetricTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricTransparent.setStatus('current')
if mibBuilder.loadTexts: rlRedistMetricTransparent.setDescription('Redistribute routes without changing the metric')
rlRedistMetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 9), Integer32().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricValue.setStatus('current')
if mibBuilder.loadTexts: rlRedistMetricValue.setDescription('When redistributing from one OSPF process to another OSPF process on the same router,\n                 the metric will be carried through from one process to the other if no metric value is specified.\n                 When redistributing other processes to an OSPF process, the default metric is 20 when no metric value is specified.')
rlRedistMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 10), RlRedistMetricType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricType.setStatus('current')
if mibBuilder.loadTexts: rlRedistMetricType.setDescription('Parameter semantic differs according to rlRedistSrcProtocol.\n                 In OSPF specifies the external link type associated with the default route advertised into the OSPF routing domain.\n                 It can be one of two values:\n                 1 - Type 1 external route\n                 2 - Type 2 external route')
rlRedistSubnets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistSubnets.setStatus('current')
if mibBuilder.loadTexts: rlRedistSubnets.setDescription('For redistributing routes into OSPF, the scope of redistribution for the specified protocol')
rlRedistOnlyNSSA = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistOnlyNSSA.setStatus('current')
if mibBuilder.loadTexts: rlRedistOnlyNSSA.setDescription('Sets the nssa-only attribute for all routes redistributed into OSPF.')
rlRedistRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26, 27, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlRedistRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlRedistRowStatus.setDescription('Row Status')
mibBuilder.exportSymbols("CISCOSB-Redistribute", RlRedistDstProtocol=RlRedistDstProtocol, RlRedistMatchType=RlRedistMatchType, RlRedistMetricType=RlRedistMetricType, RlRedistSrcProtocol=RlRedistSrcProtocol, rlRedistAsNumber=rlRedistAsNumber, rlRedistDstProcessId=rlRedistDstProcessId, rlRedistDstProtocol=rlRedistDstProtocol, rlRedistEntry=rlRedistEntry, rlRedistMatchType=rlRedistMatchType, rlRedistMetricTransparent=rlRedistMetricTransparent, rlRedistMetricType=rlRedistMetricType, rlRedistMetricValue=rlRedistMetricValue, rlRedistOnlyNSSA=rlRedistOnlyNSSA, rlRedistRoutMapName=rlRedistRoutMapName, rlRedistRowStatus=rlRedistRowStatus, rlRedistSrcProcessId=rlRedistSrcProcessId, rlRedistSrcProtocol=rlRedistSrcProtocol, rlRedistSubnets=rlRedistSubnets, rlRedistTable=rlRedistTable, rlRedistribute=rlRedistribute)
