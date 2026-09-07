#
# PySNMP MIB module CISCO-CBP-TARGET-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CBP-TARGET-TC-MIB
# Source digest sha256:64685e266f2779d9becd64f7a62572354eb68bc031a7402260d0f2be90782332
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCbpTargetTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 511))
ciscoCbpTargetTCMIB.setRevisions(('2006-03-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setLastUpdated('2006-03-24 00:00')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setContactInfo('          Cisco Systems\n                   Customer Service\n        \n           Postal: 170 W. Tasman Drive\n                   San Jose, CA 95134-1706\n                   USA\n        \n              Tel: +1 800 553-NETS\n        \n           E-mail: cs-qos@cisco.com, cs-c3pl@cisco.com')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setDescription('This MIB module defines Textual Conventions for\n         representing targets which have class based policy \n         mappings. A target can be any logical interface \n         or entity to which a class based policy is able to be \n         associated.')
class CcbptTargetType(TextualConvention, Integer32):
    description = 'A Textual Convention that represents a type of target.\n\n         genIf(1)    A target of type interface defined by \n                     CcbptTargetIdIf Textual Convention.\n\n         atmPvc(2)   A target of type ATM PVC defined \n                     by the CcbptTargetIdAtmPvc Textual Convention.\n\n         frDlci(3)   A target of type Frame Relay DLCI \n                     defined by the CcbptTargetIdFrDlci Textual \n                     Convention.\n\n         entity(4) A target of type entity defined by the \n                   CcbptTargetIdEntity Textual Convention.  This target\n                   type is used to indicate the attachment of a Class \n                   Based Policy to a physical entity.\n\n         fwZone(5)   A target of type Firewall Security Zone\n                     defined by the CcbptTargetIdNameString \n                     Textual Convention.\n\n         fwZonePair(6) A target of type Firewall Security Zone \n                       defined by the CcbptTargetIdNameString\n                       Textual Convention.\n         \n         aaaSession(7) A target of type AAA Session define by the\n                       CcbptTargetIdAaaSession Textual Convention.\n\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("genIf", 1), ("atmPvc", 2), ("frDlci", 3), ("entity", 4), ("fwZone", 5), ("fwZonePair", 6), ("aaaSession", 7))

class CcbptTargetDirection(TextualConvention, Integer32):
    description = 'A Textual Convention that represents a direction for a target.\n\n         undirected(1)    Indicates that direction has no meaning \n                          relative to the target.\n\n         input(2)    Refers to the input direction relative to the \n                     target.\n\n         output(3)   Refers to the output direction relative to the\n                     target.\n     \n         inOut(4)    Refers to both the input and output directions\n                     relative to the target.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("undirected", 1), ("input", 2), ("output", 3), ("inOut", 4))

class CcbptTargetId(TextualConvention, OctetString):
    description = 'Denotes a generic target ID.\n\n         A CcbptTargetId value is always interpreted within the \n         context of an CcbptTargetType value. Every usage of the \n         CcbptTargetId Textual Convention is required to specify the\n         CcbptTargetType object which provides the context. It is \n         suggested that the CcbptTargetType object is logically \n         registered before the object(s) which use the CcbptTargetId\n         Textual Convention if they appear in the same logical row.\n\n         The value of an CcbptTargetId object must always be\n         consistent with the value of the associated CcbptTargetType\n         object. Attempts to set a CcbptTargetId object to a value\n         which is inconsistent with the associated targetType\n         must fail with an inconsistentValue error.\n         '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdIf(TextualConvention, OctetString):
    description = 'Represents an interface target:\n\n           octets   contents              encoding\n            1-4     ifIndex               network-byte order\n         '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdAtmPvc(TextualConvention, OctetString):
    description = 'Represents an ATM PVC target:\n\n           octets    contents              encoding\n            1-4      ifIndex               network-byte order\n            5-6      atmVclVpi             network-byte order\n            7-8      atmVclVci             network-byte order\n        '
    status = 'current'
    displayHint = '4d:2d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CcbptTargetIdFrDlci(TextualConvention, OctetString):
    description = 'Represents a Frame Relay DLCI target:\n\n           octets   contents               encoding\n            1-4     ifIndex                network-byte order\n            5-6     DlciNumber             network-byte order\n\n        '
    status = 'current'
    displayHint = '4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CcbptTargetIdEntity(TextualConvention, OctetString):
    description = 'Represents the entPhysicalIndex of the physical entity \n         target:\n\n           octets   contents               encoding\n            1-4     entPhysicalIndex       network-byte order\n\n        '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdNameString(TextualConvention, OctetString):
    description = 'Represents a target identified by a name string.  \n         This is the ASCII name identifying this target.\n        '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdAaaSession(TextualConvention, OctetString):
    description = 'Represents a AAA Session target:\n\n           octets   contents               encoding\n            1-4     casnSessionId      network-byte order\n\n        '
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptPolicySourceType(TextualConvention, Integer32):
    description = 'This Textual Convention represents the types of sources of \n         policies.\n\n         ciscoCbQos(1)      Cisco Class Based QOS policy source.\n                            The source of the policy is Cisco Class \n                            Based QOS specific.\n\n         ciscoCbpCommon(2)  Cisco Common Class Based Policy type.\n                            The source of the policy is Cisco Common\n                            Class Based.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ciscoCbQos", 1), ("ciscoCbpBase", 2))

class CcbptPolicyIdentifier(TextualConvention, Unsigned32):
    description = 'A type specific, arbitrary identifier uniquely given\n         to a policy-map attachment to a target.\n        '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CcbptPolicyIdentifierOrZero(TextualConvention, Unsigned32):
    description = 'This refers to CcbptPolicyIdentifier values, as applies, \n         or 0.  The behavior of the value of 0 should be described\n         in the description of objects using this type.\n        '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("CISCO-CBP-TARGET-TC-MIB", CcbptPolicyIdentifier=CcbptPolicyIdentifier, CcbptPolicyIdentifierOrZero=CcbptPolicyIdentifierOrZero, CcbptPolicySourceType=CcbptPolicySourceType, CcbptTargetDirection=CcbptTargetDirection, CcbptTargetId=CcbptTargetId, CcbptTargetIdAaaSession=CcbptTargetIdAaaSession, CcbptTargetIdAtmPvc=CcbptTargetIdAtmPvc, CcbptTargetIdEntity=CcbptTargetIdEntity, CcbptTargetIdFrDlci=CcbptTargetIdFrDlci, CcbptTargetIdIf=CcbptTargetIdIf, CcbptTargetIdNameString=CcbptTargetIdNameString, CcbptTargetType=CcbptTargetType, PYSNMP_MODULE_ID=ciscoCbpTargetTCMIB, ciscoCbpTargetTCMIB=ciscoCbpTargetTCMIB)
