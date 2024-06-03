#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:21:39 2024
# On host fv-az1380-78 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, NotificationType, ObjectIdentity, Counter32, IpAddress, Bits, Gauge32, enterprises, iso, TimeTicks, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "IpAddress", "Bits", "Gauge32", "enterprises", "iso", "TimeTicks", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TestAndIncr, TextualConvention, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "TextualConvention", "AutonomousType", "DisplayString")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hmManagement=hmManagement, PYSNMP_MODULE_ID=hmManagement, hirschmann=hirschmann)
