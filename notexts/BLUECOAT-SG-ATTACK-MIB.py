#
# PySNMP MIB module BLUECOAT-SG-ATTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ATTACK-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:02:30 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter64, MibIdentifier, Unsigned32, Gauge32, ModuleIdentity, IpAddress, Integer32, Bits, Counter32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter64", "MibIdentifier", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "Counter32", "NotificationType", "ObjectIdentity")
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
mibBuilder.exportSymbols("BLUECOAT-SG-ATTACK-MIB", deviceAttackEntry=deviceAttackEntry, deviceAttackMIBNotifications=deviceAttackMIBNotifications, AttackStatus=AttackStatus, deviceAttackTable=deviceAttackTable, deviceAttackTime=deviceAttackTime, deviceAttackTrap=deviceAttackTrap, deviceAttackMIB=deviceAttackMIB, PYSNMP_MODULE_ID=deviceAttackMIB, deviceAttackMIBObjects=deviceAttackMIBObjects, deviceAttackStatus=deviceAttackStatus, deviceAttackIndex=deviceAttackIndex, deviceAttackMIBNotificationsPrefix=deviceAttackMIBNotificationsPrefix, deviceAttackName=deviceAttackName, deviceAttackValues=deviceAttackValues)
