#
# PySNMP MIB module COLUBRIS-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-BANDWIDTH-CONTROL-MIB.my
# Produced by pysmi-1.1.10 at Fri Nov 10 07:42:21 2023
# On host fv-az885-747 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisPriorityQueue, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisPriorityQueue")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Integer32, Unsigned32, ObjectIdentity, Gauge32, MibIdentifier, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Unsigned32", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Bits", "ModuleIdentity")
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
mibBuilder.exportSymbols("COLUBRIS-BANDWIDTH-CONTROL-MIB", colubrisBandwidthControlMIBGroups=colubrisBandwidthControlMIBGroups, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, colubrisBandwidthControlMIBObjects=colubrisBandwidthControlMIBObjects, coBandwidthControlEnable=coBandwidthControlEnable, colubrisBandwidthControlMIB=colubrisBandwidthControlMIB, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, colubrisBandwidthControlMIBGroup=colubrisBandwidthControlMIBGroup, colubrisBandwidthControlMIBCompliance=colubrisBandwidthControlMIBCompliance, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate, PYSNMP_MODULE_ID=colubrisBandwidthControlMIB, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, colubrisBandwidthControlMIBCompliances=colubrisBandwidthControlMIBCompliances, colubrisBandwidthControlMIBConformance=colubrisBandwidthControlMIBConformance, colubrisBandwidthControlLevelMIBGroup=colubrisBandwidthControlLevelMIBGroup, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, coBandwidthControlLevelTable=coBandwidthControlLevelTable, coBandwidthControlConfig=coBandwidthControlConfig)
