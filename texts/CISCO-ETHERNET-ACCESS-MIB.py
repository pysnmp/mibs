#
# PySNMP MIB module CISCO-ETHERNET-ACCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHERNET-ACCESS-MIB
# Source digest sha256:a2a62f5d9caa035e2fdddbef3accf34446eb870207a031b3fa9d19837b7c983a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
managementDomainIndex, vtpVlanIndex = mibBuilder.importSymbols("CISCO-VTP-MIB", "managementDomainIndex", "vtpVlanIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEthernetAccessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 466))
ciscoEthernetAccessMIB.setRevisions(('2007-09-14 00:00', '2005-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setRevisionsDescriptions(('Added ENI as a new port type to the ceaPortType and\n        ceaPortCapability objects.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setLastUpdated('2007-09-14 00:00')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dsbu@cisco.com')
if mibBuilder.loadTexts: ciscoEthernetAccessMIB.setDescription("The tables defined by this MIB module contain a collection\n        of managed objects that are general in nature and apply to\n        an edge device in an organizations network, e.g. a Metro \n        Ethernet network. An edge device, is a customer located \n        equipment, this is the first device which will connect the\n        Service Provider's network and map subscriber traffic into\n        the next layer. The access media could be either CAT5 or\n        fiber. The access device (edge device) can be designed for\n        DSL, Ethernet or other technologies, however, this MIB is \n        designed for Ethernet. \n\n        Terminology:\n        UNI - User to Network Interface \n        NNI - Network to Network Interface.\n        ENI - Enhanced Network Interface. Enhanced UNI port.\n        module/device\n            - In an environment (specifically, in an SNMP context)\n              consisting of a single chassis which can contain\n              multiple cards, the term 'module' refers to a card\n              and the term 'device' refers to the whole chassis.\n              In an environment where multiple chassis are 'stacked'\n              together, the term 'module' refers to a chassis and\n              the term 'device' refers to the whole stack.\n              In an environment containing only a single chassis\n              without removable cards, the terms 'device' and\n              'module' both refer to the chassis and its contents.")
ciscoEthernetAccessMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1))
ciscoEthernetAccessMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2))
ceaGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1))
ceaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2))
class CeaVlanUNIType(TextualConvention, Integer32):
    description = "The type of a VLAN.\n\n        'other' -- this VLAN is not a UNI VLAN \n\n        'isolated' -- this VLAN is a UNI isolated VLAN.  \n            UNI ports that are members of a UNI isolated VLAN can\n            not communicate with other ports in that VLAN, however \n            NNI ports can communicate with UNI and NNI ports in the\n            same VLAN. \n\n        'community' -- this VLAN is a UNI community VLAN.  \n        UNI and NNI ports that are members of the community \n        VLAN can communicate with all other UNI and NNI ports \n        in the same VLAN."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("isolated", 2), ("community", 3))

ceaMaxNNIPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxNNIPorts.setStatus('current')
if mibBuilder.loadTexts: ceaMaxNNIPorts.setDescription("The max number of interfaces per module for which the\n        ceaPortType can have the value 'nni'.\n        The value of 0 is returned by this object if there is no \n        limitation to the number of NNI ports.")
ceaMaxUNIVlanCommunityPorts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaMaxUNIVlanCommunityPorts.setStatus('current')
if mibBuilder.loadTexts: ceaMaxUNIVlanCommunityPorts.setDescription("The maximum number of ports on this device for which\n        the ceaUNIVlanType object can have the value 'community'.\n        The value of 0 is returned by this object if there is no \n        limitation to the number of UNI VLAN Communities.")
ceaPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceaPortTable.setStatus('current')
if mibBuilder.loadTexts: ceaPortTable.setDescription('This table contains Ethernet port specific information.\n        There exists an entry for each Ethernet port with an ifType\n        of 6 (ethernetCsmacd) in this table.\n        Note that the maximum number of NNI ports that can be\n        configured per module on this device is given by the value\n        of ceaMaxNNIPorts.')
ceaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceaPortEntry.setStatus('current')
if mibBuilder.loadTexts: ceaPortEntry.setDescription('A set of Ethernet port specific parameters for a device\n        which can be configured with a mixture of port types \n        defined by the ceaPortType object.')
ceaPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 1), ("uni", 2), ("nni", 3), ("eni", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaPortType.setStatus('current')
if mibBuilder.loadTexts: ceaPortType.setDescription('The current configuration of the port. Only ports that are\n        supported by the  ceaPortCapability object can be set.\n        Unspecified port type is any other port type than NNI, \n        UNI or ENI.\n        unspecified = Not UNI, or NNI, or ENI\n        uni         = User to Network Interface port type.\n        nni         = Network to Network Interface port type.\n        eni         = Enhanced UNI port type.')
ceaPortCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("nni", 0), ("uni", 1), ("eni", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceaPortCapability.setStatus('current')
if mibBuilder.loadTexts: ceaPortCapability.setDescription("Types   supported by the Ethernet port. If a port doesn't\n        support the port type the ceaPortType will not allow \n        set of the unsupported type.\n        nni  = Port supports NNI.\n        uni  = Port supports UNI.\n        eni  = Port supports ENI.")
ceaUNIVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceaUNIVlanTable.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanTable.setDescription("This table contains UNI VLAN information for all the VLANs\n        which currently exist on this device. \n        The number of UNI ports that can belong to a VLAN type \n        'community' is limited by the ceaMaxUNIVlanCommunityPorts \n        object.")
ceaUNIVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: ceaUNIVlanEntry.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanEntry.setDescription('There is an entry in this table for each VLAN that\n        exist on this device.')
ceaUNIVlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 466, 1, 2, 2, 1, 1), CeaVlanUNIType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceaUNIVlanType.setStatus('current')
if mibBuilder.loadTexts: ceaUNIVlanType.setDescription('Indicates the VLAN type defined for the UNI VLAN.')
cEthernetAccessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1))
cEthernetAccessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2))
cEthernetAccessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 1, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaPortGroup"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEthernetAccessMIBCompliance = cEthernetAccessMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cEthernetAccessMIBCompliance.setDescription('The compliance statement for entities that implement the\n        CISCO-ETHERNET-ACCESS-MIB. Implementation of this MIB is\n        mandatory for any platform that have Ethernet UNI/NNI \n        capable interfaces.')
ceaPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 1)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxNNIPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortType"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaPortCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaPortGroup = ceaPortGroup.setStatus('current')
if mibBuilder.loadTexts: ceaPortGroup.setDescription('A collection of managed objects defining port types.')
ceaVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 466, 2, 2, 2)).setObjects(("CISCO-ETHERNET-ACCESS-MIB", "ceaMaxUNIVlanCommunityPorts"), ("CISCO-ETHERNET-ACCESS-MIB", "ceaUNIVlanType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceaVlanGroup = ceaVlanGroup.setStatus('current')
if mibBuilder.loadTexts: ceaVlanGroup.setDescription('A collection of managed objects defining VLAN types.')
mibBuilder.exportSymbols("CISCO-ETHERNET-ACCESS-MIB", CeaVlanUNIType=CeaVlanUNIType, PYSNMP_MODULE_ID=ciscoEthernetAccessMIB, cEthernetAccessMIBCompliance=cEthernetAccessMIBCompliance, cEthernetAccessMIBCompliances=cEthernetAccessMIBCompliances, cEthernetAccessMIBGroups=cEthernetAccessMIBGroups, ceaConfig=ceaConfig, ceaGlobals=ceaGlobals, ceaMaxNNIPorts=ceaMaxNNIPorts, ceaMaxUNIVlanCommunityPorts=ceaMaxUNIVlanCommunityPorts, ceaPortCapability=ceaPortCapability, ceaPortEntry=ceaPortEntry, ceaPortGroup=ceaPortGroup, ceaPortTable=ceaPortTable, ceaPortType=ceaPortType, ceaUNIVlanEntry=ceaUNIVlanEntry, ceaUNIVlanTable=ceaUNIVlanTable, ceaUNIVlanType=ceaUNIVlanType, ceaVlanGroup=ceaVlanGroup, ciscoEthernetAccessMIB=ciscoEthernetAccessMIB, ciscoEthernetAccessMIBConform=ciscoEthernetAccessMIBConform, ciscoEthernetAccessMIBObjects=ciscoEthernetAccessMIBObjects)
