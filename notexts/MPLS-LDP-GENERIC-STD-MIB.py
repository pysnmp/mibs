#
# PySNMP MIB module MPLS-LDP-GENERIC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source MPLS-LDP-GENERIC-STD-MIB
# Source digest sha256:60a78f9f8cf40bc9fd9f624a7117f1685d5d5b4fff92aecc36dfbe1ee1b8a4b6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
mplsLdpEntityIndex, mplsLdpEntityLdpId = mibBuilder.importSymbols("MPLS-LDP-STD-MIB", "mplsLdpEntityIndex", "mplsLdpEntityLdpId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention")
mplsLdpGenericStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 7))
mplsLdpGenericStdMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setLastUpdated('2004-06-03 00:00')
if mibBuilder.loadTexts: mplsLdpGenericStdMIB.setOrganization('Multiprotocol Label Switching (mpls) Working Group')
mplsLdpGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1))
mplsLdpGenericConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 2))
mplsLdpEntityGenericObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1))
mplsLdpEntityGenericLRTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRTable.setStatus('current')
mplsLdpEntityGenericLREntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "MPLS-LDP-STD-MIB", "mplsLdpEntityLdpId"), (0, "MPLS-LDP-STD-MIB", "mplsLdpEntityIndex"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMin"), (0, "MPLS-LDP-GENERIC-STD-MIB", "mplsLdpEntityGenericLRMax"))
if mibBuilder.loadTexts: mplsLdpEntityGenericLREntry.setStatus('current')
mplsLdpEntityGenericLRMin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: mplsLdpEntityGenericLRMin.setStatus('current')
mplsLdpEntityGenericLRMax = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 7, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048575))).setMaxAccess("notaccessible")
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
mibBuilder.exportSymbols("MPLS-LDP-GENERIC-STD-MIB", PYSNMP_MODULE_ID=mplsLdpGenericStdMIB, mplsLdpEntityGenericIfIndexOrZero=mplsLdpEntityGenericIfIndexOrZero, mplsLdpEntityGenericLREntry=mplsLdpEntityGenericLREntry, mplsLdpEntityGenericLRMax=mplsLdpEntityGenericLRMax, mplsLdpEntityGenericLRMin=mplsLdpEntityGenericLRMin, mplsLdpEntityGenericLRRowStatus=mplsLdpEntityGenericLRRowStatus, mplsLdpEntityGenericLRStorageType=mplsLdpEntityGenericLRStorageType, mplsLdpEntityGenericLRTable=mplsLdpEntityGenericLRTable, mplsLdpEntityGenericLabelSpace=mplsLdpEntityGenericLabelSpace, mplsLdpEntityGenericObjects=mplsLdpEntityGenericObjects, mplsLdpGenericCompliances=mplsLdpGenericCompliances, mplsLdpGenericConformance=mplsLdpGenericConformance, mplsLdpGenericGroup=mplsLdpGenericGroup, mplsLdpGenericGroups=mplsLdpGenericGroups, mplsLdpGenericModuleFullCompliance=mplsLdpGenericModuleFullCompliance, mplsLdpGenericModuleReadOnlyCompliance=mplsLdpGenericModuleReadOnlyCompliance, mplsLdpGenericObjects=mplsLdpGenericObjects, mplsLdpGenericStdMIB=mplsLdpGenericStdMIB)
