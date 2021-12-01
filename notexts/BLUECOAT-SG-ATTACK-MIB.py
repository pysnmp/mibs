#
# PySNMP MIB module BLUECOAT-SG-ATTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ATTACK-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:37:47 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, TimeTicks, ModuleIdentity, Integer32, NotificationType, IpAddress, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "TimeTicks", "ModuleIdentity", "Integer32", "NotificationType", "IpAddress", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
deviceAttackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 3))
deviceAttackMIB.setRevisions(('2007-11-05 03:00', '2002-11-06 03:00',))
if mibBuilder.loadTexts: deviceAttackMIB.setLastUpdated('200711050300Z')
if mibBuilder.loadTexts: deviceAttackMIB.setOrganization('Blue Coat Systems, Inc.')
deviceAttackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1))
deviceAttackMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2))
deviceAttackMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0))
class AttackStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noAttack", 1), ("underAttack", 2))

deviceAttackValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1))
deviceAttackTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1), )
if mibBuilder.loadTexts: deviceAttackTable.setStatus('current')
deviceAttackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-ATTACK-MIB", "deviceAttackIndex"))
if mibBuilder.loadTexts: deviceAttackEntry.setStatus('current')
deviceAttackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceAttackIndex.setStatus('current')
deviceAttackName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackName.setStatus('current')
deviceAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 3), AttackStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackStatus.setStatus('current')
deviceAttackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 3, 1, 1, 1, 1, 4), TimeStamp()).setUnits('Hundredths of seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAttackTime.setStatus('current')
deviceAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 3, 2, 0, 1)).setObjects(("BLUECOAT-SG-ATTACK-MIB", "deviceAttackName"), ("BLUECOAT-SG-ATTACK-MIB", "deviceAttackStatus"))
if mibBuilder.loadTexts: deviceAttackTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-ATTACK-MIB", deviceAttackValues=deviceAttackValues, PYSNMP_MODULE_ID=deviceAttackMIB, deviceAttackTime=deviceAttackTime, deviceAttackTable=deviceAttackTable, deviceAttackMIBObjects=deviceAttackMIBObjects, deviceAttackMIBNotifications=deviceAttackMIBNotifications, deviceAttackEntry=deviceAttackEntry, deviceAttackMIBNotificationsPrefix=deviceAttackMIBNotificationsPrefix, deviceAttackName=deviceAttackName, deviceAttackStatus=deviceAttackStatus, deviceAttackTrap=deviceAttackTrap, deviceAttackMIB=deviceAttackMIB, AttackStatus=AttackStatus, deviceAttackIndex=deviceAttackIndex)
