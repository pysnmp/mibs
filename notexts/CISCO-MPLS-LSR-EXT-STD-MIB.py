#
# PySNMP MIB module CISCO-MPLS-LSR-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MPLS-LSR-EXT-STD-MIB
# Source digest sha256:8ae8b44970ddf27f3fff271220e4c0ca9e470fa1c65c0fc6e2e0448bbafd4eb4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsInSegmentGroup, mplsLsrNotificationGroup, mplsOutSegmentGroup, mplsPerfGroup, mplsXCGroup, mplsXCInSegmentIndex, mplsXCIndex, mplsXCOutSegmentIndex = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInSegmentGroup", "mplsLsrNotificationGroup", "mplsOutSegmentGroup", "mplsPerfGroup", "mplsXCGroup", "mplsXCInSegmentIndex", "mplsXCIndex", "mplsXCOutSegmentIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "TextualConvention")
cmplsLsrExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 145))
cmplsLsrExtStdMIB.setRevisions(('2012-02-22 00:00',))
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setLastUpdated('2012-04-30 00:00')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
cmplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 0))
cmplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 1))
cmplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2))
cmplsXCExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmplsXCExtTable.setStatus('current')
cmplsXCExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: cmplsXCExtEntry.setStatus('current')
cmplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setStatus('current')
cmplsXCOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setStatus('current')
cmplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1))
cmplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2))
cmplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleFullCompliance = cmplsLsrExtModuleFullCompliance.setStatus('current')
cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleReadOnlyCompliance = cmplsLsrExtModuleReadOnlyCompliance.setStatus('current')
cmplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)).setObjects(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsXCExtGroup = cmplsXCExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MPLS-LSR-EXT-STD-MIB", PYSNMP_MODULE_ID=cmplsLsrExtStdMIB, cmplsLsrExtCompliances=cmplsLsrExtCompliances, cmplsLsrExtConformance=cmplsLsrExtConformance, cmplsLsrExtGroups=cmplsLsrExtGroups, cmplsLsrExtModuleFullCompliance=cmplsLsrExtModuleFullCompliance, cmplsLsrExtModuleReadOnlyCompliance=cmplsLsrExtModuleReadOnlyCompliance, cmplsLsrExtNotifications=cmplsLsrExtNotifications, cmplsLsrExtObjects=cmplsLsrExtObjects, cmplsLsrExtStdMIB=cmplsLsrExtStdMIB, cmplsXCExtEntry=cmplsXCExtEntry, cmplsXCExtGroup=cmplsXCExtGroup, cmplsXCExtTable=cmplsXCExtTable, cmplsXCExtTunnelPointer=cmplsXCExtTunnelPointer, cmplsXCOppositeDirXCPtr=cmplsXCOppositeDirXCPtr)
