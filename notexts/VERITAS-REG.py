#
# PySNMP MIB module VERITAS-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-REG.mib
# Produced by pysmi-1.1.12 at Wed Dec  4 18:00:12 2024
# On host fv-az2036-124 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, enterprises, Unsigned32, iso, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Counter32, ModuleIdentity, IpAddress, Integer32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "Unsigned32", "iso", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Counter32", "ModuleIdentity", "IpAddress", "Integer32", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veritasGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1302, 5, 1))
veritasGlobalRegModule.setRevisions(('1901-09-05 04:45', '1901-10-22 22:30',))
if mibBuilder.loadTexts: veritasGlobalRegModule.setLastUpdated('0109050445Z')
if mibBuilder.loadTexts: veritasGlobalRegModule.setOrganization('VERITAS Software Corporation')
veritas = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302))
if mibBuilder.loadTexts: veritas.setStatus('current')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302, 3))
if mibBuilder.loadTexts: products.setStatus('current')
veritasModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302, 5))
if mibBuilder.loadTexts: veritasModules.setStatus('current')
mibBuilder.exportSymbols("VERITAS-REG", veritas=veritas, veritasModules=veritasModules, PYSNMP_MODULE_ID=veritasGlobalRegModule, products=products, veritasGlobalRegModule=veritasGlobalRegModule)
