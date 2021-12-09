#
# PySNMP MIB module GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/delta/GLOBAL-REG
# Produced by pysmi-1.1.3 at Thu Dec  9 15:33:26 2021
# On host fv-az39-899 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter64, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter64", "enterprises", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
globalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 1))
if mibBuilder.loadTexts: globalRegModule.setLastUpdated('201309131218Z')
if mibBuilder.loadTexts: globalRegModule.setOrganization('Delta Energy Systems (Switzerland) AG')
if mibBuilder.loadTexts: globalRegModule.setContactInfo('postal: Delta Energy Systems (Switzerland) AG\n                         Freiburgstrasse 251,\n                         CH-3018 Bern-Buempliz\n                 web:     www.deltapowersolutions.com\n                 email: adrian.pluess@delta-es.com')
if mibBuilder.loadTexts: globalRegModule.setDescription('The Delta Energy Systems (Switzerland) AG cental registration modules.')
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
if mibBuilder.loadTexts: controllerOrionReg.setDescription('The Controller Model Orion')
mibBuilder.exportSymbols("GLOBAL-REG", orion=orion, generic=generic, products=products, regs=regs, controllerReg=controllerReg, modules=modules, root=root, controller=controller, expr=expr, PYSNMP_MODULE_ID=globalRegModule, globalRegModule=globalRegModule, reg=reg, delta=delta, caps=caps, controllerOrionReg=controllerOrionReg)
