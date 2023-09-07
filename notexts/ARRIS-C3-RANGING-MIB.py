#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 13:20:07 2023
# On host fv-az422-951 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Unsigned32, iso, TimeTicks, enterprises, ObjectIdentity, Bits, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Unsigned32", "iso", "TimeTicks", "enterprises", "ObjectIdentity", "Bits", "NotificationType", "MibIdentifier")
MacAddress, TextualConvention, RowStatus, TruthValue, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "TruthValue", "DisplayString", "DateAndTime")
cmtsC3RngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10))
if mibBuilder.loadTexts: cmtsC3RngMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3RngMIB.setOrganization('Arris International')
phoenixRangingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1))
phxRangingPowerOverride = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingPowerOverride.setStatus('current')
phxRangingForceContinue = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingForceContinue.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", PYSNMP_MODULE_ID=cmtsC3RngMIB, phxRangingForceContinue=phxRangingForceContinue, cmtsC3RngMIB=cmtsC3RngMIB, phoenixRangingGroup=phoenixRangingGroup, phxRangingPowerOverride=phxRangingPowerOverride)
