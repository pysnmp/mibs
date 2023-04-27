#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 11:45:00 2023
# On host fv-az561-589 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, Bits, Counter64, ModuleIdentity, TimeTicks, Unsigned32, Gauge32, enterprises, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "TimeTicks", "Unsigned32", "Gauge32", "enterprises", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "iso", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
mibBuilder.exportSymbols("VEL-MIB", vel=vel, PYSNMP_MODULE_ID=vel)
