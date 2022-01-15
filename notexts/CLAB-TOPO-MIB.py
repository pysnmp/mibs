#
# PySNMP MIB module CLAB-TOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/CLAB-TOPO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 05:10:38 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Bits, iso, ModuleIdentity, Integer32, Counter32, Gauge32, ObjectIdentity, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "iso", "ModuleIdentity", "Integer32", "Counter32", "Gauge32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
clabTopoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 2))
clabTopoMib.setRevisions(('2017-06-15 00:00', '2009-01-21 00:00', '2006-12-07 17:00',))
if mibBuilder.loadTexts: clabTopoMib.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: clabTopoMib.setOrganization('Cable Television Laboratories, Inc.')
class NodeName(TextualConvention, OctetString):
    reference = 'RFC 3411.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

clabTopoMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1))
clabTopoFiberNodeCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1), )
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setStatus('current')
clabTopoFiberNodeCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setStatus('current')
clabTopoFiberNodeCfgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 1), NodeName().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setStatus('current')
clabTopoFiberNodeCfgNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 2), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setStatus('current')
clabTopoFiberNodeCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setStatus('current')
clabTopoChFnCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2), )
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setStatus('current')
clabTopoChFnCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1), ).setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"), (0, "CLAB-TOPO-MIB", "clabTopoChFnCfgChIfIndex"))
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setStatus('current')
clabTopoChFnCfgChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: clabTopoChFnCfgChIfIndex.setStatus('current')
clabTopoChFnCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoChFnCfgRowStatus.setStatus('current')
clabTopoMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2))
clabTopoMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1))
clabTopoMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2))
clabTopoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 1, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoCompliance = clabTopoCompliance.setStatus('current')
clabTopoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 4, 2, 2, 2, 1)).setObjects(("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeDescr"), ("CLAB-TOPO-MIB", "clabTopoFiberNodeCfgRowStatus"), ("CLAB-TOPO-MIB", "clabTopoChFnCfgRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabTopoGroup = clabTopoGroup.setStatus('current')
mibBuilder.exportSymbols("CLAB-TOPO-MIB", clabTopoGroup=clabTopoGroup, clabTopoMibGroups=clabTopoMibGroups, clabTopoChFnCfgRowStatus=clabTopoChFnCfgRowStatus, clabTopoMibConformance=clabTopoMibConformance, clabTopoFiberNodeCfgNodeName=clabTopoFiberNodeCfgNodeName, clabTopoChFnCfgEntry=clabTopoChFnCfgEntry, clabTopoFiberNodeCfgEntry=clabTopoFiberNodeCfgEntry, clabTopoFiberNodeCfgTable=clabTopoFiberNodeCfgTable, clabTopoFiberNodeCfgNodeDescr=clabTopoFiberNodeCfgNodeDescr, PYSNMP_MODULE_ID=clabTopoMib, clabTopoCompliance=clabTopoCompliance, clabTopoMibObjects=clabTopoMibObjects, clabTopoMib=clabTopoMib, clabTopoFiberNodeCfgRowStatus=clabTopoFiberNodeCfgRowStatus, clabTopoChFnCfgTable=clabTopoChFnCfgTable, clabTopoChFnCfgChIfIndex=clabTopoChFnCfgChIfIndex, clabTopoMibCompliances=clabTopoMibCompliances, NodeName=NodeName)
