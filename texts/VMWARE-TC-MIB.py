#
# PySNMP MIB module VMWARE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-TC-MIB
# Produced by pysmi-1.1.11 at Wed Dec  6 03:07:25 2023
# On host fv-az520-882 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, NotificationType, Counter64, TimeTicks, Integer32, ModuleIdentity, Counter32, MibIdentifier, Unsigned32, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "NotificationType", "Counter64", "TimeTicks", "Integer32", "ModuleIdentity", "Counter32", "MibIdentifier", "Unsigned32", "IpAddress", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwSystem, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwSystem")
vmwTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 1, 11))
vmwTcMIB.setRevisions(('2009-09-05 00:00', '2007-12-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwTcMIB.setRevisionsDescriptions(('Added VmwLongDisplayString', 'This is the first revision.',))
if mibBuilder.loadTexts: vmwTcMIB.setLastUpdated('200909050000Z')
if mibBuilder.loadTexts: vmwTcMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwTcMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwTcMIB.setDescription('This MIB module provides common datatypes for use in VMWARE\n     enterprise mib modules')
class VmwSubsystemTypes(TextualConvention, Integer32):
    description = 'Define the various hardware subsystems.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("chassis", 2), ("powerSupply", 3), ("fan", 4), ("cpu", 5), ("memory", 6), ("battery", 7), ("temperatureSensor", 8), ("raidController", 9), ("voltage", 10))

class VmwCIMAlertTypes(TextualConvention, Integer32):
    description = 'Primary classifications for alert messages.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("communications", 2), ("qos", 3), ("processingError", 4), ("deviceAlert", 5), ("environmentalAlert", 6), ("modelChange", 7), ("securityAlert", 8))

class VmwCIMAlertFormat(TextualConvention, Integer32):
    description = 'Indication of what the Alerting Managed Element property is.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("cimObjectPath", 2))

class VmwSubsystemStatus(TextualConvention, Integer32):
    description = 'Define the state of a given subsystem if known.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("normal", 2), ("marginal", 3), ("critical", 4), ("failed", 5))

class VmwCIMSeverity(TextualConvention, Integer32):
    description = 'Recommendation.ITU|X733.Perceived severity possible values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("other", 1), ("information", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("fatal", 7))

class VmwCimName(TextualConvention, OctetString):
    description = 'Contains a name of no more than 256 characters.'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class VmwConnectedState(TextualConvention, OctetString):
    description = "Can hold one of the following values: 'true' or 'false' or 'unknown'."
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 7)

class VmwLongDisplayString(TextualConvention, OctetString):
    description = "Represents textual information taken from the NVT ASCII\n            character set, as defined in pages 4, 10-11 of RFC 854.\n\n            To summarize RFC 854, the NVT ASCII repertoire specifies:\n\n              - the use of character codes 0-127 (decimal)\n\n              - the graphics characters (32-126) are interpreted as\n                US ASCII\n\n              - NUL, LF, CR, BEL, BS, HT, VT and FF have the special\n                meanings specified in RFC 854\n\n              - the other 25 codes have no standard interpretation\n\n              - the sequence 'CR LF' means newline\n\n              - the sequence 'CR NUL' means carriage-return\n\n              - an 'LF' not preceded by a 'CR' means moving to the\n                same column on the next line.\n\n              - the sequence 'CR x' for any x other than LF or NUL is\n                illegal.  (Note that this also means that a string may\n                end with either 'CR LF' or 'CR NUL', but not with CR.)\n\n            An object defined using this syntax may be of indefinite\n            length, as specified by the protocol, but displays may\n            choose to display only the first 4096 characters."
    status = 'current'
    displayHint = '1a'

class VmwLongSnmpAdminString(TextualConvention, OctetString):
    description = 'This TC adapted from SnmpAdminString from SNMP-FRAMEWORK-MIB An\n                 octet string containing administrative information, preferably\n                 in human-readable form.\n\n                 To facilitate internationalization, this\n                 information is represented using the ISO/IEC\n                 IS 10646-1 character set, encoded as an octet\n                 string using the UTF-8 transformation format\n                 described in [RFC2279].\n\n                 Since additional code points are added by\n                 amendments to the 10646 standard from time\n                 to time, implementations must be prepared to\n                 encounter any code point from 0x00000000 to\n                 0x7fffffff.  Byte sequences that do not\n                 correspond to the valid UTF-8 encoding of a\n                 code point or are outside this range are\n                 prohibited.\n\n                 The use of control codes should be avoided.\n\n                 When it is necessary to represent a newline,\n                 the control code sequence CR LF should be used.\n\n                 The use of leading or trailing white space should\n                 be avoided.\n\n                 For code points not directly supported by user\n                 interface hardware or software, an alternative\n                 means of entry and display, such as hexadecimal,\n                 may be provided.\n\n                 For information encoded in 7-bit US-ASCII,\n                 the UTF-8 encoding is identical to the\n                 US-ASCII encoding.\n\n                 UTF-8 may require multiple bytes to represent a\n                 single character / code point; thus the length\n                 of this object in octets may be different from\n                 the number of characters encoded.  Similarly,\n                 size constraints refer to the number of encoded\n                 octets, not the number of characters represented\n                 by an encoding.\n\n                 Note that when this TC is used for an object that\n                 is used or envisioned to be used as an index, then\n                 a SIZE restriction MUST be specified so that the\n                 number of sub-identifiers for any object instance\n                 does not exceed the limit of 128, as defined by\n                 [RFC3416].\n\n                 Note that the size of an SnmpAdminString object is\n                 measured in octets, not characters.'
    status = 'current'
    displayHint = '4096t'

class VmwUnixAbsFilePath(TextualConvention, OctetString):
    description = 'Represents the absolute path of a file on Unix system.'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("VMWARE-TC-MIB", VmwUnixAbsFilePath=VmwUnixAbsFilePath, vmwTcMIB=vmwTcMIB, VmwLongDisplayString=VmwLongDisplayString, VmwConnectedState=VmwConnectedState, VmwSubsystemTypes=VmwSubsystemTypes, VmwSubsystemStatus=VmwSubsystemStatus, VmwCIMSeverity=VmwCIMSeverity, VmwCIMAlertTypes=VmwCIMAlertTypes, PYSNMP_MODULE_ID=vmwTcMIB, VmwCIMAlertFormat=VmwCIMAlertFormat, VmwCimName=VmwCimName, VmwLongSnmpAdminString=VmwLongSnmpAdminString)
