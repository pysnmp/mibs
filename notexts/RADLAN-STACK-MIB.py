#
# PySNMP MIB module RADLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-STACK-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:31:48 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, TimeTicks, Counter64, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Bits, Integer32, Gauge32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Bits", "Integer32", "Gauge32", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
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
mibBuilder.exportSymbols("RADLAN-STACK-MIB", rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, PYSNMP_MODULE_ID=rlStack, rlStack=rlStack, rlStackUnitMode=rlStackUnitMode, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, rlStackCurrentUnitId=rlStackCurrentUnitId)
