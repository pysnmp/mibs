#
# PySNMP MIB module ARRIS-CM-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CM-DEVICE-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:42:41 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Integer32, TimeTicks, Counter64, Gauge32, NotificationType, IpAddress, ObjectIdentity, Counter32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Integer32", "TimeTicks", "Counter64", "Gauge32", "NotificationType", "IpAddress", "ObjectIdentity", "Counter32", "MibIdentifier", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("ARRIS-CM-DEVICE-MIB", PYSNMP_MODULE_ID=arrisCmDevMib, arrisCmDevOperationalSetup=arrisCmDevOperationalSetup, arrisCmDevCmTest=arrisCmDevCmTest, arrisCmDevSalesSetup=arrisCmDevSalesSetup, arrisCmDevEnableDocsis20=arrisCmDevEnableDocsis20, arrisCmDevPermanentSetup=arrisCmDevPermanentSetup, arrisCmDevMib=arrisCmDevMib, arrisCmDevProvMethodIndicator=arrisCmDevProvMethodIndicator, arrisCmDevWanIsolationState=arrisCmDevWanIsolationState, arrisCmDevSwImageBuildTime=arrisCmDevSwImageBuildTime, arrisCmDevCmSetup=arrisCmDevCmSetup, arrisCmDevBase=arrisCmDevBase, ArrsCmDevProvMethod=ArrsCmDevProvMethod, arrisCmDevManufacturingTest=arrisCmDevManufacturingTest, arrisCmDevOperationalTest=arrisCmDevOperationalTest, arrisCmDevSwImageName=arrisCmDevSwImageName, arrisCmDevMibObjects=arrisCmDevMibObjects)
