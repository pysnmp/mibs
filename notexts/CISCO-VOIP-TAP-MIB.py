#
# PySNMP MIB module CISCO-VOIP-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOIP-TAP-MIB
# Source digest sha256:41cc4acafbe3db917dd83bc05f44c9f16314a98afa413a29082d71a75f19131f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVoIpTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 716))
ciscoVoIpTapMIB.setRevisions(('2009-10-01 00:00',))
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setLastUpdated('2009-10-01 00:00')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 0))
ciscoVoIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1))
ciscoVoIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2))
cvoiptapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1))
class CvoipWarrantId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class CvoipSubscriberId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

cvoiptapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("usernameOrNumber", 1), ("uri", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setStatus('current')
cvoiptapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvoiptapStreamTable.setStatus('current')
cvoiptapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cvoiptapStreamEntry.setStatus('current')
cvoiptapStreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 1), CvoipWarrantId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamId.setStatus('current')
cvoiptapStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pen", 1), ("trace", 2), ("penAndTrace", 3), ("intercept", 4))).clone('intercept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamType.setStatus('current')
cvoiptapStreamMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 3), CvoipSubscriberId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatch.setStatus('current')
cvoiptapStreamMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usernameOrNumber", 1), ("uri", 2))).clone('usernameOrNumber')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setStatus('current')
cvoiptapStreamCCMediationDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setStatus('current')
cvoiptapStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setStatus('current')
ciscoVoIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1))
ciscoVoIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2))
ciscoVoIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "ciscoVoIpTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapMIBCompliance = ciscoVoIpTapMIBCompliance.setStatus('current')
ciscoVoIpTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCapabilities"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamId"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatch"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatchType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCCMediationDevice"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapStreamGroup = ciscoVoIpTapStreamGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-MIB", CvoipSubscriberId=CvoipSubscriberId, CvoipWarrantId=CvoipWarrantId, PYSNMP_MODULE_ID=ciscoVoIpTapMIB, ciscoVoIpTapMIB=ciscoVoIpTapMIB, ciscoVoIpTapMIBCompliance=ciscoVoIpTapMIBCompliance, ciscoVoIpTapMIBCompliances=ciscoVoIpTapMIBCompliances, ciscoVoIpTapMIBConform=ciscoVoIpTapMIBConform, ciscoVoIpTapMIBGroups=ciscoVoIpTapMIBGroups, ciscoVoIpTapMIBNotifs=ciscoVoIpTapMIBNotifs, ciscoVoIpTapMIBObjects=ciscoVoIpTapMIBObjects, ciscoVoIpTapStreamGroup=ciscoVoIpTapStreamGroup, cvoiptapStreamCCMediationDevice=cvoiptapStreamCCMediationDevice, cvoiptapStreamCapabilities=cvoiptapStreamCapabilities, cvoiptapStreamEncodePacket=cvoiptapStreamEncodePacket, cvoiptapStreamEntry=cvoiptapStreamEntry, cvoiptapStreamId=cvoiptapStreamId, cvoiptapStreamMatch=cvoiptapStreamMatch, cvoiptapStreamMatchType=cvoiptapStreamMatchType, cvoiptapStreamRowStatus=cvoiptapStreamRowStatus, cvoiptapStreamTable=cvoiptapStreamTable, cvoiptapStreamType=cvoiptapStreamType)
