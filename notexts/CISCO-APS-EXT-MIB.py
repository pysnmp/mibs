#
# PySNMP MIB module CISCO-APS-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-APS-EXT-MIB
# Source digest sha256:414b448caddac656c2124f137762669be9e6fa9481fa88d968e6375f1f615af7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
CApsK1K2, cApsChanConfigEntry, cApsChanStatusEntry, cApsConfigEntry, cApsStatusEntry = mibBuilder.importSymbols("CISCO-APS-MIB", "CApsK1K2", "cApsChanConfigEntry", "cApsChanStatusEntry", "cApsConfigEntry", "cApsStatusEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
cApsExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 72))
cApsExtMIB.setRevisions(('2003-01-31 00:00', '2002-05-31 00:00', '2002-05-20 00:00', '2001-05-21 00:00',))
if mibBuilder.loadTexts: cApsExtMIB.setLastUpdated('2003-01-31 00:00')
if mibBuilder.loadTexts: cApsExtMIB.setOrganization('Cisco Systems, Inc.')
cApsExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 1))
cApsExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2))
class CdlApsBytes(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class CApsMessageTransport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("autoSelect", 2), ("dcc", 3), ("apsChannel", 4), ("ip", 5), ("osc", 6))

class CApsChannelConfigNumber(TextualConvention, Integer32):
    reference = 'Bellcore (Telcordia Technologies) GR-253-CORE, Issue 2,Revision 2 (January 1999), 5.3.2. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 14)

cApsNotifiesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cApsNotifiesEnable.setStatus('current')
cApsConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsConfigExtTable.setStatus('current')
cApsConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1), ).setMaxAccess("notaccessible")
cApsConfigEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsConfigExtEntry"))
cApsConfigExtEntry.setIndexNames(*cApsConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cApsConfigExtEntry.setStatus('current')
cApsConfigSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hopByHop", 1), ("endToEnd", 2))).clone('hopByHop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSpan.setStatus('current')
cApsConfigYcable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noYcable", 1), ("ycable", 2), ("ycableXconnectCommon", 3))).clone('noYcable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigYcable.setStatus('current')
cApsConfigMinSearchUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMinSearchUpInterval.setStatus('current')
cApsConfigMaxSearchUpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(32)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMaxSearchUpInterval.setStatus('current')
cApsConfigSwitchoverEnableInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120)).clone(3)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigSwitchoverEnableInterval.setStatus('current')
cApsConfigMessageTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 6), CApsMessageTransport().clone('autoSelect')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageTransport.setStatus('current')
cApsConfigMessageHolddown = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000)).clone(5000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageHolddown.setStatus('current')
cApsConfigMessageHolddownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageHolddownCount.setStatus('current')
cApsConfigMessageMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1000, 120000)).clone(15000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigMessageMaxInterval.setStatus('current')
cApsConfigFarEndGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndGroupName.setStatus('current')
cApsConfigFarEndIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 11), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndIpAddressType.setStatus('current')
cApsConfigFarEndIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 2, 1, 12), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cApsConfigFarEndIpAddress.setStatus('current')
cApsStatusExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsStatusExtTable.setStatus('current')
cApsStatusExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1), ).setMaxAccess("notaccessible")
cApsStatusEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsStatusExtEntry"))
cApsStatusExtEntry.setIndexNames(*cApsStatusEntry.getIndexNames())
if mibBuilder.loadTexts: cApsStatusExtEntry.setStatus('current')
cApsStatusCdlApsBytesRcv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 1), CdlApsBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusCdlApsBytesRcv.setStatus('current')
cApsStatusCdlApsBytesTrans = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 2), CdlApsBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusCdlApsBytesTrans.setStatus('current')
cApsStatusMessageTransport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 3, 1, 3), CApsMessageTransport()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsStatusMessageTransport.setStatus('current')
cApsChanStatusExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanStatusExtTable.setStatus('current')
cApsChanStatusExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1), ).setMaxAccess("notaccessible")
cApsChanStatusEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsChanStatusExtEntry"))
cApsChanStatusExtEntry.setIndexNames(*cApsChanStatusEntry.getIndexNames())
if mibBuilder.loadTexts: cApsChanStatusExtEntry.setStatus('current')
cApsChanStatusExtRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 4, 1, 1), CApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanStatusExtRequest.setStatus('current')
cApsChanConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanConfigExtTable.setStatus('current')
cApsChanConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1), ).setMaxAccess("notaccessible")
cApsChanConfigEntry.registerAugmentions(("CISCO-APS-EXT-MIB", "cApsChanConfigExtEntry"))
cApsChanConfigExtEntry.setIndexNames(*cApsChanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cApsChanConfigExtEntry.setStatus('current')
cApsChanConfigReflectorMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanConfigReflectorMode.setStatus('current')
cApsChanAssociationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanAssociationTable.setStatus('current')
cApsChanAssociationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-APS-EXT-MIB", "cApsChanAssociationGroupName"), (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationNumber"), (0, "CISCO-APS-EXT-MIB", "cApsChanAssociationMapNumber"))
if mibBuilder.loadTexts: cApsChanAssociationEntry.setStatus('current')
cApsChanAssociationGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanAssociationGroupName.setStatus('current')
cApsChanAssociationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 2), CApsChannelConfigNumber()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanAssociationNumber.setStatus('current')
cApsChanAssociationMapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 3), CApsChannelConfigNumber()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cApsChanAssociationMapNumber.setStatus('current')
cApsChanAssociationIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanAssociationIpAddressType.setStatus('current')
cApsChanAssociationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 72, 1, 6, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cApsChanAssociationIpAddress.setStatus('current')
cApsExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1))
cApsExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2))
cApsExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 1)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnableGroup"), ("CISCO-APS-EXT-MIB", "cApsConfigPathExt"), ("CISCO-APS-EXT-MIB", "cApsConfigYcableExt"), ("CISCO-APS-EXT-MIB", "cApsConfigSearchExt"), ("CISCO-APS-EXT-MIB", "cApsStatusCdlExt"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtCompliance = cApsExtCompliance.setStatus('deprecated')
cApsExtCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 2)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnableGroup"), ("CISCO-APS-EXT-MIB", "cApsConfigPathExt"), ("CISCO-APS-EXT-MIB", "cApsConfigYcableExt"), ("CISCO-APS-EXT-MIB", "cApsConfigSearchExt"), ("CISCO-APS-EXT-MIB", "cApsStatusCdlExt"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageExt"), ("CISCO-APS-EXT-MIB", "cApsConfigSwitchoverTimerExt"), ("CISCO-APS-EXT-MIB", "cApsConfigIPExt"), ("CISCO-APS-EXT-MIB", "cApsStatusMessageExt"), ("CISCO-APS-EXT-MIB", "cApsChanStatusRequestExt"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtCompliance2 = cApsExtCompliance2.setStatus('current')
cApsExtComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 2, 3)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanConfigExt"), ("CISCO-APS-EXT-MIB", "cApsChanAssociationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsExtComplianceRev1 = cApsExtComplianceRev1.setStatus('current')
cApsNotifiesEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 1)).setObjects(("CISCO-APS-EXT-MIB", "cApsNotifiesEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsNotifiesEnableGroup = cApsNotifiesEnableGroup.setStatus('current')
cApsConfigPathExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 2)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigSpan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigPathExt = cApsConfigPathExt.setStatus('current')
cApsConfigYcableExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 3)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigYcable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigYcableExt = cApsConfigYcableExt.setStatus('current')
cApsConfigSearchExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 4)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigMinSearchUpInterval"), ("CISCO-APS-EXT-MIB", "cApsConfigMaxSearchUpInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigSearchExt = cApsConfigSearchExt.setStatus('current')
cApsStatusCdlExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 5)).setObjects(("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesRcv"), ("CISCO-APS-EXT-MIB", "cApsStatusCdlApsBytesTrans"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsStatusCdlExt = cApsStatusCdlExt.setStatus('current')
cApsConfigSwitchoverTimerExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 6)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigSwitchoverEnableInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigSwitchoverTimerExt = cApsConfigSwitchoverTimerExt.setStatus('current')
cApsConfigMessageExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 7)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigMessageTransport"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddown"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageHolddownCount"), ("CISCO-APS-EXT-MIB", "cApsConfigMessageMaxInterval"), ("CISCO-APS-EXT-MIB", "cApsConfigFarEndGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigMessageExt = cApsConfigMessageExt.setStatus('current')
cApsConfigIPExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 8)).setObjects(("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddressType"), ("CISCO-APS-EXT-MIB", "cApsConfigFarEndIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsConfigIPExt = cApsConfigIPExt.setStatus('current')
cApsStatusMessageExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 9)).setObjects(("CISCO-APS-EXT-MIB", "cApsStatusMessageTransport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsStatusMessageExt = cApsStatusMessageExt.setStatus('current')
cApsChanStatusRequestExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 10)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanStatusExtRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanStatusRequestExt = cApsChanStatusRequestExt.setStatus('current')
cApsChanConfigExt = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 11)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanConfigReflectorMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanConfigExt = cApsChanConfigExt.setStatus('current')
cApsChanAssociationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 72, 2, 1, 12)).setObjects(("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddressType"), ("CISCO-APS-EXT-MIB", "cApsChanAssociationIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cApsChanAssociationGroup = cApsChanAssociationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-APS-EXT-MIB", CApsChannelConfigNumber=CApsChannelConfigNumber, CApsMessageTransport=CApsMessageTransport, CdlApsBytes=CdlApsBytes, PYSNMP_MODULE_ID=cApsExtMIB, cApsChanAssociationEntry=cApsChanAssociationEntry, cApsChanAssociationGroup=cApsChanAssociationGroup, cApsChanAssociationGroupName=cApsChanAssociationGroupName, cApsChanAssociationIpAddress=cApsChanAssociationIpAddress, cApsChanAssociationIpAddressType=cApsChanAssociationIpAddressType, cApsChanAssociationMapNumber=cApsChanAssociationMapNumber, cApsChanAssociationNumber=cApsChanAssociationNumber, cApsChanAssociationTable=cApsChanAssociationTable, cApsChanConfigExt=cApsChanConfigExt, cApsChanConfigExtEntry=cApsChanConfigExtEntry, cApsChanConfigExtTable=cApsChanConfigExtTable, cApsChanConfigReflectorMode=cApsChanConfigReflectorMode, cApsChanStatusExtEntry=cApsChanStatusExtEntry, cApsChanStatusExtRequest=cApsChanStatusExtRequest, cApsChanStatusExtTable=cApsChanStatusExtTable, cApsChanStatusRequestExt=cApsChanStatusRequestExt, cApsConfigExtEntry=cApsConfigExtEntry, cApsConfigExtTable=cApsConfigExtTable, cApsConfigFarEndGroupName=cApsConfigFarEndGroupName, cApsConfigFarEndIpAddress=cApsConfigFarEndIpAddress, cApsConfigFarEndIpAddressType=cApsConfigFarEndIpAddressType, cApsConfigIPExt=cApsConfigIPExt, cApsConfigMaxSearchUpInterval=cApsConfigMaxSearchUpInterval, cApsConfigMessageExt=cApsConfigMessageExt, cApsConfigMessageHolddown=cApsConfigMessageHolddown, cApsConfigMessageHolddownCount=cApsConfigMessageHolddownCount, cApsConfigMessageMaxInterval=cApsConfigMessageMaxInterval, cApsConfigMessageTransport=cApsConfigMessageTransport, cApsConfigMinSearchUpInterval=cApsConfigMinSearchUpInterval, cApsConfigPathExt=cApsConfigPathExt, cApsConfigSearchExt=cApsConfigSearchExt, cApsConfigSpan=cApsConfigSpan, cApsConfigSwitchoverEnableInterval=cApsConfigSwitchoverEnableInterval, cApsConfigSwitchoverTimerExt=cApsConfigSwitchoverTimerExt, cApsConfigYcable=cApsConfigYcable, cApsConfigYcableExt=cApsConfigYcableExt, cApsExtCompliance2=cApsExtCompliance2, cApsExtCompliance=cApsExtCompliance, cApsExtComplianceRev1=cApsExtComplianceRev1, cApsExtCompliances=cApsExtCompliances, cApsExtGroups=cApsExtGroups, cApsExtMIB=cApsExtMIB, cApsExtMIBConformance=cApsExtMIBConformance, cApsExtMIBObjects=cApsExtMIBObjects, cApsNotifiesEnable=cApsNotifiesEnable, cApsNotifiesEnableGroup=cApsNotifiesEnableGroup, cApsStatusCdlApsBytesRcv=cApsStatusCdlApsBytesRcv, cApsStatusCdlApsBytesTrans=cApsStatusCdlApsBytesTrans, cApsStatusCdlExt=cApsStatusCdlExt, cApsStatusExtEntry=cApsStatusExtEntry, cApsStatusExtTable=cApsStatusExtTable, cApsStatusMessageExt=cApsStatusMessageExt, cApsStatusMessageTransport=cApsStatusMessageTransport)
