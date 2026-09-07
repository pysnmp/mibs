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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setLastUpdated('2008-06-11 00:00')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setDescription('This MIB module defines managed objects that facilitate\n        the management of policies upon host(s) admission to \n        a network. \n\n        The information available through this MIB includes:\n\n        o Statistics information such as number of total and\n          active sessions. \n\n        o Session information such as IP and MAC address of\n          host, client type, and session state.\n\n        o QoS and Security policy applied to host traffic upon \n          host admission to a network. \n        \n        The following terms are used throughout this MIB:\n\n        QoS (Quality of Service) is the method which attempts \n        to ensure that the network requirements of different \n        applications can be met by giving preferential forwarding\n        treatment to some traffic.\n\n        ACL (Access Control List) which contains filters used\n        to identify traffic flows with certain characteristics.\n\n        Downloadable ACL is a set of filters, configured on the \n        RADIUS server which are downloaded during authorization \n        phase of admission features like dot1x, authProxy, etc.\n\n        SGT (Security Group Tag) is a unique 16 bits value assigned\n        to every security group and used by network devices to\n        enforce network policies. \n        \n        URL: Universal Resource Locator.\n\n        URL-Redirect ACL is used for URL redirection feature. Any \n        ingress HTTP from the host that matches the ACL content \n        is subjected to redirection to the URL address specified by \n        the URL-Redirect string.\n\n        URL redirect string is the URL to which HTTP traffic to \n        the host would be redirected.')
class CapSessionId(TextualConvention, OctetString):
    description = 'An octet string describes an unique session identification.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class CapQosPolicy(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes a QoS policy.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapAclName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of an ACL.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapURLString(TextualConvention, OctetString):
    reference = 'Uniform Resource Locators. RFC 1738.'
    description = "This textual convention defines the URL string.\n        The Universal Resource Locator (URL). The URL strings\n        are compact string representation for a resource\n        available via internet. This is the address location\n        of the page to load. The string should represent a\n        fully qualifying string with the format\n       'protocol:/server/page'. In general the string should\n        point to any value that can be saved/loaded.\n        Any limitation for the URL must be defined as part of\n        the description of any object which uses this syntax.\n        The description of any object which uses this syntax \n        must specifically describe the meaning of zero length \n        value."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapPolicyState(TextualConvention, Integer32):
    description = "This textual convention indicates the current state\n        of a policy applied to host traffic.\n\n        'notApplicable' indicates that the policy is not applicable.\n\n        'success' indicates that the policy is applied successfully.\n\n        'failure' indicates that the policy is failed to apply.\n\n        'inProgress' indicates that the policy application is\n         in progress.\n\n        'ipWait' indicates that the policy is waiting for IP\n         address assignment. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 1), ("success", 2), ("failure", 3), ("inProgress", 4), ("ipWait", 5))

ciscoAdmissionPolicyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 0))
ciscoAdmissionPolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1))
ciscoAdmissionPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2))
capSessions = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1))
capTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTotalSessions.setStatus('current')
if mibBuilder.loadTexts: capTotalSessions.setDescription('This object indicates the total numbers of sessions\n         created in the device since the last system reset.')
capActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capActiveSessions.setStatus('current')
if mibBuilder.loadTexts: capActiveSessions.setDescription('This object indicates the currently active sessions\n         in the device.')
capSidSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionInfoTable.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoTable.setDescription('This table lists admission policy sessions based on unique\n         session identifier.\n\n         An entry is created by the agent when an admission policy \n         session has successfully registered to the system. \n \n         An entry is deleted by the agent upon de-registration of the \n         admission policy session with system.')
capSidSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"))
if mibBuilder.loadTexts: capSidSessionInfoEntry.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoEntry.setDescription('Each row contains the management information of a particular\n         active session based on unique session identifier.')
capSidSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 1), CapSessionId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionIndex.setDescription('This object uniquely identifies a session.')
capSidSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionIfIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionIfIndex.setDescription('This object indicates the ifIndex value of the interface\n         on which the session is established.')
capSidSessionMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionMacAddress.setStatus('current')
if mibBuilder.loadTexts: capSidSessionMacAddress.setDescription('This object indicates the MAC address of the host.')
capSidSessionAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddressType.setStatus('current')
if mibBuilder.loadTexts: capSidSessionAddressType.setDescription('This object indicates the type of Internet address \n         assigned for the host.')
capSidSessionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddress.setStatus('current')
if mibBuilder.loadTexts: capSidSessionAddress.setDescription('This object indicates the Internet address assigned for\n         the host. The type of this address is determined by \n         the value of capSidSessionAddressType object.')
capSidSessionFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("dot1x", 0), ("mab", 1), ("eou", 2), ("authProxy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionFeatureType.setStatus('current')
if mibBuilder.loadTexts: capSidSessionFeatureType.setDescription("This object indicates the admission features associated \n         with the session.\n\n        'dot1x' indicates that the admission feature is \n        802.1x feature.\n\n        'mab' indicates that the admission feature is \n        Mac Authentication Bypass feature.\n\n        'eou' indicates that the admission feature is \n        Extensible Authentication Protocol over UDP feature.\n\n        'authProxy' indicates that the admission feature is \n        Authentication Proxy feature.")
capSidSessionPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionPolicyTable.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyTable.setDescription('This table lists the policies that will be enforced \n        per session per admission feature. The session in this\n        table should have a corresponding entry in \n        capSidSessionInfoTable.')
capSidSessionPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"), (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyIndex"))
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setDescription('Each row contains the management information of a \n        particular admission feature of a session.')
capSidSessionPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dot1x", 1), ("mab", 2), ("eou", 3), ("authProxy", 4)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setDescription("This object indicates the admission feature which\n        a host is subjected to in a session.\n \n        'dot1x' indicates that the admission feature is \n        802.1x feature.\n\n        'mab' indicates that the admission feature is \n        Mac Authentication Bypass feature.\n\n        'eou' indicates that the admission feature is \n        Extensible Authentication Protocol over UDP feature.\n\n        'authProxy' indicates that the admission feature is \n        Authentication Proxy feature.")
capSidIngressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 2), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicy.setStatus('current')
if mibBuilder.loadTexts: capSidIngressQosPolicy.setDescription('This object indicates the name of an existing QoS \n        policy which will be applied to incoming traffic\n        in this session. An empty string indicates that no such\n        policy is applied.')
capSidIngressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 3), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setStatus('current')
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setDescription('This object indicates the current state of the \n        QoS policy which will be applied to incoming traffic\n        in this session.')
capSidEgressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 4), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicy.setStatus('current')
if mibBuilder.loadTexts: capSidEgressQosPolicy.setDescription('This object indicates the name of an existing QoS \n        policy which will be applied to outgoing traffic\n        in this session. An empty string indicates that no\n        such policy is applied.')
capSidEgressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 5), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setStatus('current')
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setDescription('This object indicates the current state of the QoS \n        policy which will be applied to outgoing traffic \n        in this session.')
capSidDownloadableAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 6), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclName.setStatus('current')
if mibBuilder.loadTexts: capSidDownloadableAclName.setDescription('This object indicates the name of a Downloadable\n        ACL which will be applied to the host traffic. \n        An empty string indicates that no such ACL is \n        applied.')
capSidDownloadableAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 7), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclState.setStatus('current')
if mibBuilder.loadTexts: capSidDownloadableAclState.setDescription('This object indicates the state of this session \n        downloadable ACL policy.')
capSidUrlRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 8), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setStatus('current')
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setDescription('This object indicates the ACL name that redirected traffic\n        from the host will be subjected to. An empty string indicates\n        that no such ACL is applied.')
capSidUrlRedirectAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 9), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setStatus('current')
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setDescription('This object indicates the state of this session \n        URL-Redirect ACL policy.')
capSidRedirectUrlString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 10), CapURLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlString.setStatus('current')
if mibBuilder.loadTexts: capSidRedirectUrlString.setDescription('This object indicates the URL that traffic from\n        the host will be redirected to. An empty string indicates\n        that no such URL is applied.')
capSidRedirectUrlStringState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 11), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setStatus('current')
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setDescription('This object indicates the state of this session \n        URL-Redirect string policy.')
capSidSecurityGroupTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSecurityGroupTag.setStatus('current')
if mibBuilder.loadTexts: capSidSecurityGroupTag.setDescription('This object indicates the SGT value assigned to the\n        host that initiated this session. Value of -1 indicates\n        that there is no SGT value assigned.')
ciscoAdmissionPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1))
ciscoAdmissionPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2))
ciscoAdmissionPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSessionStatisticsGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAdmissionPolicyMIBCompliance = ciscoAdmissionPolicyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIBCompliance.setDescription('The compliance statement for the CISCO-ADMISSION-POLICY-MIB')
capSessionStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capTotalSessions"), ("CISCO-ADMISSION-POLICY-MIB", "capActiveSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSessionStatisticsGroup = capSessionStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: capSessionStatisticsGroup.setDescription('A collection of object which provides session statistics \n         information in the device.')
capSidSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 2)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddressType"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionIfIndex"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionMacAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionFeatureType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionInfoGroup = capSidSessionInfoGroup.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoGroup.setDescription('A collection of objects which provides managed information \n         of a session based on unique session identifier.')
capSidSessionPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 3)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlString"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlStringState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSecurityGroupTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionPolicyGroup = capSidSessionPolicyGroup.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyGroup.setDescription('A collection of objects which provides policy information\n         in a session based on unique session identifier.')
mibBuilder.exportSymbols("CISCO-ADMISSION-POLICY-MIB", CapAclName=CapAclName, CapPolicyState=CapPolicyState, CapQosPolicy=CapQosPolicy, CapSessionId=CapSessionId, CapURLString=CapURLString, PYSNMP_MODULE_ID=ciscoAdmissionPolicyMIB, capActiveSessions=capActiveSessions, capSessionStatisticsGroup=capSessionStatisticsGroup, capSessions=capSessions, capSidDownloadableAclName=capSidDownloadableAclName, capSidDownloadableAclState=capSidDownloadableAclState, capSidEgressQosPolicy=capSidEgressQosPolicy, capSidEgressQosPolicyState=capSidEgressQosPolicyState, capSidIngressQosPolicy=capSidIngressQosPolicy, capSidIngressQosPolicyState=capSidIngressQosPolicyState, capSidRedirectUrlString=capSidRedirectUrlString, capSidRedirectUrlStringState=capSidRedirectUrlStringState, capSidSecurityGroupTag=capSidSecurityGroupTag, capSidSessionAddress=capSidSessionAddress, capSidSessionAddressType=capSidSessionAddressType, capSidSessionFeatureType=capSidSessionFeatureType, capSidSessionIfIndex=capSidSessionIfIndex, capSidSessionIndex=capSidSessionIndex, capSidSessionInfoEntry=capSidSessionInfoEntry, capSidSessionInfoGroup=capSidSessionInfoGroup, capSidSessionInfoTable=capSidSessionInfoTable, capSidSessionMacAddress=capSidSessionMacAddress, capSidSessionPolicyEntry=capSidSessionPolicyEntry, capSidSessionPolicyGroup=capSidSessionPolicyGroup, capSidSessionPolicyIndex=capSidSessionPolicyIndex, capSidSessionPolicyTable=capSidSessionPolicyTable, capSidUrlRedirectAclName=capSidUrlRedirectAclName, capSidUrlRedirectAclState=capSidUrlRedirectAclState, capTotalSessions=capTotalSessions, ciscoAdmissionPolicyMIB=ciscoAdmissionPolicyMIB, ciscoAdmissionPolicyMIBCompliance=ciscoAdmissionPolicyMIBCompliance, ciscoAdmissionPolicyMIBCompliances=ciscoAdmissionPolicyMIBCompliances, ciscoAdmissionPolicyMIBConformance=ciscoAdmissionPolicyMIBConformance, ciscoAdmissionPolicyMIBGroups=ciscoAdmissionPolicyMIBGroups, ciscoAdmissionPolicyMIBNotifs=ciscoAdmissionPolicyMIBNotifs, ciscoAdmissionPolicyMIBObjects=ciscoAdmissionPolicyMIBObjects)
