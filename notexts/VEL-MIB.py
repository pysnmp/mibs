#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.8 at Thu Jan 27 21:20:17 2022
# On host fv-az74-168 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, enterprises, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, TimeTicks, Counter32, Integer32, Bits, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "enterprises", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "TimeTicks", "Counter32", "Integer32", "Bits", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
mibBuilder.exportSymbols("VEL-MIB", PYSNMP_MODULE_ID=vel, vel=vel)
