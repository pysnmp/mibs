#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 07:28:46 2022
# On host fv-az215-626 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, ObjectIdentity, TimeTicks, Counter32, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits")
AutonomousType, DisplayString, TextualConvention, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention", "TestAndIncr")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hmManagement=hmManagement, hirschmann=hirschmann, PYSNMP_MODULE_ID=hmManagement)
