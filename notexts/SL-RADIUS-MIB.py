#
# PySNMP MIB module SL-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RADIUS-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 13:13:13 2022
# On host fv-az340-469 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, MibIdentifier, NotificationType, Gauge32, iso, Counter32, IpAddress, ObjectIdentity, Counter64, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "NotificationType", "Gauge32", "iso", "Counter32", "IpAddress", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "ModuleIdentity", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SL-RADIUS-MIB", PYSNMP_MODULE_ID=slRadiusMIB, slRadiusTraps=slRadiusTraps, slRadiusServerPort=slRadiusServerPort, slRadiusServerEntry=slRadiusServerEntry, slRadiusServerIndex=slRadiusServerIndex, slRadiusServerTable=slRadiusServerTable, slRadiusServerAddress=slRadiusServerAddress, slRadiusMIB=slRadiusMIB, slRadiusSharedSecret=slRadiusSharedSecret, SharedSecret=SharedSecret, slRadiusTimeout=slRadiusTimeout, slRadiusClient=slRadiusClient, slRadiusEnabled=slRadiusEnabled, slRadiusClientMIBObjects=slRadiusClientMIBObjects, slRadiusServerAdminStatus=slRadiusServerAdminStatus)
