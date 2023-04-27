#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 09:17:27 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, ModuleIdentity, Integer32, iso, Counter32, ObjectIdentity, enterprises, MibIdentifier, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "Counter32", "ObjectIdentity", "enterprises", "MibIdentifier", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
if mibBuilder.loadTexts: barracuda.setContactInfo('\n            Barracuda Networks Inc.\n            3175 S. Winchester Blvd.\n            Campbell, CA 95008\n            ')
if mibBuilder.loadTexts: barracuda.setDescription('\n            Main Barracuda MIB\n            ')
mibBuilder.exportSymbols("BARRACUDA-REF", barracuda=barracuda, PYSNMP_MODULE_ID=barracuda)
