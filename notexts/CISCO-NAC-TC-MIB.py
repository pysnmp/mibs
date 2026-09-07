#
# PySNMP MIB module CISCO-NAC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NAC-TC-MIB
# Source digest sha256:2d99886a64c8a2765e8da0a4c2fcf8b55af255a8cd4476915d55829321309ca1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNacTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 530))
ciscoNacTcMIB.setRevisions(('2006-05-31 00:00',))
if mibBuilder.loadTexts: ciscoNacTcMIB.setLastUpdated('2006-05-31 00:00')
if mibBuilder.loadTexts: ciscoNacTcMIB.setOrganization('Cisco Systems, Inc.')
class CnnEouState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("initialize", 1), ("hello", 2), ("clientless", 3), ("eapRequest", 4), ("response", 5), ("authenticated", 6), ("fail", 7), ("abort", 8), ("aaaFail", 9), ("hold", 10), ("client", 11), ("server", 12))

class CnnEouAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clientless", 1), ("eap", 2), ("static", 3), ("unknown", 4))

class CnnEouDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ciscoIpPhone", 1))

class CnnEouPostureToken(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("healthy", 2), ("checkup", 3), ("quarantine", 4), ("infected", 5))

class CnnEouPostureTokenString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-NAC-TC-MIB", CnnEouAuthType=CnnEouAuthType, CnnEouDeviceType=CnnEouDeviceType, CnnEouPostureToken=CnnEouPostureToken, CnnEouPostureTokenString=CnnEouPostureTokenString, CnnEouState=CnnEouState, PYSNMP_MODULE_ID=ciscoNacTcMIB, ciscoNacTcMIB=ciscoNacTcMIB)
