#
# PySNMP MIB module UUID-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/UUID-TC-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 08:15:27 2023
# On host fv-az447-19 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Bits, Counter64, Counter32, Gauge32, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Bits", "Counter64", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("UUID-TC-MIB", PYSNMP_MODULE_ID=uuidTCMIB, uuidTCMIB=uuidTCMIB, UUIDorZero=UUIDorZero, UUID=UUID)
