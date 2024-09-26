#
# PySNMP MIB module F5-ALERT-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-ALERT-DEF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 26 02:13:27 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
platform, f5Compliance = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "platform", "f5Compliance")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, iso, TimeTicks, Counter64, NotificationType, ModuleIdentity, Integer32, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("F5-ALERT-DEF-MIB", F5CondEffect=F5CondEffect, f5AlertNotificationGroup=f5AlertNotificationGroup, f5AlertNotificationObjectGroup=f5AlertNotificationObjectGroup, f5AlertNotificationObject=f5AlertNotificationObject, alertSource=alertSource, alertTimeStamp=alertTimeStamp, alertGroup=alertGroup, F5Severity=F5Severity, f5Alerts=f5Alerts, f5AlertGroupCompliance=f5AlertGroupCompliance, alertEffect=alertEffect, alertDescription=alertDescription, alertSeverity=alertSeverity, PYSNMP_MODULE_ID=f5Alerts, f5AlertObjects=f5AlertObjects)
