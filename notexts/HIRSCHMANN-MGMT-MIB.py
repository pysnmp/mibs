#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:03:57 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Integer32, Bits, iso, IpAddress, Unsigned32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectIdentity, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Integer32", "Bits", "iso", "IpAddress", "Unsigned32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectIdentity", "Gauge32", "enterprises")
TextualConvention, DisplayString, AutonomousType, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "AutonomousType", "TestAndIncr")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", PYSNMP_MODULE_ID=hmManagement, hirschmann=hirschmann, hmManagement=hmManagement)
