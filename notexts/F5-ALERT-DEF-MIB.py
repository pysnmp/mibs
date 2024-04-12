#
# PySNMP MIB module F5-ALERT-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-ALERT-DEF-MIB
# Produced by pysmi-1.1.12 at Fri Apr 12 00:27:58 2024
# On host fv-az975-788 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
f5Compliance, platform = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "f5Compliance", "platform")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, MibIdentifier, Counter64, Unsigned32, Bits, Counter32, NotificationType, TimeTicks, ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "Unsigned32", "Bits", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f5Alerts = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 1))
f5Alerts.setRevisions(('2019-08-01 09:41',))
if mibBuilder.loadTexts: f5Alerts.setLastUpdated('201908010941Z')
if mibBuilder.loadTexts: f5Alerts.setOrganization('F5 Networks, Inc.')
class F5Severity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("na", 8))

class F5CondEffect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 9999))
    namedValues = NamedValues(("clear", 0), ("assert", 1), ("event", 2), ("other", 9999))

f5AlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0))
f5AlertNotificationObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1))
f5AlertNotificationObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2))
f5AlertNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3))
alertSource = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSource.setStatus('current')
alertEffect = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 2), F5CondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEffect.setStatus('current')
alertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 3), F5Severity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSeverity.setStatus('current')
alertTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertTimeStamp.setStatus('current')
alertDescription = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertDescription.setStatus('current')
alertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertSource"), ("F5-ALERT-DEF-MIB", "alertEffect"), ("F5-ALERT-DEF-MIB", "alertSeverity"), ("F5-ALERT-DEF-MIB", "alertTimeStamp"), ("F5-ALERT-DEF-MIB", "alertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertGroup = alertGroup.setStatus('current')
f5AlertGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12276, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f5AlertGroupCompliance = f5AlertGroupCompliance.setStatus('current')
mibBuilder.exportSymbols("F5-ALERT-DEF-MIB", f5AlertObjects=f5AlertObjects, alertSource=alertSource, alertEffect=alertEffect, f5AlertGroupCompliance=f5AlertGroupCompliance, alertTimeStamp=alertTimeStamp, PYSNMP_MODULE_ID=f5Alerts, alertDescription=alertDescription, alertSeverity=alertSeverity, F5CondEffect=F5CondEffect, f5AlertNotificationObjectGroup=f5AlertNotificationObjectGroup, alertGroup=alertGroup, f5Alerts=f5Alerts, F5Severity=F5Severity, f5AlertNotificationGroup=f5AlertNotificationGroup, f5AlertNotificationObject=f5AlertNotificationObject)
