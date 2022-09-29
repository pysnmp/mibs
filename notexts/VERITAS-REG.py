#
# PySNMP MIB module VERITAS-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-REG.mib
# Produced by pysmi-1.1.8 at Thu Sep 29 13:20:03 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, Counter32, Integer32, NotificationType, Unsigned32, ModuleIdentity, Bits, enterprises, TimeTicks, Counter64, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter32", "Integer32", "NotificationType", "Unsigned32", "ModuleIdentity", "Bits", "enterprises", "TimeTicks", "Counter64", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("VERITAS-REG", veritasModules=veritasModules, PYSNMP_MODULE_ID=veritasGlobalRegModule, products=products, veritas=veritas, veritasGlobalRegModule=veritasGlobalRegModule)
