#
# PySNMP MIB module CISCO-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LAG-MIB
# Source digest sha256:c8dba380fc96d403d4e2d74b8504b4fc793a8f3604a37332dded4b77aabd3a86
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInterfaceIndexList, = mibBuilder.importSymbols("CISCO-TC", "CiscoInterfaceIndexList")
dot3adAggPortEntry, dot3adAggPortListEntry = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortEntry", "dot3adAggPortListEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 225))
ciscoLagMIB.setRevisions(('2014-01-14 00:00', '2010-10-20 00:00', '2009-11-19 00:00', '2008-01-08 00:00', '2006-06-21 00:00', '2004-06-11 00:00', '2002-12-13 00:00', '2002-01-02 00:00', '2001-10-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLagMIB.setRevisionsDescriptions(('Added clagAggPortListInterfaceIndexGroup.', 'Added new enum values vlanIp(5) and ipPort(6) to\n         ClagDistributionProtocol textual convention.', 'Added clagAggRateGroup, clagAggChannelIfLacpGroup,\n        clagAggChannelIfHashDistMethodGroup, clagAggChannelIfMinLinkGroup\n        and clagAggHashDistGlobalGroup.', 'Modified the description of clagAggPortListPorts.', 'Added clagAggMaxAggregatorsGroup and modified the\n        description of clagAggPortListPorts.', 'Added clagAggPortListTable.', 'Added a new value vlanIpPort(4) in TEXTUAL-CONVENTION\n        ClagDistributionProtocol.\n        Added a new object clagAggDistributionMplsProtocol.', 'Modified Description of clagAggDistributionProtocol.', 'Initial version of this MIB module.\n        Support Distribution configuration for LACP, Aggregation \n        protocol control, and  Administrative status for LACP.',))
if mibBuilder.loadTexts: ciscoLagMIB.setLastUpdated('2014-01-14 00:00')
if mibBuilder.loadTexts: ciscoLagMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLagMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail:  cs-etherchan@cisco.com\n             cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLagMIB.setDescription('Cisco Link Aggregation module for managing IEEE Std\n        802.3ad.\n\n        This MIB provides Link Aggregation information that are\n        either excluded by IEEE Std 802.3ad (IEEE8023-LAG-MIB)\n        or specific to Cisco products.')
clagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1))
class ClagDistributionProtocol(TextualConvention, Integer32):
    description = 'An enumerated type for all the supported load balancing\n        algorithms used on the port channel interface to distribute \n        outgoing data frames among its component interaces, such \n        as IP address.  \n\n        ip(1)               IP address\n        mac(2)              MAC address \n        port(3)             port number\n        vlanIpPort(4)       vlan number, IP address and\n                            port number\n        vlanIp(5)           VLAN number and IP address\n        ipPort(6)           IP address and port number'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ip", 1), ("mac", 2), ("port", 3), ("vlanIpPort", 4), ("vlanIp", 5), ("ipPort", 6))

class ClagDistributionAddressMode(TextualConvention, Integer32):
    description = 'An enumerated type for all the supported load\n        balancing address modes to distribute traffic\n        across multiple links.  The address mode can be \n        source, destination, or both used on this port \n        channel interface to distribute outgoing data frames \n        among its component interfaces. \n\n        source(1)         Source address.\n        destination(2)    Destination address.\n        both(3)           both, Source and Destination.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("source", 1), ("destination", 2), ("both", 3))

class ClagDistributionMplsProtocol(TextualConvention, Integer32):
    description = 'An enumerated type for all the supported load balancing\n        algorithms used on the port channel interface to distribute \n        outgoing MPLS (Multi-Protocol Label Switching) data \n        frames among its component interfaces, such as \n        MPLS label.\n\n        label(1)            MPLS label\n        labelIp(2)          MPLS label or IP address'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("label", 1), ("labelIp", 2))

class ClagAggregationProtocol(TextualConvention, Integer32):
    description = 'An enumerated type for all the supported aggregation\n        protocols.\n\n        lacp(1)     Link Aggregation Control Protocol(LACP),\n                    IEEE 802.3ad\n        pagp(2)     Port Aggregation Protocol'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("lacp", 1), ("pagp", 2))

class ClagPortAdminStatus(TextualConvention, Integer32):
    description = "An enumerated type for all the LACP administrative states on\n        a particular aggregation port.\n\n        off(1)          No LACP involved on the aggregation port.\n\n        on(2)           The aggregation port always join link\n                        aggregation whithout any LACP protocol\n                        involved.\n\n        active(3)       Active LACP indicates the port's preference\n                        to participate in the protocol regardless of\n                        Partner's control value.\n\n        passive(4)      Passive indicates the port's preference for\n                        not transmitting LACP PDU unless its Partner's\n                        control value is Active LACP."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("on", 2), ("active", 3), ("passive", 4))

clagGlobalConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1))
clagAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2))
clagAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3))
clagAggPortList = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4))
clagAggChannelIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5))
clagAggDistributionProtocol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 1), ClagDistributionProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionProtocol.setStatus('current')
if mibBuilder.loadTexts: clagAggDistributionProtocol.setDescription('This object controls the load balancing algorithms\n        used on this port channel interface to distribute outgoing \n        data frames among its component interfaces.')
clagAggDistributionAddressMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 2), ClagDistributionAddressMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionAddressMode.setStatus('current')
if mibBuilder.loadTexts: clagAggDistributionAddressMode.setDescription('The load balancing address mode for the device.')
clagAggDistributionMplsProtocol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 3), ClagDistributionMplsProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionMplsProtocol.setStatus('current')
if mibBuilder.loadTexts: clagAggDistributionMplsProtocol.setDescription('This object controls the load balancing algorithms\n        used on this port channel interface to distribute \n        outgoing MPLS data frames among its component interfaces.\n\n        This object is only instantiated on platforms which \n        support aggregation load balancing for MPLS packets.')
clagAggMaxAggregators = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggMaxAggregators.setStatus('current')
if mibBuilder.loadTexts: clagAggMaxAggregators.setDescription('This object indicates the maximum number of aggregators\n        supported by the device.')
clagAggHashDistMethodGlobalConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adaptive", 1), ("fixed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggHashDistMethodGlobalConfig.setStatus('current')
if mibBuilder.loadTexts: clagAggHashDistMethodGlobalConfig.setDescription('Specifies the global configuration for hash\n        distribution method applied on a port channel \n        interface among its channel members.\n\n        adaptive(1)  :  Adaptive hash distribution for the bundle\n                        among port channel members.\n        fixed(2)     :  Fixed hash distribution for the bundle\n                        among port channel members.')
clagAggProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clagAggProtocolTable.setStatus('current')
if mibBuilder.loadTexts: clagAggProtocolTable.setDescription('A table that contains protocol information about every\n        interface which supports link aggregation.')
clagAggProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clagAggProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: clagAggProtocolEntry.setDescription('Entry containing aggregation protocol type for a\n        particular interface.  An entry is created in this\n        table when its associated ifEntry is created and that \n        interface supports link aggregation.  The entry of this\n        table is deleted when the associated ifEntry is removed.')
clagAggProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1, 1), ClagAggregationProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggProtocolType.setStatus('current')
if mibBuilder.loadTexts: clagAggProtocolType.setDescription('The aggregation protocol type for the interface.\n\n        On some platforms, aggregation protocol may be assigned per\n        group.  The group can be a collection of the ports which belong\n        to a module or system.  If the aggregation protocol is assigned\n        to any of the ports in such group then the aggregation protocol\n        will apply to all ports in the same group.\n\n        On some platforms, aggregation protocol type  can be assigned\n        per aggregator.  If multiple ports belong to a aggregator,\n        the aggregation protocol assigned to any of the ports in such\n        aggregator will apply to all ports in the same.')
clagAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clagAggPortTable.setReference('IEEE 802.3 Subclause 30.7.2')
if mibBuilder.loadTexts: clagAggPortTable.setStatus('current')
if mibBuilder.loadTexts: clagAggPortTable.setDescription('A table that contains information about every\n        aggregation port that is associated with this system.\n        This table contains additional objects for the\n        dot3adAggPortTable.')
clagAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1), ).setMaxAccess("notaccessible")
dot3adAggPortEntry.registerAugmentions(("CISCO-LAG-MIB", "clagAggPortEntry"))
clagAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
if mibBuilder.loadTexts: clagAggPortEntry.setStatus('current')
if mibBuilder.loadTexts: clagAggPortEntry.setDescription('An entry containing additional management information\n        applicable to a particular aggregation port.')
clagAggPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 1), ClagPortAdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggPortAdminStatus.setStatus('current')
if mibBuilder.loadTexts: clagAggPortAdminStatus.setDescription('The administrative status of the LACP protocol on this\n        aggregation port.')
clagAggPortRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("normal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggPortRate.setStatus('current')
if mibBuilder.loadTexts: clagAggPortRate.setDescription('Specifies the requested exchange rate of LACP packets\n        on this interface.\n        fast(1)  :    The device requests its peers to send LACP packets \n                      at fast rate to this interface.\n        normal(2):    The decice requests its peers to send LACP packets\n                      at normal rate to this interface.')
clagAggPortListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clagAggPortListTable.setReference('IEEE 802.3 Subclause 30.7.1.1.30')
if mibBuilder.loadTexts: clagAggPortListTable.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListTable.setDescription('This table augments the dot3adAggPortListTable and\n        provides the complete list of ports associated with\n        each Aggregator.')
clagAggPortListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1), ).setMaxAccess("notaccessible")
dot3adAggPortListEntry.registerAugmentions(("CISCO-LAG-MIB", "clagAggPortListEntry"))
clagAggPortListEntry.setIndexNames(*dot3adAggPortListEntry.getIndexNames())
if mibBuilder.loadTexts: clagAggPortListEntry.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListEntry.setDescription('A list of the ports associated with a given Aggregator.')
clagAggPortListPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggPortListPorts.setReference('IEEE 802.3 Subclause 30.7.1.1.30')
if mibBuilder.loadTexts: clagAggPortListPorts.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListPorts.setDescription("This object contains a list of ports currently associated\n        with this Aggregator in the format of\n        '[number_of_ports][cieIfDot1dBaseMappingPort1][...]\n         [cieIfDot1dBaseMappingPortn]'\n\n        where\n        [number_of_ports] is of size 2 octet and indicates\n        the number of ports contains in this object. It\n        also indicates the number of cieIfDot1dBaseMappingPort field\n        following this field. \n\n        [cieIfDot1dBaseMappingPort'n'] is the value of \n        cieIfDot1dBaseMappingPort of the 'n' port associated with this\n        Aggregation and has size of 2 octets where n is up to\n        [number_of_ports].")
clagAggPortListInterfaceIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 2), CiscoInterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggPortListInterfaceIndexList.setReference('IEEE 802.3 Subclause 30.7.1.1.30')
if mibBuilder.loadTexts: clagAggPortListInterfaceIndexList.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListInterfaceIndexList.setDescription('This object contains a list of ports currently associated\n        with this Aggregator in the format of CiscoInterfaceIndexList.')
clagAggChannelIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: clagAggChannelIfTable.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfTable.setDescription('A table providing port channel\n        configuration information for port channel\n        interfaces identified by ifIndex.')
clagAggChannelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clagAggChannelIfEntry.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfEntry.setDescription('An entry containing port channel\n        configuration information for port \n        channel interfaces.')
clagAggChannelIfFastSwitchOver = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfFastSwitchOver.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfFastSwitchOver.setDescription('Specifies whether LACP protocol fast switchover\n        mode is enabled on this port channel interface\n        or not.')
clagAggChannelIfMaxBundle = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfMaxBundle.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfMaxBundle.setDescription('Specifies the maximum number of member\n        ports that can be bundled on this port\n        channel interface for LACP protocol.')
clagAggChannelIfMinLink = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfMinLink.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfMinLink.setDescription('Specifies the minimum number of bundled member ports that are\n        needed in order for this port channel interface to be\n        operational.\n        A value of zero for this object indicates that no minimum\n        number of bundled member ports are required for this port\n        channel interface to be operational.')
clagAggChannelIfHashDistAdminMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("adaptive", 2), ("fixed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfHashDistAdminMethod.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfHashDistAdminMethod.setDescription('Specifies the hash distribution method that is administratively\n        configured on this port channel interface upon its channel \n        membership transition event. \n\n        none(1)      :  Hash distribution algorithm on this \n                        port channel interface is not specifically \n                        configured and global configuration of \n                        clagAggHashDistMethodGlobalConfig will\n                        be applied on this port channel interface.\n        adaptive(2)  :  Adaptive hash distribution for this port \n                        channel interface among its channel members.\n        fixed(3)     :  Fixed hash distribution for this port channel\n                        interface among its channel members.')
clagAggChannelIfHashDistOperMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("adaptive", 2), ("fixed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggChannelIfHashDistOperMethod.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfHashDistOperMethod.setDescription('Specifies the operational hash distribution method\n        for this port channel interface among the port channel members.\n\n        other(1)        : None of the following. \n        adaptive(2)     : Adaptive hash distribution for the \n                          port channel interface among its \n                          channel members.\n        fixed(3)        : Fixed hash distribution for the port\n                          channel among channel members.')
clagMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 2))
clagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3))
clagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1))
clagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2))
clagMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 1)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance = clagMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: clagMIBCompliance.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 2)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance2 = clagMIBCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: clagMIBCompliance2.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 3)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance3 = clagMIBCompliance3.setStatus('deprecated')
if mibBuilder.loadTexts: clagMIBCompliance3.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 4)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance4 = clagMIBCompliance4.setStatus('deprecated')
if mibBuilder.loadTexts: clagMIBCompliance4.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 5)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"), ("CISCO-LAG-MIB", "clagAggRateGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfLacpGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistMethodGroup"), ("CISCO-LAG-MIB", "clagAggHashDistGlobalGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfMinLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance5 = clagMIBCompliance5.setStatus('deprecated')
if mibBuilder.loadTexts: clagMIBCompliance5.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 6)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"), ("CISCO-LAG-MIB", "clagAggRateGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfLacpGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistMethodGroup"), ("CISCO-LAG-MIB", "clagAggHashDistGlobalGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfMinLinkGroup"), ("CISCO-LAG-MIB", "clagAggPortListInterfaceIndexGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance6 = clagMIBCompliance6.setStatus('current')
if mibBuilder.loadTexts: clagMIBCompliance6.setDescription('The compliance statement for entities which implement\n        the Cisco Link Aggregation MIB')
clagAggProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 1)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggProtocolGroup = clagAggProtocolGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggProtocolGroup.setDescription('The object that provide aggregation protocol type of an\n        interface. These are additional to the IEEE Std 802.3ad\n        MIB.')
clagAggPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 2)).setObjects(("CISCO-LAG-MIB", "clagAggPortAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortGroup = clagAggPortGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggPortGroup.setDescription('A collection of objects that provide admin status\n        about an aggregation port.  These are additional to the\n        IEEE Std 802.3ad MIB.')
clagAggDistributionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 3)).setObjects(("CISCO-LAG-MIB", "clagAggDistributionProtocol"), ("CISCO-LAG-MIB", "clagAggDistributionAddressMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggDistributionGroup = clagAggDistributionGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggDistributionGroup.setDescription('A collection of objects that provide the load balancing\n        information for an aggregator.  These are additional to\n        the IEEE Std 802.3ad MIB.')
clagAggDistributionMplsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 4)).setObjects(("CISCO-LAG-MIB", "clagAggDistributionMplsProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggDistributionMplsGroup = clagAggDistributionMplsGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggDistributionMplsGroup.setDescription('A collection of objects that provide the load balancing\n        information for an aggregator for MPLS packets.  \n        These are additional to the IEEE Std 802.3ad MIB.')
clagAggPortListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 5)).setObjects(("CISCO-LAG-MIB", "clagAggPortListPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortListGroup = clagAggPortListGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListGroup.setDescription('A collection of object that provides information about\n        ports in an aggregation.')
clagAggMaxAggregatorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 6)).setObjects(("CISCO-LAG-MIB", "clagAggMaxAggregators"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggMaxAggregatorsGroup = clagAggMaxAggregatorsGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggMaxAggregatorsGroup.setDescription('A collection of object that provides information about\n        the maximum number of aggregators supported by the \n        device.')
clagAggRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 7)).setObjects(("CISCO-LAG-MIB", "clagAggPortRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggRateGroup = clagAggRateGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggRateGroup.setDescription('A collection of object that provides information about\n        the rate at which LACP packets are ingressed on \n        interfaces.')
clagAggChannelIfLacpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 8)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfFastSwitchOver"), ("CISCO-LAG-MIB", "clagAggChannelIfMaxBundle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfLacpGroup = clagAggChannelIfLacpGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfLacpGroup.setDescription('A collection of objects that provides information about\n        the LACP protocol configurations for port channel\n        interfaces.')
clagAggChannelIfHashDistMethodGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 9)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfHashDistAdminMethod"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistOperMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfHashDistMethodGroup = clagAggChannelIfHashDistMethodGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfHashDistMethodGroup.setDescription('A collection of objects that provides information about\n        the port channel configurations of hash distribution\n        method on port channel interfaces.')
clagAggHashDistGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 10)).setObjects(("CISCO-LAG-MIB", "clagAggHashDistMethodGlobalConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggHashDistGlobalGroup = clagAggHashDistGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggHashDistGlobalGroup.setDescription('A collection of object that provides information about global\n        configuration of hash distribution method on port channel \n        interface.')
clagAggChannelIfMinLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 11)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfMinLink"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfMinLinkGroup = clagAggChannelIfMinLinkGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggChannelIfMinLinkGroup.setDescription('A collection of objects that provides information about\n        the minimum link configurations for port channel\n        interfaces.')
clagAggPortListInterfaceIndexGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 12)).setObjects(("CISCO-LAG-MIB", "clagAggPortListInterfaceIndexList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortListInterfaceIndexGroup = clagAggPortListInterfaceIndexGroup.setStatus('current')
if mibBuilder.loadTexts: clagAggPortListInterfaceIndexGroup.setDescription('A collection of objects that provides information about\n         ports in an aggregation in the format of \n         CiscoInterfaceIndexList.')
mibBuilder.exportSymbols("CISCO-LAG-MIB", ClagAggregationProtocol=ClagAggregationProtocol, ClagDistributionAddressMode=ClagDistributionAddressMode, ClagDistributionMplsProtocol=ClagDistributionMplsProtocol, ClagDistributionProtocol=ClagDistributionProtocol, ClagPortAdminStatus=ClagPortAdminStatus, PYSNMP_MODULE_ID=ciscoLagMIB, ciscoLagMIB=ciscoLagMIB, clagAgg=clagAgg, clagAggChannelIfEntry=clagAggChannelIfEntry, clagAggChannelIfFastSwitchOver=clagAggChannelIfFastSwitchOver, clagAggChannelIfHashDistAdminMethod=clagAggChannelIfHashDistAdminMethod, clagAggChannelIfHashDistMethodGroup=clagAggChannelIfHashDistMethodGroup, clagAggChannelIfHashDistOperMethod=clagAggChannelIfHashDistOperMethod, clagAggChannelIfLacpGroup=clagAggChannelIfLacpGroup, clagAggChannelIfMaxBundle=clagAggChannelIfMaxBundle, clagAggChannelIfMinLink=clagAggChannelIfMinLink, clagAggChannelIfMinLinkGroup=clagAggChannelIfMinLinkGroup, clagAggChannelIfTable=clagAggChannelIfTable, clagAggChannelIntf=clagAggChannelIntf, clagAggDistributionAddressMode=clagAggDistributionAddressMode, clagAggDistributionGroup=clagAggDistributionGroup, clagAggDistributionMplsGroup=clagAggDistributionMplsGroup, clagAggDistributionMplsProtocol=clagAggDistributionMplsProtocol, clagAggDistributionProtocol=clagAggDistributionProtocol, clagAggHashDistGlobalGroup=clagAggHashDistGlobalGroup, clagAggHashDistMethodGlobalConfig=clagAggHashDistMethodGlobalConfig, clagAggMaxAggregators=clagAggMaxAggregators, clagAggMaxAggregatorsGroup=clagAggMaxAggregatorsGroup, clagAggPort=clagAggPort, clagAggPortAdminStatus=clagAggPortAdminStatus, clagAggPortEntry=clagAggPortEntry, clagAggPortGroup=clagAggPortGroup, clagAggPortList=clagAggPortList, clagAggPortListEntry=clagAggPortListEntry, clagAggPortListGroup=clagAggPortListGroup, clagAggPortListInterfaceIndexGroup=clagAggPortListInterfaceIndexGroup, clagAggPortListInterfaceIndexList=clagAggPortListInterfaceIndexList, clagAggPortListPorts=clagAggPortListPorts, clagAggPortListTable=clagAggPortListTable, clagAggPortRate=clagAggPortRate, clagAggPortTable=clagAggPortTable, clagAggProtocolEntry=clagAggProtocolEntry, clagAggProtocolGroup=clagAggProtocolGroup, clagAggProtocolTable=clagAggProtocolTable, clagAggProtocolType=clagAggProtocolType, clagAggRateGroup=clagAggRateGroup, clagGlobalConfigObjects=clagGlobalConfigObjects, clagMIBCompliance2=clagMIBCompliance2, clagMIBCompliance3=clagMIBCompliance3, clagMIBCompliance4=clagMIBCompliance4, clagMIBCompliance5=clagMIBCompliance5, clagMIBCompliance6=clagMIBCompliance6, clagMIBCompliance=clagMIBCompliance, clagMIBCompliances=clagMIBCompliances, clagMIBConformance=clagMIBConformance, clagMIBGroups=clagMIBGroups, clagMIBNotifications=clagMIBNotifications, clagMIBObjects=clagMIBObjects)
