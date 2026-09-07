#
# PySNMP MIB module CISCO-POLICY-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-POLICY-GROUP-MIB
# Source digest sha256:1778dd9c9449ee02573aefa14a746a092d76a1e3ce64caac22977f1e09a92111
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoPolicyGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 507))
ciscoPolicyGroupMIB.setRevisions(('2006-01-13 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setLastUpdated('2006-01-13 16:00')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setContactInfo('        Cisco Systems\n                 Customer Service\n\n         Postal: 170 W Tasman Drive\n                 San Jose, CA 95134\n                 USA\n\n            Tel: +1 800 553-NETS\n\n         E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setDescription('The MIB module is for configuration of policy and\n         policy group. A policy group can be described as a set \n         of entities identified by IP addresses or other means.\n         Members of a policy group will be subjected to the same policy.\n         In this MIB, user can apply a policy to policy group(s)\n         as well as configure and retrieve the group membership.')
class CpgPolicyName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of a policy.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CpgPolicyNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n        CpgPolicyName convention. The latter defines a non-empty\n        policy name. This extension permits the additional value\n        of empty string.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CpgGroupName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of a policy group.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

ciscoPolicyGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 0))
ciscoPolicyGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1))
ciscoPolicyGroupMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2))
cpgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1))
cpgPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2))
cpgGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupTable.setStatus('current')
if mibBuilder.loadTexts: cpgGroupTable.setDescription('A table indicates the policy groups in the device.')
cpgGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgGroupName"))
if mibBuilder.loadTexts: cpgGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cpgGroupEntry.setDescription('A row instance contains the name of a policy group,\n         the source method which creates this group, the number\n         of IP addresses contained in the group and the status\n         of this instance. A row instance can be created or removed\n         by the system or by setting the appropriate value\n         of the RowStatus object.')
cpgGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 1), CpgGroupName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgGroupName.setDescription('Indicates the name of a policy group in the device.')
cpgGroupSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("accessList", 2), ("configured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupSourceType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupSourceType.setDescription('Indicates the source i.e. the method used to create this\n         group.\n\n         unknown(1) indicates that the source of this group cannot\n         be identified.\n\n         accessList(2) indicates that this group is added via\n         the ACL (Access Control List) feature.\n\n         configured(3) indicates that this group is added via \n         this policy group configuration.')
cpgGroupIpAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpAddrCount.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddrCount.setDescription('Indicates the number of IP address(es) contained in \n         this group. This is the number of entries for this group\n         in the cpgGroupIpTable. The initial value of this object\n         in a row created via cpgGroupRowStatus object is zero.')
cpgGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgGroupRowStatus.setDescription('This object is used to manage the creation and deletion\n        of rows in this table.')
cpgGroupIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupIpTable.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpTable.setDescription('A table provides management information for policy group\n        and its IP address(es) membership in the device.')
cpgGroupIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpGroupName"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrType"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddress"))
if mibBuilder.loadTexts: cpgGroupIpEntry.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpEntry.setDescription('A row instance contains the IP address mask, source type\n        and its status. A row instance can be created or removed\n        by the system or by setting the appropriate value of its\n        RowStatus object.\n\n        A row instance is indexed by a group name, type and value\n        of an IP address. The group name index must exist in the\n        cpgGroupTable. If a group name is deleted from cpgGroupTable,\n        entries in this table using this group as an index will also be\n        automatically removed.')
cpgGroupIpGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 1), CpgGroupName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupIpGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpGroupName.setDescription('Indicates the policy group name. This group should exist in\n         cpgGroupTable.')
cpgGroupIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupIpAddrType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddrType.setDescription('The type of Internet address of a group member.')
cpgGroupIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgGroupIpAddress.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddress.setDescription('The Internet address of a group member.\n         The type of this address is determined by\n         the value of the cpgGroupIpAddrType object.\n         The cpgGroupIpAddress may not be empty due to the SIZE\n         restriction.')
cpgGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 4), InetAddress().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpMask.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpMask.setDescription("Specifies the mask to be logical-ANDed with the IP address\n        denoted in cpgGroupIpAddress object to indicate IP address\n        group membership. The type of this mask is determined by\n        the value of the cpgGroupIpAddrType object.\n\n        Value of this object can not be modified when the corresponding\n        instance of cpgGroupIpRowStatus is 'active'.")
cpgGroupIpSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("configured", 2), ("dot1x", 3), ("nac", 4), ("webAuth", 5), ("macAuth", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpSourceType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpSourceType.setDescription('Indicates the source of this IP address.\n\n         other(1) indicates the source of this IP address is\n         not one of the following types.\n\n         configured(2) indicates this IP address is configured \n         via this policy group and IP address configuration.\n\n         dot1x(3) indicates this IP address is added by \n         802.1x feature.\n\n         nac(4) indicates this IP address is added by \n         NAC (network admission control) feature.\n\n         webAuth(5) indicates this IP address is added \n         by Web-Proxy Authentication feature.\n\n         macAuth(6) indicatest this IP address is added \n         by MAC Authentication Bypass feature.')
cpgGroupIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpRowStatus.setDescription("This object is used to manage the creation and deletion\n        of rows in this table. Once a row becomes active, values\n        within this row cannot be modified, except by setting this \n        object value to 'notInService' first, or deleting and\n        re-creating it.\n\n        A conceptual row can be removed by setting this object\n        value to 'destroy' if and only if the value of corresponding\n        instance of cpgGroupIpSourceType is 'configured'.")
cpgPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgPolicyTable.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyTable.setDescription('A table describes the policies in the device.')
cpgPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyName"))
if mibBuilder.loadTexts: cpgPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyEntry.setDescription('A row instance contains the name of a policy\n         in the device.')
cpgPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 1), CpgPolicyName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgPolicyName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyName.setDescription('Indicates a policy name in the device.')
cpgPolicyGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgPolicyGroupCount.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupCount.setDescription('Indicates the number of policy group(s) associated with \n         this policy. This is the number of entries for this policy \n         in the cpgPolicyGroupTable.')
cpgPolicyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgPolicyGroupTable.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupTable.setDescription('A table provides the mechanism to configure association\n        between a policy and a policy group. When a policy associates\n        with a policy group, this policy is applied to all the\n        members of the group. A policy can associate with\n        multiple groups and vice versa.')
cpgPolicyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupPolicyName"), (1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupGroupName"))
if mibBuilder.loadTexts: cpgPolicyGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupEntry.setDescription('A row instance contains the RowStatus object to configure\n        the association between a policy and a policy group. A row\n        instance can be created or removed by the system or by setting\n        the appropriate value of the RowStatus object.\n\n        A row instance is indexed by a policy name and a policy group\n        name.  The policy name index must exist in cpgPolicyTable. The\n        policy group name index must exist in cpgGroupTable. If a policy\n        group is removed from cpgGroupTable, entries in this table\n        using this group as an index will be automatically removed.')
cpgPolicyGroupPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 1), CpgPolicyName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgPolicyGroupPolicyName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupPolicyName.setDescription('This object indicates the policy name used to associate\n        to the group denoted by cpgPolicyGroupGroupName. This policy \n        must exist in cpgPolicyTable.')
cpgPolicyGroupGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 2), CpgGroupName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cpgPolicyGroupGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupGroupName.setDescription('This object indicates the group name used to associate\n        to the policy denoted by cpgPolicyGroupPolicyName. This\n        group must exist in cpgGroupTable.')
cpgPolicyGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgPolicyGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupRowStatus.setDescription('This object is used to manage the creation and deletion\n        of rows in this table.')
ciscoPolicyGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1))
ciscoPolicyGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2))
ciscoPolicyGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupIpInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyGroupInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupMIBCompliance = ciscoPolicyGroupMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicyGroupMIBCompliance.setDescription('The compliance statement for the CISCO-POLICY-GROUP-MIB')
ciscoCpgGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrCount"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupInfoGroup = ciscoCpgGroupInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgGroupInfoGroup.setDescription('A collection of objects which provides information on\n         policy groups in the device.')
ciscoCpgGroupIpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 2)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupIpMask"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupIpInfoGroup = ciscoCpgGroupIpInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgGroupIpInfoGroup.setDescription('A collection of objects which provides information on\n         policy group and IP addresses membership.')
ciscoCpgPolicyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 3)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyInfoGroup = ciscoCpgPolicyInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgPolicyInfoGroup.setDescription('A collection of objects which provides the policies data \n         in the device.')
ciscoCpgPolicyGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 4)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyGroupInfoGroup = ciscoCpgPolicyGroupInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgPolicyGroupInfoGroup.setDescription('A collection of object which provides information on\n        group and policy association.')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-MIB", CpgGroupName=CpgGroupName, CpgPolicyName=CpgPolicyName, CpgPolicyNameOrEmpty=CpgPolicyNameOrEmpty, PYSNMP_MODULE_ID=ciscoPolicyGroupMIB, ciscoCpgGroupInfoGroup=ciscoCpgGroupInfoGroup, ciscoCpgGroupIpInfoGroup=ciscoCpgGroupIpInfoGroup, ciscoCpgPolicyGroupInfoGroup=ciscoCpgPolicyGroupInfoGroup, ciscoCpgPolicyInfoGroup=ciscoCpgPolicyInfoGroup, ciscoPolicyGroupMIB=ciscoPolicyGroupMIB, ciscoPolicyGroupMIBCompliance=ciscoPolicyGroupMIBCompliance, ciscoPolicyGroupMIBCompliances=ciscoPolicyGroupMIBCompliances, ciscoPolicyGroupMIBConformance=ciscoPolicyGroupMIBConformance, ciscoPolicyGroupMIBGroups=ciscoPolicyGroupMIBGroups, ciscoPolicyGroupMIBNotifs=ciscoPolicyGroupMIBNotifs, ciscoPolicyGroupMIBObjects=ciscoPolicyGroupMIBObjects, cpgGroup=cpgGroup, cpgGroupEntry=cpgGroupEntry, cpgGroupIpAddrCount=cpgGroupIpAddrCount, cpgGroupIpAddrType=cpgGroupIpAddrType, cpgGroupIpAddress=cpgGroupIpAddress, cpgGroupIpEntry=cpgGroupIpEntry, cpgGroupIpGroupName=cpgGroupIpGroupName, cpgGroupIpMask=cpgGroupIpMask, cpgGroupIpRowStatus=cpgGroupIpRowStatus, cpgGroupIpSourceType=cpgGroupIpSourceType, cpgGroupIpTable=cpgGroupIpTable, cpgGroupName=cpgGroupName, cpgGroupRowStatus=cpgGroupRowStatus, cpgGroupSourceType=cpgGroupSourceType, cpgGroupTable=cpgGroupTable, cpgPolicy=cpgPolicy, cpgPolicyEntry=cpgPolicyEntry, cpgPolicyGroupCount=cpgPolicyGroupCount, cpgPolicyGroupEntry=cpgPolicyGroupEntry, cpgPolicyGroupGroupName=cpgPolicyGroupGroupName, cpgPolicyGroupPolicyName=cpgPolicyGroupPolicyName, cpgPolicyGroupRowStatus=cpgPolicyGroupRowStatus, cpgPolicyGroupTable=cpgPolicyGroupTable, cpgPolicyName=cpgPolicyName, cpgPolicyTable=cpgPolicyTable)
