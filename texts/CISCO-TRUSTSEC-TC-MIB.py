#
# PySNMP MIB module CISCO-TRUSTSEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TRUSTSEC-TC-MIB
# Source digest sha256:bd75c81c392193dea412135dc7c55546094aaeb9a0b4c68ed7f00fbf352cb598
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCtsTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 694))
ciscoCtsTcMIB.setRevisions(('2013-06-06 00:00', '2012-01-30 00:00', '2009-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCtsTcMIB.setRevisionsDescriptions(('Added CtsSxpConnectionStatus.', 'Added CtsSgaclMonitorMode.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCtsTcMIB.setLastUpdated('2013-06-06 00:00')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setDescription('This module defines the textual conventions used within\n        Cisco Trusted Security framework.')
class CtsSecurityGroupTag(TextualConvention, Unsigned32):
    description = 'Indicates the SGT (Security Group Tag) value.\n\n        Semantics of a value zero CtsSecurityGroupTag are object-specific\n        and must be defined as part of the description of any object\n        which uses this syntax.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CtsAclName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of one ACL (Access Control List)\n        or a list of ACLs using a single whitespace as the\n        delimiter.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n        CtsAclName convention. The latter defines a\n        non-empty ACL name(s). This extension permits\n        the additional value of empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsAclList(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of one or more ACLs. If there is multiple\n        ACLs, each ACL name is separated by a single whitespace.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclListOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n        CtsAclList convention. The latter defines a\n        non-empty ACL name(s). This extension permits\n        the additional value of empty string.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPolicyName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the name of policy.\n\n        A zero length string indicates no policy.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPasswordEncryptionType(TextualConvention, Integer32):
    description = "The type of encryption used for TrustSec passwords.\n\n        'other'     - The read-only value 'other' indicates that\n                      the type of password encryption is not in one\n                      of the types defined below.\n\n        'none'      - Indicates that the corresponding CtsPassword \n                      object is a zero-length string.\n\n        'clearText' - Indicates that the password is not encrypted\n\n        'typeSix'   - Indicates that type-6 algorithm is used to\n                      encrypt the password\n\n        'typeSeven' - Indicates that type-7 algorithm is used to\n                      encrypt the password.\n\n         Each definition of a concrete CtsPasswordEncryptionType value\n         must be accompanied by a definition of a textual convention for \n         use with that CtsPasswordEncryptionType.\n\n         To support future extensions, the CtsPasswordEncryptionType\n         textual convention SHOULD NOT be sub-typed in object type\n         definitions. It MAY be sub-typed in compliance statements in order\n         to require only a subset of these address types for a compliant\n         implementation.\n\n         Implementations must ensure that CtsPasswordEncryptionType\n         object and any dependent objects (e.g. CtsPassword objects) are\n         consistent.  An inconsistentValue error must be generated\n         if an attempt to change an CtsPasswordEncryptionType object\n         would, for example, lead to an undefined CtsPassword value. \n         In particular, CtsPasswordEncryptionType/CtsPassword pairs\n         must be changed together if the encryption type changes.\n         (e.g. from clearText(2) to typeSix(1))."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("clearText", 3), ("typeSix", 4), ("typeSeven", 5))

class CtsPassword(TextualConvention, OctetString):
    description = "A password for TrustSec functionality.\n\n        A CtsPassword value is always interpreted within the context\n        of an CtsPasswordEncryptionType value. Every usage of the\n        CtsPassword textual convention is required to specify the\n        CtsPasswordEncryptionType object which provides the context.\n        It is suggested that the CtsPasswordEncryptionType is logically\n        registered before the object(s) which use the CtsPassword textual\n        convention if they appear in the same logical row.\n\n        The value of an CtsPassword object must always be consistent with\n        the value of the associated CtsPasswordEncryptionType object.\n        Attempts to set an CtsPassword object to a value which is \n        inconsistent with the associated CtsPasswordEncryptionType\n        must fail with an inconsistentValue error.\n\n        When this textual convention is used as the syntax of an\n        index object, there may be issues with the limit of 128\n        sub-identifiers specified in SMIv2, STD 58. In this case,\n        the object definition MUST include a 'SIZE' clause to\n        limit the number of potential instance sub-identifiers."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CtsGenerationId(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form,\n        describes the generation identification associated\n        with a TrustSec attribute such as downloaded SGACL,\n        downloaded server list .etc... \n\n        A zero length string indicates no generation identification.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CtsAcsAuthorityIdentity(TextualConvention, OctetString):
    description = 'The authority identity of an Access Control Server.\n\n        A zero length of CtsAcsAuthorityIdentity indicates\n        that the authority identity is not available.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CtsCredentialRecordType(TextualConvention, Integer32):
    description = "The secret type of TrustSec credential record.\n\n        'simpleSecret' - Simple Secret credential.\n                         This type of credential record is constructed\n                         with symmetric key with associated meta-data.\n                         For example, credential password.\n        'pac'          - Protected Access Credentials(PAC).\n                         A PAC record contains three components:\n                         PAC-key, PAC-opaque and PAC-info."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("simpleSecret", 1), ("pac", 2))

class CtsSgaclMonitorMode(TextualConvention, Integer32):
    description = "The SGACL monitor mode for the SGACL enforced traffic.\n\n        'on'   - indicates that SGACL monitor is turned on.\n\n        'off'  - indicates that SGACL monitor mode is turned off."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class CtsSxpConnectionStatus(TextualConvention, Integer32):
    description = "The status of SXP connection.\n\n        'other'      - Any other state not covered by below\n                       enumerations.\n\n        'off'        - The SXP connection has been disconnected.\n                       SGT mappings are no longer learnt through SXP\n                       connection in this state. SGT mappings\n                       already learnt through this connection will be\n                       deleted.\n\n        'on'         - The SXP connection has been successfully\n                       established. SGT mappings are learnt\n                       through this SXP connection.\n\n        'pendingOn'  - A request to establish SXP connection has been\n                       sent to the peer and is pending.\n\n        'deleteHoldDown' - The SXP connection is not operational and\n                       delete hold-down timer has been started. If the\n                       SXP connection does not recover before the\n                       expiration of the hold-down timer, the SGT\n                       mappings learnt on this connection will be\n                       deleted. If the SXP connection recovers\n                       before the expiration of the hold-down timer,\n                       the SGT mappings learnt on this connection\n                       will not be deleted."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("off", 2), ("on", 3), ("pendingOn", 4), ("deleteHoldDown", 5))

mibBuilder.exportSymbols("CISCO-TRUSTSEC-TC-MIB", CtsAclList=CtsAclList, CtsAclListOrEmpty=CtsAclListOrEmpty, CtsAclName=CtsAclName, CtsAclNameOrEmpty=CtsAclNameOrEmpty, CtsAcsAuthorityIdentity=CtsAcsAuthorityIdentity, CtsCredentialRecordType=CtsCredentialRecordType, CtsGenerationId=CtsGenerationId, CtsPassword=CtsPassword, CtsPasswordEncryptionType=CtsPasswordEncryptionType, CtsPolicyName=CtsPolicyName, CtsSecurityGroupTag=CtsSecurityGroupTag, CtsSgaclMonitorMode=CtsSgaclMonitorMode, CtsSxpConnectionStatus=CtsSxpConnectionStatus, PYSNMP_MODULE_ID=ciscoCtsTcMIB, ciscoCtsTcMIB=ciscoCtsTcMIB)
