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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setRevisionsDescriptions(('MPLS LSR specific mib objects extension',))
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setLastUpdated('2012-04-30 00:00')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setContactInfo('Venkatesan Mahalingam\n            Dell Inc,\n            350 Holger way, San Jose, CA, USA\n            Email: venkat.mahalingams@gmail.com\n\n            Kannan KV Sampath\n            Aricent,\n            India\n            Email: Kannan.Sampath@aricent.com\n\n            Sam Aldrin\n            Huawei Technologies\n            2330 Central Express Way,\n            Santa Clara, CA 95051, USA\n\n            Email:  aldrin.ietf@gmail.com\n\n            Thomas D. Nadeau\n            CA Technologies\n            273 Corporate Drive, Portsmouth, NH, USA\n            Email: thomas.nadeau@ca.com')
if mibBuilder.loadTexts: cmplsLsrExtStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified\n        as the document authors.  All rights reserved.\n\n        This MIB module contains generic object definitions for\n\n\n        MPLS LSR in transport networks.')
cmplsLsrExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 0))
cmplsLsrExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 1))
cmplsLsrExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2))
cmplsXCExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cmplsXCExtTable.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching\n              Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtTable.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtTable.setDescription('This table sparse augments the mplsXCTable of\n        MPLS-LSR-STD-MIB [RFC3813] to provide MPLS-TP specific\n        information about associated tunnel information')
cmplsXCExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsXCIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCInSegmentIndex"), (0, "MPLS-LSR-STD-MIB", "mplsXCOutSegmentIndex"))
if mibBuilder.loadTexts: cmplsXCExtEntry.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching\n              Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtEntry.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtEntry.setDescription('An entry in this table extends the cross connect\n        information represented by an entry in\n        the mplsXCTable in MPLS-LSR-STD-MIB [RFC3813] through\n        a sparse augmentation.  An entry can be created by\n        a network administrator via SNMP SET commands, or in\n        response to signaling protocol events.')
cmplsXCExtTunnelPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 1), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching\n              Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtTunnelPointer.setDescription('This object indicates the back pointer to the tunnel\n        entry segment.  This object cannot be modified if\n        mplsXCRowStatus for the corresponding entry in the\n        mplsXCTable is active(1).')
cmplsXCOppositeDirXCPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 145, 1, 1, 1, 2), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setReference('1. Multiprotocol Label Switching (MPLS) Label Switching\n              Router (LSR) Management Information Base (MIB), RFC 3813.')
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setStatus('current')
if mibBuilder.loadTexts: cmplsXCOppositeDirXCPtr.setDescription('This object indicates the pointer to the opposite\n        direction XC entry.  This object cannot be modified if\n        mplsXCRowStatus for the corresponding entry in the\n        mplsXCTable is active(1).')
cmplsLsrExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1))
cmplsLsrExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2))
cmplsLsrExtModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 1)).setObjects(("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("MPLS-LSR-STD-MIB", "mplsLsrNotificationGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleFullCompliance = cmplsLsrExtModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsLsrExtModuleFullCompliance.setDescription('Compliance statement for agents that provide full support\n\n        for MPLS-LSR-EXT-STD-MIB.\n        The mandatory group has to be implemented by all LSRs\n        that originate, terminate, or act as transit for\n        TE-LSPs/tunnels.\n        In addition, depending on the type of tunnels supported,\n        other groups become mandatory as explained below.')
cmplsLsrExtModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 2, 2)).setObjects(("MPLS-LSR-STD-MIB", "mplsInterfaceGroup"), ("MPLS-LSR-STD-MIB", "mplsInSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsOutSegmentGroup"), ("MPLS-LSR-STD-MIB", "mplsXCGroup"), ("MPLS-LSR-STD-MIB", "mplsPerfGroup"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsLsrExtModuleReadOnlyCompliance = cmplsLsrExtModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cmplsLsrExtModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only\n        provide read-only support for MPLS-LSR-EXT-STD-MIB.\n        Such devices can then be monitored but cannot be\n        configured using this MIB module.')
cmplsXCExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 145, 2, 1, 1)).setObjects(("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCExtTunnelPointer"), ("CISCO-MPLS-LSR-EXT-STD-MIB", "cmplsXCOppositeDirXCPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmplsXCExtGroup = cmplsXCExtGroup.setStatus('current')
if mibBuilder.loadTexts: cmplsXCExtGroup.setDescription('This object should be supported in order to access\n        the tunnel entry from XC entry.')
mibBuilder.exportSymbols("CISCO-MPLS-LSR-EXT-STD-MIB", PYSNMP_MODULE_ID=cmplsLsrExtStdMIB, cmplsLsrExtCompliances=cmplsLsrExtCompliances, cmplsLsrExtConformance=cmplsLsrExtConformance, cmplsLsrExtGroups=cmplsLsrExtGroups, cmplsLsrExtModuleFullCompliance=cmplsLsrExtModuleFullCompliance, cmplsLsrExtModuleReadOnlyCompliance=cmplsLsrExtModuleReadOnlyCompliance, cmplsLsrExtNotifications=cmplsLsrExtNotifications, cmplsLsrExtObjects=cmplsLsrExtObjects, cmplsLsrExtStdMIB=cmplsLsrExtStdMIB, cmplsXCExtEntry=cmplsXCExtEntry, cmplsXCExtGroup=cmplsXCExtGroup, cmplsXCExtTable=cmplsXCExtTable, cmplsXCExtTunnelPointer=cmplsXCExtTunnelPointer, cmplsXCOppositeDirXCPtr=cmplsXCOppositeDirXCPtr)
