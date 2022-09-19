#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 07:27:13 2022
# On host fv-az215-626 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
miniLink, = mibBuilder.importSymbols("MINI-LINK-MIB", "miniLink")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, IpAddress, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2))
pt.setRevisions(('2017-01-21 12:00', '2016-03-09 12:00', '2016-02-10 12:30',))
if mibBuilder.loadTexts: pt.setLastUpdated('201701211200Z')
if mibBuilder.loadTexts: pt.setOrganization('Ericsson')
ptDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptDeviceType.setStatus('current')
ptConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8))
ptCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1))
ptGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2))
ptCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1, 1)).setObjects(("PT-MIB", "ptCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompliance = ptCompliance.setStatus('current')
ptCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2, 1)).setObjects(("PT-MIB", "ptDeviceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompleteGroup = ptCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-MIB", PYSNMP_MODULE_ID=pt, ptCompliance=ptCompliance, ptDeviceType=ptDeviceType, ptCompleteGroup=ptCompleteGroup, pt=pt, ptCompliances=ptCompliances, ptGroups=ptGroups, ptConformance=ptConformance)
