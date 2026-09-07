#
# PySNMP MIB module CISCO-COPS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-COPS-CLIENT-MIB
# Source digest sha256:8b7ac52648a5c0902d34db1c9ac0b557108e659fb2679ca93ef9c06cd2af8627
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoCopsClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 140))
ciscoCopsClientMIB.setRevisions(('2005-11-14 00:00', '2000-06-11 00:00', '1999-09-16 00:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCopsClientMIB.setRevisionsDescriptions(('Updated the imports such that Unsigned32 is imported from \n            SNMPv2-SMI instead of CISCO-TC. Changed the syntax of the \n            textual conventions CopsRole, CopsRoleCombination, \n            CopsDomainName from DisplayString to OCTET STRING.', 'Added support for optional role configuration.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCopsClientMIB.setLastUpdated('2005-11-14 00:00')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setContactInfo('Cisco Systems\n        Customer Service\n\n        Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n            USA\n\n        Tel: +1 800 553-NETS\n\n        E-mail: cs-wbu@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setDescription('This MIB module is for configuration & statistic query\n        of Common Open Policy Service(COPS) client feature on the Cisco\n        device.  COPS is a simple client/server model for supporting\n        policy control over QoS Signaling Protocols and provisioned QoS\n        resource management.\n\n        COPS is a simple query and response protocol that can be used to\n        exchange policy information between a policy server (Policy\n        Decision Point or PDP) and its clients (Policy Enforcement Points\n        or PEPs).')
class CopsRole(TextualConvention, OctetString):
    description = "A display string where valid letters are a-z, A-Z, 0-9,\n        ., - and _.  Name can not start with an '_'.\n        Policies are assigned to a 'role', and one or more 'roles' are\n        assigned to interfaces, such that an interface takes on the\n        policies indirectly as the policies of the roles assigned to\n        that interface."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class CopsRoleCombination(TextualConvention, OctetString):
    description = "A display string consisting of a set of roles concatenated\n        with '+' characters where the roles are in lexicographic\n        order from minimum to maximum.  Policies are assigned to a\n        'role', and one or more 'roles' are assigned to interfaces,\n        such that an interface takes on the policies indirectly as\n        the policies of the roles assigned to that interface.\n        When one or more roles assigned to an interface, that set of\n        roles is known as a role-combination."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CopsDomainName(TextualConvention, OctetString):
    description = "A display string where valid letters are a-z, A-Z, 0-9,\n        ., - and _.  Name can not start with an '_'.\n        The COPS domain which a COPS client type belongs to.\n        This is so that a COPS server supporting multiple domains\n        can push the correct set of domain policies to a device."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class CopsClientType(TextualConvention, Integer32):
    description = 'An enumerated value for all the supported COPS client type.\n        rsvp(1)             Resource Reservation Protocol(RSVP).  RSVP is a\n                            signaling mechanism that the applications will\n                            use to signal parameters to the network, so that\n                            network can assign QoS for the application data\n                            stream.\n        provisioning(2)     Provisioning.  A client type for COPS to support\n                            policy provisioning.  This client type is\n                            independent of the type of policy (QoS, VPNs,\n                            Security, etc.) and it is based on the concept\n                            of PIBs (Policy Information Bases [PIB]).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsvp", 1), ("provisioning", 2))

ccopsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1))
ccopsGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1))
ccopsServerMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('servers').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsServerMax.setStatus('current')
if mibBuilder.loadTexts: ccopsServerMax.setDescription('Maximum number of configurable COPS servers allowed for\n            each client type.  A value of zero indicates no limitation\n            on the number of configurable COPS servers.')
ccopsMaxRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 2), Unsigned32()).setUnits('roles').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRole.setStatus('current')
if mibBuilder.loadTexts: ccopsMaxRole.setDescription('Indicates the maximum number of roles supported by\n            this device.  A value of zero indicates no limitation on\n            the number of roles.')
ccopsMaxRoleCombination = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 3), Unsigned32()).setUnits('role-combinations').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRoleCombination.setStatus('current')
if mibBuilder.loadTexts: ccopsMaxRoleCombination.setDescription('Indicates the maximum number of role-combinations supported\n            by this device.  A value of zero indicates no limitation on\n            the number of role-combinations.  Each CopsRoleCombination\n            may contain up to ccopsMaxRole roles.')
ccopsServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigTable.setDescription('A list of possible COPS servers that the COPS client will\n            try to connect to in order of ccopsServerConfigPriority.')
ccopsServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigClientType"), (1, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigName"))
if mibBuilder.loadTexts: ccopsServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigEntry.setDescription('A set of configuration information regarding a single COPS\n            server from the point of view of a COPS client.  The entry\n            is created and deleted by using ccopsServerConfigStatus.\n\n            An entry may not exist in the active state unless all\n            objects in the entry have an appropriate value.\n\n            Each client type can have its own COPS servers.\n            By creating, deleting or modifying an entry in this table,\n            users can add, delete or modify a COPS server for a particular\n            client type for the device.\n\n            In order to get policies from COPS server for a client type,\n            user has to create an entry for such client type.')
ccopsServerConfigClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 1), CopsClientType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsServerConfigClientType.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigClientType.setDescription('The type of policies to be retrieved from this server.')
ccopsServerConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsServerConfigName.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigName.setDescription('The IP address or the hostname of a COPS server. If a hostname\n            is used, it will be resolved to an address prior to each attempt\n            to setup a connection to a PDP. If the PEP cannot resolve the\n            hostname, the connection attempt will fail.\n            Use of IP address values is preferred, except in cases where a\n            hostname must/should be used (e.g. if the PDP has a dynamic\n            address)')
ccopsServerConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPriority.setReference('Reference Internet Draft, The COPS (Common Open Policy\n            Service) Protocol, PDP Redirect.')
if mibBuilder.loadTexts: ccopsServerConfigPriority.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigPriority.setDescription('The priority of this entry relative to other entries.\n            The COPS client will attempt to contact COPS servers for\n            the appropriate Client-Type in the order of their\n            priority values.  COPS servers designated by the COPS\n            protocol PDP-Redirect mechanism are always used in\n            preference to any entries in this table.\n\n            When ccopsServerMax mib object is not zero, the valid\n            value for ccopsServerConfigPriority ranges from zero to\n            ccopsServerMax minus one.  When the ccopsServerMax\n            mib object is zero, any valid unsigned value may be used.\n\n            For servers with different value of ccopsServerConfigPriority,\n            the server with lowest value has highest priority.\n\n            For servers with same value of ccopsServerConfigPriority\n            and ccopsServerConfigClientType, the relative priority\n            of Servers is determined by a numerical comparison of their\n            IP addresses, with the lowest address having higher priority.')
ccopsServerConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3288)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPort.setReference('Reference Internet Draft, The COPS (Common Open Policy\n            Service) Protocol, Port number.')
if mibBuilder.loadTexts: ccopsServerConfigPort.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigPort.setDescription('The destination port number to which COPS server messages\n            should be sent.  By default the COPS service will be provided\n            on the well-known COPS protocol port number 3288.')
ccopsServerConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigStatus.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigStatus.setDescription('The status of COPS server configuration for a client type.\n            An entry may not exist in the active state unless all\n            objects in the entry have an appropriate value.\n\n            Once a row becomes active, value in any other column within\n            such row cannot be modified except by setting\n            ccopsServerConfigStatus to notInService(2) for such row.')
ccopsInitialTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsInitialTimeout.setStatus('current')
if mibBuilder.loadTexts: ccopsInitialTimeout.setDescription('If the device can not connect to the last connected COPS\n            server, it uses this value for the initial retry time-out\n            and then retries to connect after this time-out period.\n            This value is re-used for the first retry after every\n            successful connection.\n\n            When the device is connecting to COPS server the first\n            time or the last connected COPS server is no longer\n            available, it will attempt to contact COPS servers existing\n            in ccopsServerConfigTable for the appropriate Client-Type\n            in the order of their priority values.')
ccopsTimeoutIncrement = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutIncrement.setStatus('current')
if mibBuilder.loadTexts: ccopsTimeoutIncrement.setDescription('On every consecutive failure to connect to all existing\n            COPS server for a client type, the COPS client increases\n            the retry time-out by ccopsTimeoutIncrement but not greater\n            than ccopsTimeoutMax.')
ccopsTimeoutMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutMax.setStatus('current')
if mibBuilder.loadTexts: ccopsTimeoutMax.setDescription('The maximum retry time-out that the COPS client allows.\n            On every consecutive failure to connect to all COPS servers,\n            the COPS client increases the retry time-out up to\n            ccopsTimeoutMax.')
ccopsDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsDomainTable.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainTable.setDescription('A list of COPS domains for each client type supported in\n            the device.')
ccopsDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsDomainClientType"))
if mibBuilder.loadTexts: ccopsDomainEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainEntry.setDescription('A set of domain configuration information regarding a\n            single COPS client type.\n\n            An entry will exist for each COPS client type which is\n            supported in the device.\n\n            For each COPS client type supported in the device, a\n            domain name should be specified if the COPS server for\n            that client type has multiple domains defined in its\n            database.')
ccopsDomainClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 1), CopsClientType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsDomainClientType.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainClientType.setDescription('The type of COPS client.')
ccopsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 2), CopsDomainName().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsDomainName.setReference('Reference CISCO-QOS-MIB, qosPolicySource.')
if mibBuilder.loadTexts: ccopsDomainName.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainName.setDescription('The COPS domain which this client type belongs to.\n            This is so that a COPS server supporting multiple domains\n            can push the correct set of domain policies to this device.\n            Zero length name is default.  COPS server have a default\n            set of policies for clients who have zero length domain\n            names.\n\n            Changing the COPS domain name while qosPolicySource is cops(2)\n            will result in requesting new policies from the cops server and\n            configuring the device with those new policies.  The value of\n            ccopsDomainName is ignored if qosPolicySource is local(1).')
ccopsRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsRoleTable.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleTable.setDescription('A list of roles.  The number of entries is\n            determined by ccopsMaxRole.')
ccopsRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-COPS-CLIENT-MIB", "ccopsRoleName"))
if mibBuilder.loadTexts: ccopsRoleEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleEntry.setDescription('Entry containing COPS-PR role information.  The entry is\n            created, deleted and modified by using ccopsRoleStatus.\n\n            There is a maximum on the number of roles which may be\n            configured per device.  In order to make a role available for\n            interface to construct its role combination, such role must\n            exist in the role table.  Deleting a role in ccopsRoleTable\n            also removes that role from all role combinations for all\n            interfaces.\n\n            Therefore, a particular role can not be added into the role\n            combination for any interface if it is removed from this table.')
ccopsRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 1), CopsRole()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsRoleName.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleName.setDescription('The name of the role.  Only roles which were defined in COPS\n            server should be used.  COPS server will only supply the policies\n            for those roles defined in its database.')
ccopsRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsRoleStatus.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleStatus.setDescription('This object is used to manage creation, deletion and\n            modification of rows in this table.\n\n            An entry may not exist in the active state unless all\n            objects in the entry have an appropriate value.\n            Once a row becomes active, value in any other column within\n            such row cannot be modified except by setting\n            ccopsRoleStatus to notInService(2) for such row.\n\n            Deleting a row results in removing this ccopsRoleName from all\n            role combinations in the ccopsIfTable')
ccopsIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ccopsIfTable.setStatus('current')
if mibBuilder.loadTexts: ccopsIfTable.setDescription('A list of interface entries.  An entry will exist for each\n            interface which supports COPS-PR feature.')
ccopsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccopsIfEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsIfEntry.setDescription('Entry containing COPS status for a particular interface.\n\n            By default each interface has no roles.  It then has a role\n            combination that is the zero length string.\n\n            Roles in a role combination for an interface are reported\n            to the PDP by the PEP.  An interface may have multiple roles.\n            Adding/deleting roles results in changes to the role\n            combination for an interface.  Therefore, a new set of QoS\n            policies will be used for the interface with the new role\n            combination.')
ccopsIfRoleCombination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1, 1), CopsRoleCombination()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsIfRoleCombination.setStatus('current')
if mibBuilder.loadTexts: ccopsIfRoleCombination.setDescription('A display string, role combination, that is associated\n            with an interface.  This is the administratively-desired\n            role combination which represents roles that are currently\n            set by the administrator for a particular interface in the\n            COPS domain.\n\n            If copsMaxRoleCombination is one, the new role will be\n            applied to all interfaces which support COPS feature on\n            the device.  Agent returns inconsistentValue if this role\n            does not exist in ccopsRoleTable, resourceUnavailable if\n            the role combination exceeds copsMaxRoleCombination in the\n            device, wrongValue if a non-lexicographically-ordered value\n            is written to it.\n\n            On some platforms, roles may be assigned per port group\n            rather than per port.  If multiple ports belong to a port\n            group, the role combination assigned to any of the ports\n            in such group will apply to all ports in the same group.\n\n            On some platforms, there can be a single role combination\n            for the entire device.  The role combination assigned to\n            any of the interfaces will apply to all interfaces which\n            support COPS feature in the device.')
ccopsRoleConfigSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsRoleConfigSupported.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleConfigSupported.setDescription('Indicates whether this device supports the ccopsMaxRole\n             and ccopsRoleTable, and thereby, whether a role must be\n             present in the ccopsRoleTable before it can be used within\n             a value of ccopsIfRoleCombination.')
ccopsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 2))
ccopsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3))
ccopsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1))
ccopsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2))
ccopsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBCompliance = ccopsMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ccopsMIBCompliance.setDescription('The compliance statement for the  CISCO-COPS-CLIENT-MIB.')
ccopsMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroupRev2"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBComplianceRev2 = ccopsMIBComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: ccopsMIBComplianceRev2.setDescription('The compliance statement for the CISCO-COPS-CLIENT-MIB.')
ccopsGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroup = ccopsGlobalGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ccopsGlobalGroup.setDescription('A collection of objects providing the COPS ability on the\n            device.  Devices implementing the COPS client feature should\n            support this group.')
ccopsGlobalGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleConfigSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroupRev2 = ccopsGlobalGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ccopsGlobalGroupRev2.setDescription('A collection of objects providing the COPS ability on the\n            device.')
ccopsRoleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 3)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsRoleGroup = ccopsRoleGroup.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleGroup.setDescription('A collection of objects which allow an agent to require\n            a limited set of allowed roles be specified, and to reject\n            any role-combination containing any other role.')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-MIB", CopsClientType=CopsClientType, CopsDomainName=CopsDomainName, CopsRole=CopsRole, CopsRoleCombination=CopsRoleCombination, PYSNMP_MODULE_ID=ciscoCopsClientMIB, ccopsDomainClientType=ccopsDomainClientType, ccopsDomainEntry=ccopsDomainEntry, ccopsDomainName=ccopsDomainName, ccopsDomainTable=ccopsDomainTable, ccopsGlobalGroup=ccopsGlobalGroup, ccopsGlobalGroupRev2=ccopsGlobalGroupRev2, ccopsGlobalObjects=ccopsGlobalObjects, ccopsIfEntry=ccopsIfEntry, ccopsIfRoleCombination=ccopsIfRoleCombination, ccopsIfTable=ccopsIfTable, ccopsInitialTimeout=ccopsInitialTimeout, ccopsMIBCompliance=ccopsMIBCompliance, ccopsMIBComplianceRev2=ccopsMIBComplianceRev2, ccopsMIBCompliances=ccopsMIBCompliances, ccopsMIBConformance=ccopsMIBConformance, ccopsMIBGroups=ccopsMIBGroups, ccopsMIBNotifications=ccopsMIBNotifications, ccopsMIBObjects=ccopsMIBObjects, ccopsMaxRole=ccopsMaxRole, ccopsMaxRoleCombination=ccopsMaxRoleCombination, ccopsRoleConfigSupported=ccopsRoleConfigSupported, ccopsRoleEntry=ccopsRoleEntry, ccopsRoleGroup=ccopsRoleGroup, ccopsRoleName=ccopsRoleName, ccopsRoleStatus=ccopsRoleStatus, ccopsRoleTable=ccopsRoleTable, ccopsServerConfigClientType=ccopsServerConfigClientType, ccopsServerConfigEntry=ccopsServerConfigEntry, ccopsServerConfigName=ccopsServerConfigName, ccopsServerConfigPort=ccopsServerConfigPort, ccopsServerConfigPriority=ccopsServerConfigPriority, ccopsServerConfigStatus=ccopsServerConfigStatus, ccopsServerConfigTable=ccopsServerConfigTable, ccopsServerMax=ccopsServerMax, ccopsTimeoutIncrement=ccopsTimeoutIncrement, ccopsTimeoutMax=ccopsTimeoutMax, ciscoCopsClientMIB=ciscoCopsClientMIB)
