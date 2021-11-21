#
# PySNMP MIB module BLUECOAT-SG-ATTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ATTACK-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:39:40 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, NotificationType, Bits, MibIdentifier, TimeTicks, Gauge32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "NotificationType", "Bits", "MibIdentifier", "TimeTicks", "Gauge32", "Unsigned32", "iso")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
deviceAttackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 3))
deviceAttackMIB.setRevisions(('2007-11-05 03:00', '2002-11-06 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceAttackMIB.setRevisionsDescriptions(('Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceAttackMIB.setLastUpdated('200711050300Z')
if mibBuilder.loadTexts: deviceAttackMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceAttackMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceAttackMIB.setDescription('The Blue Coat Attack MIB is used to monitor\n                         possible protocol attacks by hackers.')
deviceAttackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1))
deviceAttackMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2))
deviceAttackMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0))
class AttackStatus(TextualConvention, Integer32):
    description = 'Indicates the status of the attack.\n                noAttack(1)       - no attack.\n                underAttack(2)    - attack in progress.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noAttack", 1), ("underAttack", 2))

deviceAttackValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1))
deviceAttackTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: deviceAttackTable.setStatus('current')
if mibBuilder.loadTexts: deviceAttackTable.setDescription('This table lists the various attacks that are\n                         detected.')
deviceAttackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-ATTACK-MIB", "deviceAttackIndex"))
if mibBuilder.loadTexts: deviceAttackEntry.setStatus('current')
if mibBuilder.loadTexts: deviceAttackEntry.setDescription('A deviceAttack entry describes the\n                         present state of an attack.')
deviceAttackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceAttackIndex.setStatus('current')
if mibBuilder.loadTexts: deviceAttackIndex.setDescription('An arbitrary value which uniquely identifies an attack.')
deviceAttackName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackName.setStatus('current')
if mibBuilder.loadTexts: deviceAttackName.setDescription('The textual name of the attack i.e. SYN Flood.')
deviceAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 3), AttackStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackStatus.setStatus('current')
if mibBuilder.loadTexts: deviceAttackStatus.setDescription('noAttack(1) not under attack, underAttack(2) attack in progress.\n                         The default start-up value is noAttack(1).')
deviceAttackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 4), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackTime.setStatus('current')
if mibBuilder.loadTexts: deviceAttackTime.setDescription("The value of 'sysUpTime.0' at the time of the attack.")
deviceAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0, 1)).setObjects(("BLUECOAT-SG-ATTACK-MIB", "deviceAttackName"), ("BLUECOAT-SG-ATTACK-MIB", "deviceAttackStatus"))
if mibBuilder.loadTexts: deviceAttackTrap.setStatus('current')
if mibBuilder.loadTexts: deviceAttackTrap.setDescription("At the start of an attack a notification is\n                         generated with 'deviceAttackStatus = underAttack(2)'.\n                         At the end of an attack a notification is generated with\n                         'deviceAttackStatus = noAttack(1)'.")
mibBuilder.exportSymbols("BLUECOAT-SG-ATTACK-MIB", deviceAttackEntry=deviceAttackEntry, deviceAttackMIB=deviceAttackMIB, deviceAttackMIBObjects=deviceAttackMIBObjects, deviceAttackTime=deviceAttackTime, PYSNMP_MODULE_ID=deviceAttackMIB, deviceAttackMIBNotifications=deviceAttackMIBNotifications, deviceAttackTrap=deviceAttackTrap, deviceAttackName=deviceAttackName, deviceAttackMIBNotificationsPrefix=deviceAttackMIBNotificationsPrefix, deviceAttackTable=deviceAttackTable, deviceAttackStatus=deviceAttackStatus, AttackStatus=AttackStatus, deviceAttackValues=deviceAttackValues, deviceAttackIndex=deviceAttackIndex)
