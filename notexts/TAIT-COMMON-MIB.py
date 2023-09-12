#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 09:50:08 2023
# On host fv-az502-117 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, Bits, Counter64, iso, enterprises, NotificationType, IpAddress, Integer32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "iso", "enterprises", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "ModuleIdentity")
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
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitRegistrations=taitRegistrations, taitModules=taitModules, taitCommonRegModule=taitCommonRegModule, taitProducts=taitProducts, PYSNMP_MODULE_ID=taitCommonRegModule, tait=tait, taitGeneric=taitGeneric)
