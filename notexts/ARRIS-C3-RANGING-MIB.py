#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:17:12 2023
# On host fv-az842-726 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
TenthdBmV, docsIfCmtsCmStatusEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "TenthdBmV", "docsIfCmtsCmStatusEntry")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, Integer32, Counter32, ModuleIdentity, iso, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Gauge32, NotificationType, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Integer32", "Counter32", "ModuleIdentity", "iso", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Gauge32", "NotificationType", "Unsigned32", "ObjectIdentity")
DateAndTime, RowStatus, TruthValue, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TruthValue", "TextualConvention", "MacAddress", "DisplayString")
cmtsC3RngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10))
if mibBuilder.loadTexts: cmtsC3RngMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3RngMIB.setOrganization('Arris International')
phoenixRangingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1))
phxRangingPowerOverride = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingPowerOverride.setStatus('current')
phxRangingForceContinue = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingForceContinue.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", phxRangingPowerOverride=phxRangingPowerOverride, phxRangingForceContinue=phxRangingForceContinue, PYSNMP_MODULE_ID=cmtsC3RngMIB, cmtsC3RngMIB=cmtsC3RngMIB, phoenixRangingGroup=phoenixRangingGroup)
