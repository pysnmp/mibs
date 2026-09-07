#
# PySNMP MIB module CISCO-MOBILITY-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MOBILITY-TAP-MIB
# Source digest sha256:4804b3d4c038a99df5d42c157516d2d4b610a96269b471adb45db3bd0e251f1d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, StorageType, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention", "TruthValue")
ciscoMobilityTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 672))
ciscoMobilityTapMIB.setRevisions(('2010-06-16 00:00', '2010-04-15 00:00', '2008-08-05 00:00',))
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setLastUpdated('2010-06-16 00:00')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setOrganization('Cisco Systems, Inc.')
ciscoMobilityTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 0))
ciscoMobilityTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1))
ciscoMobilityTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2))
cmtapStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1))
class CmtapLawfulInterceptID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

class CmtapSubscriberIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("msid", 2), ("imsi", 3), ("nai", 4), ("esn", 5), ("servedMdn", 6))

class CmtapSubscriberID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

cmtapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("calledSubscriberID", 2), ("nonvolatileStorage", 3), ("msid", 4), ("imsi", 5), ("nai", 6), ("esn", 7), ("servedMdn", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmtapStreamCapabilities.setStatus('current')
cmtapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmtapStreamTable.setStatus('current')
cmtapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cmtapStreamEntry.setStatus('current')
cmtapStreamCalledSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 1), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setStatus('current')
cmtapStreamCalledSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 2), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setStatus('current')
cmtapStreamSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 3), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setStatus('current')
cmtapStreamSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 4), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setStatus('current')
cmtapStreamStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStorageType.setStatus('current')
cmtapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStatus.setStatus('current')
cmtapStreamLIIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 7), CmtapLawfulInterceptID().clone('not set')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setStatus('current')
cmtapStreamLocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setStatus('current')
cmtapStreamInterceptType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ccOnly", 1), ("iriOnly", 2), ("both", 3))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamInterceptType.setStatus('current')
ciscoMobilityTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1))
ciscoMobilityTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2))
ciscoMobilityTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBCompliance = ciscoMobilityTapMIBCompliance.setStatus('deprecated')
ciscoMobilityTapMIBComplianceRev01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBComplianceRev01 = ciscoMobilityTapMIBComplianceRev01.setStatus('current')
ciscoMobilityTapCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapCapabilityGroup = ciscoMobilityTapCapabilityGroup.setStatus('current')
ciscoMobilityTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStorageType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroup = ciscoMobilityTapStreamGroup.setStatus('current')
ciscoMobilityTapStreamGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 3)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLIIdentifier"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLocationInfo"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamInterceptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroupSup1 = ciscoMobilityTapStreamGroupSup1.setStatus('current')
mibBuilder.exportSymbols("CISCO-MOBILITY-TAP-MIB", CmtapLawfulInterceptID=CmtapLawfulInterceptID, CmtapSubscriberID=CmtapSubscriberID, CmtapSubscriberIDType=CmtapSubscriberIDType, PYSNMP_MODULE_ID=ciscoMobilityTapMIB, ciscoMobilityTapCapabilityGroup=ciscoMobilityTapCapabilityGroup, ciscoMobilityTapMIB=ciscoMobilityTapMIB, ciscoMobilityTapMIBCompliance=ciscoMobilityTapMIBCompliance, ciscoMobilityTapMIBComplianceRev01=ciscoMobilityTapMIBComplianceRev01, ciscoMobilityTapMIBCompliances=ciscoMobilityTapMIBCompliances, ciscoMobilityTapMIBConform=ciscoMobilityTapMIBConform, ciscoMobilityTapMIBGroups=ciscoMobilityTapMIBGroups, ciscoMobilityTapMIBNotifs=ciscoMobilityTapMIBNotifs, ciscoMobilityTapMIBObjects=ciscoMobilityTapMIBObjects, ciscoMobilityTapStreamGroup=ciscoMobilityTapStreamGroup, ciscoMobilityTapStreamGroupSup1=ciscoMobilityTapStreamGroupSup1, cmtapStreamCalledSubscriberID=cmtapStreamCalledSubscriberID, cmtapStreamCalledSubscriberIDType=cmtapStreamCalledSubscriberIDType, cmtapStreamCapabilities=cmtapStreamCapabilities, cmtapStreamEntry=cmtapStreamEntry, cmtapStreamGroup=cmtapStreamGroup, cmtapStreamInterceptType=cmtapStreamInterceptType, cmtapStreamLIIdentifier=cmtapStreamLIIdentifier, cmtapStreamLocationInfo=cmtapStreamLocationInfo, cmtapStreamStatus=cmtapStreamStatus, cmtapStreamStorageType=cmtapStreamStorageType, cmtapStreamSubscriberID=cmtapStreamSubscriberID, cmtapStreamSubscriberIDType=cmtapStreamSubscriberIDType, cmtapStreamTable=cmtapStreamTable)
