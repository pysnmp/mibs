#
# PySNMP MIB module F3-EOTDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-EOTDM-MIB
# Produced by pysmi-1.1.12 at Mon May 13 02:34:43 2024
# On host fv-az774-224 platform Linux version 6.5.0-1018-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
SecondaryState, OperationalState, AdminState = mibBuilder.importSymbols("CM-COMMON-MIB", "SecondaryState", "OperationalState", "AdminState")
shelfIndex, neIndex, slotIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "neIndex", "slotIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Bits, Counter64, Unsigned32, MibIdentifier, TimeTicks, NotificationType, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Bits", "Counter64", "Unsigned32", "MibIdentifier", "TimeTicks", "NotificationType", "Counter32", "Integer32", "iso")
TextualConvention, VariablePointer, RowStatus, StorageType, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "VariablePointer", "RowStatus", "StorageType", "TruthValue", "DisplayString")
f3EOTDMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17))
f3EOTDMMIB.setRevisions(('2012-05-10 00:00',))
if mibBuilder.loadTexts: f3EOTDMMIB.setLastUpdated('201205100000Z')
if mibBuilder.loadTexts: f3EOTDMMIB.setOrganization('ADVA Optical Networking')
f3EotdmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1))
f3EotdmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2))
class VcgType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 0), ("t1", 1), ("e1", 2), ("t3", 3), ("e3", 4), ("vc12", 5), ("vc3", 6), ("vc4", 7), ("vt15", 8), ("sts1", 9), ("sts3c", 10))

class WtrTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 12)

class HoldOffTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class CtrlState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ctrlNotAppl", 0), ("ctrlFixed", 1), ("ctrlAdd", 2), ("ctrlNorm", 3), ("ctrlEos", 4), ("ctrlIdle", 5), ("ctrlDnu", 6))

class LcasSoState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("srcNotAppl", 0), ("srcIdle", 1), ("srcAdd", 2), ("srcNorm", 3), ("srcDnu", 4), ("srcRemove", 5))

class MstState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("mstNotAppl", 0), ("mstOk", 1), ("mstFail", 2))

class LcasSkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("sinkNotAppl", 0), ("sinkIdle", 1), ("sinkOk", 2), ("sinkFail", 3))

vcgTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1), )
if mibBuilder.loadTexts: vcgTable.setStatus('current')
vcgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "F3-EOTDM-MIB", "vcgIndex"))
if mibBuilder.loadTexts: vcgEntry.setStatus('current')
vcgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgIndex.setStatus('current')
vcgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgIfIndex.setStatus('current')
vcgAssociatedEthernetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgAssociatedEthernetPort.setStatus('current')
vcgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 4), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgAdminState.setStatus('current')
vcgOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 5), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgOperationalState.setStatus('current')
vcgSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 6), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgSecondaryState.setStatus('current')
vcgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 7), VcgType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgType.setStatus('current')
vcgLcasEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgLcasEnabled.setStatus('current')
vcgWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 9), WtrTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgWtrTimer.setStatus('current')
vcgHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 10), HoldOffTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgHoldOffTimer.setStatus('current')
vcgClearWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgClearWtrTimer.setStatus('current')
vcgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgRowStatus.setStatus('current')
vcgMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2), )
if mibBuilder.loadTexts: vcgMemberTable.setStatus('current')
vcgMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "F3-EOTDM-MIB", "vcgIndex"), (0, "F3-EOTDM-MIB", "vcgMemberIndex"))
if mibBuilder.loadTexts: vcgMemberEntry.setStatus('current')
vcgMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberIndex.setStatus('current')
vcgMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgMemberIfIndex.setStatus('current')
vcgMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgMemberRowStatus.setStatus('current')
vcgMemberSoSendSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoSendSeq.setStatus('current')
vcgMemberSoLcasSendCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 5), CtrlState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasSendCtrl.setStatus('current')
vcgMemberSoLcasRecvMst = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 6), MstState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasRecvMst.setStatus('current')
vcgMemberSoLcasState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 7), LcasSoState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasState.setStatus('current')
vcgMemberSkRecvSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkRecvSeq.setStatus('current')
vcgMemberSkRecvExpectSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkRecvExpectSeq.setStatus('current')
vcgMemberSkLcasRecvCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 10), CtrlState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasRecvCtrl.setStatus('current')
vcgMemberSkLcasSendMst = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 11), MstState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasSendMst.setStatus('current')
vcgMemberSkLcasState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 12), LcasSkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasState.setStatus('current')
f3EotdmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1))
f3EotdmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2))
f3EotdmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1, 1)).setObjects(("F3-EOTDM-MIB", "f3EotdmObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EotdmCompliance = f3EotdmCompliance.setStatus('current')
f3EotdmObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2, 1)).setObjects(("F3-EOTDM-MIB", "vcgIndex"), ("F3-EOTDM-MIB", "vcgIfIndex"), ("F3-EOTDM-MIB", "vcgAssociatedEthernetPort"), ("F3-EOTDM-MIB", "vcgAdminState"), ("F3-EOTDM-MIB", "vcgOperationalState"), ("F3-EOTDM-MIB", "vcgSecondaryState"), ("F3-EOTDM-MIB", "vcgType"), ("F3-EOTDM-MIB", "vcgLcasEnabled"), ("F3-EOTDM-MIB", "vcgWtrTimer"), ("F3-EOTDM-MIB", "vcgHoldOffTimer"), ("F3-EOTDM-MIB", "vcgClearWtrTimer"), ("F3-EOTDM-MIB", "vcgRowStatus"), ("F3-EOTDM-MIB", "vcgMemberIndex"), ("F3-EOTDM-MIB", "vcgMemberIfIndex"), ("F3-EOTDM-MIB", "vcgMemberRowStatus"), ("F3-EOTDM-MIB", "vcgMemberSoSendSeq"), ("F3-EOTDM-MIB", "vcgMemberSoLcasSendCtrl"), ("F3-EOTDM-MIB", "vcgMemberSoLcasRecvMst"), ("F3-EOTDM-MIB", "vcgMemberSoLcasState"), ("F3-EOTDM-MIB", "vcgMemberSkRecvSeq"), ("F3-EOTDM-MIB", "vcgMemberSkRecvExpectSeq"), ("F3-EOTDM-MIB", "vcgMemberSkLcasRecvCtrl"), ("F3-EOTDM-MIB", "vcgMemberSkLcasSendMst"), ("F3-EOTDM-MIB", "vcgMemberSkLcasState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EotdmObjectGroup = f3EotdmObjectGroup.setStatus('current')
mibBuilder.exportSymbols("F3-EOTDM-MIB", vcgClearWtrTimer=vcgClearWtrTimer, vcgEntry=vcgEntry, vcgMemberIfIndex=vcgMemberIfIndex, MstState=MstState, vcgMemberIndex=vcgMemberIndex, f3EotdmObjects=f3EotdmObjects, vcgRowStatus=vcgRowStatus, PYSNMP_MODULE_ID=f3EOTDMMIB, vcgMemberSkLcasSendMst=vcgMemberSkLcasSendMst, vcgType=vcgType, f3EOTDMMIB=f3EOTDMMIB, vcgAdminState=vcgAdminState, vcgMemberEntry=vcgMemberEntry, f3EotdmCompliance=f3EotdmCompliance, f3EotdmGroups=f3EotdmGroups, vcgTable=vcgTable, vcgMemberSoLcasRecvMst=vcgMemberSoLcasRecvMst, vcgSecondaryState=vcgSecondaryState, f3EotdmObjectGroup=f3EotdmObjectGroup, vcgLcasEnabled=vcgLcasEnabled, vcgMemberSoSendSeq=vcgMemberSoSendSeq, vcgHoldOffTimer=vcgHoldOffTimer, vcgMemberSkRecvSeq=vcgMemberSkRecvSeq, vcgMemberSkLcasRecvCtrl=vcgMemberSkLcasRecvCtrl, vcgMemberSkLcasState=vcgMemberSkLcasState, f3EotdmConformance=f3EotdmConformance, CtrlState=CtrlState, vcgIndex=vcgIndex, vcgAssociatedEthernetPort=vcgAssociatedEthernetPort, vcgMemberSoLcasState=vcgMemberSoLcasState, vcgMemberTable=vcgMemberTable, vcgMemberRowStatus=vcgMemberRowStatus, vcgIfIndex=vcgIfIndex, vcgWtrTimer=vcgWtrTimer, vcgMemberSoLcasSendCtrl=vcgMemberSoLcasSendCtrl, VcgType=VcgType, WtrTime=WtrTime, LcasSkState=LcasSkState, vcgMemberSkRecvExpectSeq=vcgMemberSkRecvExpectSeq, f3EotdmCompliances=f3EotdmCompliances, vcgOperationalState=vcgOperationalState, HoldOffTime=HoldOffTime, LcasSoState=LcasSoState)
