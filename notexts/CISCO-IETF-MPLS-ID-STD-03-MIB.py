#
# PySNMP MIB module CISCO-IETF-MPLS-ID-STD-03-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-MPLS-ID-STD-03-MIB
# Source digest sha256:44933a8183fcdb6b4c83424c874d27ae5d8ee15c23890b76e5608216e1785e4b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CMplsGlobalId, CMplsIccId, CMplsNodeId = mibBuilder.importSymbols("CISCO-MPLS-TC-EXT-STD-MIB", "CMplsGlobalId", "CMplsIccId", "CMplsNodeId")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmplsIdStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 147))
cmplsIdStdMIB.setRevisions(('2012-04-08 00:00',))
if mibBuilder.loadTexts: cmplsIdStdMIB.setLastUpdated('2012-06-07 00:00')
if mibBuilder.loadTexts: cmplsIdStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsIdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 0))
cmplsIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 1))
cmplsIdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2))
cmplsGlobalId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 1), CMplsGlobalId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsGlobalId.setStatus('current')
cmplsIcc = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 2), CMplsIccId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsIcc.setStatus('current')
cmplsNodeId = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 147, 1, 3), CMplsNodeId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmplsNodeId.setStatus('current')
cmplsIdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1))
cmplsIdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2))
cmplsIdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleFullCompliance = cmplsIdModuleFullCompliance.setStatus('current')
cmplsIdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 2, 2)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIdScalarGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdModuleReadOnlyCompliance = cmplsIdModuleReadOnlyCompliance.setStatus('current')
cmplsIdScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 147, 2, 1, 1)).setObjects(("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsGlobalId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsNodeId"), ("CISCO-IETF-MPLS-ID-STD-03-MIB", "cmplsIcc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsIdScalarGroup = cmplsIdScalarGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-ID-STD-03-MIB", PYSNMP_MODULE_ID=cmplsIdStdMIB, cmplsGlobalId=cmplsGlobalId, cmplsIcc=cmplsIcc, cmplsIdCompliances=cmplsIdCompliances, cmplsIdConformance=cmplsIdConformance, cmplsIdGroups=cmplsIdGroups, cmplsIdModuleFullCompliance=cmplsIdModuleFullCompliance, cmplsIdModuleReadOnlyCompliance=cmplsIdModuleReadOnlyCompliance, cmplsIdNotifications=cmplsIdNotifications, cmplsIdObjects=cmplsIdObjects, cmplsIdScalarGroup=cmplsIdScalarGroup, cmplsIdStdMIB=cmplsIdStdMIB, cmplsNodeId=cmplsNodeId)
