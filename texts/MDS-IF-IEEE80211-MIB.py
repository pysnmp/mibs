#
# PySNMP MIB module MDS-IF-IEEE80211-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-IEEE80211-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 19:53:24 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Counter32, ObjectIdentity, IpAddress, iso, Integer32, ModuleIdentity, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Counter32", "ObjectIdentity", "IpAddress", "iso", "Integer32", "ModuleIdentity", "Gauge32", "MibIdentifier", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
mdsIfDot11MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2))
mdsIfDot11MIB.setRevisions(('2018-05-16 00:00', '2014-10-20 00:00', '2013-04-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsIfDot11MIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Removed hyphens from enumerations.', 'Initial version.',))
if mibBuilder.loadTexts: mdsIfDot11MIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfDot11MIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsIfDot11MIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsIfDot11MIB.setDescription('The MIB module to describe the IEEE802.11 interface.')
mIfDot11MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1))
mIfDot11Config = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 1))
mIfDot11Status = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2))
class Byte(TextualConvention, Integer32):
    description = 'xs:byte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    description = 'xs:unsignedShort'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Ssid(TextualConvention, OctetString):
    description = 'IEEE802.11 Service Set Identifier'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class MacString(TextualConvention, OctetString):
    description = 'MAC Identifier String'
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

mIfDot11StatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: mIfDot11StatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusTable.setDescription('This table contains status of IEEE802.11 interfaces. This table has\n         a sparse dependent relationship on the ifTable. For each entry in\n         this table, there exists an entry in the ifTable.')
mIfDot11StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfDot11StatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusEntry.setDescription('Each entry contains status of a cellular interface.')
mIfDot11SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11SerialNumber.setStatus('current')
if mibBuilder.loadTexts: mIfDot11SerialNumber.setDescription('IEEE802.11 hardware serial number.')
mIfDot11Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("station", 1), ("accessPoint", 2), ("accessPointStation", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11Mode.setStatus('current')
if mibBuilder.loadTexts: mIfDot11Mode.setDescription('IEEE802.11 operation mode.')
mIfDot11TxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 3), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11TxPower.setStatus('current')
if mibBuilder.loadTexts: mIfDot11TxPower.setDescription('IEEE802.11 transmit power (dBm).')
mIfDot11Channel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 4), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11Channel.setStatus('current')
if mibBuilder.loadTexts: mIfDot11Channel.setDescription('IEEE802.11 channel')
mIfDot11StationSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 5), Ssid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationSsid.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationSsid.setDescription('SSID of access point the unit is connected to')
mIfDot11StationBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 6), MacString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationBssid.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationBssid.setDescription('BSSID of access point the unit is connected to')
mIfDot11StationRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 7), Byte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRssi.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationRssi.setDescription('Received Signal Strength indicator (dBm).')
mIfDot11StationAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationAuthenticated.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationAuthenticated.setDescription('Whether the station has been authenticated by the AP.')
mIfDot11StationAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationAuthorized.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationAuthorized.setDescription('Whether the station has been authorized by the AP.')
mIfDot11StationInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationInactive.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationInactive.setDescription('Whether the station is active.')
mIfDot11StationRxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRxbytes.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationRxbytes.setDescription('Number of bytes received.')
mIfDot11StationRxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRxpackets.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationRxpackets.setDescription('Number of packets received.')
mIfDot11StationTxbitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 13), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxbitrate.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationTxbitrate.setDescription('Current RF transmission bit rate.')
mIfDot11StationTxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxbytes.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationTxbytes.setDescription('Number of bytes transmitted.')
mIfDot11StationTxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxpackets.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationTxpackets.setDescription('Number of packets transmitted.')
mIfDot11StationTxfailed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxfailed.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationTxfailed.setDescription('Number of transmissions that failed.')
mIfDot11StationTxretries = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxretries.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StationTxretries.setDescription('Number of transmission retries.')
mIfDot11ModemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("w51", 1), ("w52", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ModemType.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ModemType.setDescription('Modem type.')
mIfDot11StatusApTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2), )
if mibBuilder.loadTexts: mIfDot11StatusApTable.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusApTable.setDescription('The access point table.')
mIfDot11StatusApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"))
if mibBuilder.loadTexts: mIfDot11StatusApEntry.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusApEntry.setDescription('The Access Point status entry.')
mIfDot11ApSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1, 1), Ssid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApSsid.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApSsid.setDescription('Current BSS SSID/Network name')
mIfDot11StatusApClientTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3), )
if mibBuilder.loadTexts: mIfDot11StatusApClientTable.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusApClientTable.setDescription('The access point client entry.')
mIfDot11StatusApClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"))
if mibBuilder.loadTexts: mIfDot11StatusApClientEntry.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusApClientEntry.setDescription('The client connected to the AP.')
mIfDot11ApClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 1), MacString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientMac.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientMac.setDescription('The client MAC address.')
mIfDot11ApClientRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 2), Byte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRssi.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientRssi.setDescription('The client RSSI.')
mIfDot11ApClientAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientAuthenticated.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientAuthenticated.setDescription('Whether the client is authenticated.')
mIfDot11ApClientAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientAuthorized.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientAuthorized.setDescription('Whether the client is authorized.')
mIfDot11ApClientInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientInactive.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientInactive.setDescription('Whether the client is inactive.')
mIfDot11ApClientRxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRxbytes.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientRxbytes.setDescription('Number of bytes received from the client.')
mIfDot11ApClientRxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRxpackets.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientRxpackets.setDescription('Number of packets received from the client.')
mIfDot11ApClientTxbitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 8), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxbitrate.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientTxbitrate.setDescription('Transmission bit rate at which the client is connected to AP.')
mIfDot11ApClientTxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxbytes.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientTxbytes.setDescription('Number of bytes transmitted to the client.')
mIfDot11ApClientTxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxpackets.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientTxpackets.setDescription('Number of packets transmitted to the client.')
mIfDot11ApClientTxfailed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxfailed.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientTxfailed.setDescription('Number of transmissions to the client that failed.')
mIfDot11ApClientTxretries = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxretries.setStatus('current')
if mibBuilder.loadTexts: mIfDot11ApClientTxretries.setDescription('Number of transmission retries to the client.')
mdsIfDot11MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3))
mdsIfDot11MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1))
mdsIfDot11MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2))
mIfDot11Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1, 1)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11StatusCommonGroup"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusStationGroup"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusApGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11Compliance = mIfDot11Compliance.setStatus('current')
if mibBuilder.loadTexts: mIfDot11Compliance.setDescription('The compliance statement for SNMP entities that\n            implement the MDS-IF-IEEE80211-MIB.')
mIfDot11StatusCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 1)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11SerialNumber"), ("MDS-IF-IEEE80211-MIB", "mIfDot11Mode"), ("MDS-IF-IEEE80211-MIB", "mIfDot11TxPower"), ("MDS-IF-IEEE80211-MIB", "mIfDot11Channel"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ModemType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusCommonGroup = mIfDot11StatusCommonGroup.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusCommonGroup.setDescription('A collection of objects providing information about\n        common IEEE802.11 interface status.')
mIfDot11StatusStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 2)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11StationSsid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRssi"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationBssid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthenticated"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthorized"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationInactive"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbitrate"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxfailed"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxretries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusStationGroup = mIfDot11StatusStationGroup.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusStationGroup.setDescription('A collection of objects providing information about\n        IEEE802.11 interface status in station mode.')
mIfDot11StatusApGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 3)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRssi"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthenticated"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthorized"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientInactive"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbitrate"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxfailed"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxretries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusApGroup = mIfDot11StatusApGroup.setStatus('current')
if mibBuilder.loadTexts: mIfDot11StatusApGroup.setDescription('A collection of objects providing information about\n        IEEE802.11 interface status in Access Point mode.')
mibBuilder.exportSymbols("MDS-IF-IEEE80211-MIB", mIfDot11ApClientInactive=mIfDot11ApClientInactive, mIfDot11StationTxpackets=mIfDot11StationTxpackets, mIfDot11Channel=mIfDot11Channel, mIfDot11MIBObjects=mIfDot11MIBObjects, mIfDot11TxPower=mIfDot11TxPower, mdsIfDot11MIBGroups=mdsIfDot11MIBGroups, MacString=MacString, mIfDot11StatusEntry=mIfDot11StatusEntry, mdsIfDot11MIBCompliances=mdsIfDot11MIBCompliances, mIfDot11StationRxbytes=mIfDot11StationRxbytes, mIfDot11ApClientRssi=mIfDot11ApClientRssi, mIfDot11ApClientRxpackets=mIfDot11ApClientRxpackets, mIfDot11SerialNumber=mIfDot11SerialNumber, mIfDot11StationRxpackets=mIfDot11StationRxpackets, mIfDot11ApClientRxbytes=mIfDot11ApClientRxbytes, mIfDot11StationRssi=mIfDot11StationRssi, mIfDot11ApClientMac=mIfDot11ApClientMac, mIfDot11ApClientTxfailed=mIfDot11ApClientTxfailed, mIfDot11StationTxfailed=mIfDot11StationTxfailed, mIfDot11ApClientTxretries=mIfDot11ApClientTxretries, mIfDot11StatusTable=mIfDot11StatusTable, mIfDot11Config=mIfDot11Config, Ssid=Ssid, mIfDot11StatusApTable=mIfDot11StatusApTable, mIfDot11StatusStationGroup=mIfDot11StatusStationGroup, mIfDot11StatusApClientEntry=mIfDot11StatusApClientEntry, mdsIfDot11MIBConformance=mdsIfDot11MIBConformance, mIfDot11StationBssid=mIfDot11StationBssid, mIfDot11StationTxretries=mIfDot11StationTxretries, mIfDot11StationInactive=mIfDot11StationInactive, mdsIfDot11MIB=mdsIfDot11MIB, mIfDot11StationAuthorized=mIfDot11StationAuthorized, mIfDot11StationSsid=mIfDot11StationSsid, mIfDot11StationTxbitrate=mIfDot11StationTxbitrate, UnsignedByte=UnsignedByte, PYSNMP_MODULE_ID=mdsIfDot11MIB, mIfDot11ApSsid=mIfDot11ApSsid, mIfDot11ApClientAuthorized=mIfDot11ApClientAuthorized, mIfDot11StatusApClientTable=mIfDot11StatusApClientTable, mIfDot11ApClientTxpackets=mIfDot11ApClientTxpackets, mIfDot11StatusCommonGroup=mIfDot11StatusCommonGroup, mIfDot11StatusApGroup=mIfDot11StatusApGroup, mIfDot11Compliance=mIfDot11Compliance, UnsignedShort=UnsignedShort, mIfDot11ModemType=mIfDot11ModemType, mIfDot11Mode=mIfDot11Mode, mIfDot11Status=mIfDot11Status, mIfDot11StationAuthenticated=mIfDot11StationAuthenticated, mIfDot11StatusApEntry=mIfDot11StatusApEntry, mIfDot11ApClientTxbitrate=mIfDot11ApClientTxbitrate, mIfDot11StationTxbytes=mIfDot11StationTxbytes, mIfDot11ApClientTxbytes=mIfDot11ApClientTxbytes, Byte=Byte, mIfDot11ApClientAuthenticated=mIfDot11ApClientAuthenticated)
