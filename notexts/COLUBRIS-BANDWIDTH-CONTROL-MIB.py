#
# PySNMP MIB module COLUBRIS-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-BANDWIDTH-CONTROL-MIB.my
# Produced by pysmi-1.1.8 at Thu Sep  7 09:17:51 2023
# On host fv-az1234-541 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.12 (main, Jun  7 2023, 13:43:11) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisPriorityQueue, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisPriorityQueue")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, iso, NotificationType, TimeTicks, Unsigned32, Gauge32, MibIdentifier, Counter64, ObjectIdentity, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "NotificationType", "TimeTicks", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
colubrisBandwidthControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 14))
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setLastUpdated('200408170000Z')
if mibBuilder.loadTexts: colubrisBandwidthControlMIB.setOrganization('Colubris Networks, Inc.')
colubrisBandwidthControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1))
coBandwidthControlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1))
coBandwidthControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlEnable.setStatus('current')
coBandwidthControlMaxTransmitRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxTransmitRate.setStatus('current')
coBandwidthControlMaxReceiveRate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlMaxReceiveRate.setStatus('current')
coBandwidthControlLevelTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4), )
if mibBuilder.loadTexts: coBandwidthControlLevelTable.setStatus('current')
coBandwidthControlLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1), ).setIndexNames((0, "COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelIndex"))
if mibBuilder.loadTexts: coBandwidthControlLevelEntry.setStatus('current')
coBandwidthControlLevelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 1), ColubrisPriorityQueue())
if mibBuilder.loadTexts: coBandwidthControlLevelIndex.setStatus('current')
coBandwidthControlLevelMinTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinTransmitRate.setStatus('current')
coBandwidthControlLevelMaxTransmitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxTransmitRate.setStatus('current')
coBandwidthControlLevelMinReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMinReceiveRate.setStatus('current')
coBandwidthControlLevelMaxReceiveRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 14, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coBandwidthControlLevelMaxReceiveRate.setStatus('current')
colubrisBandwidthControlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2))
colubrisBandwidthControlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1))
colubrisBandwidthControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2))
colubrisBandwidthControlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 1, 1)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "colubrisBandwidthControlMIBGroup"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "colubrisBandwidthControlLevelMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlMIBCompliance = colubrisBandwidthControlMIBCompliance.setStatus('current')
colubrisBandwidthControlMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 1)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlEnable"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlMIBGroup = colubrisBandwidthControlMIBGroup.setStatus('current')
colubrisBandwidthControlLevelMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 14, 2, 2, 2)).setObjects(("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxTransmitRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMinReceiveRate"), ("COLUBRIS-BANDWIDTH-CONTROL-MIB", "coBandwidthControlLevelMaxReceiveRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisBandwidthControlLevelMIBGroup = colubrisBandwidthControlLevelMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-BANDWIDTH-CONTROL-MIB", coBandwidthControlEnable=coBandwidthControlEnable, coBandwidthControlConfig=coBandwidthControlConfig, colubrisBandwidthControlMIBGroup=colubrisBandwidthControlMIBGroup, colubrisBandwidthControlLevelMIBGroup=colubrisBandwidthControlLevelMIBGroup, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, PYSNMP_MODULE_ID=colubrisBandwidthControlMIB, colubrisBandwidthControlMIBConformance=colubrisBandwidthControlMIBConformance, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, coBandwidthControlLevelTable=coBandwidthControlLevelTable, colubrisBandwidthControlMIBCompliance=colubrisBandwidthControlMIBCompliance, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, colubrisBandwidthControlMIBCompliances=colubrisBandwidthControlMIBCompliances, colubrisBandwidthControlMIBGroups=colubrisBandwidthControlMIBGroups, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate, colubrisBandwidthControlMIBObjects=colubrisBandwidthControlMIBObjects, colubrisBandwidthControlMIB=colubrisBandwidthControlMIB, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate)
