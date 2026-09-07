#
# PySNMP MIB module ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ENTITY-MIB
# Source digest sha256:44ea8017ef63abb4ea84631017c27a45575b9b7cb8dd54dab56a211fbba4081c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
IANAPhysicalClass, = mibBuilder.importSymbols("IANA-ENTITY-MIB", "IANAPhysicalClass")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso", "mib-2")
AutonomousType, DateAndTime, DisplayString, RowPointer, TAddress, TDomain, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DateAndTime", "DisplayString", "RowPointer", "TAddress", "TDomain", "TextualConvention", "TimeStamp", "TruthValue")
UUIDorZero, = mibBuilder.importSymbols("UUID-TC-MIB", "UUIDorZero")
entityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 47))
entityMIB.setRevisions(('2013-04-05 00:00', '2005-08-10 00:00', '1999-12-07 00:00', '1996-10-31 00:00',))
if mibBuilder.loadTexts: entityMIB.setLastUpdated('2013-04-05 00:00')
if mibBuilder.loadTexts: entityMIB.setOrganization('IETF Energy Management Working Group')
entityMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 1))
entityPhysical = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 1, 1))
entityLogical = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 1, 2))
entityMapping = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 1, 3))
entityGeneral = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 1, 4))
class PhysicalIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class PhysicalIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class SnmpEngineIdOrNone(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class PhysicalClass(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12))

entPhysicalTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entPhysicalTable.setStatus('current')
entPhysicalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhysicalEntry.setStatus('current')
entPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 1), PhysicalIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entPhysicalIndex.setStatus('current')
entPhysicalDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalDescr.setStatus('current')
entPhysicalVendorType = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalVendorType.setStatus('current')
entPhysicalContainedIn = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 4), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalContainedIn.setStatus('current')
entPhysicalClass = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 5), IANAPhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalClass.setStatus('current')
entPhysicalParentRelPos = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalParentRelPos.setStatus('current')
entPhysicalName = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalName.setStatus('current')
entPhysicalHardwareRev = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalHardwareRev.setStatus('current')
entPhysicalFirmwareRev = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalFirmwareRev.setStatus('current')
entPhysicalSoftwareRev = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalSoftwareRev.setStatus('current')
entPhysicalSerialNum = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entPhysicalSerialNum.setStatus('current')
entPhysicalMfgName = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalMfgName.setStatus('current')
entPhysicalModelName = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalModelName.setStatus('current')
entPhysicalAlias = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 14), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entPhysicalAlias.setStatus('current')
entPhysicalAssetID = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 15), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entPhysicalAssetID.setStatus('current')
entPhysicalIsFRU = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalIsFRU.setStatus('current')
entPhysicalMfgDate = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 17), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalMfgDate.setStatus('current')
entPhysicalUris = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 18), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: entPhysicalUris.setStatus('current')
entPhysicalUUID = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 19), UUIDorZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalUUID.setStatus('current')
entLogicalTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entLogicalTable.setStatus('current')
entLogicalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"))
if mibBuilder.loadTexts: entLogicalEntry.setStatus('current')
entLogicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entLogicalIndex.setStatus('current')
entLogicalDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalDescr.setStatus('current')
entLogicalType = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalType.setStatus('current')
entLogicalCommunity = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalCommunity.setStatus('deprecated')
entLogicalTAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 5), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalTAddress.setStatus('current')
entLogicalTDomain = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 6), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalTDomain.setStatus('current')
entLogicalContextEngineID = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 7), SnmpEngineIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalContextEngineID.setStatus('current')
entLogicalContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLogicalContextName.setStatus('current')
entLPMappingTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entLPMappingTable.setStatus('current')
entLPMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"), (0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: entLPMappingEntry.setStatus('current')
entLPPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 1, 1, 1), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLPPhysicalIndex.setStatus('current')
entAliasMappingTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entAliasMappingTable.setStatus('current')
entAliasMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTITY-MIB", "entAliasLogicalIndexOrZero"))
if mibBuilder.loadTexts: entAliasMappingEntry.setStatus('current')
entAliasLogicalIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entAliasLogicalIndexOrZero.setStatus('current')
entAliasMappingIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entAliasMappingIdentifier.setStatus('current')
entPhysicalContainsTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: entPhysicalContainsTable.setStatus('current')
entPhysicalContainsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTITY-MIB", "entPhysicalChildIndex"))
if mibBuilder.loadTexts: entPhysicalContainsEntry.setStatus('current')
entPhysicalChildIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 3, 1, 1), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalChildIndex.setStatus('current')
entLastChangeTime = MibScalar((1, 3, 6, 1, 2, 1, 47, 1, 4, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLastChangeTime.setStatus('current')
entityMIBTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 2))
entityMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 2, 0))
entConfigChange = NotificationType((1, 3, 6, 1, 2, 1, 47, 2, 0, 1))
if mibBuilder.loadTexts: entConfigChange.setStatus('current')
entityConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 3))
entityCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 3, 1))
entityGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 47, 3, 2))
entityCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 47, 3, 1, 1)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("ENTITY-MIB", "entityLogicalGroup"), ("ENTITY-MIB", "entityMappingGroup"), ("ENTITY-MIB", "entityGeneralGroup"), ("ENTITY-MIB", "entityNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityCompliance = entityCompliance.setStatus('deprecated')
entity2Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 47, 3, 1, 2)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("ENTITY-MIB", "entityPhysical2Group"), ("ENTITY-MIB", "entityGeneralGroup"), ("ENTITY-MIB", "entityNotificationsGroup"), ("ENTITY-MIB", "entityLogical2Group"), ("ENTITY-MIB", "entityMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entity2Compliance = entity2Compliance.setStatus('deprecated')
entity3Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 47, 3, 1, 3)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("ENTITY-MIB", "entityPhysical2Group"), ("ENTITY-MIB", "entityPhysical3Group"), ("ENTITY-MIB", "entityGeneralGroup"), ("ENTITY-MIB", "entityNotificationsGroup"), ("ENTITY-MIB", "entityLogical2Group"), ("ENTITY-MIB", "entityMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entity3Compliance = entity3Compliance.setStatus('deprecated')
entity4Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 47, 3, 1, 4)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("ENTITY-MIB", "entityPhysical2Group"), ("ENTITY-MIB", "entityPhysical3Group"), ("ENTITY-MIB", "entityGeneralGroup"), ("ENTITY-MIB", "entityNotificationsGroup"), ("ENTITY-MIB", "entityPhysical4Group"), ("ENTITY-MIB", "entityLogical2Group"), ("ENTITY-MIB", "entityMappingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entity4Compliance = entity4Compliance.setStatus('current')
entity4CRCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 47, 3, 1, 5)).setObjects(("ENTITY-MIB", "entityPhysicalCRGroup"), ("ENTITY-MIB", "entityPhysical4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entity4CRCompliance = entity4CRCompliance.setStatus('current')
entityPhysicalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 1)).setObjects(("ENTITY-MIB", "entPhysicalDescr"), ("ENTITY-MIB", "entPhysicalVendorType"), ("ENTITY-MIB", "entPhysicalContainedIn"), ("ENTITY-MIB", "entPhysicalClass"), ("ENTITY-MIB", "entPhysicalParentRelPos"), ("ENTITY-MIB", "entPhysicalName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityPhysicalGroup = entityPhysicalGroup.setStatus('current')
entityLogicalGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 2)).setObjects(("ENTITY-MIB", "entLogicalDescr"), ("ENTITY-MIB", "entLogicalType"), ("ENTITY-MIB", "entLogicalCommunity"), ("ENTITY-MIB", "entLogicalTAddress"), ("ENTITY-MIB", "entLogicalTDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityLogicalGroup = entityLogicalGroup.setStatus('deprecated')
entityMappingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 3)).setObjects(("ENTITY-MIB", "entLPPhysicalIndex"), ("ENTITY-MIB", "entAliasMappingIdentifier"), ("ENTITY-MIB", "entPhysicalChildIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityMappingGroup = entityMappingGroup.setStatus('current')
entityGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 4)).setObjects(("ENTITY-MIB", "entLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityGeneralGroup = entityGeneralGroup.setStatus('current')
entityNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 5)).setObjects(("ENTITY-MIB", "entConfigChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityNotificationsGroup = entityNotificationsGroup.setStatus('current')
entityPhysical2Group = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 6)).setObjects(("ENTITY-MIB", "entPhysicalHardwareRev"), ("ENTITY-MIB", "entPhysicalFirmwareRev"), ("ENTITY-MIB", "entPhysicalSoftwareRev"), ("ENTITY-MIB", "entPhysicalSerialNum"), ("ENTITY-MIB", "entPhysicalMfgName"), ("ENTITY-MIB", "entPhysicalModelName"), ("ENTITY-MIB", "entPhysicalAlias"), ("ENTITY-MIB", "entPhysicalAssetID"), ("ENTITY-MIB", "entPhysicalIsFRU"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityPhysical2Group = entityPhysical2Group.setStatus('current')
entityLogical2Group = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 7)).setObjects(("ENTITY-MIB", "entLogicalDescr"), ("ENTITY-MIB", "entLogicalType"), ("ENTITY-MIB", "entLogicalTAddress"), ("ENTITY-MIB", "entLogicalTDomain"), ("ENTITY-MIB", "entLogicalContextEngineID"), ("ENTITY-MIB", "entLogicalContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityLogical2Group = entityLogical2Group.setStatus('current')
entityPhysical3Group = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 8)).setObjects(("ENTITY-MIB", "entPhysicalMfgDate"), ("ENTITY-MIB", "entPhysicalUris"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityPhysical3Group = entityPhysical3Group.setStatus('current')
entityPhysical4Group = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 9)).setObjects(("ENTITY-MIB", "entPhysicalUUID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityPhysical4Group = entityPhysical4Group.setStatus('current')
entityPhysicalCRGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 47, 3, 2, 10)).setObjects(("ENTITY-MIB", "entPhysicalClass"), ("ENTITY-MIB", "entPhysicalName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entityPhysicalCRGroup = entityPhysicalCRGroup.setStatus('current')
mibBuilder.exportSymbols("ENTITY-MIB", PYSNMP_MODULE_ID=entityMIB, PhysicalClass=PhysicalClass, PhysicalIndex=PhysicalIndex, PhysicalIndexOrZero=PhysicalIndexOrZero, SnmpEngineIdOrNone=SnmpEngineIdOrNone, entAliasLogicalIndexOrZero=entAliasLogicalIndexOrZero, entAliasMappingEntry=entAliasMappingEntry, entAliasMappingIdentifier=entAliasMappingIdentifier, entAliasMappingTable=entAliasMappingTable, entConfigChange=entConfigChange, entLPMappingEntry=entLPMappingEntry, entLPMappingTable=entLPMappingTable, entLPPhysicalIndex=entLPPhysicalIndex, entLastChangeTime=entLastChangeTime, entLogicalCommunity=entLogicalCommunity, entLogicalContextEngineID=entLogicalContextEngineID, entLogicalContextName=entLogicalContextName, entLogicalDescr=entLogicalDescr, entLogicalEntry=entLogicalEntry, entLogicalIndex=entLogicalIndex, entLogicalTAddress=entLogicalTAddress, entLogicalTDomain=entLogicalTDomain, entLogicalTable=entLogicalTable, entLogicalType=entLogicalType, entPhysicalAlias=entPhysicalAlias, entPhysicalAssetID=entPhysicalAssetID, entPhysicalChildIndex=entPhysicalChildIndex, entPhysicalClass=entPhysicalClass, entPhysicalContainedIn=entPhysicalContainedIn, entPhysicalContainsEntry=entPhysicalContainsEntry, entPhysicalContainsTable=entPhysicalContainsTable, entPhysicalDescr=entPhysicalDescr, entPhysicalEntry=entPhysicalEntry, entPhysicalFirmwareRev=entPhysicalFirmwareRev, entPhysicalHardwareRev=entPhysicalHardwareRev, entPhysicalIndex=entPhysicalIndex, entPhysicalIsFRU=entPhysicalIsFRU, entPhysicalMfgDate=entPhysicalMfgDate, entPhysicalMfgName=entPhysicalMfgName, entPhysicalModelName=entPhysicalModelName, entPhysicalName=entPhysicalName, entPhysicalParentRelPos=entPhysicalParentRelPos, entPhysicalSerialNum=entPhysicalSerialNum, entPhysicalSoftwareRev=entPhysicalSoftwareRev, entPhysicalTable=entPhysicalTable, entPhysicalUUID=entPhysicalUUID, entPhysicalUris=entPhysicalUris, entPhysicalVendorType=entPhysicalVendorType, entity2Compliance=entity2Compliance, entity3Compliance=entity3Compliance, entity4CRCompliance=entity4CRCompliance, entity4Compliance=entity4Compliance, entityCompliance=entityCompliance, entityCompliances=entityCompliances, entityConformance=entityConformance, entityGeneral=entityGeneral, entityGeneralGroup=entityGeneralGroup, entityGroups=entityGroups, entityLogical2Group=entityLogical2Group, entityLogical=entityLogical, entityLogicalGroup=entityLogicalGroup, entityMIB=entityMIB, entityMIBObjects=entityMIBObjects, entityMIBTrapPrefix=entityMIBTrapPrefix, entityMIBTraps=entityMIBTraps, entityMapping=entityMapping, entityMappingGroup=entityMappingGroup, entityNotificationsGroup=entityNotificationsGroup, entityPhysical2Group=entityPhysical2Group, entityPhysical3Group=entityPhysical3Group, entityPhysical4Group=entityPhysical4Group, entityPhysical=entityPhysical, entityPhysicalCRGroup=entityPhysicalCRGroup, entityPhysicalGroup=entityPhysicalGroup)
