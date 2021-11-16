#
# PySNMP MIB module ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/ENTITY-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:52:18 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, IpAddress, ModuleIdentity, ObjectIdentity, Integer32, NotificationType, iso, MibIdentifier, Counter32, Unsigned32, Gauge32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Integer32", "NotificationType", "iso", "MibIdentifier", "Counter32", "Unsigned32", "Gauge32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2")
TimeStamp, DisplayString, TAddress, AutonomousType, DateAndTime, TextualConvention, RowPointer, TruthValue, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TAddress", "AutonomousType", "DateAndTime", "TextualConvention", "RowPointer", "TruthValue", "TDomain")
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
mibBuilder.exportSymbols("ENTITY-MIB", entPhysicalAssetID=entPhysicalAssetID, entLPMappingTable=entLPMappingTable, entity2Compliance=entity2Compliance, PhysicalIndex=PhysicalIndex, entLogicalContextEngineID=entLogicalContextEngineID, entLogicalTDomain=entLogicalTDomain, entPhysicalSoftwareRev=entPhysicalSoftwareRev, entPhysicalModelName=entPhysicalModelName, entLogicalTable=entLogicalTable, entityCompliance=entityCompliance, entityPhysicalGroup=entityPhysicalGroup, entPhysicalIndex=entPhysicalIndex, entPhysicalVendorType=entPhysicalVendorType, entityGeneralGroup=entityGeneralGroup, entityMappingGroup=entityMappingGroup, entPhysicalTable=entPhysicalTable, entLogicalContextName=entLogicalContextName, entPhysicalChildIndex=entPhysicalChildIndex, entityLogicalGroup=entityLogicalGroup, entityLogical=entityLogical, PYSNMP_MODULE_ID=entityMIB, entPhysicalSerialNum=entPhysicalSerialNum, entityPhysical2Group=entityPhysical2Group, PhysicalIndexOrZero=PhysicalIndexOrZero, entPhysicalIsFRU=entPhysicalIsFRU, entAliasLogicalIndexOrZero=entAliasLogicalIndexOrZero, entityMapping=entityMapping, entLogicalCommunity=entLogicalCommunity, entPhysicalDescr=entPhysicalDescr, PhysicalClass=PhysicalClass, entLPMappingEntry=entLPMappingEntry, entPhysicalContainedIn=entPhysicalContainedIn, entPhysicalMfgDate=entPhysicalMfgDate, entPhysicalClass=entPhysicalClass, SnmpEngineIdOrNone=SnmpEngineIdOrNone, entLogicalEntry=entLogicalEntry, entAliasMappingTable=entAliasMappingTable, entPhysicalContainsTable=entPhysicalContainsTable, entPhysicalName=entPhysicalName, entityMIBTraps=entityMIBTraps, entLastChangeTime=entLastChangeTime, entityPhysical3Group=entityPhysical3Group, entPhysicalMfgName=entPhysicalMfgName, entPhysicalAlias=entPhysicalAlias, entPhysicalFirmwareRev=entPhysicalFirmwareRev, entPhysicalContainsEntry=entPhysicalContainsEntry, entityMIBTrapPrefix=entityMIBTrapPrefix, entityCompliances=entityCompliances, entityLogical2Group=entityLogical2Group, entPhysicalUris=entPhysicalUris, entAliasMappingIdentifier=entAliasMappingIdentifier, entPhysicalEntry=entPhysicalEntry, entAliasMappingEntry=entAliasMappingEntry, entityMIBObjects=entityMIBObjects, entLogicalIndex=entLogicalIndex, entLogicalType=entLogicalType, entLogicalTAddress=entLogicalTAddress, entity3Compliance=entity3Compliance, entityMIB=entityMIB, entConfigChange=entConfigChange, entityGeneral=entityGeneral, entLPPhysicalIndex=entLPPhysicalIndex, entPhysicalHardwareRev=entPhysicalHardwareRev, entPhysicalParentRelPos=entPhysicalParentRelPos, entityPhysical=entityPhysical, entityGroups=entityGroups, entityNotificationsGroup=entityNotificationsGroup, entityConformance=entityConformance, entLogicalDescr=entLogicalDescr)
