#
# PySNMP MIB module CISCO-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NTP-MIB
# Source digest sha256:f0a1321b78d56a9c29a8f2021523b264e210224a56ea4e7af14075e5f62351ee
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 168))
ciscoNtpMIB.setRevisions(('2006-07-31 00:00', '2004-07-23 00:00', '2003-07-29 00:00', '2003-07-07 00:00', '2002-02-20 00:00', '2000-06-16 00:00',))
if mibBuilder.loadTexts: ciscoNtpMIB.setLastUpdated('2006-07-31 00:00')
if mibBuilder.loadTexts: ciscoNtpMIB.setOrganization('Cisco Systems, Inc.')
ciscoNtpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 0))
ciscoNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1))
ciscoNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2))
cntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1))
cntpPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2))
cntpFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3))
class NTPTimeStamp(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.1"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol(Version 3)', RFC-1305, March 1992, Section 3.2.1"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(TextualConvention, OctetString):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 3.2.1"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(TextualConvention, Integer32):
    reference = "D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 2.2"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(TextualConvention, OctetString):
    reference = "D.L. Mills, Network Time Protocol (Version 3)', RFC-1305, March 1992, Section 3.2.1"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPPollInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-20, 20)

class NTPAssocIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

cntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysLeap.setStatus('current')
cntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cntpSysStratum.setStatus('current')
cntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPrecision.setStatus('current')
cntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 4), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDelay.setStatus('current')
cntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 5), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRootDispersion.setStatus('current')
cntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefId.setStatus('current')
cntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysRefTime.setStatus('current')
cntpSysPoll = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 8), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPoll.setStatus('current')
cntpSysPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 9), NTPAssocIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysPeer.setStatus('current')
cntpSysClock = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 10), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysClock.setStatus('current')
cntpSysSrvStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("notRunning", 2), ("notSynchronized", 3), ("syncToLocal", 4), ("syncToRefclock", 5), ("syncToRemoteServer", 6))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpSysSrvStatus.setStatus('current')
cntpPeersVarTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpPeersVarTable.setStatus('current')
cntpPeersVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"))
if mibBuilder.loadTexts: cntpPeersVarEntry.setStatus('current')
cntpPeersAssocId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 1), NTPAssocIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpPeersAssocId.setStatus('current')
cntpPeersConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersConfigured.setStatus('current')
cntpPeersPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerAddress.setStatus('current')
cntpPeersPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPort.setStatus('current')
cntpPeersHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersHostAddress.setStatus('current')
cntpPeersHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPort.setStatus('current')
cntpPeersLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 7), NTPLeapIndicator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersLeap.setStatus('current')
cntpPeersMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unspecified", 0), ("symmetricActive", 1), ("symmetricPassive", 2), ("client", 3), ("server", 4), ("broadcast", 5), ("reservedControl", 6), ("reservedPrivate", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersMode.setStatus('current')
cntpPeersStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 9), NTPStratum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersStratum.setStatus('current')
cntpPeersPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 10), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPeerPoll.setStatus('current')
cntpPeersHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 11), NTPPollInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersHostPoll.setStatus('current')
cntpPeersPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersPrecision.setStatus('current')
cntpPeersRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 13), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDelay.setStatus('current')
cntpPeersRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 14), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRootDispersion.setStatus('current')
cntpPeersRefId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 15), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefId.setStatus('current')
cntpPeersRefTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 16), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersRefTime.setStatus('current')
cntpPeersOrgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 17), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOrgTime.setStatus('current')
cntpPeersReceiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 18), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReceiveTime.setStatus('current')
cntpPeersTransmitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 19), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTransmitTime.setStatus('current')
cntpPeersUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTime.setStatus('deprecated')
cntpPeersReach = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersReach.setStatus('current')
cntpPeersTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersTimer.setStatus('current')
cntpPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 23), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersOffset.setStatus('current')
cntpPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 24), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDelay.setStatus('current')
cntpPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 25), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersDispersion.setStatus('current')
cntpPeersFilterValidEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 26), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersFilterValidEntries.setStatus('current')
cntpPeersEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 27), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersEntryStatus.setStatus('current')
cntpPeersUpdateTimeRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpPeersUpdateTimeRev1.setStatus('current')
cntpPeersPrefPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 29), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPrefPeer.setStatus('current')
cntpPeersPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 30), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerType.setStatus('current')
cntpPeersPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 31), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cntpPeersPeerName.setStatus('current')
cntpFilterRegisterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpFilterRegisterTable.setStatus('current')
cntpFilterRegisterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-NTP-MIB", "cntpPeersAssocId"), (0, "CISCO-NTP-MIB", "cntpFilterIndex"))
if mibBuilder.loadTexts: cntpFilterRegisterEntry.setStatus('current')
cntpFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cntpFilterIndex.setStatus('current')
cntpFilterPeersOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 2), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersOffset.setStatus('current')
cntpFilterPeersDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 3), NTPSignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDelay.setStatus('current')
cntpFilterPeersDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 4), NTPUnsignedTimeValue()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cntpFilterPeersDispersion.setStatus('current')
ciscoNtpSrvStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if mibBuilder.loadTexts: ciscoNtpSrvStatusChange.setStatus('current')
ciscoNtpHighPriorityConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnFailure.setStatus('current')
ciscoNtpHighPriorityConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 3)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpHighPriorityConnRestore.setStatus('current')
ciscoNtpGeneralConnFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 4))
if mibBuilder.loadTexts: ciscoNtpGeneralConnFailure.setStatus('current')
ciscoNtpGeneralConnRestore = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPeerAddress"))
if mibBuilder.loadTexts: ciscoNtpGeneralConnRestore.setStatus('current')
ciscoNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1))
ciscoNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2))
ciscoNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 1)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroup"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBCompliance = ciscoNtpMIBCompliance.setStatus('deprecated')
ciscoNtpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 2)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev1 = ciscoNtpMIBComplianceRev1.setStatus('deprecated')
ciscoNtpMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 3)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev1"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev2 = ciscoNtpMIBComplianceRev2.setStatus('deprecated')
ciscoNtpMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 4)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev3 = ciscoNtpMIBComplianceRev3.setStatus('deprecated')
ciscoNtpMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 5)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSysGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeersGroupRev2"), ("CISCO-NTP-MIB", "ciscoNtpFilterGroup"), ("CISCO-NTP-MIB", "ciscoNtpPeerExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSysExtGroup"), ("CISCO-NTP-MIB", "ciscoNtpSrvNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpMIBComplianceRev4 = ciscoNtpMIBComplianceRev4.setStatus('current')
ciscoNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 1)).setObjects(("CISCO-NTP-MIB", "cntpSysLeap"), ("CISCO-NTP-MIB", "cntpSysStratum"), ("CISCO-NTP-MIB", "cntpSysPrecision"), ("CISCO-NTP-MIB", "cntpSysRootDelay"), ("CISCO-NTP-MIB", "cntpSysRootDispersion"), ("CISCO-NTP-MIB", "cntpSysRefId"), ("CISCO-NTP-MIB", "cntpSysRefTime"), ("CISCO-NTP-MIB", "cntpSysPoll"), ("CISCO-NTP-MIB", "cntpSysPeer"), ("CISCO-NTP-MIB", "cntpSysClock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysGroup = ciscoNtpSysGroup.setStatus('current')
ciscoNtpPeersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 2)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTime"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroup = ciscoNtpPeersGroup.setStatus('deprecated')
ciscoNtpFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 3)).setObjects(("CISCO-NTP-MIB", "cntpFilterPeersOffset"), ("CISCO-NTP-MIB", "cntpFilterPeersDelay"), ("CISCO-NTP-MIB", "cntpFilterPeersDispersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpFilterGroup = ciscoNtpFilterGroup.setStatus('current')
ciscoNtpPeersGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 4)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev1 = ciscoNtpPeersGroupRev1.setStatus('deprecated')
ciscoNtpPeerExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 5)).setObjects(("CISCO-NTP-MIB", "cntpPeersPrefPeer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeerExtGroup = ciscoNtpPeerExtGroup.setStatus('current')
ciscoNtpPeersGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 6)).setObjects(("CISCO-NTP-MIB", "cntpPeersConfigured"), ("CISCO-NTP-MIB", "cntpPeersPeerAddress"), ("CISCO-NTP-MIB", "cntpPeersPeerPort"), ("CISCO-NTP-MIB", "cntpPeersHostAddress"), ("CISCO-NTP-MIB", "cntpPeersHostPort"), ("CISCO-NTP-MIB", "cntpPeersLeap"), ("CISCO-NTP-MIB", "cntpPeersMode"), ("CISCO-NTP-MIB", "cntpPeersStratum"), ("CISCO-NTP-MIB", "cntpPeersPeerPoll"), ("CISCO-NTP-MIB", "cntpPeersHostPoll"), ("CISCO-NTP-MIB", "cntpPeersPrecision"), ("CISCO-NTP-MIB", "cntpPeersRootDelay"), ("CISCO-NTP-MIB", "cntpPeersRootDispersion"), ("CISCO-NTP-MIB", "cntpPeersRefId"), ("CISCO-NTP-MIB", "cntpPeersRefTime"), ("CISCO-NTP-MIB", "cntpPeersOrgTime"), ("CISCO-NTP-MIB", "cntpPeersReceiveTime"), ("CISCO-NTP-MIB", "cntpPeersTransmitTime"), ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"), ("CISCO-NTP-MIB", "cntpPeersReach"), ("CISCO-NTP-MIB", "cntpPeersTimer"), ("CISCO-NTP-MIB", "cntpPeersOffset"), ("CISCO-NTP-MIB", "cntpPeersDelay"), ("CISCO-NTP-MIB", "cntpPeersDispersion"), ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"), ("CISCO-NTP-MIB", "cntpPeersEntryStatus"), ("CISCO-NTP-MIB", "cntpPeersPeerName"), ("CISCO-NTP-MIB", "cntpPeersPeerType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpPeersGroupRev2 = ciscoNtpPeersGroupRev2.setStatus('current')
ciscoNtpSysExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 7)).setObjects(("CISCO-NTP-MIB", "cntpSysSrvStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSysExtGroup = ciscoNtpSysExtGroup.setStatus('current')
ciscoNtpSrvNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 8)).setObjects(("CISCO-NTP-MIB", "ciscoNtpSrvStatusChange"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnRestore"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnFailure"), ("CISCO-NTP-MIB", "ciscoNtpGeneralConnRestore"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpSrvNotifGroup = ciscoNtpSrvNotifGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NTP-MIB", NTPAssocIdentifier=NTPAssocIdentifier, NTPLeapIndicator=NTPLeapIndicator, NTPPollInterval=NTPPollInterval, NTPRefId=NTPRefId, NTPSignedTimeValue=NTPSignedTimeValue, NTPStratum=NTPStratum, NTPTimeStamp=NTPTimeStamp, NTPUnsignedTimeValue=NTPUnsignedTimeValue, PYSNMP_MODULE_ID=ciscoNtpMIB, ciscoNtpFilterGroup=ciscoNtpFilterGroup, ciscoNtpGeneralConnFailure=ciscoNtpGeneralConnFailure, ciscoNtpGeneralConnRestore=ciscoNtpGeneralConnRestore, ciscoNtpHighPriorityConnFailure=ciscoNtpHighPriorityConnFailure, ciscoNtpHighPriorityConnRestore=ciscoNtpHighPriorityConnRestore, ciscoNtpMIB=ciscoNtpMIB, ciscoNtpMIBCompliance=ciscoNtpMIBCompliance, ciscoNtpMIBComplianceRev1=ciscoNtpMIBComplianceRev1, ciscoNtpMIBComplianceRev2=ciscoNtpMIBComplianceRev2, ciscoNtpMIBComplianceRev3=ciscoNtpMIBComplianceRev3, ciscoNtpMIBComplianceRev4=ciscoNtpMIBComplianceRev4, ciscoNtpMIBCompliances=ciscoNtpMIBCompliances, ciscoNtpMIBConformance=ciscoNtpMIBConformance, ciscoNtpMIBGroups=ciscoNtpMIBGroups, ciscoNtpMIBNotifs=ciscoNtpMIBNotifs, ciscoNtpMIBObjects=ciscoNtpMIBObjects, ciscoNtpPeerExtGroup=ciscoNtpPeerExtGroup, ciscoNtpPeersGroup=ciscoNtpPeersGroup, ciscoNtpPeersGroupRev1=ciscoNtpPeersGroupRev1, ciscoNtpPeersGroupRev2=ciscoNtpPeersGroupRev2, ciscoNtpSrvNotifGroup=ciscoNtpSrvNotifGroup, ciscoNtpSrvStatusChange=ciscoNtpSrvStatusChange, ciscoNtpSysExtGroup=ciscoNtpSysExtGroup, ciscoNtpSysGroup=ciscoNtpSysGroup, cntpFilter=cntpFilter, cntpFilterIndex=cntpFilterIndex, cntpFilterPeersDelay=cntpFilterPeersDelay, cntpFilterPeersDispersion=cntpFilterPeersDispersion, cntpFilterPeersOffset=cntpFilterPeersOffset, cntpFilterRegisterEntry=cntpFilterRegisterEntry, cntpFilterRegisterTable=cntpFilterRegisterTable, cntpPeers=cntpPeers, cntpPeersAssocId=cntpPeersAssocId, cntpPeersConfigured=cntpPeersConfigured, cntpPeersDelay=cntpPeersDelay, cntpPeersDispersion=cntpPeersDispersion, cntpPeersEntryStatus=cntpPeersEntryStatus, cntpPeersFilterValidEntries=cntpPeersFilterValidEntries, cntpPeersHostAddress=cntpPeersHostAddress, cntpPeersHostPoll=cntpPeersHostPoll, cntpPeersHostPort=cntpPeersHostPort, cntpPeersLeap=cntpPeersLeap, cntpPeersMode=cntpPeersMode, cntpPeersOffset=cntpPeersOffset, cntpPeersOrgTime=cntpPeersOrgTime, cntpPeersPeerAddress=cntpPeersPeerAddress, cntpPeersPeerName=cntpPeersPeerName, cntpPeersPeerPoll=cntpPeersPeerPoll, cntpPeersPeerPort=cntpPeersPeerPort, cntpPeersPeerType=cntpPeersPeerType, cntpPeersPrecision=cntpPeersPrecision, cntpPeersPrefPeer=cntpPeersPrefPeer, cntpPeersReach=cntpPeersReach, cntpPeersReceiveTime=cntpPeersReceiveTime, cntpPeersRefId=cntpPeersRefId, cntpPeersRefTime=cntpPeersRefTime, cntpPeersRootDelay=cntpPeersRootDelay, cntpPeersRootDispersion=cntpPeersRootDispersion, cntpPeersStratum=cntpPeersStratum, cntpPeersTimer=cntpPeersTimer, cntpPeersTransmitTime=cntpPeersTransmitTime, cntpPeersUpdateTime=cntpPeersUpdateTime, cntpPeersUpdateTimeRev1=cntpPeersUpdateTimeRev1, cntpPeersVarEntry=cntpPeersVarEntry, cntpPeersVarTable=cntpPeersVarTable, cntpSysClock=cntpSysClock, cntpSysLeap=cntpSysLeap, cntpSysPeer=cntpSysPeer, cntpSysPoll=cntpSysPoll, cntpSysPrecision=cntpSysPrecision, cntpSysRefId=cntpSysRefId, cntpSysRefTime=cntpSysRefTime, cntpSysRootDelay=cntpSysRootDelay, cntpSysRootDispersion=cntpSysRootDispersion, cntpSysSrvStatus=cntpSysSrvStatus, cntpSysStratum=cntpSysStratum, cntpSystem=cntpSystem)
