#
# PySNMP MIB module MDS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-EVENT-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 09:18:14 2023
# On host fv-az1110-165 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
mdsLogging, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsLogging")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, TimeTicks, iso, ModuleIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Unsigned32, Integer32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "iso", "ModuleIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Unsigned32", "Integer32", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mdsEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1))
mdsEventMIB.setRevisions(('2018-05-16 00:00', '2013-04-22 00:00',))
if mibBuilder.loadTexts: mdsEventMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsEventMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mdsEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1))
mdsEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2))
mdsEventVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1))
mdsEventName = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventName.setStatus('current')
mdsEventInfoInCee = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventInfoInCee.setStatus('current')
traps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0))
mdsEvent = NotificationType((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0, 1))
if mibBuilder.loadTexts: mdsEvent.setStatus('current')
mdsEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3))
mdsEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1))
mdsEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2))
mdsEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventNotificationsGroup"), ("MDS-EVENT-MIB", "mdsEventVariablesCeeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventMIBCompliance = mdsEventMIBCompliance.setStatus('current')
mdsEventNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 1)).setObjects(("MDS-EVENT-MIB", "mdsEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventNotificationsGroup = mdsEventNotificationsGroup.setStatus('current')
mdsEventVariablesCeeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventName"), ("MDS-EVENT-MIB", "mdsEventInfoInCee"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventVariablesCeeGroup = mdsEventVariablesCeeGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-EVENT-MIB", mdsEventMIBCompliance=mdsEventMIBCompliance, mdsEventMIBCompliances=mdsEventMIBCompliances, traps=traps, mdsEventMIBConformance=mdsEventMIBConformance, mdsEventMIBObjects=mdsEventMIBObjects, mdsEventVariables=mdsEventVariables, PYSNMP_MODULE_ID=mdsEventMIB, mdsEvent=mdsEvent, mdsEventMIBNotifications=mdsEventMIBNotifications, mdsEventInfoInCee=mdsEventInfoInCee, mdsEventMIBGroups=mdsEventMIBGroups, traps0=traps0, mdsEventNotificationsGroup=mdsEventNotificationsGroup, mdsEventVariablesCeeGroup=mdsEventVariablesCeeGroup, mdsEventMIB=mdsEventMIB, mdsEventName=mdsEventName)
