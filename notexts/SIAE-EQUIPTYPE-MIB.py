#
# PySNMP MIB module SIAE-EQUIPTYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-EQUIPTYPE-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:44:22 2024
# On host fv-az973-242 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Counter64, Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "iso", "Bits")
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
mibBuilder.exportSymbols("SIAE-EQUIPTYPE-MIB", equipTypeAGS20=equipTypeAGS20, equipTypeList=equipTypeList, equipTypeALFO80HDsm=equipTypeALFO80HDsm, equipTypeUnknown=equipTypeUnknown, PYSNMP_MODULE_ID=equipTypeMib, equipTypeMib=equipTypeMib, equipTypeALFO80HD=equipTypeALFO80HD, equipTypeEasyCellGateway=equipTypeEasyCellGateway, equipTypeALFOplus2=equipTypeALFOplus2)
