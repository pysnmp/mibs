#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:22:46 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Integer32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Counter32, MibIdentifier, IpAddress, enterprises, Unsigned32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Counter32", "MibIdentifier", "IpAddress", "enterprises", "Unsigned32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
mibBuilder.exportSymbols("VEL-MIB", PYSNMP_MODULE_ID=vel, vel=vel)
