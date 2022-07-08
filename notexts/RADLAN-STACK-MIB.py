#
# PySNMP MIB module RADLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-STACK-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:07:45 2022
# On host fv-az121-197 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, TimeTicks, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter32, IpAddress, ObjectIdentity, Gauge32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "TimeTicks", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter32", "IpAddress", "ObjectIdentity", "Gauge32", "Bits", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("RADLAN-STACK-MIB", rlStackCurrentUnitId=rlStackCurrentUnitId, rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, rlStack=rlStack, rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, PYSNMP_MODULE_ID=rlStack, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, rlStackUnitMode=rlStackUnitMode, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry)
