#
# PySNMP MIB module MPLS-ID-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MPLS-ID-STD-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:30:22 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
MplsGlobalId, MplsCcId, MplsNodeId, MplsIccId = mibBuilder.importSymbols("MPLS-TC-EXT-STD-MIB", "MplsGlobalId", "MplsCcId", "MplsNodeId", "MplsIccId")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Gauge32, iso, Integer32, NotificationType, Counter64, IpAddress, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Gauge32", "iso", "Integer32", "NotificationType", "Counter64", "IpAddress", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("MPLS-ID-STD-MIB", mplsIdNotifications=mplsIdNotifications, mplsIdGlobalId=mplsIdGlobalId, mplsIdStdMIB=mplsIdStdMIB, PYSNMP_MODULE_ID=mplsIdStdMIB, mplsIdIccOperatorGroup=mplsIdIccOperatorGroup, mplsIdGroups=mplsIdGroups, mplsIdIcc=mplsIdIcc, mplsIdCc=mplsIdCc, mplsIdModuleReadOnlyCompliance=mplsIdModuleReadOnlyCompliance, mplsIdCompliances=mplsIdCompliances, mplsIdObjects=mplsIdObjects, mplsIdModuleFullCompliance=mplsIdModuleFullCompliance, mplsIdNodeId=mplsIdNodeId, mplsIdIpOperatorGroup=mplsIdIpOperatorGroup, mplsIdConformance=mplsIdConformance)
