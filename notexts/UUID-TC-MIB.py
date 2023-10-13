#
# PySNMP MIB module UUID-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/UUID-TC-MIB
# Produced by pysmi-1.1.8 at Fri Oct 13 14:15:09 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, mib_2, iso, NotificationType, Gauge32, IpAddress, MibIdentifier, Counter64, Bits, ObjectIdentity, Unsigned32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "mib-2", "iso", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "Bits", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
uuidTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 217))
uuidTCMIB.setRevisions(('2013-04-05 00:00',))
if mibBuilder.loadTexts: uuidTCMIB.setLastUpdated('201304050000Z')
if mibBuilder.loadTexts: uuidTCMIB.setOrganization('IETF Energy Management Working Group')
class UUID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class UUIDorZero(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
mibBuilder.exportSymbols("UUID-TC-MIB", UUID=UUID, UUIDorZero=UUIDorZero, PYSNMP_MODULE_ID=uuidTCMIB, uuidTCMIB=uuidTCMIB)
