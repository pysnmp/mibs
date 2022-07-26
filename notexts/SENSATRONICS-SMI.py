#
# PySNMP MIB module SENSATRONICS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-SMI
# Produced by pysmi-1.1.8 at Tue Jul 26 15:51:05 2022
# On host fv-az299-344 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, ModuleIdentity, enterprises, Bits, NotificationType, Unsigned32, Counter32, Integer32, iso, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "ModuleIdentity", "enterprises", "Bits", "NotificationType", "Unsigned32", "Counter32", "Integer32", "iso", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SENSATRONICS-SMI", consumerProducts=consumerProducts, sensatronics=sensatronics, customTools=customTools, productITTM=productITTM, envMonitors=envMonitors, customProducts=customProducts, productEM1=productEM1, PYSNMP_MODULE_ID=sensatronics, productCRYO=productCRYO, consumerTools=consumerTools)
