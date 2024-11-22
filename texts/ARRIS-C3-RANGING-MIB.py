#
# PySNMP MIB module ARRIS-C3-RANGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-RANGING-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:52:26 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
docsIfCmtsCmStatusEntry, TenthdBmV = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "TenthdBmV")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Integer32, TimeTicks, ObjectIdentity, NotificationType, Counter32, Unsigned32, Gauge32, Bits, MibIdentifier, enterprises, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "Gauge32", "Bits", "MibIdentifier", "enterprises", "IpAddress", "iso")
MacAddress, TextualConvention, RowStatus, DisplayString, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString", "TruthValue", "DateAndTime")
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
mibBuilder.exportSymbols("ARRIS-C3-RANGING-MIB", cmtsC3RngMIB=cmtsC3RngMIB, phoenixRangingGroup=phoenixRangingGroup, phxRangingPowerOverride=phxRangingPowerOverride, PYSNMP_MODULE_ID=cmtsC3RngMIB, phxRangingForceContinue=phxRangingForceContinue)
