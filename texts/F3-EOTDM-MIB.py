#
# PySNMP MIB module F3-EOTDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-EOTDM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:10:39 2024
# On host fv-az735-175 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
AdminState, OperationalState, SecondaryState = mibBuilder.importSymbols("CM-COMMON-MIB", "AdminState", "OperationalState", "SecondaryState")
slotIndex, neIndex, shelfIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "slotIndex", "neIndex", "shelfIndex")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, TimeTicks, Gauge32, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, Counter64, Unsigned32, NotificationType, Integer32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "Counter64", "Unsigned32", "NotificationType", "Integer32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, VariablePointer, TextualConvention, TruthValue, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "VariablePointer", "TextualConvention", "TruthValue", "StorageType", "DisplayString")
f3EOTDMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17))
f3EOTDMMIB.setRevisions(('2012-05-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3EOTDMMIB.setRevisionsDescriptions(('Notes from release 201205100000Z,\n             (1)MIB version ready for release FSP150CM 5.5.',))
if mibBuilder.loadTexts: f3EOTDMMIB.setLastUpdated('201205100000Z')
if mibBuilder.loadTexts: f3EOTDMMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3EOTDMMIB.setContactInfo('        Kasen Zeng\n                     ADVA Optical Networking, Inc.\n                     Tel: \n                     E-mail: kzeng@advaoptical.com\n                     Postal: 18/F, Maoye Times Square,\n                     Haide 2nd Road, Nanshan District,\n                     Shenzhen, P.R.China 518054')
if mibBuilder.loadTexts: f3EOTDMMIB.setDescription('This module defines the EOTDM MIB definitions used by \n             the F3 (FSP150CM/CC) product lines.\n             Copyright (C) ADVA Optical Networking.')
f3EotdmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1))
f3EotdmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2))
class VcgType(TextualConvention, Integer32):
    description = 'Describes the VC type in a virtual concatenate group. All VCs in this\n        group is the same type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 0), ("t1", 1), ("e1", 2), ("t3", 3), ("e3", 4), ("vc12", 5), ("vc3", 6), ("vc4", 7), ("vt15", 8), ("sts1", 9), ("sts3c", 10))

class WtrTime(TextualConvention, Integer32):
    description = 'Wait to restore(WTR) time for LCAS protocol when the dMSU defect\n        occured (Unit: minute).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 12)

class HoldOffTime(TextualConvention, Integer32):
    description = 'Hold off time for LCAS protocol when the dMSU defect occured\n        (Unit: 100ms).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class CtrlState(TextualConvention, Integer32):
    description = 'Discribes the CTRL status of a virtual container in LCAS\n         control packet:\n         - ctrlNotAppl: NA:    Not applicable, ie, this VC is not allocated\n                               to a VCG or LCAS is disabled\n         - ctrlFixed:   FIXED: This end uses fixed bandwidth (non-LCAS mode)\n         - ctrlAdd:     ADD:   This member is about to be added to the group\n         - ctrlNorm:    NORM:  Normal transmission\n         - ctrlEos:     EOS:   End of Sequence and Normal transmission\n         - ctrlIdle:    IDLE:  This member is not part of the group or about\n                               to be removed\n         - ctrlDnu:     DNU:   Do Not Use (the payload) the Sk side reported\n                               FAIL status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ctrlNotAppl", 0), ("ctrlFixed", 1), ("ctrlAdd", 2), ("ctrlNorm", 3), ("ctrlEos", 4), ("ctrlIdle", 5), ("ctrlDnu", 6))

class LcasSoState(TextualConvention, Integer32):
    description = "The status of LCAS protocol at the source end of a virtual container:\n         - srcNotAppl: NA:     Not applicable, ie, this VC is not allocated\n                             to a VCG or LCAS is disabled\n         -srcIdle:    IDLE:   The VC is not in use or has been removed.\n         - srcAdd:     ADD:    The VC is in the process of being added.\n                             May also indicate that the sink end:\n                             - does not have LCAS enabled and this VC is\n                               in use at this end, or\n                             - this VC is not allocated in the service.\n         - srcNorm:    NORM:   The VC is in use with a good path to the\n                             sink end.\n         - srcDnu:     DNU:   'Do not use' indicates the VC is in use but\n                             has a failed path to the sink end.\n         - srcRemove:  REMOVE: The VC is being deleted from the service."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("srcNotAppl", 0), ("srcIdle", 1), ("srcAdd", 2), ("srcNorm", 3), ("srcDnu", 4), ("srcRemove", 5))

class MstState(TextualConvention, Integer32):
    description = 'Discribes the MST status of a virtual container in LCAS\n         control packet:\n         - mstNotAppl: NA:   Not applicable, ie, this VC is not allocated\n                             to a VCG or LCAS is disabled\n         - mstOk:      OK:   The MST status of this virtual container is OK\n         - mstFail:    FAIL: The MST status of this virtual container is FAIL'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("mstNotAppl", 0), ("mstOk", 1), ("mstFail", 2))

class LcasSkState(TextualConvention, Integer32):
    description = 'The status of LCAS protocol at the sink end of a virtual container:\n         - sinkNotAppl: NA:   Not applicable, ie, this VC is not allocated\n                              to a VCG or LCAS is disabled\n         - sinkIdle:    IDLE: The virtual container is not in use.\n         - sinkOk:      OK:   Normal incoming signal, or has acknowledged\n                              a request to be added to the service.\n         - sinkFail:    FAIL: Failure condition on incoming signal, or has\n                              acknowledged a request for removal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("sinkNotAppl", 0), ("sinkIdle", 1), ("sinkOk", 2), ("sinkFail", 3))

vcgTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1), )
if mibBuilder.loadTexts: vcgTable.setStatus('current')
if mibBuilder.loadTexts: vcgTable.setDescription('A list of entries corresponding to virtual concatenate groups.')
vcgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "F3-EOTDM-MIB", "vcgIndex"))
if mibBuilder.loadTexts: vcgEntry.setStatus('current')
if mibBuilder.loadTexts: vcgEntry.setDescription('A conceptual row in the vcgTable.')
vcgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgIndex.setStatus('current')
if mibBuilder.loadTexts: vcgIndex.setDescription('An integer index value used to uniquely identify this vcg within a card.')
vcgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgIfIndex.setStatus('current')
if mibBuilder.loadTexts: vcgIfIndex.setDescription('This object has the same value as ifIndex for vcg.')
vcgAssociatedEthernetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgAssociatedEthernetPort.setStatus('current')
if mibBuilder.loadTexts: vcgAssociatedEthernetPort.setDescription('This object describes the related Ethernet Port of the vcg.')
vcgAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 4), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgAdminState.setStatus('current')
if mibBuilder.loadTexts: vcgAdminState.setDescription('This object represents the Administrative State of the vcg.')
vcgOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 5), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgOperationalState.setStatus('current')
if mibBuilder.loadTexts: vcgOperationalState.setDescription('This object represents the Operational State of the vcg.')
vcgSecondaryState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 6), SecondaryState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgSecondaryState.setStatus('current')
if mibBuilder.loadTexts: vcgSecondaryState.setDescription('This object represents the Secondary State of the vcg.')
vcgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 7), VcgType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgType.setStatus('current')
if mibBuilder.loadTexts: vcgType.setDescription('Type of paths in this VCG. All paths in this VCG are the same type.\n          This is a required field when creating a VCG, and can not be\n          changed on an existing VCG.\n          See the definition of VcType for more details.')
vcgLcasEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgLcasEnabled.setStatus('current')
if mibBuilder.loadTexts: vcgLcasEnabled.setDescription('This object provides whether Lcas is enabled/disabled.')
vcgWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 9), WtrTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgWtrTimer.setStatus('current')
if mibBuilder.loadTexts: vcgWtrTimer.setDescription('This object specifies wait to restore(WTR) time for LCAS protocol.\n         When creating VCG with LCAS enabled, it is the default value,\n         says 5 minutes. When creating VCG with LCAS disabled, it is 0 (means\n         that the WTR is disabled).')
vcgHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 10), HoldOffTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcgHoldOffTimer.setStatus('current')
if mibBuilder.loadTexts: vcgHoldOffTimer.setDescription('This object specifies hold off time for LCAS protocol.\n         When creating VCG with LCAS enabled, it is the default value,\n         says 0 ms. When creating VCG with LCAS disabled, it is 0 ms.')
vcgClearWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgClearWtrTimer.setStatus('current')
if mibBuilder.loadTexts: vcgClearWtrTimer.setDescription("This object will trigger an action.\n         When writing with '1', a 'clear WTR timer' action for all paths in\n         the VCG is triggered. Writing '0' is no effect.\n         When reading, it always returns 0.")
vcgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgRowStatus.setStatus('current')
if mibBuilder.loadTexts: vcgRowStatus.setDescription('The status of this row.  An entry MUST NOT exist in the \n            active state unless all objects in the entry have an \n            appropriate value, as described\n            in the description clause for each writable object.\n\n            The values of vcgRowStatus supported are\n            createAndGo(4) and destroy(6).  All mandatory attributes\n            must be specified in a single SNMP SET request with\n            neRowStatus value as createAndGo(4).\n            Upon successful row creation, this object has a\n            value of active(1).\n\n            The vcgRowStatus object may be modified if\n            the associated instance of this object is equal to active(1).')
vcgMemberTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2), )
if mibBuilder.loadTexts: vcgMemberTable.setStatus('current')
if mibBuilder.loadTexts: vcgMemberTable.setDescription('A list of entries corresponding to VCGs. Each entry of the table\n             represents a path which is allocated to a VCG.')
vcgMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "F3-EOTDM-MIB", "vcgIndex"), (0, "F3-EOTDM-MIB", "vcgMemberIndex"))
if mibBuilder.loadTexts: vcgMemberEntry.setStatus('current')
if mibBuilder.loadTexts: vcgMemberEntry.setDescription('A conceptual row in the vcgMemberTable.')
vcgMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberIndex.setStatus('current')
if mibBuilder.loadTexts: vcgMemberIndex.setDescription('An integer index value used to uniquely identify this vcg member.')
vcgMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgMemberIfIndex.setStatus('current')
if mibBuilder.loadTexts: vcgMemberIfIndex.setDescription('This object has the same value as ifIndex for \n             vcg path.  An integer index value used to \n             uniquely identify this vcg path.')
vcgMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vcgMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: vcgMemberRowStatus.setDescription('The status of this row.  An entry MUST NOT exist in the \n            active state unless all objects in the entry have an \n            appropriate value, as described\n            in the description clause for each writable object.\n\n            The values of vcgMemberRowStatus supported are\n            createAndGo(4) and destroy(6).  All mandatory attributes\n            must be specified in a single SNMP SET request with\n            neRowStatus value as createAndGo(4).\n            Upon successful row creation, this object has a\n            value of active(1).\n\n            The vcgMemberRowStatus object may be modified if\n            the associated instance of this object is equal to active(1).')
vcgMemberSoSendSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoSendSeq.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSoSendSeq.setDescription('As the source side, this object reports the sequence number sent\n          to the sink side. The sequence number is determined by the LCAS\n          protocol (when LCAS is enabled) or by the order that each path was\n          added into the VCG (when LCAS is disabled). If SQ is invalid,\n          -1 is returned')
vcgMemberSoLcasSendCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 5), CtrlState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasSendCtrl.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSoLcasSendCtrl.setDescription("As the source side, this object reports the CTRL status which is\n          sent to the sink side. The CTRL status is determined by the LCAS\n          protocol.\n          When LCAS is not used, the value 'ctrlNotAppl' is returned.")
vcgMemberSoLcasRecvMst = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 6), MstState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasRecvMst.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSoLcasRecvMst.setDescription("As the source side, this object reports the member status which is\n          received from sink side. The member status is determined by the\n          LCAS protocol.\n          When LCAS is not used, the value 'mstNotAppl' is returned.")
vcgMemberSoLcasState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 7), LcasSoState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSoLcasState.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSoLcasState.setDescription("This object reports the current source status of this path as\n          determined by the LCAS protocol. When LCAS is not in use,\n          the value 'srcNotAppl' is returned.")
vcgMemberSkRecvSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkRecvSeq.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSkRecvSeq.setDescription('As the sink side, this object reports the sequence number which is\n          received from source side. If SQ is invalid, -1 is returned.')
vcgMemberSkRecvExpectSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkRecvExpectSeq.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSkRecvExpectSeq.setDescription("As the sink side, this object reports the sequence number expected.\n          If LCAS is enabled, this value is -1. Otherwise, it's the order that\n          each path was added into the VCG, starting from 0.\n          If SQ is invalid, -1 is returned.")
vcgMemberSkLcasRecvCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 10), CtrlState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasRecvCtrl.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSkLcasRecvCtrl.setDescription("As the sink side, this object reports the CTRL status which is\n          received from source side. The CTRL status is determined by the\n          LCAS protocol. When LCAS is not used, the value 'ctrlNotAppl'\n          is returned.")
vcgMemberSkLcasSendMst = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 11), MstState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasSendMst.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSkLcasSendMst.setDescription("As the sink side, this object reports the member status which is\n          sent to source side. The 'member status' is determined by the status\n          of received path member. When LCAS is not used, the value 'mstNotAppl'\n          is returned.")
vcgMemberSkLcasState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 12), LcasSkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcgMemberSkLcasState.setStatus('current')
if mibBuilder.loadTexts: vcgMemberSkLcasState.setDescription("This object reports the current sink status of this path as\n          determined by the LCAS protocol. When LCAS is not in use,\n          the value 'sinkNotAppl' is returned.")
f3EotdmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1))
f3EotdmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2))
f3EotdmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1, 1)).setObjects(("F3-EOTDM-MIB", "f3EotdmObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EotdmCompliance = f3EotdmCompliance.setStatus('current')
if mibBuilder.loadTexts: f3EotdmCompliance.setDescription('Describes the requirements for conformance to the f3 Tdm\n             group.')
f3EotdmObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2, 1)).setObjects(("F3-EOTDM-MIB", "vcgIndex"), ("F3-EOTDM-MIB", "vcgIfIndex"), ("F3-EOTDM-MIB", "vcgAssociatedEthernetPort"), ("F3-EOTDM-MIB", "vcgAdminState"), ("F3-EOTDM-MIB", "vcgOperationalState"), ("F3-EOTDM-MIB", "vcgSecondaryState"), ("F3-EOTDM-MIB", "vcgType"), ("F3-EOTDM-MIB", "vcgLcasEnabled"), ("F3-EOTDM-MIB", "vcgWtrTimer"), ("F3-EOTDM-MIB", "vcgHoldOffTimer"), ("F3-EOTDM-MIB", "vcgClearWtrTimer"), ("F3-EOTDM-MIB", "vcgRowStatus"), ("F3-EOTDM-MIB", "vcgMemberIndex"), ("F3-EOTDM-MIB", "vcgMemberIfIndex"), ("F3-EOTDM-MIB", "vcgMemberRowStatus"), ("F3-EOTDM-MIB", "vcgMemberSoSendSeq"), ("F3-EOTDM-MIB", "vcgMemberSoLcasSendCtrl"), ("F3-EOTDM-MIB", "vcgMemberSoLcasRecvMst"), ("F3-EOTDM-MIB", "vcgMemberSoLcasState"), ("F3-EOTDM-MIB", "vcgMemberSkRecvSeq"), ("F3-EOTDM-MIB", "vcgMemberSkRecvExpectSeq"), ("F3-EOTDM-MIB", "vcgMemberSkLcasRecvCtrl"), ("F3-EOTDM-MIB", "vcgMemberSkLcasSendMst"), ("F3-EOTDM-MIB", "vcgMemberSkLcasState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3EotdmObjectGroup = f3EotdmObjectGroup.setStatus('current')
if mibBuilder.loadTexts: f3EotdmObjectGroup.setDescription('A collection of objects used to manage the f3 Tdm\n             group.')
mibBuilder.exportSymbols("F3-EOTDM-MIB", vcgMemberSoLcasState=vcgMemberSoLcasState, f3EotdmGroups=f3EotdmGroups, vcgMemberSkRecvSeq=vcgMemberSkRecvSeq, vcgType=vcgType, vcgMemberIndex=vcgMemberIndex, vcgMemberSoLcasSendCtrl=vcgMemberSoLcasSendCtrl, vcgClearWtrTimer=vcgClearWtrTimer, WtrTime=WtrTime, vcgHoldOffTimer=vcgHoldOffTimer, LcasSoState=LcasSoState, vcgRowStatus=vcgRowStatus, vcgOperationalState=vcgOperationalState, vcgAdminState=vcgAdminState, f3EotdmObjects=f3EotdmObjects, vcgMemberSoSendSeq=vcgMemberSoSendSeq, f3EotdmConformance=f3EotdmConformance, VcgType=VcgType, vcgIndex=vcgIndex, vcgMemberTable=vcgMemberTable, vcgMemberSkLcasState=vcgMemberSkLcasState, vcgMemberSoLcasRecvMst=vcgMemberSoLcasRecvMst, vcgEntry=vcgEntry, vcgAssociatedEthernetPort=vcgAssociatedEthernetPort, vcgWtrTimer=vcgWtrTimer, vcgMemberSkLcasRecvCtrl=vcgMemberSkLcasRecvCtrl, f3EotdmCompliance=f3EotdmCompliance, CtrlState=CtrlState, vcgMemberRowStatus=vcgMemberRowStatus, vcgIfIndex=vcgIfIndex, vcgSecondaryState=vcgSecondaryState, vcgMemberSkRecvExpectSeq=vcgMemberSkRecvExpectSeq, HoldOffTime=HoldOffTime, vcgTable=vcgTable, vcgMemberIfIndex=vcgMemberIfIndex, f3EOTDMMIB=f3EOTDMMIB, MstState=MstState, PYSNMP_MODULE_ID=f3EOTDMMIB, LcasSkState=LcasSkState, vcgMemberEntry=vcgMemberEntry, vcgLcasEnabled=vcgLcasEnabled, f3EotdmCompliances=f3EotdmCompliances, f3EotdmObjectGroup=f3EotdmObjectGroup, vcgMemberSkLcasSendMst=vcgMemberSkLcasSendMst)
