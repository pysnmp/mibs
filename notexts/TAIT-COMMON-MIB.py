#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:44:57 2024
# On host fv-az1210-277 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, enterprises, TimeTicks, Gauge32, IpAddress, MibIdentifier, ObjectIdentity, Integer32, iso, Counter64, Bits, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "enterprises", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "iso", "Counter64", "Bits", "NotificationType", "Unsigned32")
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
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitModules=taitModules, tait=tait, taitGeneric=taitGeneric, taitRegistrations=taitRegistrations, PYSNMP_MODULE_ID=taitCommonRegModule, taitCommonRegModule=taitCommonRegModule, taitProducts=taitProducts)
