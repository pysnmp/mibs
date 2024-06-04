#
# PySNMP MIB module MDS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-EVENT-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 10:06:02 2024
# On host fv-az1773-903 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
mdsLogging, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsLogging")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Counter32, NotificationType, Counter64, Integer32, ObjectIdentity, TimeTicks, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "NotificationType", "Counter64", "Integer32", "ObjectIdentity", "TimeTicks", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MDS-EVENT-MIB", mdsEventName=mdsEventName, mdsEventMIBCompliance=mdsEventMIBCompliance, mdsEventVariables=mdsEventVariables, mdsEventVariablesCeeGroup=mdsEventVariablesCeeGroup, PYSNMP_MODULE_ID=mdsEventMIB, mdsEventMIBCompliances=mdsEventMIBCompliances, mdsEventNotificationsGroup=mdsEventNotificationsGroup, traps0=traps0, traps=traps, mdsEventMIBConformance=mdsEventMIBConformance, mdsEventMIB=mdsEventMIB, mdsEventInfoInCee=mdsEventInfoInCee, mdsEventMIBNotifications=mdsEventMIBNotifications, mdsEventMIBGroups=mdsEventMIBGroups, mdsEventMIBObjects=mdsEventMIBObjects, mdsEvent=mdsEvent)
