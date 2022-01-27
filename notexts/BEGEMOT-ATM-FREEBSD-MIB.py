#
# PySNMP MIB module BEGEMOT-ATM-FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-ATM-FREEBSD-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:17:20 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
begemotAtmIfEntry, begemotAtmSysGroup = mibBuilder.importSymbols("BEGEMOT-ATM-MIB", "begemotAtmIfEntry", "begemotAtmSysGroup")
NgNodeIdOrZero, = mibBuilder.importSymbols("BEGEMOT-NETGRAPH-MIB", "NgNodeIdOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, Bits, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Bits", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotAtmFreeBSDGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1))
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setLastUpdated('200408060000Z')
if mibBuilder.loadTexts: begemotAtmFreeBSDGroup.setOrganization('German Aerospace Centre')
begemotAtmNgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1))
begemotAtmNgIfTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1), )
if mibBuilder.loadTexts: begemotAtmNgIfTable.setStatus('current')
begemotAtmNgIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1), )
begemotAtmIfEntry.registerAugmentions(("BEGEMOT-ATM-FREEBSD-MIB", "begemotAtmNgIfEntry"))
begemotAtmNgIfEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
if mibBuilder.loadTexts: begemotAtmNgIfEntry.setStatus('current')
begemotAtmNgIfNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1, 1), NgNodeIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmNgIfNodeId.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-ATM-FREEBSD-MIB", begemotAtmNgIfNodeId=begemotAtmNgIfNodeId, begemotAtmNgIfTable=begemotAtmNgIfTable, PYSNMP_MODULE_ID=begemotAtmFreeBSDGroup, begemotAtmNgIfEntry=begemotAtmNgIfEntry, begemotAtmNgGroup=begemotAtmNgGroup, begemotAtmFreeBSDGroup=begemotAtmFreeBSDGroup)
