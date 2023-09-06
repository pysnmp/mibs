#
# PySNMP MIB module MDS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-EVENT-MIB
# Produced by pysmi-1.1.8 at Wed Sep  6 13:31:55 2023
# On host fv-az361-883 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
mdsLogging, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsLogging")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ModuleIdentity, iso, MibIdentifier, Unsigned32, TimeTicks, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ModuleIdentity", "iso", "MibIdentifier", "Unsigned32", "TimeTicks", "Gauge32", "Counter64")
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
mibBuilder.exportSymbols("MDS-EVENT-MIB", traps0=traps0, traps=traps, mdsEventVariables=mdsEventVariables, mdsEventName=mdsEventName, PYSNMP_MODULE_ID=mdsEventMIB, mdsEventInfoInCee=mdsEventInfoInCee, mdsEventMIBConformance=mdsEventMIBConformance, mdsEventMIBCompliances=mdsEventMIBCompliances, mdsEventVariablesCeeGroup=mdsEventVariablesCeeGroup, mdsEventMIBGroups=mdsEventMIBGroups, mdsEventNotificationsGroup=mdsEventNotificationsGroup, mdsEventMIBCompliance=mdsEventMIBCompliance, mdsEvent=mdsEvent, mdsEventMIBNotifications=mdsEventMIBNotifications, mdsEventMIB=mdsEventMIB, mdsEventMIBObjects=mdsEventMIBObjects)
