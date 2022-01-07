#
# PySNMP MIB module COLUBRIS-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SYSLOG-MIB.my
# Produced by pysmi-1.1.8 at Fri Jan  7 16:12:35 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, Counter64, Counter32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, ObjectIdentity, Integer32, TimeTicks, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter64", "Counter32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "ObjectIdentity", "Integer32", "TimeTicks", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 3))
if mibBuilder.loadTexts: colubrisSyslogMIB.setLastUpdated('200402100000Z')
if mibBuilder.loadTexts: colubrisSyslogMIB.setOrganization('Colubris Networks, Inc.')
colubrisSyslogMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1))
syslogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1))
syslogMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2))
class SyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

syslogSeverityNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityNotificationEnabled.setStatus('current')
syslogRegExMatchNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 2), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRegExMatchNotificationEnabled.setStatus('current')
syslogSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 3), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityLevel.setStatus('current')
syslogTrapSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 4), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogTrapSeverityLevel.setStatus('current')
syslogMessageRegEx = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogMessageRegEx.setStatus('current')
syslogMsgNumber = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgNumber.setStatus('current')
syslogMsgFacility = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
syslogMsgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 3), SyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
syslogMsgText = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgText.setStatus('current')
colubrisSyslogMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2))
colubrisSyslogMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0))
syslogSeverityNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogSeverityNotification.setStatus('current')
syslogRegExMatchNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 2)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogRegExMatchNotification.setStatus('current')
colubrisSyslogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3))
colubrisSyslogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1))
colubrisSyslogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2))
colubrisSyslogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "colubrisSyslogMIBGroup"), ("COLUBRIS-SYSLOG-MIB", "colubrisSyslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogMIBCompliance = colubrisSyslogMIBCompliance.setStatus('current')
colubrisSyslogMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 1)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotificationEnabled"), ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotificationEnabled"), ("COLUBRIS-SYSLOG-MIB", "syslogSeverityLevel"), ("COLUBRIS-SYSLOG-MIB", "syslogTrapSeverityLevel"), ("COLUBRIS-SYSLOG-MIB", "syslogMessageRegEx"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"), ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogMIBGroup = colubrisSyslogMIBGroup.setStatus('current')
colubrisSyslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 2)).setObjects(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotification"), ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisSyslogNotificationGroup = colubrisSyslogNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SYSLOG-MIB", colubrisSyslogMIBConformance=colubrisSyslogMIBConformance, syslogMsgText=syslogMsgText, syslogSeverityNotificationEnabled=syslogSeverityNotificationEnabled, colubrisSyslogMIBGroups=colubrisSyslogMIBGroups, syslogRegExMatchNotificationEnabled=syslogRegExMatchNotificationEnabled, syslogTrapSeverityLevel=syslogTrapSeverityLevel, colubrisSyslogMIB=colubrisSyslogMIB, syslogMsgNumber=syslogMsgNumber, syslogSeverityLevel=syslogSeverityLevel, colubrisSyslogMIBCompliances=colubrisSyslogMIBCompliances, colubrisSyslogMIBGroup=colubrisSyslogMIBGroup, colubrisSyslogMIBNotificationPrefix=colubrisSyslogMIBNotificationPrefix, syslogConfig=syslogConfig, syslogMessageRegEx=syslogMessageRegEx, syslogSeverityNotification=syslogSeverityNotification, colubrisSyslogMIBObjects=colubrisSyslogMIBObjects, syslogMsgSeverity=syslogMsgSeverity, syslogMessage=syslogMessage, SyslogSeverity=SyslogSeverity, colubrisSyslogMIBNotifications=colubrisSyslogMIBNotifications, syslogMsgFacility=syslogMsgFacility, colubrisSyslogMIBCompliance=colubrisSyslogMIBCompliance, PYSNMP_MODULE_ID=colubrisSyslogMIB, colubrisSyslogNotificationGroup=colubrisSyslogNotificationGroup, syslogRegExMatchNotification=syslogRegExMatchNotification)
