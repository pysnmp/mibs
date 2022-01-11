#
# PySNMP MIB module PRVT-PORT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-PORT-SECURITY-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 20:54:44 2022
# On host fv-az42-180 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
configL2IfaceEnable, switch = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "configL2IfaceEnable", "switch")
dot1qVlanStatus, dot1qTpFdbStatus = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanStatus", "dot1qTpFdbStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, TimeTicks, Bits, ObjectIdentity, Integer32, Unsigned32, iso, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "TimeTicks", "Bits", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtPortSecurityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 109))
prvtPortSecurityMib.setRevisions(('2008-06-18 00:00', '2005-02-16 00:00', '2004-05-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtPortSecurityMib.setRevisionsDescriptions(('Added prvtDuplicatedMACAddressAlarm.', 'Fixed spelling errors and changed the contact info.', 'Initial version.',))
if mibBuilder.loadTexts: prvtPortSecurityMib.setLastUpdated('200806180000Z')
if mibBuilder.loadTexts: prvtPortSecurityMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtPortSecurityMib.setContactInfo(' BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtPortSecurityMib.setDescription('The Port Security MIB module for managing the port security attributes.')
prvtPortSECNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0))
prvtPortSECObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1))
prvtPortSECConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2))
prvtPortSECViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 1)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"), ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
if mibBuilder.loadTexts: prvtPortSECViolation.setStatus('current')
if mibBuilder.loadTexts: prvtPortSECViolation.setDescription('This notification is sent by the agent when a security violation occurres on a port.')
prvtDuplicatedMACAddressAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 2)).setObjects(("Q-BRIDGE-MIB", "dot1qVlanStatus"), ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"), ("PRVT-SWITCH-MIB", "configL2IfaceEnable"))
if mibBuilder.loadTexts: prvtDuplicatedMACAddressAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtDuplicatedMACAddressAlarm.setDescription('This notification is sent by the agent when a duplicated MAC is recived.')
prvtPortSECMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2))
prvtPortSECNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 2, 2, 1)).setObjects(("PRVT-PORT-SECURITY-MIB", "prvtPortSECViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtPortSECNotificationGroup = prvtPortSECNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: prvtPortSECNotificationGroup.setDescription('Notification Group for the private Port Security Violation Trap')
mibBuilder.exportSymbols("PRVT-PORT-SECURITY-MIB", PYSNMP_MODULE_ID=prvtPortSecurityMib, prvtPortSECViolation=prvtPortSECViolation, prvtPortSECConformance=prvtPortSECConformance, prvtPortSecurityMib=prvtPortSecurityMib, prvtPortSECObjects=prvtPortSECObjects, prvtDuplicatedMACAddressAlarm=prvtDuplicatedMACAddressAlarm, prvtPortSECMIBGroups=prvtPortSECMIBGroups, prvtPortSECNotifications=prvtPortSECNotifications, prvtPortSECNotificationGroup=prvtPortSECNotificationGroup)
