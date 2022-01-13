#
# PySNMP MIB module CLAB-TOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/CLAB-TOPO-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 22:39:58 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, NotificationType, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, IpAddress, TimeTicks, Integer32, ObjectIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "NotificationType", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "IpAddress", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CLAB-TOPO-MIB", clabTopoFiberNodeCfgNodeDescr=clabTopoFiberNodeCfgNodeDescr, clabTopoGroup=clabTopoGroup, NodeName=NodeName, clabTopoChFnCfgEntry=clabTopoChFnCfgEntry, clabTopoMibGroups=clabTopoMibGroups, clabTopoCompliance=clabTopoCompliance, clabTopoFiberNodeCfgNodeName=clabTopoFiberNodeCfgNodeName, clabTopoMibCompliances=clabTopoMibCompliances, clabTopoMibConformance=clabTopoMibConformance, clabTopoMib=clabTopoMib, clabTopoFiberNodeCfgRowStatus=clabTopoFiberNodeCfgRowStatus, clabTopoFiberNodeCfgEntry=clabTopoFiberNodeCfgEntry, clabTopoChFnCfgRowStatus=clabTopoChFnCfgRowStatus, clabTopoFiberNodeCfgTable=clabTopoFiberNodeCfgTable, clabTopoChFnCfgTable=clabTopoChFnCfgTable, PYSNMP_MODULE_ID=clabTopoMib, clabTopoChFnCfgChIfIndex=clabTopoChFnCfgChIfIndex, clabTopoMibObjects=clabTopoMibObjects)
