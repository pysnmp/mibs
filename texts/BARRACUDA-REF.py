#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:00:08 2024
# On host fv-az1433-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Counter64, Unsigned32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, NotificationType, enterprises, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "Unsigned32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "NotificationType", "enterprises", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
if mibBuilder.loadTexts: barracuda.setContactInfo('\n            Barracuda Networks Inc.\n            3175 S. Winchester Blvd.\n            Campbell, CA 95008\n            ')
if mibBuilder.loadTexts: barracuda.setDescription('\n            Main Barracuda MIB\n            ')
mibBuilder.exportSymbols("BARRACUDA-REF", PYSNMP_MODULE_ID=barracuda, barracuda=barracuda)
