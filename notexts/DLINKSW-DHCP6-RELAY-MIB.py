#
# PySNMP MIB module DLINKSW-DHCP6-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-DHCP6-RELAY-MIB
# Source digest sha256:f9b237214f3ac8915169d437320cb3ae0999a18f364f39796b228d6e1ec8fda6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
dlinkSwDhcp6RelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 88))
dlinkSwDhcp6RelayMIB.setRevisions(('2013-01-18 00:00', '2013-09-05 00:00',))
if mibBuilder.loadTexts: dlinkSwDhcp6RelayMIB.setLastUpdated('2013-09-05 00:00')
if mibBuilder.loadTexts: dlinkSwDhcp6RelayMIB.setOrganization('D-Link Corp.')
class RemoteIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("default", 1), ("cidWithUserDefine", 2), ("userDefine", 3))

dDhcp6RelayMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 0))
dDhcp6RelayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 1))
dDhcp6RelayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 2))
dDhcp6RelayGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1))
dDhcp6RRemoteIdInsertEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDhcp6RRemoteIdInsertEnabled.setStatus('current')
dDhcp6RRemoteIdPolicy = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("drop", 1), ("keep", 2))).clone('keep')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDhcp6RRemoteIdPolicy.setStatus('current')
dDhcp6RRemoteIdFormat = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 3), RemoteIdType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDhcp6RRemoteIdFormat.setStatus('current')
dDhcp6RRemoteIdUdfType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("string", 1), ("hex", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDhcp6RRemoteIdUdfType.setStatus('current')
dDhcp6RRemoteIdUdfValue = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dDhcp6RRemoteIdUdfValue.setStatus('current')
dDhcp6RelayIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2))
dDhcp6RIfRelayDestTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dDhcp6RIfRelayDestTable.setStatus('current')
dDhcp6RIfRelayDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestIndex"), (0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestDestAddr"), (0, "DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestOutIfIndex"))
if mibBuilder.loadTexts: dDhcp6RIfRelayDestEntry.setStatus('current')
dDhcp6RIfRelayDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dDhcp6RIfRelayDestIndex.setStatus('current')
dDhcp6RIfRelayDestDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 2), InetAddressIPv6()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dDhcp6RIfRelayDestDestAddr.setStatus('current')
dDhcp6RIfRelayDestOutIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: dDhcp6RIfRelayDestOutIfIndex.setStatus('current')
dDhcp6RIfRelayDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 88, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dDhcp6RIfRelayDestRowStatus.setStatus('current')
dDhcp6RelayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 1))
dDhcp6RelayCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 1, 1)).setObjects(("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RBasicGroup"), ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RelayOption37Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDhcp6RelayCompliance = dDhcp6RelayCompliance.setStatus('current')
dDhcp6RelayGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2))
dDhcp6RBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2, 1)).setObjects(("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RIfRelayDestRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDhcp6RBasicGroup = dDhcp6RBasicGroup.setStatus('current')
dDhcp6RelayOption37Group = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 88, 2, 2, 2)).setObjects(("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdInsertEnabled"), ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdPolicy"), ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdFormat"), ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdUdfType"), ("DLINKSW-DHCP6-RELAY-MIB", "dDhcp6RRemoteIdUdfValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dDhcp6RelayOption37Group = dDhcp6RelayOption37Group.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-DHCP6-RELAY-MIB", PYSNMP_MODULE_ID=dlinkSwDhcp6RelayMIB, RemoteIdType=RemoteIdType, dDhcp6RBasicGroup=dDhcp6RBasicGroup, dDhcp6RIfRelayDestDestAddr=dDhcp6RIfRelayDestDestAddr, dDhcp6RIfRelayDestEntry=dDhcp6RIfRelayDestEntry, dDhcp6RIfRelayDestIndex=dDhcp6RIfRelayDestIndex, dDhcp6RIfRelayDestOutIfIndex=dDhcp6RIfRelayDestOutIfIndex, dDhcp6RIfRelayDestRowStatus=dDhcp6RIfRelayDestRowStatus, dDhcp6RIfRelayDestTable=dDhcp6RIfRelayDestTable, dDhcp6RRemoteIdFormat=dDhcp6RRemoteIdFormat, dDhcp6RRemoteIdInsertEnabled=dDhcp6RRemoteIdInsertEnabled, dDhcp6RRemoteIdPolicy=dDhcp6RRemoteIdPolicy, dDhcp6RRemoteIdUdfType=dDhcp6RRemoteIdUdfType, dDhcp6RRemoteIdUdfValue=dDhcp6RRemoteIdUdfValue, dDhcp6RelayCompliance=dDhcp6RelayCompliance, dDhcp6RelayCompliances=dDhcp6RelayCompliances, dDhcp6RelayGeneral=dDhcp6RelayGeneral, dDhcp6RelayGroups=dDhcp6RelayGroups, dDhcp6RelayIfObjects=dDhcp6RelayIfObjects, dDhcp6RelayMIBConformance=dDhcp6RelayMIBConformance, dDhcp6RelayMIBNotifications=dDhcp6RelayMIBNotifications, dDhcp6RelayMIBObjects=dDhcp6RelayMIBObjects, dDhcp6RelayOption37Group=dDhcp6RelayOption37Group, dlinkSwDhcp6RelayMIB=dlinkSwDhcp6RelayMIB)
