#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 12:06:21 2023
# On host fv-az741-387 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter32, Counter64, Unsigned32, ObjectIdentity, Gauge32, TimeTicks, NotificationType, enterprises, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32", "TimeTicks", "NotificationType", "enterprises", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
if mibBuilder.loadTexts: barracuda.setContactInfo('\n            Barracuda Networks Inc.\n            3175 S. Winchester Blvd.\n            Campbell, CA 95008\n            ')
if mibBuilder.loadTexts: barracuda.setDescription('\n            Main Barracuda MIB\n            ')
mibBuilder.exportSymbols("BARRACUDA-REF", PYSNMP_MODULE_ID=barracuda, barracuda=barracuda)
