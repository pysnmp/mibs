#
# PySNMP MIB module CISCO-CBP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CBP-TC-MIB
# Source digest sha256:e184be14f474ae095bd5f0c2938f4f6fdccafb3a3d4b79c8f8570b06a6768485
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCbpTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 662))
ciscoCbpTcMIB.setRevisions(('2008-06-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCbpTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoCbpTcMIB.setLastUpdated('2008-06-24 00:00')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setDescription('This MIB module defines textual conventions used by the\n        CISCO-CBP-BASE-CFG-MIB, CISCO-CBP-BASE-MON-MIB, and any MIB\n        modules extending these MIB modules.')
class CbpElementName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for\n        Describing Simple Network Management Protocol (SNMP)\n        Management Frameworks', RFC-3411, December 2002."
    description = "A string-value that identifies an element used to specify\n        a class-based policy.  The semantics of the string-value are\n        the same those specified by the SnmpAdminString textual\n        convention defined by the SNMP-FRAMEWORK-MIB [RFC3411].\n\n        Observe that the null string is reserved for cases when an\n        instance of an object needs to specify 'no element'."
    status = 'current'
    displayHint = '127a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class CbpElementIdentifier(TextualConvention, Unsigned32):
    description = 'A positive, non-zero integer-value that uniquely identifies\n        an element used to specify a class-based policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpElementIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the\n        CbpElementIdentifier textual convention, which permits the value\n        '0'.  The use of the value '0' is specific to an object, thus\n        requiring the descriptive text associated with the object to\n        describe the semantics of its use."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpInstanceIdentifier(TextualConvention, Unsigned32):
    description = 'A positive, non-zero integer-value that uniquely identifies\n        an instance of an element used to define a class-based policy.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the\n        CbpInstanceIdentifier textual convention, which permits the\n        value '0'.  The use of the value '0' is specific to an object,\n        thus requiring the descriptive text associated with the object\n        to describe the semantics of its use."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpExecutionPriority(TextualConvention, Unsigned32):
    description = "An positive, integer-value denoting the relative priority of an\n        element, where '1' represents the highest priority and greater\n        values represent lower priorities.\n\n        The priority assigned to an element determines the order in\n        which the system processes the elements relative to like\n        elements having the same parent, where the system processes\n        elements having a greater priority first.  The system processes\n        sibling elements having the same priority in the order they were\n        created."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpExecutionStrategy(TextualConvention, Integer32):
    description = "An enumerated integer-value describing how to execute an\n        ordered set of actions:\n\n            'other'\n                The implementation of the MIB using this textual\n                convention does not recognize the specified execution\n                strategy.\n\n            'doUntilSuccess'\n                The system sequentially executes the actions in the\n                set until one succeeds.\n\n            'doUntilFailure'\n                The system sequentially executes the actions in the\n                set until one fails.\n\n            'doAll'\n                The system sequentially executes all actions in the set,\n                regardless of whether they succeed or fail."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("doUntilSuccess", 2), ("doUntilFailure", 3), ("doAll", 4))

mibBuilder.exportSymbols("CISCO-CBP-TC-MIB", CbpElementIdentifier=CbpElementIdentifier, CbpElementIdentifierOrZero=CbpElementIdentifierOrZero, CbpElementName=CbpElementName, CbpExecutionPriority=CbpExecutionPriority, CbpExecutionStrategy=CbpExecutionStrategy, CbpInstanceIdentifier=CbpInstanceIdentifier, CbpInstanceIdentifierOrZero=CbpInstanceIdentifierOrZero, PYSNMP_MODULE_ID=ciscoCbpTcMIB, ciscoCbpTcMIB=ciscoCbpTcMIB)
