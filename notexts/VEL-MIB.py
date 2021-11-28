#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 21:22:21 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, iso, Counter64, IpAddress, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks, Counter32, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "iso", "Counter64", "IpAddress", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks", "Counter32", "Bits", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
mibBuilder.exportSymbols("VEL-MIB", PYSNMP_MODULE_ID=vel, vel=vel)
