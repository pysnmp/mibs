#
# PySNMP MIB module PRVT-MONITOR-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-MONITOR-SESSION-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:35:06 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Integer32, NotificationType, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtMonitorSessionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000))
prvtMonitorSessionMib.setRevisions(('2011-05-23 00:00',))
if mibBuilder.loadTexts: prvtMonitorSessionMib.setLastUpdated('201105230000Z')
if mibBuilder.loadTexts: prvtMonitorSessionMib.setOrganization('BATM Advanced Communication')
class Direction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rx", 1), ("tx", 2))

prvtMonitorSessionNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 0))
prvtMonitorSessionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1))
prvtMonitorSessionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2))
prvtMonitorSessionTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1), )
if mibBuilder.loadTexts: prvtMonitorSessionTable.setStatus('current')
prvtMonitorSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1), ).setIndexNames((0, "PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDirection"))
if mibBuilder.loadTexts: prvtMonitorSessionEntry.setStatus('current')
prvtMonitorSessionDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 1), Direction())
if mibBuilder.loadTexts: prvtMonitorSessionDirection.setStatus('current')
prvtMonitorSessionSource = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtMonitorSessionSource.setStatus('current')
prvtMonitorSessionDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtMonitorSessionDestination.setStatus('current')
prvtAnalyzerVLANTagTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2), )
if mibBuilder.loadTexts: prvtAnalyzerVLANTagTable.setStatus('current')
prvtAnalyzerVLANTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1), ).setIndexNames((0, "PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDirection"))
if mibBuilder.loadTexts: prvtAnalyzerVLANTagEntry.setStatus('current')
prvtAnalyzerVLANTagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtAnalyzerVLANTagEnable.setStatus('current')
prvtAnalyzerVLANTagVID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtAnalyzerVLANTagVID.setStatus('current')
prvtAnalyzerVLANTagEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtAnalyzerVLANTagEtherType.setStatus('current')
prvtAnalyzerVLANTagCFI = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("clear", 0), ("set", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtAnalyzerVLANTagCFI.setStatus('current')
prvtAnalyzerVLANTagVPT = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("vpt-value0", 0), ("vpt-value1", 1), ("vpt-value2", 2), ("vpt-value3", 3), ("vpt-value4", 4), ("vpt-value5", 5), ("vpt-value6", 6), ("vpt-value7", 7), ("undefined", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtAnalyzerVLANTagVPT.setStatus('current')
prvtMonitorSessionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 1))
prvtMonitorSessionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2))
prvtMonitorSessionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 1, 1)).setObjects(("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionMirroredGroup"), ("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionAnalyzerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtMonitorSessionCompliance = prvtMonitorSessionCompliance.setStatus('current')
prvtMonitorSessionMirroredGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2, 1)).setObjects(("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtMonitorSessionMirroredGroup = prvtMonitorSessionMirroredGroup.setStatus('current')
prvtMonitorSessionAnalyzerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2, 2)).setObjects(("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDestination"), ("PRVT-MONITOR-SESSION-MIB", "prvtAnalyzerVLANTagEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtMonitorSessionAnalyzerGroup = prvtMonitorSessionAnalyzerGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-MONITOR-SESSION-MIB", prvtMonitorSessionGroups=prvtMonitorSessionGroups, prvtAnalyzerVLANTagVID=prvtAnalyzerVLANTagVID, prvtMonitorSessionEntry=prvtMonitorSessionEntry, Direction=Direction, prvtAnalyzerVLANTagCFI=prvtAnalyzerVLANTagCFI, prvtMonitorSessionSource=prvtMonitorSessionSource, prvtMonitorSessionCompliances=prvtMonitorSessionCompliances, prvtMonitorSessionCompliance=prvtMonitorSessionCompliance, prvtMonitorSessionNotification=prvtMonitorSessionNotification, prvtAnalyzerVLANTagEntry=prvtAnalyzerVLANTagEntry, prvtMonitorSessionMirroredGroup=prvtMonitorSessionMirroredGroup, prvtMonitorSessionObjects=prvtMonitorSessionObjects, prvtMonitorSessionDirection=prvtMonitorSessionDirection, prvtAnalyzerVLANTagVPT=prvtAnalyzerVLANTagVPT, prvtMonitorSessionConformance=prvtMonitorSessionConformance, prvtMonitorSessionMib=prvtMonitorSessionMib, prvtAnalyzerVLANTagEnable=prvtAnalyzerVLANTagEnable, prvtMonitorSessionDestination=prvtMonitorSessionDestination, PYSNMP_MODULE_ID=prvtMonitorSessionMib, prvtAnalyzerVLANTagEtherType=prvtAnalyzerVLANTagEtherType, prvtMonitorSessionAnalyzerGroup=prvtMonitorSessionAnalyzerGroup, prvtAnalyzerVLANTagTable=prvtAnalyzerVLANTagTable, prvtMonitorSessionTable=prvtMonitorSessionTable)
