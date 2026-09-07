#
# PySNMP MIB module CISCO-ADMISSION-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ADMISSION-POLICY-MIB
# Source digest sha256:c2d82573ad7b8886d19c898b417fc72a9eaf2444191db8caf7492e8650d0f898
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
ciscoAdmissionPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 653))
ciscoAdmissionPolicyMIB.setRevisions(('2008-06-11 00:00',))
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setLastUpdated('2008-06-11 00:00')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setOrganization('Cisco Systems, Inc.')
class CapSessionId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class CapQosPolicy(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapAclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapURLString(TextualConvention, OctetString):
    reference = 'Uniform Resource Locators. RFC 1738.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapPolicyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 1), ("success", 2), ("failure", 3), ("inProgress", 4), ("ipWait", 5))

ciscoAdmissionPolicyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 0))
ciscoAdmissionPolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1))
ciscoAdmissionPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2))
capSessions = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1))
capTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTotalSessions.setStatus('current')
capActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capActiveSessions.setStatus('current')
capSidSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionInfoTable.setStatus('current')
capSidSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"))
if mibBuilder.loadTexts: capSidSessionInfoEntry.setStatus('current')
capSidSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 1), CapSessionId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionIndex.setStatus('current')
capSidSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionIfIndex.setStatus('current')
capSidSessionMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionMacAddress.setStatus('current')
capSidSessionAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddressType.setStatus('current')
capSidSessionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddress.setStatus('current')
capSidSessionFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("dot1x", 0), ("mab", 1), ("eou", 2), ("authProxy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionFeatureType.setStatus('current')
capSidSessionPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionPolicyTable.setStatus('current')
capSidSessionPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"), (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyIndex"))
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setStatus('current')
capSidSessionPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dot1x", 1), ("mab", 2), ("eou", 3), ("authProxy", 4)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setStatus('current')
capSidIngressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 2), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicy.setStatus('current')
capSidIngressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 3), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setStatus('current')
capSidEgressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 4), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicy.setStatus('current')
capSidEgressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 5), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setStatus('current')
capSidDownloadableAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 6), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclName.setStatus('current')
capSidDownloadableAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 7), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclState.setStatus('current')
capSidUrlRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 8), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setStatus('current')
capSidUrlRedirectAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 9), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setStatus('current')
capSidRedirectUrlString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 10), CapURLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlString.setStatus('current')
capSidRedirectUrlStringState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 11), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setStatus('current')
capSidSecurityGroupTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSecurityGroupTag.setStatus('current')
ciscoAdmissionPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1))
ciscoAdmissionPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2))
ciscoAdmissionPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSessionStatisticsGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAdmissionPolicyMIBCompliance = ciscoAdmissionPolicyMIBCompliance.setStatus('current')
capSessionStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capTotalSessions"), ("CISCO-ADMISSION-POLICY-MIB", "capActiveSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSessionStatisticsGroup = capSessionStatisticsGroup.setStatus('current')
capSidSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 2)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddressType"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionIfIndex"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionMacAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionFeatureType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionInfoGroup = capSidSessionInfoGroup.setStatus('current')
capSidSessionPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 3)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlString"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlStringState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSecurityGroupTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionPolicyGroup = capSidSessionPolicyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ADMISSION-POLICY-MIB", CapAclName=CapAclName, CapPolicyState=CapPolicyState, CapQosPolicy=CapQosPolicy, CapSessionId=CapSessionId, CapURLString=CapURLString, PYSNMP_MODULE_ID=ciscoAdmissionPolicyMIB, capActiveSessions=capActiveSessions, capSessionStatisticsGroup=capSessionStatisticsGroup, capSessions=capSessions, capSidDownloadableAclName=capSidDownloadableAclName, capSidDownloadableAclState=capSidDownloadableAclState, capSidEgressQosPolicy=capSidEgressQosPolicy, capSidEgressQosPolicyState=capSidEgressQosPolicyState, capSidIngressQosPolicy=capSidIngressQosPolicy, capSidIngressQosPolicyState=capSidIngressQosPolicyState, capSidRedirectUrlString=capSidRedirectUrlString, capSidRedirectUrlStringState=capSidRedirectUrlStringState, capSidSecurityGroupTag=capSidSecurityGroupTag, capSidSessionAddress=capSidSessionAddress, capSidSessionAddressType=capSidSessionAddressType, capSidSessionFeatureType=capSidSessionFeatureType, capSidSessionIfIndex=capSidSessionIfIndex, capSidSessionIndex=capSidSessionIndex, capSidSessionInfoEntry=capSidSessionInfoEntry, capSidSessionInfoGroup=capSidSessionInfoGroup, capSidSessionInfoTable=capSidSessionInfoTable, capSidSessionMacAddress=capSidSessionMacAddress, capSidSessionPolicyEntry=capSidSessionPolicyEntry, capSidSessionPolicyGroup=capSidSessionPolicyGroup, capSidSessionPolicyIndex=capSidSessionPolicyIndex, capSidSessionPolicyTable=capSidSessionPolicyTable, capSidUrlRedirectAclName=capSidUrlRedirectAclName, capSidUrlRedirectAclState=capSidUrlRedirectAclState, capTotalSessions=capTotalSessions, ciscoAdmissionPolicyMIB=ciscoAdmissionPolicyMIB, ciscoAdmissionPolicyMIBCompliance=ciscoAdmissionPolicyMIBCompliance, ciscoAdmissionPolicyMIBCompliances=ciscoAdmissionPolicyMIBCompliances, ciscoAdmissionPolicyMIBConformance=ciscoAdmissionPolicyMIBConformance, ciscoAdmissionPolicyMIBGroups=ciscoAdmissionPolicyMIBGroups, ciscoAdmissionPolicyMIBNotifs=ciscoAdmissionPolicyMIBNotifs, ciscoAdmissionPolicyMIBObjects=ciscoAdmissionPolicyMIBObjects)
