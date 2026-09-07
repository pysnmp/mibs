#
# PySNMP MIB module CISCO-FLOW-METADATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FLOW-METADATA-MIB
# Source digest sha256:dddbd146c6ad6ac356660ff712b9966fb25c72fe0ffd51b4bd5e5978924aad43
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlowMetadataMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 789))
ciscoFlowMetadataMIB.setRevisions(('2012-12-17 00:00', '2011-03-20 00:00',))
if mibBuilder.loadTexts: ciscoFlowMetadataMIB.setLastUpdated('2012-12-20 00:00')
if mibBuilder.loadTexts: ciscoFlowMetadataMIB.setOrganization('Cisco Systems, Inc.')
class CfmMetadataFlowAttributeType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 94, 95, 96, 97, 98, 100, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139))
    namedValues = NamedValues(("other", 0), ("appDescription", 94), ("appTag", 95), ("appName", 96), ("appVersion", 97), ("appVendor", 98), ("vmFlowTimeout", 100), ("vmRTPClockFrequency", 101), ("pakRate", 103), ("l3Bitrate", 104), ("mediaBitrate", 105), ("mediaVideoPaksize", 106), ("globalSessionID", 107), ("multipartySessionID", 108), ("rtpMediaFlow", 109), ("mediaEncryptionStatus", 110), ("syntheticTraffic", 111), ("meteringPriority", 112), ("endpointModel", 113), ("endpointVendor", 114), ("endpointVersion", 115), ("ssrc", 116), ("endpointIPAddressType", 117), ("endpointIPAddressLength", 118), ("endpointIPAddressValue", 119), ("sipProxyServerType", 120), ("sipProxyServerLength", 121), ("sipProxyServerValue", 122), ("bandwidth", 123), ("deviceName", 124), ("deviceClass", 125), ("sipUserName", 126), ("sipEmail", 127), ("audioCodec", 128), ("bandwidthConsumed", 129), ("payloadType", 130), ("mimeType", 131), ("extrapolatedBandwidth", 132), ("cname", 134), ("videoCodec", 135), ("sdpSessionID", 136), ("domainName", 137), ("endpointSwVersion", 138), ("tosDscp", 139))

class CfmMetadataFlowAttrVal(TextualConvention, OctetString):
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

cFlowMetadataMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 789, 0))
cFlowMetadataMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 789, 1))
cFlowMetadataMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 789, 2))
cfmMetadataFlowTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataFlowTable.setStatus('current')
cfmMetadataFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"))
if mibBuilder.loadTexts: cfmMetadataFlowEntry.setStatus('current')
cfmMetadataFlowId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 1), Unsigned32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataFlowId.setStatus('current')
cfmMetadataFlowProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowProtocolType.setStatus('current')
cfmMetadataFlowDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowDestAddrType.setStatus('current')
cfmMetadataFlowDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowDestAddr.setStatus('current')
cfmMetadataFlowDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 5), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowDestPort.setStatus('current')
cfmMetadataFlowSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowSrcAddrType.setStatus('current')
cfmMetadataFlowSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowSrcAddr.setStatus('current')
cfmMetadataFlowSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 8), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowSrcPort.setStatus('current')
cfmMetadataFlowSSRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowSSRC.setStatus('current')
cfmMetadataFlowAttrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataFlowAttrTable.setStatus('deprecated')
cfmMetadataFlowAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"), (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrType"))
if mibBuilder.loadTexts: cfmMetadataFlowAttrEntry.setStatus('deprecated')
cfmMetadataFlowAttrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1, 1), CfmMetadataFlowAttributeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowAttrType.setStatus('deprecated')
cfmMetadataFlowAttrValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 2, 1, 2), CfmMetadataFlowAttrVal()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowAttrValue.setStatus('deprecated')
cfmMetadataFlowAllAttrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataFlowAllAttrTable.setStatus('current')
cfmMetadataFlowAllAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowId"), (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataIpFixIeId"), (0, "CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrInstanceId"))
if mibBuilder.loadTexts: cfmMetadataFlowAllAttrEntry.setStatus('current')
cfmMetadataIpFixIeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataIpFixIeId.setStatus('current')
cfmMetadataFlowAllAttrInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cfmMetadataFlowAllAttrInstanceId.setStatus('current')
cfmMetadataFlowAllAttrValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowAllAttrValue.setStatus('current')
cfmMetadataFlowAllAttrPen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 789, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMetadataFlowAllAttrPen.setStatus('current')
cfmMetadataMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1))
cfmMetadataMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2))
cfmMetadataMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1, 1)).setObjects(("CISCO-FLOW-METADATA-MIB", "cfmMetadateFlowInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMetadataMIBCompliance = cfmMetadataMIBCompliance.setStatus('deprecated')
cfmMetadataMIBComplianceV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 1, 2)).setObjects(("CISCO-FLOW-METADATA-MIB", "cfmMetadateFlowInfoGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMetadataMIBComplianceV2 = cfmMetadataMIBComplianceV2.setStatus('current')
cfmMetadateFlowInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2, 1)).setObjects(("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowProtocolType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddrType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddr"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestPort"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddrType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddr"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcPort"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSSRC"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAttrValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMetadateFlowInfoGroup = cfmMetadateFlowInfoGroup.setStatus('deprecated')
cfmMetadateFlowInfoGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 789, 2, 2, 2)).setObjects(("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowProtocolType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddrType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestAddr"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowDestPort"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddrType"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcAddr"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSrcPort"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowSSRC"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrValue"), ("CISCO-FLOW-METADATA-MIB", "cfmMetadataFlowAllAttrPen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmMetadateFlowInfoGroupV2 = cfmMetadateFlowInfoGroupV2.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLOW-METADATA-MIB", CfmMetadataFlowAttrVal=CfmMetadataFlowAttrVal, CfmMetadataFlowAttributeType=CfmMetadataFlowAttributeType, PYSNMP_MODULE_ID=ciscoFlowMetadataMIB, cFlowMetadataMIBConform=cFlowMetadataMIBConform, cFlowMetadataMIBNotifs=cFlowMetadataMIBNotifs, cFlowMetadataMIBObjects=cFlowMetadataMIBObjects, cfmMetadataFlowAllAttrEntry=cfmMetadataFlowAllAttrEntry, cfmMetadataFlowAllAttrInstanceId=cfmMetadataFlowAllAttrInstanceId, cfmMetadataFlowAllAttrPen=cfmMetadataFlowAllAttrPen, cfmMetadataFlowAllAttrTable=cfmMetadataFlowAllAttrTable, cfmMetadataFlowAllAttrValue=cfmMetadataFlowAllAttrValue, cfmMetadataFlowAttrEntry=cfmMetadataFlowAttrEntry, cfmMetadataFlowAttrTable=cfmMetadataFlowAttrTable, cfmMetadataFlowAttrType=cfmMetadataFlowAttrType, cfmMetadataFlowAttrValue=cfmMetadataFlowAttrValue, cfmMetadataFlowDestAddr=cfmMetadataFlowDestAddr, cfmMetadataFlowDestAddrType=cfmMetadataFlowDestAddrType, cfmMetadataFlowDestPort=cfmMetadataFlowDestPort, cfmMetadataFlowEntry=cfmMetadataFlowEntry, cfmMetadataFlowId=cfmMetadataFlowId, cfmMetadataFlowProtocolType=cfmMetadataFlowProtocolType, cfmMetadataFlowSSRC=cfmMetadataFlowSSRC, cfmMetadataFlowSrcAddr=cfmMetadataFlowSrcAddr, cfmMetadataFlowSrcAddrType=cfmMetadataFlowSrcAddrType, cfmMetadataFlowSrcPort=cfmMetadataFlowSrcPort, cfmMetadataFlowTable=cfmMetadataFlowTable, cfmMetadataIpFixIeId=cfmMetadataIpFixIeId, cfmMetadataMIBCompliance=cfmMetadataMIBCompliance, cfmMetadataMIBComplianceV2=cfmMetadataMIBComplianceV2, cfmMetadataMIBCompliances=cfmMetadataMIBCompliances, cfmMetadataMIBGroups=cfmMetadataMIBGroups, cfmMetadateFlowInfoGroup=cfmMetadateFlowInfoGroup, cfmMetadateFlowInfoGroupV2=cfmMetadateFlowInfoGroupV2, ciscoFlowMetadataMIB=ciscoFlowMetadataMIB)
