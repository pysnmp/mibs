#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:10:10 2023
# On host fv-az247-870 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, NotificationType, Integer32, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, MibIdentifier, IpAddress, ModuleIdentity, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "NotificationType", "Integer32", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Counter32", "TimeTicks", "Bits")
TruthValue, TextualConvention, RowStatus, DateAndTime, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DateAndTime", "MacAddress", "DisplayString")
cmtsC3RngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10))
if mibBuilder.loadTexts: cmtsC3RngMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3RngMIB.setOrganization('Arris International')
phoenixRangingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1))
phxRangingPowerOverride = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingPowerOverride.setStatus('current')
phxRangingForceContinue = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingForceContinue.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", phoenixRangingGroup=phoenixRangingGroup, phxRangingPowerOverride=phxRangingPowerOverride, cmtsC3RngMIB=cmtsC3RngMIB, phxRangingForceContinue=phxRangingForceContinue, PYSNMP_MODULE_ID=cmtsC3RngMIB)
