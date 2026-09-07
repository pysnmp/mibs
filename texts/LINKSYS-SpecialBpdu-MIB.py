#
# PySNMP MIB module LINKSYS-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-SpecialBpdu-MIB
# Source digest sha256:d70ed590aa5bd6fcdb6d7ea606ccb3ad052e86bfea0a5033bbc289e6a3f5580d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpecialBpdu.setRevisionsDescriptions(('The private MIB module definition Traffic Segmentation MIB.',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('2008-05-03 12:34')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlSpecialBpdu.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlSpecialBpdu.setDescription('<description>')
class EncapType(TextualConvention, Integer32):
    description = 'The L2 encapsulation type. In case the entry contains MAC only,\n         the encapsulation will be none(1), otherwisw:\n         EthernetV2 (2), LLC (2) or LLC-Snap (3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    description = 'Action to be taken. Bridge(1) or Discard (2)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    description = 'Configured action in the HW. Forward(1), Drop (2) or Trap(3)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduTable.setDescription('A table contains entries of Special BPDU configuration')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEntry.setDescription('An entry of Special BPDU configuration table')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 1), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setDescription('Reserved MAC Mc 01:80:C2:00:00:00 - 01:80:C2:00:00:2F.')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 2), EncapType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduEncap.setDescription('L2 Encapsulation Type: Ethernet-V2, LLC or LLC-Snap.')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduProtId.setDescription('Protocol ID. For Ethernet-V2: 0x600 - 0xFFFF; For LLC: 0 - 0xFFFF;\n         For LLC-Snap: 0 - 0xFFFFFFFFFF.')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduAction.setDescription('Action to be taken on the incoming frame: Discard or Bridge.')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setDescription('This object indicates the status of this entry.')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setDescription('A table contains entries of Special BPDU Hw status')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "LINKSYS-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setDescription('An entry of Special BPDU Hw status table')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setDescription('HW action per MAC address: Forward, Drop or Trap.')
mibBuilder.exportSymbols("LINKSYS-SpecialBpdu-MIB", Action=Action, EncapType=EncapType, HwAction=HwAction, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpdu=rlSpecialBpdu, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduTable=rlSpecialBpduTable)
