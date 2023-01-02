#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 15:29:49 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, IpAddress, NotificationType, ModuleIdentity, TimeTicks, Bits, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "IpAddress", "NotificationType", "ModuleIdentity", "TimeTicks", "Bits", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "Counter64", "Counter32", "Gauge32")
TextualConvention, TestAndIncr, DisplayString, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "DisplayString", "AutonomousType")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hirschmann=hirschmann, PYSNMP_MODULE_ID=hmManagement, hmManagement=hmManagement)
