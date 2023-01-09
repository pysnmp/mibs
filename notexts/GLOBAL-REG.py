#
# PySNMP MIB module GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/delta/GLOBAL-REG
# Produced by pysmi-1.1.8 at Mon Jan  9 13:35:38 2023
# On host fv-az210-608 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Counter64, ObjectIdentity, ModuleIdentity, Gauge32, enterprises, Bits, MibIdentifier, Integer32, TimeTicks, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Counter64", "ObjectIdentity", "ModuleIdentity", "Gauge32", "enterprises", "Bits", "MibIdentifier", "Integer32", "TimeTicks", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("GLOBAL-REG", controllerOrionReg=controllerOrionReg, delta=delta, reg=reg, caps=caps, products=products, orion=orion, globalRegModule=globalRegModule, regs=regs, expr=expr, controllerReg=controllerReg, controller=controller, generic=generic, root=root, PYSNMP_MODULE_ID=globalRegModule, modules=modules)
