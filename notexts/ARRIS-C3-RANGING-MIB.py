#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:21:02 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Unsigned32, TimeTicks, iso, Gauge32, MibIdentifier, Counter64, IpAddress, NotificationType, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Unsigned32", "TimeTicks", "iso", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "Bits", "enterprises")
TruthValue, MacAddress, DisplayString, DateAndTime, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "DateAndTime", "TextualConvention", "RowStatus")
cmtsC3RngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10))
if mibBuilder.loadTexts: cmtsC3RngMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3RngMIB.setOrganization('Arris International')
phoenixRangingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1))
phxRangingPowerOverride = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingPowerOverride.setStatus('current')
phxRangingForceContinue = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingForceContinue.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", phoenixRangingGroup=phoenixRangingGroup, phxRangingPowerOverride=phxRangingPowerOverride, cmtsC3RngMIB=cmtsC3RngMIB, PYSNMP_MODULE_ID=cmtsC3RngMIB, phxRangingForceContinue=phxRangingForceContinue)
