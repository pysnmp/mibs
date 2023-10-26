#
# PySNMP MIB module BARRACUDA-REF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/barracuda/BARRACUDA-REF-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 12:07:57 2023
# On host fv-az1234-823 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, MibIdentifier, enterprises, TimeTicks, Bits, Counter64, NotificationType, Counter32, ObjectIdentity, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "MibIdentifier", "enterprises", "TimeTicks", "Bits", "Counter64", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
barracuda = ModuleIdentity((1, 3, 6, 1, 4, 1, 20632))
if mibBuilder.loadTexts: barracuda.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: barracuda.setOrganization('Barracuda Networks, Inc.')
mibBuilder.exportSymbols("BARRACUDA-REF", barracuda=barracuda, PYSNMP_MODULE_ID=barracuda)
