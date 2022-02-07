#
# PySNMP MIB module ARRIS-CM-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-DEVICE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 15:44:47 2022
# On host fv-az77-513 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, TimeTicks, Gauge32, iso, IpAddress, ModuleIdentity, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32", "iso", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
arrisCmDevMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1))
arrisCmDevMib.setRevisions(('1902-11-08 00:00', '1902-10-29 00:00', '1902-10-23 00:00', '1902-07-10 00:00',))
if mibBuilder.loadTexts: arrisCmDevMib.setLastUpdated('0212100000Z')
if mibBuilder.loadTexts: arrisCmDevMib.setOrganization('ARRIS Broadband')
class ArrsCmDevProvMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("docsisOnly", 0), ("fullPacketCable", 1), ("packetCableMinusKDC", 2), ("cps", 3), ("gupi", 4), ("singleMAC", 5))

arrisCmDevMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1))
arrisCmDevBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1))
arrisCmDevCmSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2))
arrisCmDevCmTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3))
arrisCmDevPermanentSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 2))
arrisCmDevOperationalSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3))
arrisCmDevSalesSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 4))
arrisCmDevManufacturingTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 2))
arrisCmDevOperationalTest = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 3, 3))
arrisCmDevWanIsolationState = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off-InActiveMode", 1), ("on-ActiveMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevWanIsolationState.setStatus('current')
arrisCmDevSwImageName = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisCmDevSwImageName.setStatus('current')
arrisCmDevSwImageBuildTime = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisCmDevSwImageBuildTime.setStatus('current')
arrisCmDevProvMethodIndicator = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 2), ArrsCmDevProvMethod()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevProvMethodIndicator.setStatus('current')
arrisCmDevEnableDocsis20 = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 1, 1, 2, 3, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisCmDevEnableDocsis20.setStatus('current')
mibBuilder.exportSymbols("ARRIS-CM-DEVICE-MIB", arrisCmDevSwImageName=arrisCmDevSwImageName, arrisCmDevOperationalSetup=arrisCmDevOperationalSetup, ArrsCmDevProvMethod=ArrsCmDevProvMethod, arrisCmDevCmTest=arrisCmDevCmTest, arrisCmDevProvMethodIndicator=arrisCmDevProvMethodIndicator, arrisCmDevMib=arrisCmDevMib, arrisCmDevPermanentSetup=arrisCmDevPermanentSetup, arrisCmDevEnableDocsis20=arrisCmDevEnableDocsis20, arrisCmDevBase=arrisCmDevBase, arrisCmDevCmSetup=arrisCmDevCmSetup, arrisCmDevSalesSetup=arrisCmDevSalesSetup, arrisCmDevMibObjects=arrisCmDevMibObjects, PYSNMP_MODULE_ID=arrisCmDevMib, arrisCmDevOperationalTest=arrisCmDevOperationalTest, arrisCmDevSwImageBuildTime=arrisCmDevSwImageBuildTime, arrisCmDevManufacturingTest=arrisCmDevManufacturingTest, arrisCmDevWanIsolationState=arrisCmDevWanIsolationState)
