#
# PySNMP MIB module PRVT-LMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-LMGR-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:48:04 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, TimeTicks, Integer32, NotificationType, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "Integer32", "NotificationType", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
prvtLmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4))
prvtLmgrMIB.setRevisions(('2006-06-11 00:00',))
if mibBuilder.loadTexts: prvtLmgrMIB.setLastUpdated('200606110000Z')
if mibBuilder.loadTexts: prvtLmgrMIB.setOrganization('BATM Advanced Communication')
class PrvtLmgrAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtLmgrOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtLmgrPartnerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

class PrvtLmgrIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PrvtLmgrControlModes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ordered", 1), ("independent", 2))

prvtLmgrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1))
prvtLmgrLsrEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2), )
if mibBuilder.loadTexts: prvtLmgrLsrEntityTable.setStatus('current')
prvtLmgrLsrEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrEntityEntry.setStatus('current')
prvtlmgrLsrEntityLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 1), PrvtLmgrIndex())
if mibBuilder.loadTexts: prvtlmgrLsrEntityLsrIndex.setStatus('current')
prvtLmgrLsrEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityRowStatus.setStatus('current')
prvtLmgrLsrEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 3), PrvtLmgrAdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityAdminStatus.setStatus('current')
prvtLmgrLsrEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 4), PrvtLmgrOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrEntityOperStatus.setStatus('current')
prvtLmgrLsrEntityLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityLsrId.setStatus('current')
prvtLmgrLsrEntityTranAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrType.setStatus('current')
prvtLmgrLsrEntityTranAddrLen = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrLen.setStatus('current')
prvtLmgrLsrEntityTranAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddr.setStatus('current')
prvtLmgrLsrLspXcTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3), )
if mibBuilder.loadTexts: prvtLmgrLsrLspXcTable.setStatus('current')
prvtLmgrLsrLspXcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspXcIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrLspXcEntry.setStatus('current')
prvtLmgrLsrLspXcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspXcIndex.setStatus('current')
prvtLmgrLsrLspInSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIndex.setStatus('current')
prvtLmgrLsrLspInSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIfIndex.setStatus('current')
prvtLmgrLsrLspInSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 5), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegLabel.setStatus('current')
prvtLmgrLsrLspOutSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 6), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIndex.setStatus('current')
prvtLmgrLsrLspOutSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIfIndex.setStatus('current')
prvtLmgrLsrLspOutSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegLabel.setStatus('current')
prvtLmgrLsrLspOutSegNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegNextHopAddr.setStatus('current')
mibBuilder.exportSymbols("PRVT-LMGR-MIB", prvtLmgrLsrLspOutSegNextHopAddr=prvtLmgrLsrLspOutSegNextHopAddr, prvtLmgrLsrEntityAdminStatus=prvtLmgrLsrEntityAdminStatus, prvtLmgrLsrLspXcTable=prvtLmgrLsrLspXcTable, prvtLmgrLsrEntityOperStatus=prvtLmgrLsrEntityOperStatus, prvtLmgrLsrLspOutSegLabel=prvtLmgrLsrLspOutSegLabel, prvtLmgrLsrLspInSegLabel=prvtLmgrLsrLspInSegLabel, PrvtLmgrControlModes=PrvtLmgrControlModes, PYSNMP_MODULE_ID=prvtLmgrMIB, prvtLmgrLsrLspOutSegIndex=prvtLmgrLsrLspOutSegIndex, prvtLmgrMIB=prvtLmgrMIB, PrvtLmgrAdminStatus=PrvtLmgrAdminStatus, prvtLmgrLsrLspOutSegIfIndex=prvtLmgrLsrLspOutSegIfIndex, prvtLmgrLsrEntityTranAddr=prvtLmgrLsrEntityTranAddr, prvtLmgrLsrLspXcIndex=prvtLmgrLsrLspXcIndex, prvtLmgrLsrEntityLsrId=prvtLmgrLsrEntityLsrId, PrvtLmgrIndex=PrvtLmgrIndex, PrvtLmgrOperStatus=PrvtLmgrOperStatus, prvtLmgrLsrEntityTable=prvtLmgrLsrEntityTable, prvtLmgrLsrLspXcEntry=prvtLmgrLsrLspXcEntry, prvtLmgrLsrEntityEntry=prvtLmgrLsrEntityEntry, prvtLmgrObjects=prvtLmgrObjects, PrvtLmgrPartnerStatus=PrvtLmgrPartnerStatus, prvtLmgrLsrEntityTranAddrLen=prvtLmgrLsrEntityTranAddrLen, prvtLmgrLsrEntityTranAddrType=prvtLmgrLsrEntityTranAddrType, prvtlmgrLsrEntityLsrIndex=prvtlmgrLsrEntityLsrIndex, prvtLmgrLsrLspInSegIndex=prvtLmgrLsrLspInSegIndex, prvtLmgrLsrLspInSegIfIndex=prvtLmgrLsrLspInSegIfIndex, prvtLmgrLsrEntityRowStatus=prvtLmgrLsrEntityRowStatus)
