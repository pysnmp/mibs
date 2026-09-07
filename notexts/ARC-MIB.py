#
# PySNMP MIB module ARC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ARC-MIB
# Source digest sha256:837fbd86a028c3fe74e7f407eeaa892dc8a7e2e78e947f911b6092e6956ee510
# Produced by pysmi-2.3.0
#
ResourceId, = mibBuilder.importSymbols("ALARM-MIB", "ResourceId")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention")
arcMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 117))
arcMibModule.setRevisions(('2004-09-09 00:00',))
if mibBuilder.loadTexts: arcMibModule.setLastUpdated('2004-09-09 00:00')
if mibBuilder.loadTexts: arcMibModule.setOrganization('IETF Distributed Management Working Group')
class IANAItuProbableCauseOrZero(TextualConvention, Integer32):
    reference = 'IANA-ITU-ALARM-TC MIB module as maintained at the IANA web site. The initial module was also published in RFC 3877.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

arcTimeIntervals = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 1))
arcObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 2))
arcTITimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcTITimeInterval.setStatus('current')
arcCDTimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcCDTimeInterval.setStatus('current')
arcTable = MibTable((1, 3, 6, 1, 2, 1, 117, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arcTable.setStatus('current')
arcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 117, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ARC-MIB", "arcIndex"), (0, "ARC-MIB", "arcAlarmType"), (0, "ARC-MIB", "arcNotificationId"))
if mibBuilder.loadTexts: arcEntry.setStatus('current')
arcIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 1), ResourceId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arcIndex.setStatus('current')
arcAlarmType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 2), IANAItuProbableCauseOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arcAlarmType.setStatus('current')
arcNotificationId = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 3), ObjectIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: arcNotificationId.setStatus('current')
arcState = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nalm", 1), ("nalmQI", 2), ("nalmTI", 3), ("nalmQICD", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcState.setStatus('current')
arcNalmTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcNalmTimeRemaining.setStatus('current')
arcRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcRowStatus.setStatus('current')
arcStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcStorageType.setStatus('current')
arcConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3))
arcCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 1))
arcCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 117, 3, 1, 1)).setObjects(("ARC-MIB", "arcSettingGroup"), ("ARC-MIB", "arcTIGroup"), ("ARC-MIB", "arcQICDGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcCompliance = arcCompliance.setStatus('current')
arcGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 2))
arcSettingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 1)).setObjects(("ARC-MIB", "arcState"), ("ARC-MIB", "arcRowStatus"), ("ARC-MIB", "arcStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcSettingGroup = arcSettingGroup.setStatus('current')
arcTIGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 2)).setObjects(("ARC-MIB", "arcTITimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcTIGroup = arcTIGroup.setStatus('current')
arcQICDGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 3)).setObjects(("ARC-MIB", "arcCDTimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcQICDGroup = arcQICDGroup.setStatus('current')
mibBuilder.exportSymbols("ARC-MIB", IANAItuProbableCauseOrZero=IANAItuProbableCauseOrZero, PYSNMP_MODULE_ID=arcMibModule, arcAlarmType=arcAlarmType, arcCDTimeInterval=arcCDTimeInterval, arcCompliance=arcCompliance, arcCompliances=arcCompliances, arcConformance=arcConformance, arcEntry=arcEntry, arcGroups=arcGroups, arcIndex=arcIndex, arcMibModule=arcMibModule, arcNalmTimeRemaining=arcNalmTimeRemaining, arcNotificationId=arcNotificationId, arcObjects=arcObjects, arcQICDGroup=arcQICDGroup, arcRowStatus=arcRowStatus, arcSettingGroup=arcSettingGroup, arcState=arcState, arcStorageType=arcStorageType, arcTIGroup=arcTIGroup, arcTITimeInterval=arcTITimeInterval, arcTable=arcTable, arcTimeIntervals=arcTimeIntervals)
