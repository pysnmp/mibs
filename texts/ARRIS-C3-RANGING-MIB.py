#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.8 at Mon Feb  6 14:20:38 2023
# On host fv-az442-130 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, enterprises, Gauge32, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, TimeTicks, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "enterprises", "Gauge32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "TimeTicks", "iso", "Bits", "Counter64")
MacAddress, DisplayString, TextualConvention, DateAndTime, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "DateAndTime", "RowStatus", "TruthValue")
cmtsC3RngMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10))
if mibBuilder.loadTexts: cmtsC3RngMIB.setLastUpdated('200308200000Z')
if mibBuilder.loadTexts: cmtsC3RngMIB.setOrganization('Arris International')
if mibBuilder.loadTexts: cmtsC3RngMIB.setContactInfo('   Network Management\n                Postal: Arris International.\n                        4400 Cork Airport Business Park\n                        Cork Airport, Kinsale Road\n                        Cork, Ireland.\n                Tel:    +353 21 7305 800\n                Fax:    +353 21 4321 972')
if mibBuilder.loadTexts: cmtsC3RngMIB.setDescription('This MIB manages the FFT software on the Arris CMTS C3')
phoenixRangingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1))
phxRangingPowerOverride = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingPowerOverride.setStatus('current')
if mibBuilder.loadTexts: phxRangingPowerOverride.setDescription('Allows the CMTS to be configured to make only 0 dBmV\n                     power adjustments in RNG-RSP messages.')
phxRangingForceContinue = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: phxRangingForceContinue.setStatus('current')
if mibBuilder.loadTexts: phxRangingForceContinue.setDescription('Enable the CMTS to force all RNG-RSP messages to issue a\n                     Continue status indefinitely regardless of timing, power,\n                     etc. accuracy of previous incoming RNG-REQ')
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", PYSNMP_MODULE_ID=cmtsC3RngMIB, phoenixRangingGroup=phoenixRangingGroup, cmtsC3RngMIB=cmtsC3RngMIB, phxRangingPowerOverride=phxRangingPowerOverride, phxRangingForceContinue=phxRangingForceContinue)
