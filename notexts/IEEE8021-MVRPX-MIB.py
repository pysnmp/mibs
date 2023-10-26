#
# PySNMP MIB module IEEE8021-MVRPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-MVRPX-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:21:13 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
TimeTicks, Integer32, Counter32, Unsigned32, NotificationType, ModuleIdentity, Counter64, Gauge32, Bits, MibIdentifier, ObjectIdentity, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Counter32", "Unsigned32", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "Bits", "MibIdentifier", "ObjectIdentity", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ieee8021MvrpxMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 22))
ieee8021MvrpxMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2011-04-05 00:00',))
if mibBuilder.loadTexts: ieee8021MvrpxMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021MvrpxMib.setOrganization('IEEE 802.1 Working Group')
ieee8021MvrpxMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 1))
ieee8021MvrpxConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2))
ieee8021MvrpxPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 22, 1, 1), )
if mibBuilder.loadTexts: ieee8021MvrpxPortTable.setStatus('current')
ieee8021MvrpxPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortEntry"))
ieee8021MvrpxPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MvrpxPortEntry.setStatus('current')
ieee8021MvrpxPortNewOnly = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortNewOnly.setStatus('current')
ieee8021MvrpxPortMvrpNewPropagated = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortMvrpNewPropagated.setStatus('current')
ieee8021MvrpxPortXmitZero = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 22, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MvrpxPortXmitZero.setStatus('current')
ieee8021MvrpxCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 1))
ieee8021MvrpxGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 22, 2, 2))
ieee8021MvrpxReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 22, 2, 2, 1)).setObjects(("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortNewOnly"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortMvrpNewPropagated"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxPortXmitZero"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxReqdGroup = ieee8021MvrpxReqdGroup.setStatus('current')
ieee8021MvrpxCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 22, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IEEE8021-MVRPX-MIB", "ieee8021MvrpxReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MvrpxCompliance = ieee8021MvrpxCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-MVRPX-MIB", ieee8021MvrpxCompliances=ieee8021MvrpxCompliances, ieee8021MvrpxPortXmitZero=ieee8021MvrpxPortXmitZero, ieee8021MvrpxPortEntry=ieee8021MvrpxPortEntry, ieee8021MvrpxPortNewOnly=ieee8021MvrpxPortNewOnly, ieee8021MvrpxMIBObjects=ieee8021MvrpxMIBObjects, ieee8021MvrpxPortMvrpNewPropagated=ieee8021MvrpxPortMvrpNewPropagated, ieee8021MvrpxCompliance=ieee8021MvrpxCompliance, ieee8021MvrpxConformance=ieee8021MvrpxConformance, ieee8021MvrpxGroups=ieee8021MvrpxGroups, ieee8021MvrpxReqdGroup=ieee8021MvrpxReqdGroup, ieee8021MvrpxPortTable=ieee8021MvrpxPortTable, PYSNMP_MODULE_ID=ieee8021MvrpxMib, ieee8021MvrpxMib=ieee8021MvrpxMib)
