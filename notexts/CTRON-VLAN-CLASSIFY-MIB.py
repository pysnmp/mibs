#
# PySNMP MIB module CTRON-VLAN-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-VLAN-CLASSIFY-MIB
# Produced by pysmi-1.1.12 at Sat Jul  6 01:08:17 2024
# On host fv-az1532-138 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctVlanExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctVlanExt")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, ObjectIdentity, NotificationType, Gauge32, Integer32, TimeTicks, MibIdentifier, IpAddress, Counter32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "ObjectIdentity", "NotificationType", "Gauge32", "Integer32", "TimeTicks", "MibIdentifier", "IpAddress", "Counter32", "iso", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ctVlanClassify = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6))
ctVlanClassify.setRevisions(('2002-12-19 16:31', '2002-03-27 20:55',))
if mibBuilder.loadTexts: ctVlanClassify.setLastUpdated('200301292215Z')
if mibBuilder.loadTexts: ctVlanClassify.setOrganization('Enterasys Networks, Inc')
ctVlanClassifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1))
class CtVlanClassifyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("etherType", 1), ("llcDsapSsap", 2), ("ipTypeOfService", 3), ("ipProtocolType", 4), ("ipxClassOfService", 5), ("ipxPacketType", 6), ("ipAddressSource", 7), ("ipAddressDestination", 8), ("ipAddressBilateral", 9), ("ipxNetworkSource", 10), ("ipxNetworkDestination", 11), ("ipxNetworkBilateral", 12), ("ipUdpPortSource", 13), ("ipUdpPortDestination", 14), ("ipUdpPortBilateral", 15), ("ipTcpPortSource", 16), ("ipTcpPortDestination", 17), ("ipTcpPortBilateral", 18), ("ipxSocketSource", 19), ("ipxSocketDestination", 20), ("ipxSocketBilateral", 21), ("macAddressSource", 22), ("macAddressDestination", 23), ("macAddressBilateral", 24), ("ipFragments", 25), ("ipUdpPortSourceRange", 26), ("ipUdpPortDestinationRange", 27), ("ipUdpPortBilateralRange", 28), ("ipTcpPortSourceRange", 29), ("ipTcpPortDestinationRange", 30), ("ipTcpPortBilateralRange", 31), ("icmpType", 32), ("vlanId", 33), ("tci", 34))

class VlanIndex(TextualConvention, Unsigned32):
    status = 'current'

ctVlanClassifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctVlanClassifyStatus.setStatus('current')
ctVlanClassifyMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanClassifyMaxEntries.setStatus('current')
ctVlanClassifyNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanClassifyNumEntries.setStatus('current')
ctVlanClassifyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4), )
if mibBuilder.loadTexts: ctVlanClassifyTable.setStatus('current')
ctVlanClassifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1), ).setIndexNames((0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyVlanIndex"), (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataMeaning"), (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataVal"), (0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyDataMask"))
if mibBuilder.loadTexts: ctVlanClassifyEntry.setStatus('current')
ctVlanClassifyVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: ctVlanClassifyVlanIndex.setStatus('current')
ctVlanClassifyDataMeaning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 2), CtVlanClassifyType())
if mibBuilder.loadTexts: ctVlanClassifyDataMeaning.setStatus('current')
ctVlanClassifyDataVal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ctVlanClassifyDataVal.setStatus('current')
ctVlanClassifyDataMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: ctVlanClassifyDataMask.setStatus('current')
ctVlanClassifyIngressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 5), PortList().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctVlanClassifyIngressList.setStatus('current')
ctVlanClassifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctVlanClassifyRowStatus.setStatus('current')
ctVlanClassifyRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanClassifyRowInfo.setStatus('current')
ctVlanClassifyAbilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5), )
if mibBuilder.loadTexts: ctVlanClassifyAbilityTable.setStatus('current')
ctVlanClassifyAbilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1), ).setIndexNames((0, "CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyAbility"))
if mibBuilder.loadTexts: ctVlanClassifyAbilityEntry.setStatus('current')
ctVlanClassifyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 1), CtVlanClassifyType())
if mibBuilder.loadTexts: ctVlanClassifyAbility.setStatus('current')
ctVlanClassifyPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanClassifyPorts.setStatus('current')
ctVlanClassifyActionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwardNoFrames", 1), ("forwardAllFrames", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctVlanClassifyActionStatus.setStatus('current')
ctVlanClassifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2))
ctVlanClassifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 1))
ctVlanClassifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 2))
ctVlanClassifyBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 1, 1)).setObjects(("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyStatus"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyMaxEntries"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyNumEntries"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyIngressList"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyRowStatus"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyRowInfo"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyPorts"), ("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyActionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctVlanClassifyBaseGroup = ctVlanClassifyBaseGroup.setStatus('current')
ctVlanClassifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 6, 2, 2, 1)).setObjects(("CTRON-VLAN-CLASSIFY-MIB", "ctVlanClassifyBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctVlanClassifyCompliance = ctVlanClassifyCompliance.setStatus('current')
mibBuilder.exportSymbols("CTRON-VLAN-CLASSIFY-MIB", ctVlanClassifyAbility=ctVlanClassifyAbility, ctVlanClassifyDataVal=ctVlanClassifyDataVal, ctVlanClassifyBaseGroup=ctVlanClassifyBaseGroup, ctVlanClassifyCompliance=ctVlanClassifyCompliance, ctVlanClassifyAbilityTable=ctVlanClassifyAbilityTable, ctVlanClassifyGroups=ctVlanClassifyGroups, ctVlanClassifyAbilityEntry=ctVlanClassifyAbilityEntry, ctVlanClassifyPorts=ctVlanClassifyPorts, PYSNMP_MODULE_ID=ctVlanClassify, ctVlanClassifyIngressList=ctVlanClassifyIngressList, ctVlanClassify=ctVlanClassify, ctVlanClassifyStatus=ctVlanClassifyStatus, ctVlanClassifyObjects=ctVlanClassifyObjects, ctVlanClassifyDataMeaning=ctVlanClassifyDataMeaning, CtVlanClassifyType=CtVlanClassifyType, ctVlanClassifyNumEntries=ctVlanClassifyNumEntries, ctVlanClassifyRowInfo=ctVlanClassifyRowInfo, ctVlanClassifyConformance=ctVlanClassifyConformance, ctVlanClassifyMaxEntries=ctVlanClassifyMaxEntries, ctVlanClassifyVlanIndex=ctVlanClassifyVlanIndex, ctVlanClassifyCompliances=ctVlanClassifyCompliances, ctVlanClassifyTable=ctVlanClassifyTable, ctVlanClassifyRowStatus=ctVlanClassifyRowStatus, ctVlanClassifyEntry=ctVlanClassifyEntry, VlanIndex=VlanIndex, ctVlanClassifyDataMask=ctVlanClassifyDataMask, ctVlanClassifyActionStatus=ctVlanClassifyActionStatus)
