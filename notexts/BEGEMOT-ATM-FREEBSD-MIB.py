#
# PySNMP MIB module BEGEMOT-ATM-FREEBSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-ATM-FREEBSD-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 10:07:31 2023
# On host fv-az351-613 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
begemotAtmSysGroup, begemotAtmIfEntry = mibBuilder.importSymbols("BEGEMOT-ATM-MIB", "begemotAtmSysGroup", "begemotAtmIfEntry")
NgNodeIdOrZero, = mibBuilder.importSymbols("BEGEMOT-NETGRAPH-MIB", "NgNodeIdOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, Bits, Integer32, IpAddress, MibIdentifier, Counter32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits", "Integer32", "IpAddress", "MibIdentifier", "Counter32", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BEGEMOT-ATM-FREEBSD-MIB", begemotAtmNgIfTable=begemotAtmNgIfTable, begemotAtmFreeBSDGroup=begemotAtmFreeBSDGroup, begemotAtmNgIfNodeId=begemotAtmNgIfNodeId, PYSNMP_MODULE_ID=begemotAtmFreeBSDGroup, begemotAtmNgGroup=begemotAtmNgGroup, begemotAtmNgIfEntry=begemotAtmNgIfEntry)
