#
# PySNMP MIB module SENSATRONICS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-SMI
# Produced by pysmi-1.1.11 at Wed Apr  3 14:56:19 2024
# On host fv-az1198-695 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter64, iso, ModuleIdentity, ObjectIdentity, Counter32, enterprises, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter64", "iso", "ModuleIdentity", "ObjectIdentity", "Counter32", "enterprises", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sensatronics = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174))
sensatronics.setRevisions(('2004-04-20 00:00',))
if mibBuilder.loadTexts: sensatronics.setLastUpdated('200404200000Z')
if mibBuilder.loadTexts: sensatronics.setOrganization('Sensatronics LLC')
consumerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1))
if mibBuilder.loadTexts: consumerProducts.setStatus('current')
envMonitors = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1))
if mibBuilder.loadTexts: envMonitors.setStatus('current')
consumerTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 2))
if mibBuilder.loadTexts: consumerTools.setStatus('current')
customProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 3))
if mibBuilder.loadTexts: customProducts.setStatus('current')
customTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 4))
if mibBuilder.loadTexts: customTools.setStatus('current')
productITTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1))
if mibBuilder.loadTexts: productITTM.setStatus('current')
productCRYO = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 2))
if mibBuilder.loadTexts: productCRYO.setStatus('current')
productEM1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3))
if mibBuilder.loadTexts: productEM1.setStatus('current')
mibBuilder.exportSymbols("SENSATRONICS-SMI", sensatronics=sensatronics, PYSNMP_MODULE_ID=sensatronics, consumerProducts=consumerProducts, productEM1=productEM1, consumerTools=consumerTools, productCRYO=productCRYO, productITTM=productITTM, customTools=customTools, envMonitors=envMonitors, customProducts=customProducts)
