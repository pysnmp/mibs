#
# PySNMP MIB module GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/delta/GLOBAL-REG
# Produced by pysmi-1.1.8 at Thu Oct 12 08:16:18 2023
# On host fv-az585-225 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter64, iso, MibIdentifier, Gauge32, TimeTicks, enterprises, Unsigned32, Counter32, ModuleIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter64", "iso", "MibIdentifier", "Gauge32", "TimeTicks", "enterprises", "Unsigned32", "Counter32", "ModuleIdentity", "NotificationType", "Bits")
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
mibBuilder.exportSymbols("GLOBAL-REG", globalRegModule=globalRegModule, orion=orion, generic=generic, regs=regs, controller=controller, controllerOrionReg=controllerOrionReg, controllerReg=controllerReg, PYSNMP_MODULE_ID=globalRegModule, caps=caps, root=root, expr=expr, reg=reg, products=products, modules=modules, delta=delta)
