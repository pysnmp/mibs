#
# PySNMP MIB module IANA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-ENTITY-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:18:25 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Unsigned32, IpAddress, Integer32, mib_2, Counter64, MibIdentifier, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Unsigned32", "IpAddress", "Integer32", "mib-2", "Counter64", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaEntityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 216))
ianaEntityMIB.setRevisions(('2015-07-16 00:00', '2015-07-16 00:00', '2013-04-05 00:00',))
if mibBuilder.loadTexts: ianaEntityMIB.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: ianaEntityMIB.setOrganization('IANA')
class IANAPhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("energyObject", 13), ("battery", 14), ("storageDrive", 15))

mibBuilder.exportSymbols("IANA-ENTITY-MIB", ianaEntityMIB=ianaEntityMIB, IANAPhysicalClass=IANAPhysicalClass, PYSNMP_MODULE_ID=ianaEntityMIB)
