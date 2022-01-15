#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 23:32:27 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, iso, Unsigned32, IpAddress, MibIdentifier, Integer32, Bits, ModuleIdentity, Counter32, Gauge32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "Bits", "ModuleIdentity", "Counter32", "Gauge32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
equipTypeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 501))
equipTypeMib.setRevisions(('2015-04-23 00:00', '2014-10-29 00:00', '2014-06-23 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: equipTypeMib.setLastUpdated('201504230000Z')
if mibBuilder.loadTexts: equipTypeMib.setOrganization('SIAE MICROELETTRONICA spa')
equipTypeList = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5))
equipTypeUnknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 1))
if mibBuilder.loadTexts: equipTypeUnknown.setStatus('current')
equipTypeALFO80HD = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 74))
if mibBuilder.loadTexts: equipTypeALFO80HD.setStatus('current')
equipTypeALFO80HDsm = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 75))
if mibBuilder.loadTexts: equipTypeALFO80HDsm.setStatus('current')
equipTypeAGS20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 76))
if mibBuilder.loadTexts: equipTypeAGS20.setStatus('current')
equipTypeALFOplus2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 77))
if mibBuilder.loadTexts: equipTypeALFOplus2.setStatus('current')
equipTypeEasyCellGateway = ObjectIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 1, 5, 78))
if mibBuilder.loadTexts: equipTypeEasyCellGateway.setStatus('current')
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", equipTypeList=equipTypeList, equipTypeALFO80HD=equipTypeALFO80HD, PYSNMP_MODULE_ID=equipTypeMib, equipTypeMib=equipTypeMib, equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeUnknown=equipTypeUnknown, equipTypeAGS20=equipTypeAGS20, equipTypeALFOplus2=equipTypeALFOplus2)
