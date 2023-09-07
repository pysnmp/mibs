#
# PySNMP MIB module GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/delta/GLOBAL-REG
# Produced by pysmi-1.1.8 at Thu Sep  7 13:56:19 2023
# On host fv-az444-965 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Bits, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, enterprises, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Bits", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "enterprises", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
globalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 1))
if mibBuilder.loadTexts: globalRegModule.setLastUpdated('201309131218Z')
if mibBuilder.loadTexts: globalRegModule.setOrganization('Delta Energy Systems (Switzerland) AG')
delta = MibIdentifier((1, 3, 6, 1, 4, 1, 20246))
root = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2))
reg = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 1))
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 1, 1))
generic = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 2))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 3))
controller = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 3, 1))
orion = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1))
caps = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 4))
regs = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 5))
expr = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 6))
controllerReg = MibIdentifier((1, 3, 6, 1, 4, 1, 20246, 2, 1, 2))
controllerOrionReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 20246, 2, 1, 2, 1))
if mibBuilder.loadTexts: controllerOrionReg.setStatus('current')
mibBuilder.exportSymbols("GLOBAL-REG", regs=regs, controller=controller, root=root, generic=generic, controllerReg=controllerReg, delta=delta, reg=reg, orion=orion, PYSNMP_MODULE_ID=globalRegModule, caps=caps, expr=expr, products=products, globalRegModule=globalRegModule, controllerOrionReg=controllerOrionReg, modules=modules)
