#
# PySNMP MIB module CISCOSB-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-SpecialBpdu-MIB
# Source digest sha256:74fab94bf901ddf26794020580b96657e2e57810d0b9735f4450a2d02726297d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('2008-05-03 12:34')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Cisco Systems, Inc.')
class EncapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 1), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 2), EncapType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SpecialBpdu-MIB", Action=Action, EncapType=EncapType, HwAction=HwAction, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpdu=rlSpecialBpdu, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduEntry=rlSpecialBpduEntry, rlSpecialBpduHwAction=rlSpecialBpduHwAction, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, rlSpecialBpduProtId=rlSpecialBpduProtId, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, rlSpecialBpduTable=rlSpecialBpduTable)
