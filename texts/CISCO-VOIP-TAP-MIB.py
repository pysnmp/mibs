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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoIpTapMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setLastUpdated('2009-10-01 00:00')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setContactInfo('      Cisco Systems\n                     Customer Service\n\n                     Postal:170 W. Tasman Drive\n                     San Jose, CA  95134\n                     USA\n\n                     Tel:+1 800 553-NETS\n                     E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setDescription("This module manages Cisco's intercept feature for Voice\n         over IP (VoIP). This MIB is used along with CISCO-TAP2-MIB \n         to intercept VoIP Control and Data traffic.")
ciscoVoIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 0))
ciscoVoIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1))
ciscoVoIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2))
cvoiptapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1))
class CvoipWarrantId(TextualConvention, OctetString):
    description = 'The warrant identifier used by the Mediation Device.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class CvoipSubscriberId(TextualConvention, OctetString):
    description = 'The subscriber identifier for identifying the endpoint.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

cvoiptapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("usernameOrNumber", 1), ("uri", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setDescription("This object identifies what types of intercept streams can be\n        configured on this type of device. This may be dependent on\n        hardware capabilities, software capabilities. The following\n        fields may be supported:\n             tapEnable:   set if table entries with\n                          cTap2StreamInterceptEnable set to 'false'\n                          are used to pre-screen packets for intercept\n                          otherwise these entries are ignored.\n             usernameOrNumber: SNMP ifIndex value may be used to \n                          select interception of calls to or from \n                          a user or phone number may be used to \n                          select traffic to be intercepted.\n             uri:         Session Initiation Protocol (SIP) Uniform \n                          Resource Identifier (URI) may be used to \n                          select traffic to be intercepted.")
cvoiptapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvoiptapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamTable.setDescription("The Intercept Stream VoIP Table lists the streams to be \n         intercepted. To create a VoIP intercept, an entry \n         cvoiptapStreamEntry is created which contains the \n         filter details. An entry cTap2StreamEntry of CISCO-TAP2-MIB \n         is created, which is the common stream information for all \n         kinds of intercepts and type of the specific stream is set \n         to IP in this entry. The same data stream may be required by \n         multiple taps, and one might assume that often the \n         intercepted stream is a small subset of the traffic that \n         could be intercepted.  This essentially provides options \n         for call selection. For example, if all traffic to or from \n         a given user is to be intercepted, one would configure an \n         entry which lists the user with approprite tap type. The \n         first index indicates which Mediation Device the intercepted \n         traffic will be diverted to. The second index permits \n         multiple classifiers to be used together, such as having an \n         IP address as source or destination. The value of the second \n         index is that of the stream's counter entry in the \n         cTap2StreamTable. Entries are added to this table via \n         citapStreamStatus in accordance with the RowStatus \n         convention.")
cvoiptapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cvoiptapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamEntry.setDescription('A stream entry indicates a single data stream to be\n          intercepted to a Mediation Device. Many selected data\n          streams may go to the same application interface, and many\n          application interfaces are supported.')
cvoiptapStreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 1), CvoipWarrantId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamId.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamId.setDescription('This object uniquely identifies this warrant. \n          It has to be unique among all the rows.')
cvoiptapStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pen", 1), ("trace", 2), ("penAndTrace", 3), ("intercept", 4))).clone('intercept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamType.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamType.setDescription('pen :         Pen Register - provides trace of all outgoing \n                       calls.  Only Call Data is sent.\n         trace :       Trace - provides trace of all incoming calls.  \n                       Only Call Data is sent.\n         penAndTrace : Provides trace of both incoming and outgoing \n                       calls.  Only Call Data is sent.\n         intercept :   Provides both Call Data and Call Content to \n                       Commission on Accreditation for Law \n                       Enforcement Agencies (CALEA). Intercept \n                       is applicable to both originating and \n                       terminating calls.')
cvoiptapStreamMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 3), CvoipSubscriberId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatch.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamMatch.setDescription('This field describes the candidate which needs to be tapped.')
cvoiptapStreamMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usernameOrNumber", 1), ("uri", 2))).clone('usernameOrNumber')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setDescription("This field specifies the type of information in \n          cvoiptapStreamMatch. A subscriber or intercept candidate can\n          be defined either as username, phone number or Session \n          Initiation Protocol (SIP) Uniform Resource Identifier (URI). \n          'username' is defined as per RFC-3261. Same value is being \n          used for either username or phone number.")
cvoiptapStreamCCMediationDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setDescription('This object points to a row in Mediation Table which contains\n          the IP address and port number for sending the Call Content \n          intercept information.')
cvoiptapStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setDescription("The status of this conceptual row. This object manages\n          creation, modification, and deletion of rows in this table.\n          When any rows must be changed, cvoiptapStreamRowStatus must \n          be first set to 'notInService'. Row will be created when\n          the service provider has to provision a tap for a VoIP \n          endpoint. Row will be deleted when the warrant has expired.\n          Row will be changed when the warrant type has been changed.\n          cTap2StreamTable defined in CISCO-TAP2-MIB goes in \n          conjunction with this row, using the same index.")
ciscoVoIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1))
ciscoVoIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2))
ciscoVoIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "ciscoVoIpTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapMIBCompliance = ciscoVoIpTapMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVoIpTapMIBCompliance.setDescription('The compliance statement for entities which implement the \n         Cisco Intercept MIB for VoIP.')
ciscoVoIpTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCapabilities"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamId"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatch"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatchType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCCMediationDevice"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapStreamGroup = ciscoVoIpTapStreamGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVoIpTapStreamGroup.setDescription('These objects are necessary for a description of VoIP \n         Signaling and Data packets to select for interception.')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-MIB", CvoipSubscriberId=CvoipSubscriberId, CvoipWarrantId=CvoipWarrantId, PYSNMP_MODULE_ID=ciscoVoIpTapMIB, ciscoVoIpTapMIB=ciscoVoIpTapMIB, ciscoVoIpTapMIBCompliance=ciscoVoIpTapMIBCompliance, ciscoVoIpTapMIBCompliances=ciscoVoIpTapMIBCompliances, ciscoVoIpTapMIBConform=ciscoVoIpTapMIBConform, ciscoVoIpTapMIBGroups=ciscoVoIpTapMIBGroups, ciscoVoIpTapMIBNotifs=ciscoVoIpTapMIBNotifs, ciscoVoIpTapMIBObjects=ciscoVoIpTapMIBObjects, ciscoVoIpTapStreamGroup=ciscoVoIpTapStreamGroup, cvoiptapStreamCCMediationDevice=cvoiptapStreamCCMediationDevice, cvoiptapStreamCapabilities=cvoiptapStreamCapabilities, cvoiptapStreamEncodePacket=cvoiptapStreamEncodePacket, cvoiptapStreamEntry=cvoiptapStreamEntry, cvoiptapStreamId=cvoiptapStreamId, cvoiptapStreamMatch=cvoiptapStreamMatch, cvoiptapStreamMatchType=cvoiptapStreamMatchType, cvoiptapStreamRowStatus=cvoiptapStreamRowStatus, cvoiptapStreamTable=cvoiptapStreamTable, cvoiptapStreamType=cvoiptapStreamType)
