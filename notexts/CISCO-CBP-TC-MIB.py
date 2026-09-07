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
if mibBuilder.loadTexts: ciscoCbpTcMIB.setLastUpdated('2008-06-24 00:00')
if mibBuilder.loadTexts: ciscoCbpTcMIB.setOrganization('Cisco Systems, Inc.')
class CbpElementName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '127a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class CbpElementIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpElementIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpInstanceIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpInstanceIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class CbpExecutionPriority(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CbpExecutionStrategy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("doUntilSuccess", 2), ("doUntilFailure", 3), ("doAll", 4))

mibBuilder.exportSymbols("CISCO-CBP-TC-MIB", CbpElementIdentifier=CbpElementIdentifier, CbpElementIdentifierOrZero=CbpElementIdentifierOrZero, CbpElementName=CbpElementName, CbpExecutionPriority=CbpExecutionPriority, CbpExecutionStrategy=CbpExecutionStrategy, CbpInstanceIdentifier=CbpInstanceIdentifier, CbpInstanceIdentifierOrZero=CbpInstanceIdentifierOrZero, PYSNMP_MODULE_ID=ciscoCbpTcMIB, ciscoCbpTcMIB=ciscoCbpTcMIB)
