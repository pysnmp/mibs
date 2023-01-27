#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.8 at Fri Jan 27 14:06:49 2023
# On host fv-az417-962 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, ModuleIdentity, Counter64, Gauge32, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, MibIdentifier, Bits, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "MibIdentifier", "Bits", "enterprises", "IpAddress")
DisplayString, TestAndIncr, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TextualConvention", "AutonomousType")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hmManagement=hmManagement, hirschmann=hirschmann, PYSNMP_MODULE_ID=hmManagement)
