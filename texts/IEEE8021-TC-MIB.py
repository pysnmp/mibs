#
# PySNMP MIB module IEEE8021-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 14:59:54 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, Bits, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Counter32, org, TimeTicks, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Bits", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Counter32", "org", "TimeTicks", "IpAddress", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ieee8021TcMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 1))
ieee8021TcMib.setRevisions(('2012-02-15 00:00', '2011-08-23 00:00', '2011-04-06 00:00', '2011-02-27 00:00', '2008-11-18 00:00', '2008-10-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021TcMib.setRevisionsDescriptions(('Modified IEEE8021BridgePortType textual convention to\n          include stationFacingBridgePort, \n          uplinkAccessPort, and uplinkRelayPort types.', 'Modified textual conventions  to support the IEEE 802.1\n          MIBs for PBB-TE Infrastructure Protection Switching.', 'Modified textual conventions  to support Remote Customer\n          Service Interfaces.', 'Minor edits to contact information etc. as part of \n          2011 revision of IEEE Std 802.1Q.', 'Added textual conventions needed to support the IEEE 802.1\n          MIBs for PBB-TE.  Additionally, some textual conventions were\n          modified for the same reason.', 'Initial version.',))
if mibBuilder.loadTexts: ieee8021TcMib.setLastUpdated('201202150000Z')
if mibBuilder.loadTexts: ieee8021TcMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021TcMib.setContactInfo('  WG-URL: http://grouper.ieee.org/groups/802/1/index.html\n         WG-EMail: stds-802-1@ieee.org\n\n          Contact: David Levi\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   P.O. Box 1331\n                   Piscataway\n                   NJ 08855-1331\n                   USA\n           E-mail: STDS-802-1-L@LISTSERV.IEEE.ORG\n\n          Contact: Kevin Nolish\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   P.O. Box 1331\n                   Piscataway\n                   NJ 08855-1331\n                   USA\n           E-mail: STDS-802-1-L@LISTSERV.IEEE.ORG')
if mibBuilder.loadTexts: ieee8021TcMib.setDescription('Textual conventions used throughout the various IEEE 802.1 MIB\n         modules.\n\n         Unless otherwise indicated, the references in this MIB\n         module are to IEEE 802.1Q-2011.\n\n         Copyright (C) IEEE.\n         This version of this MIB module is part of IEEE802.1Q;\n         see the draft itself for full legal notices.')
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class IEEE8021PbbComponentIdentifier(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    description = 'The component identifier is used to distinguish between the\n        multiple virtual bridge instances within a PB or PBB.  Each\n        virtual bridge instance is called a component.  In simple\n        situations where there is only a single component the default\n        value is 1.  The component is identified by a component\n        identifier unique within the BEB and by a MAC address unique\n        within the PBBN.  Each component is associated with a Backbone\n        Edge Bridge (BEB) Configuration managed object.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PbbComponentIdentifierOrZero(TextualConvention, Unsigned32):
    reference = '12.3 l)'
    description = "The component identifier is used to distinguish between the\n        multiple virtual bridge instances within a PB or PBB.  In simple\n        situations where there is only a single component the default\n        value is 1.  The component is identified by a component\n        identifier unique within the BEB and by a MAC address unique\n        within the PBBN.  Each component is associated with a Backbone\n        Edge Bridge (BEB) Configuration managed object.\n\n        The special value '0' means 'no component identifier'.  When\n        this TC is used as the SYNTAX of an object, that object must\n        specify the exact meaning for this value."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021PbbServiceIdentifier(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    description = 'The service instance identifier is used at the Customer\n        Backbone Port of a PBB to distinguish a service instance\n        (Local-SID). If the Local-SID field is supported, it is\n        used to perform a bidirectional 1:1 mapping between the\n        Backbone I-SID and the Local-SID. If the Local-SID field\n        is not supported, the Local-SID value is the same as the\n        Backbone I-SID value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 16777214)

class IEEE8021PbbServiceIdentifierOrUnassigned(TextualConvention, Unsigned32):
    reference = '12.16.3, 12.16.5'
    description = 'The service instance identifier is used at the Customer\n        Backbone Port of a PBB to distinguish a service instance\n        (Local-SID). If the Local-SID field is supported, it is\n        used to perform a bidirectional 1:1 mapping between the\n        Backbone I-SID and the Local-SID. If the Local-SID field\n        is not supported, the Local-SID value is the same as the\n        Backbone I-SID value.\n\n        The special value of 1 indicates an unassigned I-SID.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(256, 16777214), )
class IEEE8021PbbIngressEgress(TextualConvention, Bits):
    reference = '12.16.3, 12.16.5, 12.16.6'
    description = 'A 2 bit selector which determines if frames on this VIP may\n        ingress to the PBBN but not egress the PBBN, egress to the\n        PBBN but not ingress the PBBN, or both ingress and egress\n        the PBBN.'
    status = 'current'
    namedValues = NamedValues(("ingress", 0), ("egress", 1))

class IEEE8021PriorityCodePoint(TextualConvention, Integer32):
    reference = '12.6.2.6'
    description = 'Bridge ports may encode or decode the PCP value of the \n        frames that traverse the port. This textual convention \n        names the possible encoding and decoding schemes that\n        the port may use.  The priority and drop_eligible\n        parameters are encoded in the Priority Code Point (PCP)\n        field of the VLAN tag using the Priority Code Point\n        Encoding Table for the Port, and they are decoded from\n        the PCP using the Priority Code Point Decoding Table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("codePoint8p0d", 1), ("codePoint7p1d", 2), ("codePoint6p2d", 3), ("codePoint5p3d", 4))

class IEEE8021BridgePortNumber(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    description = 'An integer that uniquely identifies a bridge port, as\n        specified in 17.3.2.2 of IEEE 802.1ap.\n        This value is used within the spanning tree\n        protocol to identify this port to neighbor bridges.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class IEEE8021BridgePortNumberOrZero(TextualConvention, Unsigned32):
    reference = '17.3.2.2'
    description = 'An integer that uniquely identifies a bridge port, as\n        specified in 17.3.2.2 of IEEE 802.1ap.  The value 0\n        means no port number, and this must be clarified in the\n        DESCRIPTION clause of any object defined using this\n        TEXTUAL-CONVENTION.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IEEE8021BridgePortType(TextualConvention, Integer32):
    reference = '12.16.1.1.3 h4), 12.16.2.1/2,\n                 12.13.1.1, 12.13.1.2, 12.15.2.1, 12.15.2.2'
    description = "A port type.  The possible port types are:\n\n             customerVlanPort(2) - Indicates a port is a C-tag\n                 aware port of an enterprise VLAN aware bridge.\n\n             providerNetworkPort(3) - Indicates a port is an S-tag\n                 aware port of a Provider Bridge or Backbone Edge\n                 Bridge used for connections within a PBN or PBBN.\n\n             customerNetworkPort(4) - Indicates a port is an S-tag\n                 aware port of a Provider Bridge or Backbone Edge\n                 Bridge used for connections to the exterior of a\n                 PBN or PBBN.\n\n             customerEdgePort(5) - Indicates a port is a C-tag\n                 aware port of a Provider Bridge used for connections\n                 to the exterior of a PBN or PBBN.\n\n             customerBackbonePort(6) - Indicates a port is a I-tag\n                 aware port of a Backbone Edge Bridge's B-component.\n\n             virtualInstancePort(7) - Indicates a port is a virtual\n                 S-tag aware port within a Backbone Edge Bridge's\n                 I-component which is responsible for handling\n                 S-tagged traffic for a specific backbone service\n                 instance.\n\n             dBridgePort(8) - Indicates a port is a VLAN-unaware\n                 member of an 802.1D bridge.\n\n             remoteCustomerAccessPort (9) - Indicates a port is an\n                 S-tag aware port of a Provider Bridge used for\n                 connections to remote customer interface LANs\n                 through another PBN.\n                 \n             stationFacingBridgePort (10) - Indicates a port of a\n                 Bridge that supports the EVB status parameters\n                 (6.6.5) with an EVBMode parameter value of\n                 EVB Bridge.\n                 \n             uplinkAccessPort (11) - Indicates a port on a\n                 Port-mapping S-VLAN component that connects an EVB\n                 Bridge with an EVB station.             \n                 \n             uplinkRelayPort (12) - Indicates a port of an edge relay\n                 that supports the EVB status parameters (6.6.5)\n                 with an EVBMode parameter value of EVB station."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 1), ("customerVlanPort", 2), ("providerNetworkPort", 3), ("customerNetworkPort", 4), ("customerEdgePort", 5), ("customerBackbonePort", 6), ("virtualInstancePort", 7), ("dBridgePort", 8), ("remoteCustomerAccessPort", 9), ("stationFacingBridgePort", 10), ("uplinkAccessPort", 11), ("uplinkRelayPort", 12))

class IEEE8021VlanIndex(TextualConvention, Unsigned32):
    reference = '9.6'
    description = 'A value used to index per-VLAN tables: values of 0 and\n        4095 are not permitted.  If the value is between 1 and\n        4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with\n        global scope within a given bridged domain (see VlanId\n        textual convention).  If the value is greater than 4095,\n        then it represents a VLAN with scope local to the\n        particular agent, i.e., one without a global VLAN-ID\n        assigned to it.  Such VLANs are outside the scope of\n        IEEE 802.1Q, but it is convenient to be able to manage them\n        in the same way using this MIB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 4094), ValueRangeConstraint(4096, 4294967295), )
class IEEE8021VlanIndexOrWildcard(TextualConvention, Unsigned32):
    reference = '9.6'
    description = "A value used to index per-VLAN tables.  The value 0 is not\n        permitted, while the value 4095 represents a 'wildcard'\n        value.  An object whose SYNTAX is IEEE8021VlanIndexOrWildcard\n        must specify in its DESCRIPTION the specific meaning of the\n        wildcard value.  If the value is between 1 and\n        4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with\n        global scope within a given bridged domain (see VlanId\n        textual convention).  If the value is greater than 4095,\n        then it represents a VLAN with scope local to the\n        particular agent, i.e., one without a global VLAN-ID\n        assigned to it.  Such VLANs are outside the scope of\n        IEEE 802.1Q, but it is convenient to be able to manage them\n        in the same way using this MIB."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021MstIdentifier(TextualConvention, Unsigned32):
    description = 'In an MSTP Bridge, an MSTID, i.e., a value used to identify\n        a spanning tree (or MST) instance.  In the PBB-TE environment\n        the value 4094 is used to identify VIDs managed by the PBB-TE\n        procedures.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4094)

class IEEE8021ServiceSelectorType(TextualConvention, Integer32):
    description = 'A value that represents a type (and thereby the format)\n        of a IEEE8021ServiceSelectorValue.  The value can be one of\n        the following:\n\n        ieeeReserved(0)   Reserved for definition by IEEE 802.1\n                          recommend to not use zero unless\n                          absolutely needed.\n        vlanId(1)         12-Bit identifier as described in IEEE802.1Q.\n        isid(2)           24-Bit identifier as described in IEEE802.1ah.\n        tesid(3)          32 Bit identifier as described below.\n        segid(4)          32 Bit identifier as described below.\n        ieeeReserved(xx)  Reserved for definition by IEEE 802.1\n                          xx values can be [5..7].\n\n        To support future extensions, the IEEE8021ServiceSelectorType\n        textual convention SHOULD NOT be sub-typed in object type\n        definitions.  It MAY be sub-typed in compliance statements in\n        order to require only a subset of these address types for a\n        compliant implementation.\n\n        The tesid is used as a service selector for MAs that are present\n        in bridges that implement PBB-TE functionality.  A selector of\n        this type is interpreted as a 32 bit unsigned value of type\n        IEEE8021PbbTeTSidId.  This type is used to index the\n        Ieee8021PbbTeTeSidTable to find the ESPs which comprise the TE\n        Service Instance named by this TE-SID value.\n        \n        The segid is used as a service selector for MAs that are present\n        in bridges that implement IPS functionality.  A selector of\n        this type is interpreted as a 32 bit unsigned value of type\n        IEEE8021TeipsSegid.  This type is used to index the\n        Ieee8021TeipsSegTable to find the SMPs which comprise the\n        Infrastructure Segment named by this segid value.\n\n        Implementations MUST ensure that IEEE8021ServiceSelectorType\n        objects and any dependent objects (e.g.,\n        IEEE8021ServiceSelectorValue objects) are consistent.  An\n        inconsistentValue error MUST be generated if an attempt to\n        change an IEEE8021ServiceSelectorType object would, for\n        example, lead to an undefined IEEE8021ServiceSelectorValue value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("vlanId", 1), ("isid", 2), ("tesid", 3), ("segid", 4))

class IEEE8021ServiceSelectorValueOrNone(TextualConvention, Unsigned32):
    description = "An integer that uniquely identifies a generic MAC service,\n         or none.  Examples of service selectors are a VLAN-ID\n         (IEEE 802.1Q) and an I-SID (IEEE 802.1ah).\n\n         An IEEE8021ServiceSelectorValueOrNone value is always\n         interpreted within the context of an\n         IEEE8021ServiceSelectorType value.  Every usage of the\n         IEEE8021ServiceSelectorValueOrNone textual convention is\n         required to specify the IEEE8021ServiceSelectorType object\n         that provides the context.  It is suggested that the\n         IEEE8021ServiceSelectorType object be logically registered\n         before the object(s) that use the\n         IEEE8021ServiceSelectorValueOrNone textual convention, if\n         they appear in the same logical row.\n\n         The value of an IEEE8021ServiceSelectorValueOrNone object\n         must always be consistent with the value of the associated\n         IEEE8021ServiceSelectorType object.  Attempts to set an\n         IEEE8021ServiceSelectorValueOrNone object to a value\n         inconsistent with the associated\n         IEEE8021ServiceSelectorType must fail with an\n         inconsistentValue error.\n\n         The special value of zero is used to indicate that no\n         service selector is present or used.  This can be used in\n         any situation where an object or a table entry MUST either\n         refer to a specific service, or not make a selection.\n\n         Note that a MIB object that is defined using this\n         TEXTUAL-CONVENTION SHOULD clarify the meaning of\n         'no service' (i.e., the special value 0), as well as the\n         maximum value (i.e., 4094, for a VLAN ID)."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class IEEE8021ServiceSelectorValue(TextualConvention, Unsigned32):
    description = 'An integer that uniquely identifies a generic MAC service.\n         Examples of service selectors are a VLAN-ID (IEEE 802.1Q)\n         and an I-SID (IEEE 802.1ah).\n\n         An IEEE8021ServiceSelectorValue value is always interpreted\n         within the context of an IEEE8021ServiceSelectorType value.\n         Every usage of the IEEE8021ServiceSelectorValue textual\n         convention is required to specify the\n         IEEE8021ServiceSelectorType object that provides the context.\n         It is suggested that the IEEE8021ServiceSelectorType object\n         be logically registered before the object(s) that use the\n         IEEE8021ServiceSelectorValue textual convention, if they\n         appear in the same logical row.\n\n         The value of an IEEE8021ServiceSelectorValue object must\n         always be consistent with the value of the associated\n         IEEE8021ServiceSelectorType object.  Attempts to set an\n         IEEE8021ServiceSelectorValue object to a value inconsistent\n         with the associated IEEE8021ServiceSelectorType must fail\n         with an inconsistentValue error.\n\n         Note that a MIB object that is defined using this\n         TEXTUAL-CONVENTION SHOULD clarify the\n         maximum value (i.e., 4094, for a VLAN ID).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class IEEE8021PortAcceptableFrameTypes(TextualConvention, Integer32):
    reference = '12.10.1.3, 12.13.3.3, 12.13.3.4'
    description = 'Acceptable frame types on a port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("admitAll", 1), ("admitUntaggedAndPriority", 2), ("admitTagged", 3))

class IEEE8021PriorityValue(TextualConvention, Unsigned32):
    reference = '12.13.3.3'
    description = 'An 802.1Q user priority value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE8021PbbTeProtectionGroupId(TextualConvention, Unsigned32):
    reference = '12.19.2'
    description = 'The PbbTeProtectionGroupId identifier is used to distinguish \n         protection group instances present in the B Component of\n         an IB-BEB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021PbbTeEsp(TextualConvention, OctetString):
    reference = '802.1Qay 3.2'
    description = 'This textual convention is used to represent the logical\n        components that comprise the 3-tuple that identifies an\n        Ethernet Switched Path.  The 3-tuple consists of a\n        destination MAC address, a source MAC address and a VID.\n        Bytes (1..6) of this textual convention contain the\n        ESP-MAC-DA, bytes (7..12) contain the ESP-MAC-SA, and bytes\n        (13..14) contain the ESP-VID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021PbbTeTSidId(TextualConvention, Unsigned32):
    reference = '802.1Qay 3.11'
    description = 'This textual convention is used to represent an identifier\n        that refers to a TE Service Instance.  Note that, internally\n        a TE-SID is implementation dependent.  This textual convention\n        defines the external representation of TE-SID values.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021PbbTeProtectionGroupConfigAdmin(TextualConvention, Integer32):
    reference = '26.10.3.3.5\n               26.10.3.3.6\n               26.10.3.3.7\n               12.19.2.3.2'
    description = 'This textual convention is used to represent administrative\n        commands that can be issued to a protection group.  The value\n        noAdmin(1) is used to indicate that no administrative action\n        is to be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021PbbTeProtectionGroupActiveRequests(TextualConvention, Integer32):
    reference = '12.19.2.1.3 d)'
    description = 'This textual convention is used to represent the status of\n        active requests within a protection group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

class IEEE8021TeipsIpgid(TextualConvention, Unsigned32):
    reference = '12.24.1.1.3 a)'
    description = 'The TEIPS IPG identifier is used to distinguish \n         IPG instances present in a PBB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 429467295)

class IEEE8021TeipsSegid(TextualConvention, Unsigned32):
    reference = '26.11.1'
    description = 'This textual convention is used to represent an\n        identifier that refers to an Infrastructure Segment.\n        Note that, internally a SEG-ID implementation\n        dependent.  This textual convention defines the\n        external representation of SEG-ID values.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 42947295)

class IEEE8021TeipsSmpid(TextualConvention, OctetString):
    reference = '26.11.1'
    description = 'This textual convention is used to represent the logical\n        components that comprise the 3-tuple that identifies a\n        Segment Monitoring Path (SMP).  The 3-tuple consists of a\n        destination MAC address, a source MAC address and a VID.\n        Bytes (1..6) of this textual convention contain the\n        SMP-MAC-DA, bytes (7..12) contain the SMP-MAC-SA, and bytes\n        (13..14) contain the SMP-VID.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(14, 14)
    fixedLength = 14

class IEEE8021TeipsIpgConfigAdmin(TextualConvention, Integer32):
    reference = '12.24.2.1.3 h)'
    description = 'This textual convention is used to represent administrative\n        commands that can be issued to an IPG.  The value\n        clear(1) is used to indicate that no administrative action\n        is to be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("lockOutProtection", 2), ("forceSwitch", 3), ("manualSwitchToProtection", 4), ("manualSwitchToWorking", 5))

class IEEE8021TeipsIpgConfigActiveRequests(TextualConvention, Integer32):
    reference = '12.24.2.1.3 d)'
    description = 'This textual convention is used to represent the status of\n        active requests within an IPG.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noRequest", 1), ("loP", 2), ("fs", 3), ("pSFH", 4), ("wSFH", 5), ("manualSwitchToProtection", 6), ("manualSwitchToWorking", 7))

mibBuilder.exportSymbols("IEEE8021-TC-MIB", IEEE8021PriorityValue=IEEE8021PriorityValue, IEEE8021ServiceSelectorValue=IEEE8021ServiceSelectorValue, IEEE8021PriorityCodePoint=IEEE8021PriorityCodePoint, IEEE8021ServiceSelectorValueOrNone=IEEE8021ServiceSelectorValueOrNone, IEEE8021VlanIndexOrWildcard=IEEE8021VlanIndexOrWildcard, ieee8021TcMib=ieee8021TcMib, IEEE8021PbbServiceIdentifier=IEEE8021PbbServiceIdentifier, IEEE8021TeipsIpgConfigActiveRequests=IEEE8021TeipsIpgConfigActiveRequests, IEEE8021BridgePortNumber=IEEE8021BridgePortNumber, IEEE8021VlanIndex=IEEE8021VlanIndex, ieee802dot1mibs=ieee802dot1mibs, IEEE8021PbbComponentIdentifierOrZero=IEEE8021PbbComponentIdentifierOrZero, PYSNMP_MODULE_ID=ieee8021TcMib, IEEE8021PbbComponentIdentifier=IEEE8021PbbComponentIdentifier, IEEE8021PbbTeProtectionGroupId=IEEE8021PbbTeProtectionGroupId, IEEE8021BridgePortNumberOrZero=IEEE8021BridgePortNumberOrZero, IEEE8021PbbTeTSidId=IEEE8021PbbTeTSidId, IEEE8021TeipsIpgid=IEEE8021TeipsIpgid, IEEE8021BridgePortType=IEEE8021BridgePortType, IEEE8021TeipsSegid=IEEE8021TeipsSegid, IEEE8021PbbTeProtectionGroupActiveRequests=IEEE8021PbbTeProtectionGroupActiveRequests, IEEE8021TeipsIpgConfigAdmin=IEEE8021TeipsIpgConfigAdmin, IEEE8021PbbServiceIdentifierOrUnassigned=IEEE8021PbbServiceIdentifierOrUnassigned, IEEE8021PortAcceptableFrameTypes=IEEE8021PortAcceptableFrameTypes, IEEE8021ServiceSelectorType=IEEE8021ServiceSelectorType, IEEE8021TeipsSmpid=IEEE8021TeipsSmpid, IEEE8021MstIdentifier=IEEE8021MstIdentifier, IEEE8021PbbTeEsp=IEEE8021PbbTeEsp, IEEE8021PbbTeProtectionGroupConfigAdmin=IEEE8021PbbTeProtectionGroupConfigAdmin, IEEE8021PbbIngressEgress=IEEE8021PbbIngressEgress)
