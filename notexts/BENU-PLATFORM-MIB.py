#
# PySNMP MIB module BENU-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 10:02:56 2024
# On host fv-az1773-903 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, IpAddress, NotificationType, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, iso, Unsigned32, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "NotificationType", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "iso", "Unsigned32", "Bits", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatform = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1))
benuPlatform.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatform.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benuPlatform.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-MIB", benuPlatform=benuPlatform, PYSNMP_MODULE_ID=benuPlatform)
