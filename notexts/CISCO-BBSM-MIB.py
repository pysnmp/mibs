#
# PySNMP MIB module CISCO-BBSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BBSM-MIB
# Source digest sha256:cbd91c5fe5a5b22a3885e7f4c98f0d441c916251aeece94e32dfdbdd6c14c609
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
ciscoBbsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 358))
ciscoBbsmMIB.setRevisions(('2004-04-03 00:00',))
if mibBuilder.loadTexts: ciscoBbsmMIB.setLastUpdated('2004-04-03 00:00')
if mibBuilder.loadTexts: ciscoBbsmMIB.setOrganization('Cisco Systems, Inc.')
ciscoBbsmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 0))
ciscoBbsmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1))
ciscoBbsmEventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1))
cbbsmEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 1), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventDescription.setStatus('current')
cbbsmEventSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventSource.setStatus('current')
cbbsmEventID = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventID.setStatus('current')
cbbsmEventType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("information", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventType.setStatus('current')
cbbsmEventTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 5), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cbbsmEventTime.setStatus('current')
ciscoBbsmEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 358, 0, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if mibBuilder.loadTexts: ciscoBbsmEvent.setStatus('current')
ciscoBbsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2))
ciscoBbsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1))
ciscoBbsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2))
ciscoBbsmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1, 1)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmMIBGroup"), ("CISCO-BBSM-MIB", "ciscoBbsmMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBCompliance = ciscoBbsmMIBCompliance.setStatus('current')
ciscoBbsmMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 1)).setObjects(("CISCO-BBSM-MIB", "cbbsmEventDescription"), ("CISCO-BBSM-MIB", "cbbsmEventSource"), ("CISCO-BBSM-MIB", "cbbsmEventID"), ("CISCO-BBSM-MIB", "cbbsmEventType"), ("CISCO-BBSM-MIB", "cbbsmEventTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBGroup = ciscoBbsmMIBGroup.setStatus('current')
ciscoBbsmMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 2)).setObjects(("CISCO-BBSM-MIB", "ciscoBbsmEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBbsmMIBNotificationGroup = ciscoBbsmMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-BBSM-MIB", PYSNMP_MODULE_ID=ciscoBbsmMIB, cbbsmEventDescription=cbbsmEventDescription, cbbsmEventID=cbbsmEventID, cbbsmEventSource=cbbsmEventSource, cbbsmEventTime=cbbsmEventTime, cbbsmEventType=cbbsmEventType, ciscoBbsmEvent=ciscoBbsmEvent, ciscoBbsmEventInfo=ciscoBbsmEventInfo, ciscoBbsmMIB=ciscoBbsmMIB, ciscoBbsmMIBCompliance=ciscoBbsmMIBCompliance, ciscoBbsmMIBCompliances=ciscoBbsmMIBCompliances, ciscoBbsmMIBConformance=ciscoBbsmMIBConformance, ciscoBbsmMIBGroup=ciscoBbsmMIBGroup, ciscoBbsmMIBGroups=ciscoBbsmMIBGroups, ciscoBbsmMIBNotificationGroup=ciscoBbsmMIBNotificationGroup, ciscoBbsmMIBObjects=ciscoBbsmMIBObjects, ciscoBbsmNotifications=ciscoBbsmNotifications)
