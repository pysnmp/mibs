#
# PySNMP MIB module PRVT-MONITOR-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-MONITOR-SESSION-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 16:38:54 2021
# On host fv-az33-471 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, Bits, Gauge32, Counter64, iso, ObjectIdentity, Integer32, IpAddress, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "Gauge32", "Counter64", "iso", "ObjectIdentity", "Integer32", "IpAddress", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("PRVT-MONITOR-SESSION-MIB", prvtMonitorSessionGroups=prvtMonitorSessionGroups, prvtAnalyzerVLANTagEtherType=prvtAnalyzerVLANTagEtherType, prvtMonitorSessionMirroredGroup=prvtMonitorSessionMirroredGroup, prvtMonitorSessionConformance=prvtMonitorSessionConformance, prvtAnalyzerVLANTagTable=prvtAnalyzerVLANTagTable, prvtAnalyzerVLANTagEntry=prvtAnalyzerVLANTagEntry, prvtMonitorSessionSource=prvtMonitorSessionSource, prvtMonitorSessionCompliance=prvtMonitorSessionCompliance, prvtAnalyzerVLANTagCFI=prvtAnalyzerVLANTagCFI, prvtMonitorSessionTable=prvtMonitorSessionTable, prvtMonitorSessionCompliances=prvtMonitorSessionCompliances, prvtMonitorSessionDirection=prvtMonitorSessionDirection, prvtMonitorSessionDestination=prvtMonitorSessionDestination, prvtMonitorSessionMib=prvtMonitorSessionMib, prvtAnalyzerVLANTagEnable=prvtAnalyzerVLANTagEnable, PYSNMP_MODULE_ID=prvtMonitorSessionMib, prvtAnalyzerVLANTagVID=prvtAnalyzerVLANTagVID, prvtMonitorSessionEntry=prvtMonitorSessionEntry, prvtMonitorSessionObjects=prvtMonitorSessionObjects, prvtMonitorSessionNotification=prvtMonitorSessionNotification, prvtAnalyzerVLANTagVPT=prvtAnalyzerVLANTagVPT, Direction=Direction, prvtMonitorSessionAnalyzerGroup=prvtMonitorSessionAnalyzerGroup)
