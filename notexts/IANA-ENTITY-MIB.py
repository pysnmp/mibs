#
# PySNMP MIB module IANA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-ENTITY-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:51:58 2024
# On host fv-az530-296 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Bits, mib_2, Counter64, ModuleIdentity, NotificationType, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter32, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Bits", "mib-2", "Counter64", "ModuleIdentity", "NotificationType", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter32", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaEntityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 216))
ianaEntityMIB.setRevisions(('2015-07-16 00:00', '2015-07-16 00:00', '2013-04-05 00:00',))
if mibBuilder.loadTexts: ianaEntityMIB.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: ianaEntityMIB.setOrganization('IANA')
class IANAPhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("energyObject", 13), ("battery", 14), ("storageDrive", 15))

mibBuilder.exportSymbols("IANA-ENTITY-MIB", IANAPhysicalClass=IANAPhysicalClass, ianaEntityMIB=ianaEntityMIB, PYSNMP_MODULE_ID=ianaEntityMIB)
