#
# PySNMP MIB module SENSATRONICS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-SMI
# Produced by pysmi-1.1.3 at Sun Nov 28 19:20:39 2021
# On host fv-az83-233 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, IpAddress, TimeTicks, Gauge32, Integer32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Unsigned32, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Bits", "enterprises")
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
mibBuilder.exportSymbols("SENSATRONICS-SMI", productEM1=productEM1, sensatronics=sensatronics, consumerTools=consumerTools, PYSNMP_MODULE_ID=sensatronics, productCRYO=productCRYO, consumerProducts=consumerProducts, envMonitors=envMonitors, productITTM=productITTM, customTools=customTools, customProducts=customProducts)
