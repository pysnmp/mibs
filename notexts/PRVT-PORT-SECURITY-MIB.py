#
# PySNMP MIB module PRVT-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-PORT-SECURITY-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 15:22:56 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
switch, configL2IfaceEnable = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch", "configL2IfaceEnable")
dot1qVlanStatus, dot1qTpFdbStatus = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStatus", "dot1qTpFdbStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter64, Gauge32, NotificationType, Unsigned32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter64", "Gauge32", "NotificationType", "Unsigned32", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PRVT-PORT-SECURITY-MIB", prvtPortSecurityMib=prvtPortSecurityMib, prvtPortSECConformance=prvtPortSECConformance, prvtDuplicatedMACAddressAlarm=prvtDuplicatedMACAddressAlarm, prvtPortSECMIBGroups=prvtPortSECMIBGroups, prvtPortSECNotificationGroup=prvtPortSECNotificationGroup, prvtPortSECObjects=prvtPortSECObjects, PYSNMP_MODULE_ID=prvtPortSecurityMib, prvtPortSECNotifications=prvtPortSECNotifications, prvtPortSECViolation=prvtPortSECViolation)
