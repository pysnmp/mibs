#
# PySNMP MIB module ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/ENTITY-MIB
# Produced by pysmi-1.1.12 at Mon Jul 22 06:05:13 2024
# On host fv-az1756-666 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, TimeTicks, Bits, MibIdentifier, Unsigned32, Counter32, NotificationType, Gauge32, mib_2, IpAddress, Counter64, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Bits", "MibIdentifier", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "mib-2", "IpAddress", "Counter64", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TAddress, TextualConvention, DateAndTime, AutonomousType, DisplayString, TruthValue, TimeStamp, TDomain, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TextualConvention", "DateAndTime", "AutonomousType", "DisplayString", "TruthValue", "TimeStamp", "TDomain", "RowPointer")
entityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 47))
entityMIB.setRevisions(('2005-08-10 00:00', '1999-12-07 00:00', '1996-10-31 00:00',))
if mibBuilder.loadTexts: entityMIB.setLastUpdated('200508100000Z')
if mibBuilder.loadTexts: entityMIB.setOrganization('IETF ENTMIB Working Group')
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

class PhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12))

class SnmpEngineIdOrNone(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

entPhysicalTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 1, 1), )
if mibBuilder.loadTexts: entPhysicalTable.setStatus('current')
entPhysicalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhysicalEntry.setStatus('current')
entPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 1), PhysicalIndex())
if mibBuilder.loadTexts: entPhysicalIndex.setStatus('current')
entPhysicalDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalDescr.setStatus('current')
entPhysicalVendorType = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalVendorType.setStatus('current')
entPhysicalContainedIn = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 4), PhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhysicalContainedIn.setStatus('current')
entPhysicalClass = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 1, 1, 1, 5), PhysicalClass()).setMaxAccess("readonly")
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
entLogicalTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 2, 1), )
if mibBuilder.loadTexts: entLogicalTable.setStatus('current')
entLogicalEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"))
if mibBuilder.loadTexts: entLogicalEntry.setStatus('current')
entLogicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
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
entLPMappingTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 1), )
if mibBuilder.loadTexts: entLPMappingTable.setStatus('current')
entLPMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLogicalIndex"), (0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: entLPMappingEntry.setStatus('current')
entLPPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 1, 1, 1), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entLPPhysicalIndex.setStatus('current')
entAliasMappingTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 2), )
if mibBuilder.loadTexts: entAliasMappingTable.setStatus('current')
entAliasMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTITY-MIB", "entAliasLogicalIndexOrZero"))
if mibBuilder.loadTexts: entAliasMappingEntry.setStatus('current')
entAliasLogicalIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: entAliasLogicalIndexOrZero.setStatus('current')
entAliasMappingIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 47, 1, 3, 2, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entAliasMappingIdentifier.setStatus('current')
entPhysicalContainsTable = MibTable((1, 3, 6, 1, 2, 1, 47, 1, 3, 3), )
if mibBuilder.loadTexts: entPhysicalContainsTable.setStatus('current')
entPhysicalContainsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 47, 1, 3, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENTITY-MIB", "entPhysicalChildIndex"))
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
    entity3Compliance = entity3Compliance.setStatus('current')
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
mibBuilder.exportSymbols("ENTITY-MIB", entityGroups=entityGroups, entityMIB=entityMIB, entPhysicalName=entPhysicalName, entPhysicalTable=entPhysicalTable, entityCompliance=entityCompliance, entityCompliances=entityCompliances, entityPhysical3Group=entityPhysical3Group, entPhysicalContainedIn=entPhysicalContainedIn, entPhysicalAlias=entPhysicalAlias, entityLogicalGroup=entityLogicalGroup, entLPMappingEntry=entLPMappingEntry, entityPhysical=entityPhysical, entLogicalType=entLogicalType, PhysicalIndexOrZero=PhysicalIndexOrZero, entLogicalEntry=entLogicalEntry, entPhysicalModelName=entPhysicalModelName, entPhysicalHardwareRev=entPhysicalHardwareRev, entAliasMappingTable=entAliasMappingTable, SnmpEngineIdOrNone=SnmpEngineIdOrNone, entity3Compliance=entity3Compliance, entityLogical=entityLogical, entityLogical2Group=entityLogical2Group, entPhysicalEntry=entPhysicalEntry, entLogicalTAddress=entLogicalTAddress, entityMapping=entityMapping, entPhysicalClass=entPhysicalClass, entPhysicalSerialNum=entPhysicalSerialNum, entityConformance=entityConformance, entityPhysicalGroup=entityPhysicalGroup, PhysicalIndex=PhysicalIndex, entLogicalIndex=entLogicalIndex, entLogicalTDomain=entLogicalTDomain, entPhysicalParentRelPos=entPhysicalParentRelPos, entityMIBObjects=entityMIBObjects, entPhysicalIndex=entPhysicalIndex, entPhysicalMfgDate=entPhysicalMfgDate, entLogicalTable=entLogicalTable, PYSNMP_MODULE_ID=entityMIB, entLogicalContextEngineID=entLogicalContextEngineID, entityPhysical2Group=entityPhysical2Group, entAliasLogicalIndexOrZero=entAliasLogicalIndexOrZero, entPhysicalDescr=entPhysicalDescr, entLogicalCommunity=entLogicalCommunity, entPhysicalContainsTable=entPhysicalContainsTable, entPhysicalVendorType=entPhysicalVendorType, entityNotificationsGroup=entityNotificationsGroup, entityGeneral=entityGeneral, entAliasMappingIdentifier=entAliasMappingIdentifier, entityMIBTrapPrefix=entityMIBTrapPrefix, entLastChangeTime=entLastChangeTime, entity2Compliance=entity2Compliance, entPhysicalIsFRU=entPhysicalIsFRU, entPhysicalSoftwareRev=entPhysicalSoftwareRev, entLogicalDescr=entLogicalDescr, entPhysicalFirmwareRev=entPhysicalFirmwareRev, entPhysicalChildIndex=entPhysicalChildIndex, entPhysicalMfgName=entPhysicalMfgName, entConfigChange=entConfigChange, entityMappingGroup=entityMappingGroup, entityGeneralGroup=entityGeneralGroup, entityMIBTraps=entityMIBTraps, PhysicalClass=PhysicalClass, entAliasMappingEntry=entAliasMappingEntry, entPhysicalUris=entPhysicalUris, entLogicalContextName=entLogicalContextName, entPhysicalContainsEntry=entPhysicalContainsEntry, entLPPhysicalIndex=entLPPhysicalIndex, entPhysicalAssetID=entPhysicalAssetID, entLPMappingTable=entLPMappingTable)
