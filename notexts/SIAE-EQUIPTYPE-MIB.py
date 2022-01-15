#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:28:51 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, Integer32, Gauge32, Bits, NotificationType, IpAddress, Unsigned32, MibIdentifier, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Integer32", "Gauge32", "Bits", "NotificationType", "IpAddress", "Unsigned32", "MibIdentifier", "iso", "Counter32")
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
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeMib=equipTypeMib, equipTypeList=equipTypeList, equipTypeUnknown=equipTypeUnknown, PYSNMP_MODULE_ID=equipTypeMib, equipTypeAGS20=equipTypeAGS20, equipTypeALFO80HD=equipTypeALFO80HD, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeALFOplus2=equipTypeALFOplus2)
