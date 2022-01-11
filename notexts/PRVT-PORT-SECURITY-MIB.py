#
# PySNMP MIB module PRVT-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-PORT-SECURITY-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:46:18 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
configL2IfaceEnable, switch = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "configL2IfaceEnable", "switch")
dot1qVlanStatus, dot1qTpFdbStatus = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStatus", "dot1qTpFdbStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, Counter32, Counter64, Gauge32, ModuleIdentity, Unsigned32, IpAddress, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtPortSecurityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 109))
prvtPortSecurityMib.setRevisions(('2008-06-18 00:00', '2005-02-16 00:00', '2004-05-10 00:00',))
if mibBuilder.loadTexts: prvtPortSecurityMib.setLastUpdated('200806180000Z')
if mibBuilder.loadTexts: prvtPortSecurityMib.setOrganization('BATM Advanced Communication')
prvtPortSECNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0))
prvtPortSECObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1))
prvtPortSECConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2))
prvtPortSECViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 1)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"), ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
if mibBuilder.loadTexts: prvtPortSECViolation.setStatus('current')
prvtDuplicatedMACAddressAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 2)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"), ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
if mibBuilder.loadTexts: prvtDuplicatedMACAddressAlarm.setStatus('current')
prvtPortSECMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2))
prvtPortSECNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2, 1)).setObjects(("PRVT-PORT-SECURITY-MIB", "prvtPortSECViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtPortSECNotificationGroup = prvtPortSECNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-PORT-SECURITY-MIB", PYSNMP_MODULE_ID=prvtPortSecurityMib, prvtPortSECMIBGroups=prvtPortSECMIBGroups, prvtPortSecurityMib=prvtPortSecurityMib, prvtPortSECNotificationGroup=prvtPortSECNotificationGroup, prvtPortSECViolation=prvtPortSECViolation, prvtPortSECObjects=prvtPortSECObjects, prvtPortSECConformance=prvtPortSECConformance, prvtDuplicatedMACAddressAlarm=prvtDuplicatedMACAddressAlarm, prvtPortSECNotifications=prvtPortSECNotifications)
