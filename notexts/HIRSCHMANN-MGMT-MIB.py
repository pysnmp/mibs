#
# PySNMP MIB module HIRSCHMANN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/HIRSCHMANN-MGMT-MIB
# Produced by pysmi-1.1.12 at Fri Apr 12 00:28:49 2024
# On host fv-az975-788 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32, NotificationType, Bits, iso, TimeTicks, Counter32, Gauge32, Counter64, ObjectIdentity, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32", "NotificationType", "Bits", "iso", "TimeTicks", "Counter32", "Gauge32", "Counter64", "ObjectIdentity", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString, AutonomousType, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "AutonomousType", "TestAndIncr")
hmManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 16))
hmManagement.setRevisions(('2010-09-14 12:00',))
if mibBuilder.loadTexts: hmManagement.setLastUpdated('201009141200Z')
if mibBuilder.loadTexts: hmManagement.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
mibBuilder.exportSymbols("HIRSCHMANN-MGMT-MIB", hirschmann=hirschmann, hmManagement=hmManagement, PYSNMP_MODULE_ID=hmManagement)
