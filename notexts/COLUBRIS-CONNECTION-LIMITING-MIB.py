#
# PySNMP MIB module COLUBRIS-CONNECTION-LIMITING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-CONNECTION-LIMITING-MIB.my
# Produced by pysmi-1.1.12 at Fri Apr 12 00:28:53 2024
# On host fv-az975-788 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, IpAddress, Integer32, Counter32, Bits, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Unsigned32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "Integer32", "Counter32", "Bits", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Unsigned32", "Counter64", "MibIdentifier")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
colubrisConnectionLimitingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 18))
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setLastUpdated('200501210000Z')
if mibBuilder.loadTexts: colubrisConnectionLimitingMIB.setOrganization('Colubris Networks, Inc.')
colubrisConnectionLimitingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1))
connectionLimitingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1))
connectionLimitingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2))
connectionLimitingMaximumUserConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnections.setStatus('current')
connectionLimitingNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 1, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connectionLimitingNotificationEnabled.setStatus('current')
connectionLimitingMaximumSystemConnections = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectionLimitingMaximumSystemConnections.setStatus('current')
connectionLimitingUserMACAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserMACAddress.setStatus('current')
connectionLimitingUserIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 18, 1, 2, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: connectionLimitingUserIPAddress.setStatus('current')
colubrisConnectionLimitingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2))
colubrisConnectionLimitingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0))
connectionLimitingMaximumUserConnectionsReached = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 18, 2, 0, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if mibBuilder.loadTexts: connectionLimitingMaximumUserConnectionsReached.setStatus('current')
colubrisConnectionLimitingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3))
colubrisConnectionLimitingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1))
colubrisConnectionLimitingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2))
colubrisConnectionLimitingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 1, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingConfigMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingInfoMIBGroup"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "colubrisConnectionLimitingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingMIBCompliance = colubrisConnectionLimitingMIBCompliance.setStatus('current')
colubrisConnectionLimitingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 1)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingConfigMIBGroup = colubrisConnectionLimitingConfigMIBGroup.setStatus('current')
colubrisConnectionLimitingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 2)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumSystemConnections"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserMACAddress"), ("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingUserIPAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingInfoMIBGroup = colubrisConnectionLimitingInfoMIBGroup.setStatus('current')
colubrisConnectionLimitingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 18, 3, 2, 3)).setObjects(("COLUBRIS-CONNECTION-LIMITING-MIB", "connectionLimitingMaximumUserConnectionsReached"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisConnectionLimitingNotificationGroup = colubrisConnectionLimitingNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-CONNECTION-LIMITING-MIB", colubrisConnectionLimitingMIBObjects=colubrisConnectionLimitingMIBObjects, connectionLimitingNotificationEnabled=connectionLimitingNotificationEnabled, connectionLimitingMaximumSystemConnections=connectionLimitingMaximumSystemConnections, connectionLimitingUserIPAddress=connectionLimitingUserIPAddress, colubrisConnectionLimitingNotificationGroup=colubrisConnectionLimitingNotificationGroup, colubrisConnectionLimitingMIBCompliances=colubrisConnectionLimitingMIBCompliances, colubrisConnectionLimitingMIBConformance=colubrisConnectionLimitingMIBConformance, colubrisConnectionLimitingMIB=colubrisConnectionLimitingMIB, connectionLimitingInfo=connectionLimitingInfo, colubrisConnectionLimitingMIBNotificationPrefix=colubrisConnectionLimitingMIBNotificationPrefix, connectionLimitingConfig=connectionLimitingConfig, colubrisConnectionLimitingInfoMIBGroup=colubrisConnectionLimitingInfoMIBGroup, connectionLimitingMaximumUserConnections=connectionLimitingMaximumUserConnections, colubrisConnectionLimitingMIBNotifications=colubrisConnectionLimitingMIBNotifications, connectionLimitingMaximumUserConnectionsReached=connectionLimitingMaximumUserConnectionsReached, PYSNMP_MODULE_ID=colubrisConnectionLimitingMIB, colubrisConnectionLimitingMIBGroups=colubrisConnectionLimitingMIBGroups, colubrisConnectionLimitingMIBCompliance=colubrisConnectionLimitingMIBCompliance, connectionLimitingUserMACAddress=connectionLimitingUserMACAddress, colubrisConnectionLimitingConfigMIBGroup=colubrisConnectionLimitingConfigMIBGroup)
