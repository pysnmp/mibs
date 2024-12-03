#
# PySNMP MIB module SL-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RADIUS-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:43:55 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Bits, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Counter32, mib_2, Counter64, iso, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "mib-2", "Counter64", "iso", "TimeTicks", "ObjectIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("SL-RADIUS-MIB", slRadiusTraps=slRadiusTraps, slRadiusMIB=slRadiusMIB, slRadiusClient=slRadiusClient, slRadiusServerIndex=slRadiusServerIndex, slRadiusServerAddress=slRadiusServerAddress, slRadiusServerPort=slRadiusServerPort, slRadiusClientMIBObjects=slRadiusClientMIBObjects, slRadiusTimeout=slRadiusTimeout, SharedSecret=SharedSecret, PYSNMP_MODULE_ID=slRadiusMIB, slRadiusServerAdminStatus=slRadiusServerAdminStatus, slRadiusServerTable=slRadiusServerTable, slRadiusEnabled=slRadiusEnabled, slRadiusSharedSecret=slRadiusSharedSecret, slRadiusServerEntry=slRadiusServerEntry)
