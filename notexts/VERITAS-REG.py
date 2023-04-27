#
# PySNMP MIB module VERITAS-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-REG.mib
# Produced by pysmi-1.1.8 at Thu Apr 27 10:46:42 2023
# On host fv-az988-178 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, Bits, ObjectIdentity, Integer32, Gauge32, NotificationType, TimeTicks, MibIdentifier, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "Bits", "ObjectIdentity", "Integer32", "Gauge32", "NotificationType", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter32")
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
mibBuilder.exportSymbols("VERITAS-REG", veritasGlobalRegModule=veritasGlobalRegModule, veritas=veritas, PYSNMP_MODULE_ID=veritasGlobalRegModule, products=products, veritasModules=veritasModules)
