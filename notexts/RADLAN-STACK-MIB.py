#
# PySNMP MIB module RADLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-STACK-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:42:36 2024
# On host fv-az984-576 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, TimeTicks, Counter64, ObjectIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Integer32, Unsigned32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "Counter32", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("RADLAN-STACK-MIB", rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, rlStackUnitMode=rlStackUnitMode, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, PYSNMP_MODULE_ID=rlStack, rlStackCurrentUnitId=rlStackCurrentUnitId, rlStack=rlStack, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset)
