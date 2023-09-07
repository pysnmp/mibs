#
# PySNMP MIB module RADLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-STACK-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 13:33:21 2023
# On host fv-az422-951 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, TimeTicks, Bits, ObjectIdentity, Counter32, Unsigned32, ModuleIdentity, Integer32, NotificationType, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "Bits", "ObjectIdentity", "Counter32", "Unsigned32", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 107))
rlStack.setRevisions(('2005-04-14 00:00',))
if mibBuilder.loadTexts: rlStack.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlStack.setOrganization('Radlan Computer Communications Ltd.')
rlStackActiveUnitIdTable = MibTable((1, 3, 6, 1, 4, 1, 89, 107, 1), )
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setStatus('current')
rlStackActiveUnitIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 107, 1, 1), ).setIndexNames((0, "RADLAN-STACK-MIB", "rlStackCurrentUnitId"))
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setStatus('current')
rlStackCurrentUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 107, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackCurrentUnitId.setStatus('current')
rlStackActiveUnitIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 107, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setStatus('current')
rlStackUnitModeAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setStatus('current')
rlStackUnitMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackUnitMode.setStatus('current')
rlStackUnitMacAddressAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitMacAddressAfterReset.setStatus('current')
mibBuilder.exportSymbols("RADLAN-STACK-MIB", rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, rlStackCurrentUnitId=rlStackCurrentUnitId, PYSNMP_MODULE_ID=rlStack, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, rlStack=rlStack, rlStackUnitMode=rlStackUnitMode)
