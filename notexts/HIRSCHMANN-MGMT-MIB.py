#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 13:52:22 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Unsigned32, iso, MibIdentifier, IpAddress, ObjectIdentity, NotificationType, Gauge32, ModuleIdentity, Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "iso", "MibIdentifier", "IpAddress", "ObjectIdentity", "NotificationType", "Gauge32", "ModuleIdentity", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32")
TextualConvention, AutonomousType, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "TestAndIncr", "DisplayString")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hmManagement=hmManagement, PYSNMP_MODULE_ID=hmManagement, hirschmann=hirschmann)
