#
# PySNMP MIB module IANA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-ENTITY-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:10:40 2023
# On host fv-az443-612 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Integer32, Bits, iso, Gauge32, ModuleIdentity, Counter64, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "Bits", "iso", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaEntityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 216))
ianaEntityMIB.setRevisions(('2015-07-16 00:00', '2015-07-16 00:00', '2013-04-05 00:00',))
if mibBuilder.loadTexts: ianaEntityMIB.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: ianaEntityMIB.setOrganization('IANA')
class IANAPhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("energyObject", 13), ("battery", 14), ("storageDrive", 15))

mibBuilder.exportSymbols("IANA-ENTITY-MIB", IANAPhysicalClass=IANAPhysicalClass, PYSNMP_MODULE_ID=ianaEntityMIB, ianaEntityMIB=ianaEntityMIB)
