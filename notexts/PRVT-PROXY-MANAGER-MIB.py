#
# PySNMP MIB module PRVT-PROXY-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-PROXY-MANAGER-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 20:08:00 2021
# On host fv-az42-715 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Gauge32, NotificationType, Unsigned32, Integer32, Counter64, IpAddress, ModuleIdentity, Counter32, ObjectIdentity, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "Integer32", "Counter64", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "MibIdentifier")
MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
prvtProxyManager = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 6))
prvtProxyManager.setRevisions(('2009-01-16 00:00', '2007-11-13 00:00',))
if mibBuilder.loadTexts: prvtProxyManager.setLastUpdated('200901160000Z')
if mibBuilder.loadTexts: prvtProxyManager.setOrganization('BATM Advanced Communication')
prvtProxyManNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0))
prvtProxyManObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1))
class PrvtProxyManStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class PrvtProxyManProtocols(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("snmp-udp", 1), ("snmptrap-udp", 2), ("telnet-tcp", 3), ("ssh-tcp", 4), ("tftp-udp", 5), ("syslog-udp", 6))

class PrvtProxyManPortTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcp", 1), ("udp", 2))

class PrvtProxyManDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noDirection", 0), ("inbound", 1), ("outbound", 2))

class PrvtProxyManAuthentication(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("authenticated", 0), ("unauthenticated", 1))

class PrvtProxySecurity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("securityEnabled", 0), ("securityDisabled", 1))

class PrvtProxyAcceptInformsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("informsEnabled", 0), ("informsDisabled", 1))

prvtProxyManDeviceAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtProxyManDeviceAddress.setStatus('current')
prvtProxyManConfigTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2), )
if mibBuilder.loadTexts: prvtProxyManConfigTable.setStatus('current')
prvtProxyManConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1), ).setIndexNames((0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManIndex"))
if mibBuilder.loadTexts: prvtProxyManConfigEntry.setStatus('current')
prvtProxyManIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtProxyManIndex.setStatus('current')
prvtProxyManStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 2), PrvtProxyManStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManStatus.setStatus('current')
prvtProxyManAutoMapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 3), PrvtProxyManStates().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManAutoMapMode.setStatus('current')
prvtProxyManVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManVlan.setStatus('current')
prvtProxyManIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManIpAddr.setStatus('current')
prvtProxyManIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManIpMask.setStatus('current')
prvtProxyManIpRangeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManIpRangeStart.setStatus('current')
prvtProxyManIpRangeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManIpRangeEnd.setStatus('current')
prvtProxyManLeasePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManLeasePeriod.setStatus('current')
prvtProxyManRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtProxyManRowStatus.setStatus('current')
prvtProxySecurityEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 11), PrvtProxySecurity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxySecurityEnabled.setStatus('current')
prvtProxyAcceptInforms = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 2, 1, 12), PrvtProxyAcceptInformsType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyAcceptInforms.setStatus('current')
prvtProxyManProtoTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3), )
if mibBuilder.loadTexts: prvtProxyManProtoTable.setStatus('current')
prvtProxyManProtoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1), ).setIndexNames((0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManProtoIndex"))
if mibBuilder.loadTexts: prvtProxyManProtoEntry.setStatus('current')
prvtProxyManProtoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 1), PrvtProxyManProtocols())
if mibBuilder.loadTexts: prvtProxyManProtoIndex.setStatus('current')
prvtProxyManProtoSvcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManProtoSvcPort.setStatus('current')
prvtProxyManProtoSvcPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 3), PrvtProxyManPortTypes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManProtoSvcPortType.setStatus('current')
prvtProxyManProtoSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManProtoSrcPort.setStatus('current')
prvtProxyManProtoDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 5), PrvtProxyManDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManProtoDirection.setStatus('current')
prvtProxyManProtoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 3, 1, 6), PrvtProxyManStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManProtoStatus.setStatus('current')
prvtProxyManMappingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4), )
if mibBuilder.loadTexts: prvtProxyManMappingTable.setStatus('current')
prvtProxyManMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1), ).setIndexNames((0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingDevice"), (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingIndex"), (0, "PRVT-PROXY-MANAGER-MIB", "prvtProxyManMappingProto"))
if mibBuilder.loadTexts: prvtProxyManMappingEntry.setStatus('current')
prvtProxyManMappingDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: prvtProxyManMappingDevice.setStatus('current')
prvtProxyManMappingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtProxyManMappingIndex.setStatus('current')
prvtProxyManMappingProto = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 3), PrvtProxyManProtocols())
if mibBuilder.loadTexts: prvtProxyManMappingProto.setStatus('current')
prvtProxyManMappingDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 4), PrvtProxyManDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManMappingDirection.setStatus('current')
prvtProxyManMappingGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManMappingGlobalPort.setStatus('current')
prvtProxyManMappingLocalSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManMappingLocalSrcPort.setStatus('current')
prvtProxyManMappingLocalDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManMappingLocalDstPort.setStatus('current')
prvtProxyManMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtProxyManMappingRowStatus.setStatus('current')
prvtProxyManMappingMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 9), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtProxyManMappingMAC.setStatus('current')
prvtProxyManMappingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManMappingIfIndex.setStatus('current')
prvtProxyManMappingAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 1, 4, 1, 11), PrvtProxyManAuthentication()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtProxyManMappingAuthenticated.setStatus('current')
prvtProxyManagerNewDevice = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 1)).setObjects(("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress"))
if mibBuilder.loadTexts: prvtProxyManagerNewDevice.setStatus('current')
prvtProxyManagerRemovedDevice = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 2)).setObjects(("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress"))
if mibBuilder.loadTexts: prvtProxyManagerRemovedDevice.setStatus('current')
prvtProxyManagerUnauthenticatedDevice = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 6, 6, 0, 3)).setObjects(("PRVT-PROXY-MANAGER-MIB", "prvtProxyManDeviceAddress"))
if mibBuilder.loadTexts: prvtProxyManagerUnauthenticatedDevice.setStatus('current')
mibBuilder.exportSymbols("PRVT-PROXY-MANAGER-MIB", prvtProxyManMappingGlobalPort=prvtProxyManMappingGlobalPort, prvtProxyManProtoStatus=prvtProxyManProtoStatus, prvtProxyManMappingDirection=prvtProxyManMappingDirection, PrvtProxyAcceptInformsType=PrvtProxyAcceptInformsType, prvtProxyManIpRangeEnd=prvtProxyManIpRangeEnd, prvtProxyManLeasePeriod=prvtProxyManLeasePeriod, prvtProxyManProtoEntry=prvtProxyManProtoEntry, prvtProxyManConfigTable=prvtProxyManConfigTable, PrvtProxyManProtocols=PrvtProxyManProtocols, prvtProxyManMappingIfIndex=prvtProxyManMappingIfIndex, prvtProxyManIpMask=prvtProxyManIpMask, prvtProxyManMappingMAC=prvtProxyManMappingMAC, prvtProxyManAutoMapMode=prvtProxyManAutoMapMode, prvtProxyManProtoDirection=prvtProxyManProtoDirection, prvtProxyManRowStatus=prvtProxyManRowStatus, prvtProxyManMappingLocalDstPort=prvtProxyManMappingLocalDstPort, prvtProxyManStatus=prvtProxyManStatus, prvtProxyManagerUnauthenticatedDevice=prvtProxyManagerUnauthenticatedDevice, prvtProxyManConfigEntry=prvtProxyManConfigEntry, prvtProxyManIpRangeStart=prvtProxyManIpRangeStart, prvtProxyManIndex=prvtProxyManIndex, prvtProxyManVlan=prvtProxyManVlan, prvtProxyManProtoSvcPort=prvtProxyManProtoSvcPort, prvtProxyManMappingTable=prvtProxyManMappingTable, PrvtProxyManPortTypes=PrvtProxyManPortTypes, prvtProxyManMappingIndex=prvtProxyManMappingIndex, prvtProxyManagerRemovedDevice=prvtProxyManagerRemovedDevice, PYSNMP_MODULE_ID=prvtProxyManager, PrvtProxyManDirection=PrvtProxyManDirection, prvtProxyManDeviceAddress=prvtProxyManDeviceAddress, prvtProxyManMappingEntry=prvtProxyManMappingEntry, prvtProxyManNotifications=prvtProxyManNotifications, prvtProxyManMappingAuthenticated=prvtProxyManMappingAuthenticated, prvtProxyManager=prvtProxyManager, prvtProxyManIpAddr=prvtProxyManIpAddr, prvtProxyManMappingLocalSrcPort=prvtProxyManMappingLocalSrcPort, prvtProxyManProtoSrcPort=prvtProxyManProtoSrcPort, PrvtProxyManStates=PrvtProxyManStates, prvtProxyManProtoIndex=prvtProxyManProtoIndex, PrvtProxySecurity=PrvtProxySecurity, PrvtProxyManAuthentication=PrvtProxyManAuthentication, prvtProxyManMappingProto=prvtProxyManMappingProto, prvtProxyManagerNewDevice=prvtProxyManagerNewDevice, prvtProxyManObjects=prvtProxyManObjects, prvtProxyManProtoSvcPortType=prvtProxyManProtoSvcPortType, prvtProxyAcceptInforms=prvtProxyAcceptInforms, prvtProxyManMappingRowStatus=prvtProxyManMappingRowStatus, prvtProxyManProtoTable=prvtProxyManProtoTable, prvtProxyManMappingDevice=prvtProxyManMappingDevice, prvtProxySecurityEnabled=prvtProxySecurityEnabled)
