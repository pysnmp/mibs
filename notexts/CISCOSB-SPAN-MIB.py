#
# PySNMP MIB module CISCOSB-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-SPAN-MIB
# Source digest sha256:c90a158b892129f6054d34979d3538e47d00e6ef5bba5e12e4da9fb4de88d497
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
class SpanDestinationPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

class SpanSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("flow", 3), ("remote-vlan", 4))

class SpanSourceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

class SpanDestinationReflectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("span", 1), ("rspan-start", 2), ("rspan-final", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('2015-03-25 00:00')
if mibBuilder.loadTexts: rlSpan.setOrganization('Cisco Systems, Inc.')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 1), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 3), SpanDestinationReflectorType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
rlSpanDestinationRemoteVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 5), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRemoteVlanId.setStatus('current')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanSourceSessionId"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceType"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 1), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 2), SpanSourceType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 3), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SPAN-MIB", PYSNMP_MODULE_ID=rlSpan, SpanDestinationPortType=SpanDestinationPortType, SpanDestinationReflectorType=SpanDestinationReflectorType, SpanSourceDirection=SpanSourceDirection, SpanSourceType=SpanSourceType, rlSpan=rlSpan, rlSpanDestinationEntry=rlSpanDestinationEntry, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex, rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, rlSpanDestinationPortType=rlSpanDestinationPortType, rlSpanDestinationRemoteVlanId=rlSpanDestinationRemoteVlanId, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpanDestinationTable=rlSpanDestinationTable, rlSpanMibVersion=rlSpanMibVersion, rlSpanSourceDirection=rlSpanSourceDirection, rlSpanSourceEntry=rlSpanSourceEntry, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanSourceRowStatus=rlSpanSourceRowStatus, rlSpanSourceSessionId=rlSpanSourceSessionId, rlSpanSourceTable=rlSpanSourceTable, rlSpanSourceType=rlSpanSourceType)
