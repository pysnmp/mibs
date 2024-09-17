#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:56:48 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
miniLink, = mibBuilder.importSymbols("MINI-LINK-MIB", "miniLink")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier, Integer32, Bits, Gauge32, Counter32, iso, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "Gauge32", "Counter32", "iso", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("PT-MIB", pt=pt, ptGroups=ptGroups, ptConformance=ptConformance, ptCompliance=ptCompliance, ptDeviceType=ptDeviceType, ptCompliances=ptCompliances, ptCompleteGroup=ptCompleteGroup, PYSNMP_MODULE_ID=pt)
