#
# PySNMP MIB module CISCO-SUBSCRIBER-IDENTITY-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SUBSCRIBER-IDENTITY-TC-MIB
# Source digest sha256:817bcc66406cdea36a819ac669d13b48361d07509e10375f6c1e229c76051c9b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberIdentityTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 782))
ciscoSubscriberIdentityTcMIB.setRevisions(('2011-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setLastUpdated('2011-12-23 00:00')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setDescription('This MIB module defines textual conventions describing\n        subscriber session identities.  A subscriber session identity\n        consists of data associated with a subscriber session serving as\n        credentials used to determine authority, status, rights, or\n        entitlement to privileges.')
class SubSessionIdentity(TextualConvention, Integer32):
    description = "An enumerated integer-value describing a subscriber session\n        identity:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the subscriber session\n                identity.\n\n            'ifIndex'\n                The ifIndex assigned to the interface representing the\n                subscriber session.\n\n            'subscriberLabel'\n                The arbitrary integer-value assigned by the system\n                to uniquely identify the subscriber session within the\n                scope of the system.\n\n            'macAddress'\n                The subscriber's MAC address.\n\n            'nativeVrf'\n                The name of the VRF on which the subscriber session\n                originates.\n\n            'nativeIpAddress'\n                The IP address assigned to the subscriber session on\n        the\n                customer-facing side of the system.\n\n            'domainVrf'\n                The name of the VRF to which the system transfers the\n                subscriber session traffic.\n\n            'domainIpAddress'\n                The IP address assigned to the subscriber session on\n        the\n                service-facing side of the system.\n\n            'pbhk'\n                The Port-Bundle Host Key (PBHK) uniquely identifying\n        the\n                subscriber session.  A PBHK consists of a source IP\n                address and a TCP port number.\n\n            'remoteId'\n                The name identifying the 'calling station', access\n                multiplexor, or access switch providing access to the\n                subscriber.\n\n            'circuitId'\n                The name identifying the circuit on the 'calling\n                station', access multiplexor, or access switch that\n                provides access to the subscriber.\n\n            'nasPort'\n                An octet string identifying the port on the Network\n                Access Server (NAS) that provides access to the\n                subscriber.\n\n            'domain'\n                The subscriber's domain name.\n\n            'username'\n                The subscriber's username.\n\n            'acctSessionId'\n                The subscriber's accounting session identifier.\n\n            'dnis'\n                The Dialed Number Identification Service (DNIS) number\n                (or called-party number) dialed by the subscriber.\n\n            'media'\n                The type of media providing access to the subscriber.\n\n            'mlpNegotiated'\n                Indicates whether the subscriber session was\n        established\n                using multi-link PPP negotiation.\n\n            'protocol'\n                The type of protocol providing access to the\n        subscriber.\n\n            'dhcpClass'\n                The name of the class matching the DHCP DISCOVER\n        message\n                received from the subscriber.\n\n            'serviceName'\n                The name identifying the service associated with the\n                subscriber.\n             'tunnelName'\n                 The name of the VPDN used to carry the subscriber\n                 session."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("ifIndex", 2), ("subscriberLabel", 3), ("macAddress", 4), ("nativeVrf", 5), ("nativeIpAddress", 6), ("domainVrf", 7), ("domainIpAddress", 8), ("pbhk", 9), ("remoteId", 10), ("circuitId", 11), ("nasPort", 12), ("domain", 13), ("username", 14), ("acctSessionId", 15), ("dnis", 16), ("media", 17), ("mlpNegotiated", 18), ("protocol", 19), ("serviceName", 20), ("dhcpClass", 21), ("tunnelName", 22))

class SubSessionIdentities(TextualConvention, Bits):
    description = "A bit string describing a set of subscriber session identities:\n\n        'ifIndex'\n            The ifIndex assigned to the interface representing the\n            subscriber session.\n\n        'subscriberLabel'\n            The arbitrary integer-value assigned by the system\n            to uniquely identify the subscriber session within the\n            scope of the system.\n\n        'macAddress'\n            The subscriber's MAC address.\n\n        'nativeVrf'\n            The name of the VRF on which the subscriber session\n            originates.\n\n        'nativeIpAddress'\n            The IP address assigned to the subscriber session on the\n            customer-facing side of the system.\n\n        'domainVrf'\n            The name of the VRF to which the system transfers the\n            subscriber session traffic.\n\n        'domainIpAddress'\n            The IP address assigned to the subscriber session on the\n            service-facing side of the system.\n\n        'pbhk'\n            The Port-Bundle Host Key (PBHK) uniquely identifying the\n            subscriber session.  A PBHK consists of a source IP\n            address and a TCP port number.\n\n        'remoteId'\n            The name identifying the 'calling station' or access\n            multiplexor providing access to the subscriber.\n\n        'circuitId'\n            The name identifying the circuit on the 'calling\n            station', access multiplexor, or access switch that\n            provides access to the subscriber.\n\n        'nasPort'\n            An octet string identifying the port on the Network\n            Access Server (NAS) that provides access to the\n            subscriber.\n\n        'domain'\n            The subscriber's domain name.\n\n        'username'\n            The subscriber's username.\n\n        'dnis'\n            The Dialed Number Identification Service (DNIS) number\n            (or called-party number) dialed by the subscriber.\n\n        'acctSessionId'\n            The subscriber's accounting session identifier.\n\n        'media'\n            The type of media providing access to the subscriber.\n\n        'mlpNegotiated'\n            Indicates whether the subscriber session was established\n            using multi-link PPP negotiation.\n\n        'protocol'\n            The type of protocol providing access to the subscriber.\n\n        'serviceName'\n            The name identifying the service associated with the\n            subscriber.\n\n        'dhcpClass'\n            The name of the class matching the DHCP DISCOVER message\n            received from the subscriber.\n\n        'tunnelName'\n            The name of the VPDN used to carry the subscriber\n            session."
    status = 'current'
    namedValues = NamedValues(("ifIndex", 0), ("subscriberLabel", 1), ("macAddress", 2), ("nativeVrf", 3), ("nativeIpAddress", 4), ("domainVrf", 5), ("domainIpAddress", 6), ("pbhk", 7), ("remoteId", 8), ("circuitId", 9), ("nasPort", 10), ("domain", 11), ("username", 12), ("acctSessionId", 13), ("dnis", 14), ("media", 15), ("mlpNegotiated", 16), ("protocol", 17), ("serviceName", 18), ("dhcpClass", 19), ("tunnelName", 20))

class SubscriberLabel(TextualConvention, Unsigned32):
    description = "A positive integer-value uniquely identifying a subscriber\n        session within the scope of a system.\n\n        The value '0' is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberVRF(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value identifying a VRF associated with a subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberPbhk(TextualConvention, OctetString):
    description = "An octet string specifying a Port-Bundle Host Key (PBHK)\n        identifying a subscriber.  The octet string has the following\n        format:\n\n            Octets  Field\n            ------------------------------\n            1-4     subscriber IP address\n            5-6     TCP port number\n\n        Observe that the subscriber IP address is always an IPv4\n        address.\n\n        The value '000000'H is not a valid value.  However, it serves as\n        a convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SubscriberRemoteId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = "A string-value identifying the 'calling station', access\n        multiplexor, or access switch providing access to a subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberCircuitId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = "A string-value identifying the circuit on the 'calling\n        station', access multiplexor, or access switch that provides\n        access to the subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberNasPort(TextualConvention, OctetString):
    description = "An octet string identifying port on the Network Access Server\n        (NAS) that provides access to the subscriber.\n\n        The value '000000'H is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SubscriberDomain(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the domain associated with a\n        subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberUsername(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the username identifying a\n        subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberAcctSessionId(TextualConvention, Unsigned32):
    description = "An positive, integer-value specifying the accounting session ID\n        assigned to a subscriber.\n\n        The value '0' is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberDnis(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the Dialed Number Identification\n        Service (DNIS) number (or called-party number) dialed by a\n        subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberMediaType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of media\n        providing access to the subscriber:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the type of media\n                providing access to the subscriber.\n\n            'async'\n                An asynchronous serial line provides access to the\n                subscriber.\n\n            'atm'\n                An ATM network provides access to the subscriber.\n\n            'ethernet'\n                An Ethernet-based network provides access to the\n                subscriber.\n\n            'ip'\n                An IP network provides access to the subscriber.\n\n            'isdn'\n                An ISDN line provides access to the subscriber.\n\n            'mpls'\n                An MPLS network provides access to the subscriber.\n\n            'sync'\n                A synchronous serial line provides access to the\n                subscriber.\n\n        The value 'other' cannot be written to an instance of an object.\n        However, it serves as a convenient value when an instance of an\n        object using this textual convention is not valid."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("async", 2), ("atm", 3), ("ethernet", 4), ("ip", 5), ("isdn", 6), ("mpls", 7), ("sync", 8))

class SubscriberProtocolType(TextualConvention, Integer32):
    description = "An enumerated integer-value describing the type of protocol\n        providing access to the subscriber:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the type of protocol\n                providing access to the subscriber.\n\n            'atom'\n                Any Transport over MPLS (AToM) provides access to the\n                subscriber.\n\n            'ip'\n                The Internet Protocol (IP) provides access to the\n                subscriber.\n\n            'psdn'\n                A Public Switched Data Network (PSDN) provides access to\n                the subscriber.\n\n            'ppp'\n                The Point-to-Point Protocol (PPP) provides access to the\n                subscriber.\n\n            'vpdn'\n                A Virtual Private Data Network (VPDN) provides access to\n                the subscriber.\n\n        The value 'other' cannot be written to an instance of an object.\n        However, it serves as a convenient value when an instance of an\n        object using this textual convention is not valid."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("atom", 2), ("ip", 3), ("psdn", 4), ("ppp", 5), ("vpdn", 6))

class SubscriberDhcpClass(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the name of the class matching the\n        DHCP DISCOVER message received from the subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberTunnelName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = "A string-value specifying the name of the VPDN used to carry\n        a subscriber's session.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberLocationName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the location associated with a\n        subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberServiceName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = 'A string-value specifying the subscriber service associated\n        with a subscriber.\n\n        The semantics of the string-value are the same those specified\n        by the SnmpAdminString textual convention defined by the\n        SNMP-FRAMEWORK-MIB (RFC-3411).\n\n        The null string is not a valid value.  However, it serves as a\n        convenient value when an instance of an object using this\n        textual convention is not valid.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-IDENTITY-TC-MIB", PYSNMP_MODULE_ID=ciscoSubscriberIdentityTcMIB, SubSessionIdentities=SubSessionIdentities, SubSessionIdentity=SubSessionIdentity, SubscriberAcctSessionId=SubscriberAcctSessionId, SubscriberCircuitId=SubscriberCircuitId, SubscriberDhcpClass=SubscriberDhcpClass, SubscriberDnis=SubscriberDnis, SubscriberDomain=SubscriberDomain, SubscriberLabel=SubscriberLabel, SubscriberLocationName=SubscriberLocationName, SubscriberMediaType=SubscriberMediaType, SubscriberNasPort=SubscriberNasPort, SubscriberPbhk=SubscriberPbhk, SubscriberProtocolType=SubscriberProtocolType, SubscriberRemoteId=SubscriberRemoteId, SubscriberServiceName=SubscriberServiceName, SubscriberTunnelName=SubscriberTunnelName, SubscriberUsername=SubscriberUsername, SubscriberVRF=SubscriberVRF, ciscoSubscriberIdentityTcMIB=ciscoSubscriberIdentityTcMIB)
