#
# PySNMP MIB module CLAB-TOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CLAB-TOPO-MIB
# Source digest sha256:e75142139324cad4579b7ca46cf9cf16292d43e204d5178af491bc95442aa6c3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
clabTopoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 2))
clabTopoMib.setRevisions(('2017-06-15 00:00', '2009-01-21 00:00', '2006-12-07 17:00',))
if mibBuilder.loadTexts: clabTopoMib.setLastUpdated('2017-06-15 00:00')
if mibBuilder.loadTexts: clabTopoMib.setOrganization('Cable Television Laboratories, Inc.')
class NodeName(TextualConvention, OctetString):
    reference = 'RFC 3411.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

clabTopoMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1))
clabTopoFiberNodeCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgTable.setStatus('current')
clabTopoFiberNodeCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"))
if mibBuilder.loadTexts: clabTopoFiberNodeCfgEntry.setStatus('current')
clabTopoFiberNodeCfgNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 1), NodeName().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeName.setStatus('current')
clabTopoFiberNodeCfgNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 2), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgNodeDescr.setStatus('current')
clabTopoFiberNodeCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: clabTopoFiberNodeCfgRowStatus.setStatus('current')
clabTopoChFnCfgTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clabTopoChFnCfgTable.setStatus('current')
clabTopoChFnCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"), (0, "CLAB-TOPO-MIB", "clabTopoChFnCfgChIfIndex"))
if mibBuilder.loadTexts: clabTopoChFnCfgEntry.setStatus('current')
clabTopoChFnCfgChIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 4, 2, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
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
mibBuilder.exportSymbols("CLAB-TOPO-MIB", NodeName=NodeName, PYSNMP_MODULE_ID=clabTopoMib, clabTopoChFnCfgChIfIndex=clabTopoChFnCfgChIfIndex, clabTopoChFnCfgEntry=clabTopoChFnCfgEntry, clabTopoChFnCfgRowStatus=clabTopoChFnCfgRowStatus, clabTopoChFnCfgTable=clabTopoChFnCfgTable, clabTopoCompliance=clabTopoCompliance, clabTopoFiberNodeCfgEntry=clabTopoFiberNodeCfgEntry, clabTopoFiberNodeCfgNodeDescr=clabTopoFiberNodeCfgNodeDescr, clabTopoFiberNodeCfgNodeName=clabTopoFiberNodeCfgNodeName, clabTopoFiberNodeCfgRowStatus=clabTopoFiberNodeCfgRowStatus, clabTopoFiberNodeCfgTable=clabTopoFiberNodeCfgTable, clabTopoGroup=clabTopoGroup, clabTopoMib=clabTopoMib, clabTopoMibCompliances=clabTopoMibCompliances, clabTopoMibConformance=clabTopoMibConformance, clabTopoMibGroups=clabTopoMibGroups, clabTopoMibObjects=clabTopoMibObjects)
