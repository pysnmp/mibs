#
# PySNMP MIB module CISCO-DOT11-LBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-LBS-MIB
# Source digest sha256:55712465e4e526a5486cccc5ac2b2988d6edffe828c17760881f955aa6a05aa1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
ciscoDot11LbsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 454))
ciscoDot11LbsMIB.setRevisions(('2004-11-17 00:00',))
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setLastUpdated('2004-11-17 00:00')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setOrganization('Cisco System Inc.')
ciscoDot11LbsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 0))
ciscoDot11LbsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1))
ciscoDot11LbsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2))
ciscoDot11LbsConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1))
ciscoDot11LbsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 2))
class Cdot11LbsTrackMethodType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rssi", 0))

class Cdot11LbsPsPacketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("extended", 1), ("short", 2))

cdot11LbsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cdot11LbsProfileTable.setStatus('current')
cdot11LbsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"))
if mibBuilder.loadTexts: cdot11LbsProfileEntry.setStatus('current')
cdot11LbsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cdot11LbsProfileName.setStatus('current')
cdot11LbsServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddressType.setStatus('current')
cdot11LbsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddress.setStatus('current')
cdot11LbsServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerUdpPort.setStatus('current')
cdot11LbsTrackMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 5), Cdot11LbsTrackMethodType().clone(('rssi',))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMethod.setStatus('current')
cdot11LbsPsPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 6), Cdot11LbsPsPacketType().clone('extended')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsPsPacketType.setStatus('current')
cdot11LbsTrackMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 7), MacAddress().clone(hexValue="014096000010")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMulticast.setStatus('current')
cdot11LbsMatchChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsMatchChannel.setStatus('current')
cdot11LbsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfileRowStatus.setStatus('current')
cdot11LbsProfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cdot11LbsProfInterfaceTable.setStatus('current')
cdot11LbsProfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11LbsProfInterfaceEntry.setStatus('current')
cdot11LbsProfInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfInterfaceRowStatus.setStatus('current')
ciscoDot11LbsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1))
ciscoDot11LbsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2))
ciscoDot11LbsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "ciscoDot11LbsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsMIBCompliance = ciscoDot11LbsMIBCompliance.setStatus('current')
ciscoDot11LbsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddressType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddress"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerUdpPort"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMethod"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsPsPacketType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMulticast"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsMatchChannel"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfileRowStatus"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsConfigGroup = ciscoDot11LbsConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-LBS-MIB", Cdot11LbsPsPacketType=Cdot11LbsPsPacketType, Cdot11LbsTrackMethodType=Cdot11LbsTrackMethodType, PYSNMP_MODULE_ID=ciscoDot11LbsMIB, cdot11LbsMatchChannel=cdot11LbsMatchChannel, cdot11LbsProfInterfaceEntry=cdot11LbsProfInterfaceEntry, cdot11LbsProfInterfaceRowStatus=cdot11LbsProfInterfaceRowStatus, cdot11LbsProfInterfaceTable=cdot11LbsProfInterfaceTable, cdot11LbsProfileEntry=cdot11LbsProfileEntry, cdot11LbsProfileName=cdot11LbsProfileName, cdot11LbsProfileRowStatus=cdot11LbsProfileRowStatus, cdot11LbsProfileTable=cdot11LbsProfileTable, cdot11LbsPsPacketType=cdot11LbsPsPacketType, cdot11LbsServerAddress=cdot11LbsServerAddress, cdot11LbsServerAddressType=cdot11LbsServerAddressType, cdot11LbsServerUdpPort=cdot11LbsServerUdpPort, cdot11LbsTrackMethod=cdot11LbsTrackMethod, cdot11LbsTrackMulticast=cdot11LbsTrackMulticast, ciscoDot11LbsConfigGroup=ciscoDot11LbsConfigGroup, ciscoDot11LbsConfigInfo=ciscoDot11LbsConfigInfo, ciscoDot11LbsMIB=ciscoDot11LbsMIB, ciscoDot11LbsMIBCompliance=ciscoDot11LbsMIBCompliance, ciscoDot11LbsMIBCompliances=ciscoDot11LbsMIBCompliances, ciscoDot11LbsMIBConformance=ciscoDot11LbsMIBConformance, ciscoDot11LbsMIBGroups=ciscoDot11LbsMIBGroups, ciscoDot11LbsMIBNotifs=ciscoDot11LbsMIBNotifs, ciscoDot11LbsMIBObjects=ciscoDot11LbsMIBObjects, ciscoDot11LbsStatistics=ciscoDot11LbsStatistics)
