#
# PySNMP MIB module BLUECOAT-SG-ATTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ATTACK-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:19:28 2024
# On host fv-az1984-402 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, iso, IpAddress, TimeTicks, Unsigned32, Counter64, Bits, ObjectIdentity, Integer32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "iso", "IpAddress", "TimeTicks", "Unsigned32", "Counter64", "Bits", "ObjectIdentity", "Integer32", "Gauge32", "MibIdentifier")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
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
mibBuilder.exportSymbols("BLUECOAT-SG-ATTACK-MIB", deviceAttackMIBNotificationsPrefix=deviceAttackMIBNotificationsPrefix, deviceAttackTrap=deviceAttackTrap, deviceAttackMIBObjects=deviceAttackMIBObjects, deviceAttackName=deviceAttackName, PYSNMP_MODULE_ID=deviceAttackMIB, deviceAttackIndex=deviceAttackIndex, deviceAttackTime=deviceAttackTime, deviceAttackMIBNotifications=deviceAttackMIBNotifications, deviceAttackStatus=deviceAttackStatus, deviceAttackMIB=deviceAttackMIB, deviceAttackEntry=deviceAttackEntry, deviceAttackValues=deviceAttackValues, deviceAttackTable=deviceAttackTable, AttackStatus=AttackStatus)
