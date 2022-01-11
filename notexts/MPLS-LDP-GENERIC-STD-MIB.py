#
# PySNMP MIB module MPLS-LDP-GENERIC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-LDP-GENERIC-STD-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:07:55 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityLdpId, mplsLdpEntityIndex = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId", "mplsLdpEntityIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, MibIdentifier, IpAddress, Integer32, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits", "iso", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "StorageType")
mplsLdpGenericStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 7))
mplsLdpGenericStdMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setOrganization('Multiprotocol Label Switching (mpls) Working Group')
mplsLdpGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1))
mplsLdpGenericConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2))
mplsLdpEntityGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1))
mplsLdpEntityGenericLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1), )
if mibBuilder.loadTexts: mplsLdpEntityGenericLRTable.setStatus('current')
mplsLdpEntityGenericLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1), ).setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMin"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMax"))
if mibBuilder.loadTexts: mplsLdpEntityGenericLREntry.setStatus('current')
mplsLdpEntityGenericLRMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMin.setStatus('current')
mplsLdpEntityGenericLRMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575)))
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMax.setStatus('current')
mplsLdpEntityGenericLabelSpace = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("perPlatform", 1), ("perInterface", 2))).clone('perPlatform')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLabelSpace.setStatus('current')
mplsLdpEntityGenericIfIndexOrZero = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericIfIndexOrZero.setStatus('current')
mplsLdpEntityGenericLRStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRStorageType.setStatus('current')
mplsLdpEntityGenericLRRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRRowStatus.setStatus('current')
mplsLdpGenericGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1))
mplsLdpGenericCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2))
mplsLdpGenericModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleFullCompliance = mplsLdpGenericModuleFullCompliance.setStatus('current')
mplsLdpGenericModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 2, 2)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpGenericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericModuleReadOnlyCompliance = mplsLdpGenericModuleReadOnlyCompliance.setStatus('current')
mplsLdpGenericGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 7, 2, 1, 1)).setObjects(("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLabelSpace"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericIfIndexOrZero"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRStorageType"), ("MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsLdpGenericGroup = mplsLdpGenericGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-STD-MIB", mplsLdpGenericObjects=mplsLdpGenericObjects, mplsLdpEntityGenericLRStorageType=mplsLdpEntityGenericLRStorageType, mplsLdpEntityGenericLRRowStatus=mplsLdpEntityGenericLRRowStatus, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpGenericStdMIB=mplsLdpGenericStdMIB, mplsLdpGenericModuleReadOnlyCompliance=mplsLdpGenericModuleReadOnlyCompliance, mplsLdpEntityGenericLabelSpace=mplsLdpEntityGenericLabelSpace, mplsLdpEntityGenericLREntry=mplsLdpEntityGenericLREntry, mplsLdpGenericCompliances=mplsLdpGenericCompliances, PYSNMP_MODULE_ID=mplsLdpGenericStdMIB, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpEntityGenericLRMax=mplsLdpEntityGenericLRMax, mplsLdpEntityGenericIfIndexOrZero=mplsLdpEntityGenericIfIndexOrZero, mplsLdpGenericConformance=mplsLdpGenericConformance, mplsLdpGenericModuleFullCompliance=mplsLdpGenericModuleFullCompliance, mplsLdpEntityGenericLRMin=mplsLdpEntityGenericLRMin, mplsLdpEntityGenericLRTable=mplsLdpEntityGenericLRTable, mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects)
