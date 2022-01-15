#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:29:47 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, ObjectIdentity, Bits, iso, Counter32, Gauge32, IpAddress, NotificationType, TimeTicks, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "ObjectIdentity", "Bits", "iso", "Counter32", "Gauge32", "IpAddress", "NotificationType", "TimeTicks", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitCommonRegModule=taitCommonRegModule, taitRegistrations=taitRegistrations, taitGeneric=taitGeneric, tait=tait, taitModules=taitModules, taitProducts=taitProducts, PYSNMP_MODULE_ID=taitCommonRegModule)
