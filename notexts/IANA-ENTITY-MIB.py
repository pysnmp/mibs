#
# PySNMP MIB module IANA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-ENTITY-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:17:22 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, Counter64, ObjectIdentity, TimeTicks, mib_2, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter32, ModuleIdentity, IpAddress, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Counter64", "ObjectIdentity", "TimeTicks", "mib-2", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "IpAddress", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaEntityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 216))
ianaEntityMIB.setRevisions(('2015-07-16 00:00', '2015-07-16 00:00', '2013-04-05 00:00',))
if mibBuilder.loadTexts: ianaEntityMIB.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: ianaEntityMIB.setOrganization('IANA')
class IANAPhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("energyObject", 13), ("battery", 14), ("storageDrive", 15))

mibBuilder.exportSymbols("IANA-ENTITY-MIB", PYSNMP_MODULE_ID=ianaEntityMIB, IANAPhysicalClass=IANAPhysicalClass, ianaEntityMIB=ianaEntityMIB)
