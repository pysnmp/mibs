#
# PySNMP MIB module CISCOSB-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-SMON-MIB
# Source digest sha256:46b0c1d61266bc2b0926c97a44eb61dc7852b57c73971216dde95e3ae7d40982
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
class CopyModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

rlSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84))
rlSmon.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlSmon.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlSmon.setOrganization('Cisco Systems, Inc.')
rlPortCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopyMibVersion.setStatus('current')
rlPortCopySupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("supported", 1), ("notSupported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPortCopySupport.setStatus('current')
rlPortCopyVlanTaggingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlPortCopyVlanTaggingTable.setStatus('current')
rlPortCopyVlanTaggingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: rlPortCopyVlanTaggingEntry.setStatus('current')
rlPortCopyVlanTagging = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 3, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyVlanTagging.setStatus('current')
rlPortCopyMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 4), CopyModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopyMode.setStatus('current')
rlPortCopySessionsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPortCopySessionsEnabled.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SMON-MIB", CopyModeType=CopyModeType, PYSNMP_MODULE_ID=rlSmon, rlPortCopyMibVersion=rlPortCopyMibVersion, rlPortCopyMode=rlPortCopyMode, rlPortCopySessionsEnabled=rlPortCopySessionsEnabled, rlPortCopySupport=rlPortCopySupport, rlPortCopyVlanTagging=rlPortCopyVlanTagging, rlPortCopyVlanTaggingEntry=rlPortCopyVlanTaggingEntry, rlPortCopyVlanTaggingTable=rlPortCopyVlanTaggingTable, rlSmon=rlSmon)
