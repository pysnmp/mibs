#
# PySNMP MIB module COLUBRIS-BANDWIDTH-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-BANDWIDTH-CONTROL-MIB.my
# Produced by pysmi-1.1.12 at Mon Sep 16 14:55:49 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisPriorityQueue, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisPriorityQueue")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Integer32, NotificationType, iso, Gauge32, Bits, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "iso", "Gauge32", "Bits", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("COLUBRIS-BANDWIDTH-CONTROL-MIB", colubrisBandwidthControlLevelMIBGroup=colubrisBandwidthControlLevelMIBGroup, coBandwidthControlLevelEntry=coBandwidthControlLevelEntry, coBandwidthControlLevelMaxReceiveRate=coBandwidthControlLevelMaxReceiveRate, PYSNMP_MODULE_ID=colubrisBandwidthControlMIB, colubrisBandwidthControlMIBObjects=colubrisBandwidthControlMIBObjects, coBandwidthControlConfig=coBandwidthControlConfig, colubrisBandwidthControlMIBConformance=colubrisBandwidthControlMIBConformance, coBandwidthControlLevelMinReceiveRate=coBandwidthControlLevelMinReceiveRate, coBandwidthControlLevelMinTransmitRate=coBandwidthControlLevelMinTransmitRate, colubrisBandwidthControlMIBGroups=colubrisBandwidthControlMIBGroups, coBandwidthControlLevelTable=coBandwidthControlLevelTable, coBandwidthControlLevelMaxTransmitRate=coBandwidthControlLevelMaxTransmitRate, colubrisBandwidthControlMIBCompliance=colubrisBandwidthControlMIBCompliance, coBandwidthControlEnable=coBandwidthControlEnable, coBandwidthControlLevelIndex=coBandwidthControlLevelIndex, colubrisBandwidthControlMIB=colubrisBandwidthControlMIB, colubrisBandwidthControlMIBCompliances=colubrisBandwidthControlMIBCompliances, coBandwidthControlMaxTransmitRate=coBandwidthControlMaxTransmitRate, colubrisBandwidthControlMIBGroup=colubrisBandwidthControlMIBGroup, coBandwidthControlMaxReceiveRate=coBandwidthControlMaxReceiveRate)
