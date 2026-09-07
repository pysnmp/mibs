#
# PySNMP MIB module ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB
# Source digest sha256:9b48ff39310874c372bf2ebbba4ce4f3aee98a8d62bc053e1230ac9f42adea75
# Produced by pysmi-2.3.0
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
cgnv6SharedServiceGroupModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412))
if mibBuilder.loadTexts: cgnv6SharedServiceGroupModule.setLastUpdated('2007-05-07 13:27')
if mibBuilder.loadTexts: cgnv6SharedServiceGroupModule.setOrganization('A10 Networks, Inc.')
sharedServiceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1))
sharedServiceGroupOperSharedServiceGroupListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListTable.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", "sharedServiceGroupOperSharedServiceGroupListSlotId"), (0, "ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", "sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId"))
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListEntry.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListSlotId.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId.setStatus('current')
sharedServiceGroupOperSharedServiceGroupListServiceGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 412, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sharedServiceGroupOperSharedServiceGroupListServiceGroupName.setStatus('current')
mibBuilder.exportSymbols("ACOS-CGNV6-SHARED-SERVICE-GROUP-MIB", PYSNMP_MODULE_ID=cgnv6SharedServiceGroupModule, cgnv6SharedServiceGroupModule=cgnv6SharedServiceGroupModule, sharedServiceGroup=sharedServiceGroup, sharedServiceGroupOperSharedServiceGroupListEntry=sharedServiceGroupOperSharedServiceGroupListEntry, sharedServiceGroupOperSharedServiceGroupListServiceGroupName=sharedServiceGroupOperSharedServiceGroupListServiceGroupName, sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId=sharedServiceGroupOperSharedServiceGroupListSharedServiceGroupListListId, sharedServiceGroupOperSharedServiceGroupListSlotId=sharedServiceGroupOperSharedServiceGroupListSlotId, sharedServiceGroupOperSharedServiceGroupListTable=sharedServiceGroupOperSharedServiceGroupListTable)
