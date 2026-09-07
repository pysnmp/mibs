#
# PySNMP MIB module IF-INVERTED-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IF-INVERTED-STACK-MIB
# Source digest sha256:fc47b49328c3e9f9878e995878f4b5c8702b122185b20261f3efde74ee0a02b4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifStackGroup2, ifStackHigherLayer, ifStackLowerLayer = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifStackHigherLayer", "ifStackLowerLayer")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ifInvertedStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 77))
ifInvertedStackMIB.setRevisions(('2000-06-14 00:00',))
if mibBuilder.loadTexts: ifInvertedStackMIB.setLastUpdated('2000-06-14 00:00')
if mibBuilder.loadTexts: ifInvertedStackMIB.setOrganization('IETF Interfaces MIB Working Group')
ifInvMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1))
ifInvStackTable = MibTable((1, 3, 6, 1, 2, 1, 77, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ifInvStackTable.setStatus('current')
ifInvStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 77, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvStackEntry.setStatus('current')
ifInvStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvStackStatus.setStatus('current')
ifInvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2))
ifInvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 1))
ifInvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 2))
ifInvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"), ("IF-MIB", "ifStackGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvCompliance = ifInvCompliance.setStatus('current')
ifInvStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvStackGroup = ifInvStackGroup.setStatus('current')
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", PYSNMP_MODULE_ID=ifInvertedStackMIB, ifInvCompliance=ifInvCompliance, ifInvCompliances=ifInvCompliances, ifInvConformance=ifInvConformance, ifInvGroups=ifInvGroups, ifInvMIBObjects=ifInvMIBObjects, ifInvStackEntry=ifInvStackEntry, ifInvStackGroup=ifInvStackGroup, ifInvStackStatus=ifInvStackStatus, ifInvStackTable=ifInvStackTable, ifInvertedStackMIB=ifInvertedStackMIB)
