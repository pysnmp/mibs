#
# PySNMP MIB module SL-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RADIUS-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:38:49 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, mib_2, TimeTicks, NotificationType, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, iso, Integer32, Unsigned32, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "mib-2", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "iso", "Integer32", "Unsigned32", "IpAddress", "ModuleIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
slRadiusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23))
if mibBuilder.loadTexts: slRadiusMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: slRadiusMIB.setOrganization('PacketLight Networks Ltd.')
slRadiusClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1))
slRadiusClient = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1))
slRadiusTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 2))
class SharedSecret(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

slRadiusEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusEnabled.setStatus('current')
slRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2), )
if mibBuilder.loadTexts: slRadiusServerTable.setStatus('current')
slRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1), ).setIndexNames((0, "SL-RADIUS-MIB", "slRadiusServerIndex"))
if mibBuilder.loadTexts: slRadiusServerEntry.setStatus('current')
slRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRadiusServerIndex.setStatus('current')
slRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAddress.setStatus('current')
slRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerPort.setStatus('current')
slRadiusServerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusServerAdminStatus.setStatus('current')
slRadiusTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusTimeout.setStatus('current')
slRadiusSharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 23, 1, 1, 2, 1, 6), SharedSecret()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRadiusSharedSecret.setStatus('current')
mibBuilder.exportSymbols("SL-RADIUS-MIB", slRadiusClient=slRadiusClient, SharedSecret=SharedSecret, slRadiusTraps=slRadiusTraps, slRadiusServerAdminStatus=slRadiusServerAdminStatus, slRadiusSharedSecret=slRadiusSharedSecret, slRadiusEnabled=slRadiusEnabled, slRadiusTimeout=slRadiusTimeout, slRadiusServerEntry=slRadiusServerEntry, slRadiusServerPort=slRadiusServerPort, PYSNMP_MODULE_ID=slRadiusMIB, slRadiusServerIndex=slRadiusServerIndex, slRadiusServerAddress=slRadiusServerAddress, slRadiusMIB=slRadiusMIB, slRadiusServerTable=slRadiusServerTable, slRadiusClientMIBObjects=slRadiusClientMIBObjects)
