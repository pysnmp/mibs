#
# PySNMP MIB module MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-TC-EXT-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:53 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, NotificationType, ObjectIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter32, Gauge32, MibIdentifier, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter32", "Gauge32", "MibIdentifier", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 17))
mplsTcExtStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTcExtStdMIB.setRevisionsDescriptions(('MPLS Textual Convention Extensions',))
if mibBuilder.loadTexts: mplsTcExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setContactInfo('\n             Venkatesan Mahalingam\n             Dell Inc,\n             5450 Great America Parkway,\n             Santa Clara, CA 95054, USA\n       Email: venkat.mahalingams@gmail.com\n\n             Kannan KV Sampath\n             Redeem,\n             India\n       Email: kannankvs@gmail.com\n\n             Sam Aldrin\n             Huawei Technologies\n             2330 Central Express Way,\n             Santa Clara, CA 95051, USA\n       Email:  aldrin.ietf@gmail.com\n\n             Thomas D. Nadeau\n       Email: tnadeau@lucidvision.com\n      ')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setDescription("This MIB module contains Textual Conventions for LSPs of MPLS-\n       based transport networks.\n\n       Copyright (c) 2015 IETF Trust and the persons identified as\n       authors of the code.  All rights reserved.\n\n       Redistribution and use in source and binary forms, with or\n       without modification, is permitted pursuant to, and subject to\n       the license terms contained in, the Simplified BSD License set\n       forth in Section 4.c of the IETF Trust's Legal Provisions\n       Relating to IETF Documents\n       (http://trustee.ietf.org/license-info).")
class MplsGlobalId(TextualConvention, OctetString):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370,\n         Section 3'
    description = "This object contains the Textual Convention for an IP-based\n         operator-unique identifier (Global_ID).  The Global_ID can\n         contain the 2-octet or 4-octet value of the operator's\n         Autonomous System Number (ASN).\n\n         When the Global_ID is derived from a 2-octet ASN,\n         the two high-order octets of this 4-octet identifier\n         MUST be set to zero (0x00).  Further, ASN 0 is reserved.\n         The size of the Global_ID string MUST be zero if\n         the Global_ID is invalid.\n\n         Note that a Global_ID of zero is limited to entities\n         contained within a single operator and MUST NOT be used\n         across a Network-to-Network Interface (NNI).  A non-zero\n         Global_ID MUST be derived from an ASN owned by\n         the operator."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsCcId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions,\n      RFC 6923, Section 3.\n      International Reference Alphabet (IRA) (Formerly\n      International Alphabet No. 5 or IA5) - Information\n      technology - 7-bit coded character set for information\n      exchange, ITU-T Recommendation T.50, September 1992.'
    description = 'The CC (Country Code) is a string of two characters, each\n      being an uppercase Basic Latin alphabetic (i.e., A-Z).\n\n      The characters are encoded using ITU-T Recommendation T.50.\n      The size of the CC string MUST be zero if the CC identifier\n      is invalid.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class MplsIccId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions,\n      RFC 6923, Section 3.\n      International Reference Alphabet (IRA) (Formerly\n      International Alphabet No. 5 or IA5) - Information\n      technology - 7-bit coded character set for information\n      exchange, ITU-T Recommendation T.50, September 1992.'
    description = 'The ICC is a string of one to six characters, each\n      an uppercase Basic Latin alphabetic (i.e., A-Z) or\n      numeric (i.e., 0-9).  The characters are encoded\n      using ITU-T Recommendation T.50.  The size of\n      the ICC string MUST be zero if the ICC identifier\n      is invalid.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 6), )
class MplsNodeId(TextualConvention, Unsigned32):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370,\n         Section 4'
    description = "The Node_ID is assigned within the scope of\n        the Global_ID/ICC_Operator_ID.\n\n        When IPv4 addresses are in use, the value of this object\n        can be derived from the LSR's IPv4 loopback address.\n        When IPv6 addresses are in use, the value of this object\n        can be a 32-bit value unique within the scope of\n        a Global_ID.\n\n        Note that, when IP reachability is not needed, the 32-bit\n        Node_ID is not required to have any association\n        with the IPv4 address space.  The value of 0 indicates\n        an invalid Node_ID."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
mibBuilder.exportSymbols("MPLS-TC-EXT-STD-MIB", MplsCcId=MplsCcId, mplsTcExtStdMIB=mplsTcExtStdMIB, MplsNodeId=MplsNodeId, MplsIccId=MplsIccId, MplsGlobalId=MplsGlobalId, PYSNMP_MODULE_ID=mplsTcExtStdMIB)
