#
# PySNMP MIB module F5-ALERT-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-ALERT-DEF-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:22:20 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
platform, f5Compliance = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform", "f5Compliance")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, IpAddress, NotificationType, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Counter32, Gauge32, ObjectIdentity, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "NotificationType", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "ObjectIdentity", "iso", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f5Alerts = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 1))
f5Alerts.setRevisions(('2019-08-01 09:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f5Alerts.setRevisionsDescriptions(('F5 Alert Common MIB definitions.',))
if mibBuilder.loadTexts: f5Alerts.setLastUpdated('201908010941Z')
if mibBuilder.loadTexts: f5Alerts.setOrganization('F5 Networks, Inc.')
if mibBuilder.loadTexts: f5Alerts.setContactInfo('postal: F5 Networks, Inc.\n                  801 5th Ave\n                  Seattle,  WA 98104\n          phone:  (206) 272-5555\n          email:  support@f5.com')
if mibBuilder.loadTexts: f5Alerts.setDescription('Top-level infrastructure of the F5 Networks enterprise Alert MIB tree.')
class F5Severity(TextualConvention, Integer32):
    description = 'The severity of the alerts.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("na", 8))

class F5CondEffect(TextualConvention, Integer32):
    description = 'The effect of the condition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 9999))
    namedValues = NamedValues(("clear", 0), ("assert", 1), ("event", 2), ("other", 9999))

f5AlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0))
f5AlertNotificationObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1))
f5AlertNotificationObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2))
f5AlertNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3))
alertSource = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSource.setStatus('current')
if mibBuilder.loadTexts: alertSource.setDescription('The source/facility generating this trap.')
alertEffect = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 2), F5CondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEffect.setStatus('current')
if mibBuilder.loadTexts: alertEffect.setDescription('The effect of the alert, whether it is raising or clearing.')
alertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 3), F5Severity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSeverity.setStatus('current')
if mibBuilder.loadTexts: alertSeverity.setDescription('The severity of the alarm.')
alertTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertTimeStamp.setStatus('current')
if mibBuilder.loadTexts: alertTimeStamp.setDescription('This object specifies the date and time the Trap was generated.')
alertDescription = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertDescription.setStatus('current')
if mibBuilder.loadTexts: alertDescription.setDescription('The alarm Trap description.')
alertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertSource"), ("F5-ALERT-DEF-MIB", "alertEffect"), ("F5-ALERT-DEF-MIB", "alertSeverity"), ("F5-ALERT-DEF-MIB", "alertTimeStamp"), ("F5-ALERT-DEF-MIB", "alertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertGroup = alertGroup.setStatus('current')
if mibBuilder.loadTexts: alertGroup.setDescription('This is a generic Trap for reporting alerts.')
f5AlertGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12276, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f5AlertGroupCompliance = f5AlertGroupCompliance.setStatus('current')
if mibBuilder.loadTexts: f5AlertGroupCompliance.setDescription('This specifies the objects that are required to claim\n         compliance to F5 Alert Notifications.')
mibBuilder.exportSymbols("F5-ALERT-DEF-MIB", f5AlertNotificationObject=f5AlertNotificationObject, F5CondEffect=F5CondEffect, alertSeverity=alertSeverity, alertGroup=alertGroup, PYSNMP_MODULE_ID=f5Alerts, alertTimeStamp=alertTimeStamp, alertEffect=alertEffect, f5AlertGroupCompliance=f5AlertGroupCompliance, F5Severity=F5Severity, f5Alerts=f5Alerts, f5AlertNotificationGroup=f5AlertNotificationGroup, f5AlertObjects=f5AlertObjects, alertDescription=alertDescription, alertSource=alertSource, f5AlertNotificationObjectGroup=f5AlertNotificationObjectGroup)
