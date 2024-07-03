#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:53:19 2024
# On host fv-az530-296 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, Counter64, NotificationType, Counter32, ModuleIdentity, iso, Gauge32, Integer32, enterprises, TimeTicks, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Counter32", "ModuleIdentity", "iso", "Gauge32", "Integer32", "enterprises", "TimeTicks", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, MacAddress, RowStatus, DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "RowStatus", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", phxRangingPowerOverride=phxRangingPowerOverride, phxRangingForceContinue=phxRangingForceContinue, PYSNMP_MODULE_ID=cmtsC3RngMIB, phoenixRangingGroup=phoenixRangingGroup, cmtsC3RngMIB=cmtsC3RngMIB)
