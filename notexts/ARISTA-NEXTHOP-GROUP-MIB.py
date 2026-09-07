#
# PySNMP MIB module ARISTA-NEXTHOP-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ARISTA-NEXTHOP-GROUP-MIB
# Source digest sha256:e7331a9b62f093208e4f4d9a47dac9059c350c85ba5e2e021fdee1d8f9d13024
# Produced by pysmi-2.3.0
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaNexthopGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 21))
aristaNexthopGroupMIB.setRevisions(('2016-04-17 00:00',))
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setLastUpdated('2016-04-17 00:00')
if mibBuilder.loadTexts: aristaNexthopGroupMIB.setOrganization('Arista Networks, Inc.')
aristaNexthopGroupMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1))
aristaNexthopGroupMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2))
class NexthopGroupName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class NexthopGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("invalid", 0), ("ipInIp", 1), ("gre", 2), ("mpls", 3), ("ip", 4), ("mplsOverGre", 5))

aristaNexthopGroupTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: aristaNexthopGroupTable.setStatus('current')
aristaNexthopGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"))
if mibBuilder.loadTexts: aristaNexthopGroupEntry.setStatus('current')
aristaNexthopGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: aristaNexthopGroupId.setStatus('current')
aristaNexthopGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 2), NexthopGroupName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupName.setStatus('current')
aristaNexthopGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 1, 1, 3), NexthopGroupType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupType.setStatus('current')
aristaNexthopGroupCounterTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: aristaNexthopGroupCounterTable.setStatus('current')
aristaNexthopGroupCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupId"), (0, "ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupEntryIndex"))
if mibBuilder.loadTexts: aristaNexthopGroupCounterEntry.setStatus('current')
aristaNexthopGroupEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: aristaNexthopGroupEntryIndex.setStatus('current')
aristaNexthopGroupCounterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterIndex.setStatus('current')
aristaNexthopGroupCounterPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterPacketCount.setStatus('current')
aristaNexthopGroupCounterByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 21, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaNexthopGroupCounterByteCount.setStatus('current')
aristaNexthopGroupMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1))
aristaNexthopGroupMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2))
aristaNexthopGroupMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 1, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupGroup"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupMibCompliance = aristaNexthopGroupMibCompliance.setStatus('current')
aristaNexthopGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 1)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupName"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupGroup = aristaNexthopGroupGroup.setStatus('current')
aristaNexthopGroupCounterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 21, 2, 2, 2)).setObjects(("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterIndex"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterPacketCount"), ("ARISTA-NEXTHOP-GROUP-MIB", "aristaNexthopGroupCounterByteCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaNexthopGroupCounterGroup = aristaNexthopGroupCounterGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-NEXTHOP-GROUP-MIB", NexthopGroupName=NexthopGroupName, NexthopGroupType=NexthopGroupType, PYSNMP_MODULE_ID=aristaNexthopGroupMIB, aristaNexthopGroupCounterByteCount=aristaNexthopGroupCounterByteCount, aristaNexthopGroupCounterEntry=aristaNexthopGroupCounterEntry, aristaNexthopGroupCounterGroup=aristaNexthopGroupCounterGroup, aristaNexthopGroupCounterIndex=aristaNexthopGroupCounterIndex, aristaNexthopGroupCounterPacketCount=aristaNexthopGroupCounterPacketCount, aristaNexthopGroupCounterTable=aristaNexthopGroupCounterTable, aristaNexthopGroupEntry=aristaNexthopGroupEntry, aristaNexthopGroupEntryIndex=aristaNexthopGroupEntryIndex, aristaNexthopGroupGroup=aristaNexthopGroupGroup, aristaNexthopGroupId=aristaNexthopGroupId, aristaNexthopGroupMIB=aristaNexthopGroupMIB, aristaNexthopGroupMibCompliance=aristaNexthopGroupMibCompliance, aristaNexthopGroupMibCompliances=aristaNexthopGroupMibCompliances, aristaNexthopGroupMibConformance=aristaNexthopGroupMibConformance, aristaNexthopGroupMibGroups=aristaNexthopGroupMibGroups, aristaNexthopGroupMibObjects=aristaNexthopGroupMibObjects, aristaNexthopGroupName=aristaNexthopGroupName, aristaNexthopGroupTable=aristaNexthopGroupTable, aristaNexthopGroupType=aristaNexthopGroupType)
