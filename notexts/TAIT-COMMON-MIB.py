#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:55:24 2024
# On host fv-az1490-927 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, Gauge32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, Bits, Integer32, Counter64, Counter32, NotificationType, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Gauge32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "Bits", "Integer32", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitCommonRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 1))
taitCommonRegModule.setRevisions(('2012-02-20 12:00',))
if mibBuilder.loadTexts: taitCommonRegModule.setLastUpdated('201202201200Z')
if mibBuilder.loadTexts: taitCommonRegModule.setOrganization('www.taitradio.com')
tait = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570))
if mibBuilder.loadTexts: tait.setStatus('current')
taitRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1))
if mibBuilder.loadTexts: taitRegistrations.setStatus('current')
taitModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1))
if mibBuilder.loadTexts: taitModules.setStatus('current')
taitGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 2))
if mibBuilder.loadTexts: taitGeneric.setStatus('current')
taitProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 3))
if mibBuilder.loadTexts: taitProducts.setStatus('current')
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitModules=taitModules, taitGeneric=taitGeneric, taitProducts=taitProducts, PYSNMP_MODULE_ID=taitCommonRegModule, taitRegistrations=taitRegistrations, tait=tait, taitCommonRegModule=taitCommonRegModule)
