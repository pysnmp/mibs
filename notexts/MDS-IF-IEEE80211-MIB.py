#
# PySNMP MIB module MDS-IF-IEEE80211-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-IEEE80211-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:25:26 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32, TimeTicks, NotificationType, ObjectIdentity, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
mdsIfDot11MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2))
mdsIfDot11MIB.setRevisions(('2018-05-16 00:00', '2014-10-20 00:00', '2013-04-26 00:00',))
if mibBuilder.loadTexts: mdsIfDot11MIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfDot11MIB.setOrganization('GE MDS LLC http://www.gemds.com')
mIfDot11MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1))
mIfDot11Config = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 1))
mIfDot11Status = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2))
class Byte(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Ssid(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class MacString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

mIfDot11StatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: mIfDot11StatusTable.setStatus('current')
mIfDot11StatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfDot11StatusEntry.setStatus('current')
mIfDot11SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11SerialNumber.setStatus('current')
mIfDot11Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("station", 1), ("accessPoint", 2), ("accessPointStation", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11Mode.setStatus('current')
mIfDot11TxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 3), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11TxPower.setStatus('current')
mIfDot11Channel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 4), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11Channel.setStatus('current')
mIfDot11StationSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 5), Ssid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationSsid.setStatus('current')
mIfDot11StationBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 6), MacString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationBssid.setStatus('current')
mIfDot11StationRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 7), Byte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRssi.setStatus('current')
mIfDot11StationAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationAuthenticated.setStatus('current')
mIfDot11StationAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationAuthorized.setStatus('current')
mIfDot11StationInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationInactive.setStatus('current')
mIfDot11StationRxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRxbytes.setStatus('current')
mIfDot11StationRxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationRxpackets.setStatus('current')
mIfDot11StationTxbitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 13), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxbitrate.setStatus('current')
mIfDot11StationTxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxbytes.setStatus('current')
mIfDot11StationTxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxpackets.setStatus('current')
mIfDot11StationTxfailed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxfailed.setStatus('current')
mIfDot11StationTxretries = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11StationTxretries.setStatus('current')
mIfDot11ModemType = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("w51", 1), ("w52", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ModemType.setStatus('current')
mIfDot11StatusApTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2), )
if mibBuilder.loadTexts: mIfDot11StatusApTable.setStatus('current')
mIfDot11StatusApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"))
if mibBuilder.loadTexts: mIfDot11StatusApEntry.setStatus('current')
mIfDot11ApSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 2, 1, 1), Ssid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApSsid.setStatus('current')
mIfDot11StatusApClientTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3), )
if mibBuilder.loadTexts: mIfDot11StatusApClientTable.setStatus('current')
mIfDot11StatusApClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"), (0, "MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"))
if mibBuilder.loadTexts: mIfDot11StatusApClientEntry.setStatus('current')
mIfDot11ApClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 1), MacString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientMac.setStatus('current')
mIfDot11ApClientRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 2), Byte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRssi.setStatus('current')
mIfDot11ApClientAuthenticated = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientAuthenticated.setStatus('current')
mIfDot11ApClientAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientAuthorized.setStatus('current')
mIfDot11ApClientInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientInactive.setStatus('current')
mIfDot11ApClientRxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRxbytes.setStatus('current')
mIfDot11ApClientRxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientRxpackets.setStatus('current')
mIfDot11ApClientTxbitrate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 8), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxbitrate.setStatus('current')
mIfDot11ApClientTxbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxbytes.setStatus('current')
mIfDot11ApClientTxpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxpackets.setStatus('current')
mIfDot11ApClientTxfailed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxfailed.setStatus('current')
mIfDot11ApClientTxretries = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfDot11ApClientTxretries.setStatus('current')
mdsIfDot11MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3))
mdsIfDot11MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1))
mdsIfDot11MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2))
mIfDot11Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 1, 1)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11StatusCommonGroup"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusStationGroup"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StatusApGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11Compliance = mIfDot11Compliance.setStatus('current')
mIfDot11StatusCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 1)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11SerialNumber"), ("MDS-IF-IEEE80211-MIB", "mIfDot11Mode"), ("MDS-IF-IEEE80211-MIB", "mIfDot11TxPower"), ("MDS-IF-IEEE80211-MIB", "mIfDot11Channel"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ModemType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusCommonGroup = mIfDot11StatusCommonGroup.setStatus('current')
mIfDot11StatusStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 2)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11StationSsid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRssi"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationBssid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthenticated"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationAuthorized"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationInactive"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationRxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbitrate"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxfailed"), ("MDS-IF-IEEE80211-MIB", "mIfDot11StationTxretries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusStationGroup = mIfDot11StatusStationGroup.setStatus('current')
mIfDot11StatusApGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 2, 3, 2, 3)).setObjects(("MDS-IF-IEEE80211-MIB", "mIfDot11ApSsid"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientMac"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRssi"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthenticated"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientAuthorized"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientInactive"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientRxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbitrate"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxbytes"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxpackets"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxfailed"), ("MDS-IF-IEEE80211-MIB", "mIfDot11ApClientTxretries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfDot11StatusApGroup = mIfDot11StatusApGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-IF-IEEE80211-MIB", mIfDot11StationBssid=mIfDot11StationBssid, mIfDot11StatusApTable=mIfDot11StatusApTable, mIfDot11ApClientTxbytes=mIfDot11ApClientTxbytes, mdsIfDot11MIBGroups=mdsIfDot11MIBGroups, mIfDot11TxPower=mIfDot11TxPower, Byte=Byte, mIfDot11MIBObjects=mIfDot11MIBObjects, mIfDot11ApClientAuthenticated=mIfDot11ApClientAuthenticated, mIfDot11StationRxpackets=mIfDot11StationRxpackets, mIfDot11StationAuthorized=mIfDot11StationAuthorized, mIfDot11ApClientRssi=mIfDot11ApClientRssi, mIfDot11StationRssi=mIfDot11StationRssi, MacString=MacString, mIfDot11ApClientRxpackets=mIfDot11ApClientRxpackets, mIfDot11StationAuthenticated=mIfDot11StationAuthenticated, mIfDot11ApClientInactive=mIfDot11ApClientInactive, Ssid=Ssid, mIfDot11StationTxbytes=mIfDot11StationTxbytes, mIfDot11StationTxfailed=mIfDot11StationTxfailed, mIfDot11Compliance=mIfDot11Compliance, mIfDot11SerialNumber=mIfDot11SerialNumber, mIfDot11ApSsid=mIfDot11ApSsid, mIfDot11Config=mIfDot11Config, mIfDot11StatusApClientTable=mIfDot11StatusApClientTable, PYSNMP_MODULE_ID=mdsIfDot11MIB, mIfDot11Channel=mIfDot11Channel, mIfDot11ApClientMac=mIfDot11ApClientMac, mIfDot11StatusApGroup=mIfDot11StatusApGroup, mIfDot11StationTxretries=mIfDot11StationTxretries, mIfDot11Mode=mIfDot11Mode, mdsIfDot11MIB=mdsIfDot11MIB, mIfDot11StationTxpackets=mIfDot11StationTxpackets, mIfDot11StatusApEntry=mIfDot11StatusApEntry, mIfDot11ApClientAuthorized=mIfDot11ApClientAuthorized, mIfDot11ApClientTxbitrate=mIfDot11ApClientTxbitrate, mIfDot11StatusCommonGroup=mIfDot11StatusCommonGroup, mIfDot11StatusStationGroup=mIfDot11StatusStationGroup, mIfDot11ApClientRxbytes=mIfDot11ApClientRxbytes, mIfDot11StationInactive=mIfDot11StationInactive, mIfDot11Status=mIfDot11Status, mIfDot11StationRxbytes=mIfDot11StationRxbytes, mIfDot11ApClientTxretries=mIfDot11ApClientTxretries, mIfDot11StatusTable=mIfDot11StatusTable, mIfDot11ModemType=mIfDot11ModemType, UnsignedByte=UnsignedByte, mIfDot11ApClientTxpackets=mIfDot11ApClientTxpackets, mIfDot11ApClientTxfailed=mIfDot11ApClientTxfailed, mdsIfDot11MIBConformance=mdsIfDot11MIBConformance, UnsignedShort=UnsignedShort, mIfDot11StatusApClientEntry=mIfDot11StatusApClientEntry, mIfDot11StationSsid=mIfDot11StationSsid, mIfDot11StationTxbitrate=mIfDot11StationTxbitrate, mdsIfDot11MIBCompliances=mdsIfDot11MIBCompliances, mIfDot11StatusEntry=mIfDot11StatusEntry)
