#
# PySNMP MIB module CISCO-MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MPLS-TC-EXT-STD-MIB
# Source digest sha256:86a0d46ff971fb4a119673d008c788a222e46e2b68882608cf3b9ab596c581c3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 144))
cmplsTcExtStdMIB.setRevisions(('2012-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsTcExtStdMIB.setRevisionsDescriptions(('MPLS Textual Convention Extensions',))
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setLastUpdated('2012-02-22 00:00')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setContactInfo('Venkatesan Mahalingam\n            Dell Inc,\n            350 Holger way, San Jose, CA, USA\n            Email: venkat.mahalingams@gmail.com\n\n            Kannan KV Sampath\n            Aricent,\n            India\n            Email: Kannan.Sampath@aricent.com\n\n            Sam Aldrin\n            Huawei Technologies\n            2330 Central Express Way,\n            Santa Clara, CA 95051, USA\n            Email:  aldrin.ietf@gmail.com\n\n            Thomas D. Nadeau\n            CA Technologies\n            273 Corporate Drive, Portsmouth, NH, USA\n            Email: thomas.nadeau@ca.com')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified\n        as the document authors.  All rights reserved.\n\n        This MIB module contains Textual Conventions for\n        MPLS based transport networks.')
class CMplsGlobalId(TextualConvention, OctetString):
    description = "This object contains the Textual Convention of IP based\n        operator unique identifier (Global_ID), the Global_ID can\n        contain the 2-octet or 4-octet value of the operator's\n        Autonomous System Number (ASN).\n\n        It is expected that the Global_ID will be derived from\n        the globally unique ASN of the autonomous system hosting\n        the PEs containing the actual AIIs.\n        The presence of a Global_ID based on the operator's\n        ASN ensures that the AII will be globally unique.\n\n        When the Global_ID is derived from a 2-octet AS number,\n\n\n\n        the two high-order octets of this 4-octet identifier\n        MUST be set to zero.\n        Further ASN 0 is reserved.  A Global_ID of zero means\n        that no Global_ID is present.  Note that a Global_ID of\n        zero is limited to entities contained within a single\n        operator and MUST NOT be used across an NNI.\n        A non-zero Global_ID MUST be derived from an ASN owned by\n        the operator."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CMplsNodeId(TextualConvention, Unsigned32):
    description = "The Node_ID is assigned within the scope of the Global_ID.\n        The value 0(or 0.0.0.0 in dotted decimal notation) is\n        reserved and MUST NOT be used.\n\n        When IPv4 addresses are in use, the value of this object\n        can be derived from the LSR's /32 IPv4 loop back address.\n        When IPv6 addresses are in use, the value of this object\n        can be a 32-bit value unique within the scope of\n        a Global_ID.\n\n        Note that, when IP reach ability is not needed, the 32-bit\n        Node_ID is not required to have any association\n        with the IPv4 address space."
    status = 'current'
    displayHint = 'd'

class CMplsIccId(TextualConvention, OctetString):
    description = 'The ICC is a string of one to six characters, each\n        character being either alphabetic (i.e.  A-Z) or\n        numeric (i.e. 0-9) characters.\n        Alphabetic characters in the ICC SHOULD be represented\n\n        with upper case letters.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 6)

class CMplsLocalId(TextualConvention, Unsigned32):
    description = "This textual convention is used in accommodating the bigger\n        size Global_Node_ID and/or ICC with lower size LSR\n        identifier in order to index the mplsTunnelTable.\n\n        The Local Identifier is configured between 1 and 16777215,\n        as valid IP address range starts from 16777216(01.00.00.00).\n        This range is chosen to identify the mplsTunnelTable's\n        Ingress/Egress LSR-id is IP address or Local identifier,\n        if the configured range is not IP address, administrator is\n        expected to retrieve the complete information\n        (Global_Node_ID or ICC) from mplsNodeConfigTable. This way,\n        existing mplsTunnelTable is reused for bidirectional tunnel\n        extensions for MPLS based transport networks.\n\n        This Local Identifier allows the administrator to assign\n        a unique identifier to map Global_Node_ID and/or ICC."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16777215)

mibBuilder.exportSymbols("CISCO-MPLS-TC-EXT-STD-MIB", CMplsGlobalId=CMplsGlobalId, CMplsIccId=CMplsIccId, CMplsLocalId=CMplsLocalId, CMplsNodeId=CMplsNodeId, PYSNMP_MODULE_ID=cmplsTcExtStdMIB, cmplsTcExtStdMIB=cmplsTcExtStdMIB)
