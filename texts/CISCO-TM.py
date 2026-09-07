#
# PySNMP MIB module CISCO-TM (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TM
# Source digest sha256:74f1ee4c4647e0bb2bf98441dc6cdad231de900373ad05b8795cedff8ab00448
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDomains, = mibBuilder.importSymbols("CISCO-SMI", "ciscoDomains")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTransportMappings = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1))
ciscoTransportMappings.setRevisions(('2001-08-23 16:00', '2000-06-21 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTransportMappings.setRevisionsDescriptions(('Added Cisco Networking Services (CNS) Transport\n\t\tdomain and identifier.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTransportMappings.setLastUpdated('2001-08-23 16:00')
if mibBuilder.loadTexts: ciscoTransportMappings.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTransportMappings.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTransportMappings.setDescription('Extension of SNMPv2-TM MIB')
snmpUDPVPNDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 1))
if mibBuilder.loadTexts: snmpUDPVPNDomain.setStatus('current')
if mibBuilder.loadTexts: snmpUDPVPNDomain.setDescription("This transport domain is used to specify that particular\n            SNMP messages are to be sent/received over a particular\n            Virtual Private Network (VPN), implemented using MPLS\n            (Multiprotocol Label Switching).  The corresponding\n            transport address is of type SnmpUDPVPNAddress.\n\n            A VPN is defined as a set of sites with a common\n            community of interest.  Sites within an MPLS-based VPN\n            often have private addresses which aren't accessible from\n            outside of the VPN, and may be duplicates of private\n            addresses used in other VPNs.  To uniquely identify such\n            a private address, it must be associated with a\n            particular VPN routing/forwarding instance, also known as\n            a VRF (VPN Routing and Forwarding table).")
if mibBuilder.loadTexts: snmpUDPVPNDomain.setReference('RFC 2547: BGP/MPLS VPNs')
class SnmpUDPVPNAddress(TextualConvention, OctetString):
    description = 'Represents a UDP VPN address:\n\n             octets     contents            encoding\n              1-4       IP-address          network-byte order\n              5-6       UDP-port            network-byte order\n              7..38     VRF name            string of (up to 32) octets\n            IP address and port numbers should be represented in \n            binary format.  String must contain printable characters.'
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 38)

snmpAAL5Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 2))
if mibBuilder.loadTexts: snmpAAL5Domain.setStatus('current')
if mibBuilder.loadTexts: snmpAAL5Domain.setDescription('This transport domain is used to specify that particular\n            SNMP messages are to be sent/received over AAL5 transport.\n            The corresponding transport address is of type \n            SnmpAAL5VCIdentifier.\n\n            An ATM VCC referenced by a SnmpAAL5VCIdentifier must be\n            used only for SNMP packets, and not for any other kind \n            of packets. \n\n            Care must be taken with the use of this domain because its\n            associated transport address, SnmpAAL5VCIdentifier, \n            contains identifiers which only have local and temporal \n            uniqueness: ifIndex, VPI, VCI.\n\n            Use of this transport mapping is not recommended, except \n            in circumstances where an IP address is not available \n            and thus a mapping over UDP, such as snmpUDPDomain, \n            can not be used.')
class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    description = 'Represents a AAL5 VCC:\n\n               octets       contents             encoding\n                1-4         ifIndex              network_byte order\n                5-8         vpi                  network-byte order\n                9-12        vci                  network-byte order\n             ifIndex, vpi and vci should be represented in binary\n             format.            \n             \n             ifIndex specifies the value of the ifIndex object\n             associated with the interface supporting the VCC.\n             vpi specifies the value of the VPI (Virtual Path\n             Identifier) associated with the VCC.\n             vci specifies the value of the VCI (Virtual Channel\n             Identifier) associated with the VCC.'
    status = 'current'
    displayHint = '4d/4d/4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

snmpCNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 3))
if mibBuilder.loadTexts: snmpCNSDomain.setStatus('current')
if mibBuilder.loadTexts: snmpCNSDomain.setDescription('This transport domain is used for transporting\n             SNMP messages over the CNS Event Service. The\n             corresponding transport addresses are of type\n             SnmpCNSIdentifier.\n\n             CNS Event service is an event based transport\n             mechanism. Events are published by producers\n             on particular subjects. Consumers listening\n             for these subjects receive the events.\n\n             Point to point communication is provided on\n             the CNS Event Service by the use of Name Space\n             Mapper Service that uses the device-id, appended \n             at the end of the subject, to locate a specific\n             target.\n\n             An Event Agent subject used by a SnmpCNSIdentifier \n             must be used only for SNMP events, and not for \n             any other kind of events.\n\n             Use of this transport mapping is not recommended, except \n             in circumstances where an IP address is not available \n             and thus a mapping over UDP, such as snmpUDPDomain, \n             can not be used.')
class SnmpCNSIdentifier(TextualConvention, OctetString):
    description = "Represents the address that identifies targets\n             in the CNS Event Service Transport mapping.\n\n              octets       contents             encoding\n              1-19       service-field   string of (19) octets   \n              20-274     device-id       string of (upto 255) octets \n\n             service-field specifies the type of service \n             (request, response or notifications) and has a fixed \n             length of 19 octets. It also serves the purpose of \n             distinguishing SNMP Message events from other CNS Events.\n\n             device-id uniquely identifies devices subscribed to\n             the CNS Event Service Bus. device-id may be same\n             as the hostname for the device.\n\n             The device-id must be separated from the service-field by \n             a '.'. If the device-id is omitted, SnmpCNSIdentifier\n             would contain just the fixed-length (19 octets)\n             service-field.\n\n             Thus target addresses are CNS Event subjects of the\n             form: <service-field>.<device-id>"
    status = 'current'
    displayHint = '19a.255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 274)

mibBuilder.exportSymbols("CISCO-TM", PYSNMP_MODULE_ID=ciscoTransportMappings, SnmpAAL5VCIdentifier=SnmpAAL5VCIdentifier, SnmpCNSIdentifier=SnmpCNSIdentifier, SnmpUDPVPNAddress=SnmpUDPVPNAddress, ciscoTransportMappings=ciscoTransportMappings, snmpAAL5Domain=snmpAAL5Domain, snmpCNSDomain=snmpCNSDomain, snmpUDPVPNDomain=snmpUDPVPNDomain)
