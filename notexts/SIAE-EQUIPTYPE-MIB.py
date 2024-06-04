#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 14:16:43 2024
# On host fv-az693-600 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Integer32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "Bits")
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
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", equipTypeALFOplus2=equipTypeALFOplus2, PYSNMP_MODULE_ID=equipTypeMib, equipTypeALFO80HD=equipTypeALFO80HD, equipTypeAGS20=equipTypeAGS20, equipTypeUnknown=equipTypeUnknown, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeMib=equipTypeMib, equipTypeList=equipTypeList)
