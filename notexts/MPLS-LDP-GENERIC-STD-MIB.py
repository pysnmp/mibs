#
# PySNMP MIB module MPLS-LDP-GENERIC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-LDP-GENERIC-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:27:40 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityLdpId, mplsLdpEntityIndex = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId", "mplsLdpEntityIndex")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, NotificationType, Integer32, Bits, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "NotificationType", "Integer32", "Bits", "Counter32", "Counter64", "IpAddress")
RowStatus, StorageType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-STD-MIB", mplsLdpEntityGenericLRMin=mplsLdpEntityGenericLRMin, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpEntityGenericLRMax=mplsLdpEntityGenericLRMax, mplsLdpGenericCompliances=mplsLdpGenericCompliances, mplsLdpEntityGenericIfIndexOrZero=mplsLdpEntityGenericIfIndexOrZero, mplsLdpGenericObjects=mplsLdpGenericObjects, mplsLdpEntityGenericLabelSpace=mplsLdpEntityGenericLabelSpace, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpGenericModuleFullCompliance=mplsLdpGenericModuleFullCompliance, mplsLdpGenericModuleReadOnlyCompliance=mplsLdpGenericModuleReadOnlyCompliance, mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects, mplsLdpEntityGenericLRRowStatus=mplsLdpEntityGenericLRRowStatus, mplsLdpEntityGenericLREntry=mplsLdpEntityGenericLREntry, mplsLdpEntityGenericLRStorageType=mplsLdpEntityGenericLRStorageType, PYSNMP_MODULE_ID=mplsLdpGenericStdMIB, mplsLdpGenericStdMIB=mplsLdpGenericStdMIB, mplsLdpEntityGenericLRTable=mplsLdpEntityGenericLRTable, mplsLdpGenericConformance=mplsLdpGenericConformance)
