#
# PySNMP MIB module MPLS-ID-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-ID-STD-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:59:48 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
MplsGlobalId, MplsIccId, MplsNodeId, MplsCcId = mibBuilder.importSymbols("MPLS-TC-EXT-STD-MIB", "MplsGlobalId", "MplsIccId", "MplsNodeId", "MplsCcId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, IpAddress, Unsigned32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Counter32, iso, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Unsigned32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Gauge32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 18))
mplsIdStdMIB.setRevisions(('2015-02-02 00:00',))
if mibBuilder.loadTexts: mplsIdStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
mplsIdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 0))
mplsIdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 1))
mplsIdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2))
mplsIdGlobalId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 1), MplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdGlobalId.setStatus('current')
mplsIdNodeId = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 2), MplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdNodeId.setStatus('current')
mplsIdCc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 3), MplsCcId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdCc.setStatus('current')
mplsIdIcc = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 18, 1, 4), MplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsIdIcc.setStatus('current')
mplsIdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1))
mplsIdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2))
mplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleFullCompliance = mplsIdModuleFullCompliance.setStatus('current')
mplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 1, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdIpOperatorGroup"), ("MPLS-ID-STD-MIB", "mplsIdIccOperatorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdModuleReadOnlyCompliance = mplsIdModuleReadOnlyCompliance.setStatus('current')
mplsIdIpOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 1)).setObjects(("MPLS-ID-STD-MIB", "mplsIdGlobalId"), ("MPLS-ID-STD-MIB", "mplsIdNodeId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIpOperatorGroup = mplsIdIpOperatorGroup.setStatus('current')
mplsIdIccOperatorGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 18, 2, 2, 2)).setObjects(("MPLS-ID-STD-MIB", "mplsIdNodeId"), ("MPLS-ID-STD-MIB", "mplsIdCc"), ("MPLS-ID-STD-MIB", "mplsIdIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsIdIccOperatorGroup = mplsIdIccOperatorGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-ID-STD-MIB", mplsIdGlobalId=mplsIdGlobalId, mplsIdIpOperatorGroup=mplsIdIpOperatorGroup, mplsIdIcc=mplsIdIcc, PYSNMP_MODULE_ID=mplsIdStdMIB, mplsIdModuleReadOnlyCompliance=mplsIdModuleReadOnlyCompliance, mplsIdStdMIB=mplsIdStdMIB, mplsIdIccOperatorGroup=mplsIdIccOperatorGroup, mplsIdConformance=mplsIdConformance, mplsIdModuleFullCompliance=mplsIdModuleFullCompliance, mplsIdCompliances=mplsIdCompliances, mplsIdNotifications=mplsIdNotifications, mplsIdNodeId=mplsIdNodeId, mplsIdCc=mplsIdCc, mplsIdGroups=mplsIdGroups, mplsIdObjects=mplsIdObjects)
