#
# PySNMP MIB module Juniper-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/Juniper-TC
# Produced by pysmi-1.1.3 at Wed Dec  8 18:23:37 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Bits, IpAddress, ObjectIdentity, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter64, Integer32, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Bits", "IpAddress", "ObjectIdentity", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter64", "Integer32", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 1))
juniTextualConventions.setRevisions(('2005-12-21 20:13', '2005-11-18 22:30', '2004-12-03 22:12', '2003-11-12 22:31', '2002-09-16 21:44', '2002-04-04 16:35', '2001-03-08 22:26', '1999-12-12 00:00', '1999-07-14 00:00', '1998-11-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTextualConventions.setRevisionsDescriptions(('Added JuniNibbleConfig.', 'Added JuniTimeFilter.', 'Added JuniVrfGroupName.', 'Increased the size of JuniInterfaceLocation.\n         Added JuniInterfaceLocationType and JuniInterfaceLocationValue.', 'Replaced Unisphere names with Juniper names.\n         Added JuniInterfaceDescrFormat and JuniInterfaceLocation.', 'Increased the size limits on JuniName and JuniVrfName.', 'Added JuniVrfName and JuniSetMap.', 'Added JuniLogSeverity.', 'Added JuniAcctngAdminType and JuniAcctngOperType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniTextualConventions.setLastUpdated('200512212013Z')
if mibBuilder.loadTexts: juniTextualConventions.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTextualConventions.setContactInfo('       Juniper Networks, Inc.\n        Postal: 10 Technology Park Drive\n                Westford, MA  01886-3146\n                USA\n        Tel:    +1 978 589 5800\n        Email:  mib@Juniper.net')
if mibBuilder.loadTexts: juniTextualConventions.setDescription('Textual conventions defined and used by the Juniper Networks\n        enterprise.')
class JuniEnable(TextualConvention, Integer32):
    description = "Enterprise-standard SYNTAX for MIB objects having enumerated value pair\n        'enable' and 'disable'.  Used for both admin (configurable) and oper\n        (read-only) objects."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class JuniName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A virtual router text name of restricted length.  Represents textual\n        information taken from the NVT ASCII graphics character set (codes 32\n        through 126).'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class JuniVrfName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A VPN routing forwarding text name of restricted length.  Represents\n        textual information taken from the NVT ASCII graphics character set\n        (codes 32 through 126).'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniNextIfIndex(TextualConvention, Integer32):
    description = 'Coordinate ifIndex value allocation for entries in an associated\n        ifIndex-ed interface table, by first reading an ifIndex value from this\n        object, then creating an entry, having that ifIndex value, in the\n        associated interface table.\n\n        The DESCRIPTION clause for an object of this type must identify the\n        associated interface table.\n\n        A GET of this object returns the next available ifIndex value to be used\n        to create an entry in the associated interface table; or zero, if no\n        valid ifIndex value is available.  This object also returns a value of\n        zero when it is the lexicographic successor of a varbind presented in an\n        SNMP GETNEXT or GETBULK request, for which circumstance it is assumed\n        that ifIndex allocation is unintended.\n\n        Successive GETs will typically return different values, thus avoiding\n        collisions among cooperating management clients seeking to create table\n        entries simultaneously.\n\n        Unless specified otherwise by its MAX-ACCESS and DESCRIPTION clauses, an\n        object of this type is read-only, and a SET of such an object returns a\n        notWritable error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JuniIpAddrLessIf(TextualConvention, IpAddress):
    description = "Compressed index representation to identify both numbered and\n        unnumbered ('address-less') IP subnetworks.\n\n        One approach is to identify such interfaces with a 2-tuple consisting of\n        <IpAddress, ifIndex>, where only one of the pair is nonzero for a valid\n        interface (IpAddress is nonzero for numbered interfaces, ifIndex is\n        nonzero for unnumbered interfaces).\n\n        As an alternative, this textual convention compresses the 2-tuple\n        information into an IpAddress (32-bit) format a.b.c.d having the\n        following interpretation:\n\n        Format              Interpretation      IP Interface Type\n        ------------------------------------------------------------------\n        0.0.0.0             'null' value        'none' or 'wildcard', etc.\n        a.b.c.d, a != 0     IP Address          Numbered\n        0.b.c.d             ifIndex             Unnumbered\n\n        For the unnumbered case, the value of the ifIndex is given by\n        (b * 65536) + (c * 256) + (d)\n\n        A side-effect of this approach is that ifIndex values for IP network\n        interfaces must fall in the range 1..16777215 (i.e. 24 bits)."
    status = 'current'

class JuniTimeSlotMap(TextualConvention, OctetString):
    description = 'A bit map representing one or more timeslots of a DS1/E1 interface.\n        Bits are numbered in descending order from 31-0 starting from the most\n        significant bit of the first octet and ending with the least significant\n        bit of the fourth octet.  Bits 1-24 are relevant for DS1 interfaces,\n        bits 0-31 are relevant for E1 interfaces.\n\n        A bit is set if the associated timeslot is in use, and cleared if the\n        associated timeslot is not in use.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class JuniAcctngAdminType(TextualConvention, Integer32):
    description = 'The desired administrative state for the collection of accounting\n        records.  The administrative domain governed by an object of\n        JuniAcctngAdminType is defined in the MIB OBJECT description that uses\n        this type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class JuniAcctngOperType(TextualConvention, Integer32):
    description = 'The operational state for the collection of accounting records.  The\n        administrative domain that an object of this type is reporting state\n        for, is defined in the MIB object description that uses this type.\n\n        The notSupported(2) state indicates that accounting data collection is\n        not supported for the entity using an object of JuniAcctngOperType type.\n        If an entity does not support accounting data collection, an object of\n        JuniAcctngOperType type will report notSupported(2) regardless of the\n        value set in the corresponding JuniAcctngAdminType.\n\n        The disabled(0) state indicates that the corresponding\n        JuniAcctngAdminType object has been set to disabled(0).  If a data\n        collection is in process, the value of JuniAcctngOperType will change to\n        disabled(0) after the current collection completes.\n\n        The enabled(1) state indicates that the corresponding\n        JuniAcctngAdminType object has been set to enabled(1) and that the\n        entity is ready to collect accounting records.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("enable", 1), ("notSupported", 2))

class JuniLogSeverity(TextualConvention, Integer32):
    description = "The log severity level.\n\n        Lower numerical values correspond to higher severity levels.  The value\n        'off' filters all severity levels."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("off", -1), ("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class JuniSetMap(TextualConvention, OctetString):
    description = "A bitmap indicating which objects in a table entry have been explicitly\n        configured.\n\n        A 1 in a bit position indicates the corresponding table entry object has\n        been explicitly configured.\n\n        A 0 in a bit position indicates the corresponding table entry has NOT\n        been explicitly configured (and typically contains the default setting\n        defined in the DEFVAL clause for that object).\n\n        Once set, a bit typically remains set until the table entry is\n        destroyed.  The semantics of an object of this type should specify by\n        what circumstances, if any, bits in the map may be cleared.\n\n        If an entry exists in a table but no entry objects have been configured,\n        JuniSetMap will contain a zero-length string.\n\n        The DESCRIPTION clause for an object having this SYNTAX should indicate\n        which, if any, entry objects are excluded from representation in the\n        JuniSetMap.  Typically, index and RowStatus entry objects would not be\n        represented.\n\n        Bit positions correspond to table entry objects as follows:  Objects in\n        the table entry are numbered according to the last OID subidentifier of\n        their object type as defined in the MIB.  For example, an object in a\n        table entry having OID 1.3.6.1.2.1.2.2.1.5 would be object number\n        5. (Instance-identifying OID subidentifiers are ignored.)\n\n        Octets in the map are numbered 1..N beginning with the first octet.\n\n        Bits in an octet are numbered 1..8 beginning with the MOST significant\n        bit.\n\n        Bit B in octet Q represents the entry object numbered E thus:\n            E = (((Q - 1) * 8) + B)\n\n        For example, the third most significant bit in the second octet\n        represents the entry object numbered 11:\n            ((((2 - 1) * 8) + 3) = 11\n\n        Conversely, the octet Q and bit B positions of the corresponding bit for\n        a given entry object numbered E is determined by:\n            Q = (((E - 1) / 8) + 1)     (where '/' means integer division)\n            B = (((E - 1) modulo 8) + 1)\n\n        For example, the octet and bit positions of the entry object numbered 11\n        are:\n            (((11 - 1) / 8) + 1)      = 2 (octet number)\n            (((11 - 1) modulo 8) + 1) = 3 (3rd most sig. bit) "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceDescrFormat(TextualConvention, Integer32):
    description = 'The interface description format setting.\n            proprietary(0)      Juniper encoding\n                                Example Column: IP 3/0.1, ATM 3/0.1, ATM 3/0\n            industryCommon(1)                   ATM 3/0.1, ATM3/0.1 ATM 3/0 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("proprietary", 0), ("industryCommon", 1))

class JuniInterfaceLocation(TextualConvention, OctetString):
    description = "An ASCII string representation of an interfaces location in the\n        following forms:\n            slot/port\n            slot/adapter/port\n            adapter/port\n\n        Examples:  3/0, 12/0/1, 0/0 \n\n        The form is determined by the physical architecture of the router\n        platform.  E.g., the ERX family of platforms (first generation E-series)\n        requires the 'slot/port' form."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class JuniInterfaceLocationType(TextualConvention, Integer32):
    description = "Describes the platform-dependent interpretation of a\n        JuniInterfaceLocationValue object:\n            unknown           - Unspecified/unknown\n            slotPort          - Two octets in length; 1st octet is 'slot', 2nd\n                                octet is 'port' \n            slotAdapterPort   - Three octets in length; 1st octet is 'slot', 2nd\n                                octet is 'adapter', 3rd octet is 'port' \n            adapterPort       - Two octets in length; 1st octet is 'adapter',\n                                2nd octet is 'port' "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slotPort", 1), ("slotAdapterPort", 2), ("adapterPort", 3))

class JuniInterfaceLocationValue(TextualConvention, OctetString):
    description = "The value of a platform-dependent interface location, represented as an\n        OCTET STRING.  A corresponding JuniInterfaceLocationType object will identify\n        the mapping of octets to location elements, e.g. 'slot.port'.\n\n        Note: When the value of an object having this syntax is encoded as a MIB\n        table INDEX, the rules for encoding a variable-length OCTET STRING are\n        observed."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class JuniVrfGroupName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set.'
    description = 'A VPN routing forwarding group name of restricted length.  Represents\n        textual information taken from the NVT ASCII graphics character set\n        (codes 32 through 126).'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class JuniTimeFilter(TextualConvention, TimeTicks):
    reference = 'Refer to RFC 2021 for the definition of the TimeFilter, its usage and \n        implementation notes.'
    description = 'Used as an index to a table. A TimeFilter variable allows a GetNext\n        or GetBulk request to find rows in a table for which the TimeFilter \n        index variable is greater than or equal to a specified value.\n        JuniTimeFilter is same as TimeFilter. Detailed description of \n        TimeFilter variables, their implementation and use is documented in the \n        RMON2 MIB.'
    status = 'current'

class JuniNibbleConfig(TextualConvention, Integer32):
    description = 'A configuration variable comprised of nibbles i.e. 4 bits, such that \n         a client can supply a list of 0 to 8 selections.  The least \n         significant nibble is the first value of the list, and the most \n         significant nibble is the last value.  The value in each field \n         ranges from 0 to 15, however the first nibble with value 0 indicates\n         the end of the list.  Repetition of values is not allowed. \n         Segregation of values in not allowed.\n\n         Example valid encoding:\n         0x00000321\n         0x00083E12\n\n         Not a valid encoding:\n         0x00000121- will return an error\n         0x01002001- will return an error.'
    status = 'current'

mibBuilder.exportSymbols("Juniper-TC", JuniVrfGroupName=JuniVrfGroupName, JuniNextIfIndex=JuniNextIfIndex, JuniName=JuniName, JuniInterfaceLocationType=JuniInterfaceLocationType, JuniNibbleConfig=JuniNibbleConfig, juniTextualConventions=juniTextualConventions, JuniInterfaceDescrFormat=JuniInterfaceDescrFormat, JuniTimeFilter=JuniTimeFilter, JuniAcctngAdminType=JuniAcctngAdminType, JuniAcctngOperType=JuniAcctngOperType, JuniInterfaceLocationValue=JuniInterfaceLocationValue, JuniTimeSlotMap=JuniTimeSlotMap, JuniEnable=JuniEnable, JuniVrfName=JuniVrfName, JuniLogSeverity=JuniLogSeverity, JuniInterfaceLocation=JuniInterfaceLocation, JuniIpAddrLessIf=JuniIpAddrLessIf, PYSNMP_MODULE_ID=juniTextualConventions, JuniSetMap=JuniSetMap)
