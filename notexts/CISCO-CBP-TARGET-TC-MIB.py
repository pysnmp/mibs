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
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setLastUpdated('2006-03-24 00:00')
if mibBuilder.loadTexts: ciscoCbpTargetTCMIB.setOrganization('Cisco Systems, Inc.')
class CcbptTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("genIf", 1), ("atmPvc", 2), ("frDlci", 3), ("entity", 4), ("fwZone", 5), ("fwZonePair", 6), ("aaaSession", 7))

class CcbptTargetDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("undirected", 1), ("input", 2), ("output", 3), ("inOut", 4))

class CcbptTargetId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdIf(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdAtmPvc(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:2d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CcbptTargetIdFrDlci(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class CcbptTargetIdEntity(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptTargetIdNameString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CcbptTargetIdAaaSession(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CcbptPolicySourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ciscoCbQos", 1), ("ciscoCbpBase", 2))

class CcbptPolicyIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CcbptPolicyIdentifierOrZero(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("CISCO-CBP-TARGET-TC-MIB", CcbptPolicyIdentifier=CcbptPolicyIdentifier, CcbptPolicyIdentifierOrZero=CcbptPolicyIdentifierOrZero, CcbptPolicySourceType=CcbptPolicySourceType, CcbptTargetDirection=CcbptTargetDirection, CcbptTargetId=CcbptTargetId, CcbptTargetIdAaaSession=CcbptTargetIdAaaSession, CcbptTargetIdAtmPvc=CcbptTargetIdAtmPvc, CcbptTargetIdEntity=CcbptTargetIdEntity, CcbptTargetIdFrDlci=CcbptTargetIdFrDlci, CcbptTargetIdIf=CcbptTargetIdIf, CcbptTargetIdNameString=CcbptTargetIdNameString, CcbptTargetType=CcbptTargetType, PYSNMP_MODULE_ID=ciscoCbpTargetTCMIB, ciscoCbpTargetTCMIB=ciscoCbpTargetTCMIB)
