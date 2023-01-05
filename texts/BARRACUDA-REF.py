#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:24:41 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Gauge32, iso, Unsigned32, MibIdentifier, ObjectIdentity, Bits, NotificationType, Counter64, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType", "Counter64", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
if mibBuilder.loadTexts: barracuda.setContactInfo('\n            Barracuda Networks Inc.\n            3175 S. Winchester Blvd.\n            Campbell, CA 95008\n            ')
if mibBuilder.loadTexts: barracuda.setDescription('\n            Main Barracuda MIB\n            ')
mibBuilder.exportSymbols("BARRACUDA-REF", PYSNMP_MODULE_ID=barracuda, barracuda=barracuda)
