#
# PySNMP MIB module CTRON-RATE-POLICING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-RATE-POLICING-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 17:57:30 2022
# On host fv-az121-846 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, Unsigned32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctRatePolicing = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7))
ctRatePolicing.setRevisions(('2003-04-10 15:18', '2003-03-11 15:53', '2000-11-28 15:51', '1999-06-21 00:00',))
if mibBuilder.loadTexts: ctRatePolicing.setLastUpdated('200304101518Z')
if mibBuilder.loadTexts: ctRatePolicing.setOrganization('Enterasys Networks, Inc')
ctRatePolicingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1))
class CtPriList(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CtRatePolActionList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dropPacket", 1), ("flowCtrlPacketAndDrop", 2), ("dropPacketOrFlowCtrlAndDrop", 3))

class CtRatePolDirectionList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("inbound", 1), ("outbound", 2), ("inboundAndOutbound", 3))

ctRatePolicingAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingAdminStatus.setStatus('current')
ctRatePolicingConfigLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingConfigLastChange.setStatus('current')
ctRatePolicingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3), )
if mibBuilder.loadTexts: ctRatePolicingConfigTable.setStatus('current')
ctRatePolicingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CTRON-RATE-POLICING-MIB", "ctRatePolicingResourceIndex"))
if mibBuilder.loadTexts: ctRatePolicingConfigEntry.setStatus('current')
ctRatePolicingResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ctRatePolicingResourceIndex.setStatus('current')
ctRatePolicingActionsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 2), CtRatePolActionList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingActionsAllowed.setStatus('current')
ctRatePolicingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 3), CtRatePolActionList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingAction.setStatus('current')
ctRatePolicingThreshHoldMin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingThreshHoldMin.setStatus('current')
ctRatePolicingThreshHold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kilobytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingThreshHold.setStatus('current')
ctRatePolicingPriorityList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 6), CtPriList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingPriorityList.setStatus('current')
ctRatePolicingRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingRuleStatus.setStatus('current')
ctRatePolicingActionsTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingActionsTaken.setStatus('current')
ctRatePolicingDirectionsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 9), CtRatePolDirectionList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingDirectionsAllowed.setStatus('current')
ctRatePolicingDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 10), CtRatePolDirectionList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingDirection.setStatus('current')
ctRatePolicingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2))
ctRatePolicingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1))
ctRatePolicingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2))
ctRatePolicingConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1, 1)).setObjects(("CTRON-RATE-POLICING-MIB", "ctRatePolicingAdminStatus"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingConfigLastChange"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsAllowed"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingAction"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingThreshHold"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingPriorityList"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingRuleStatus"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsTaken"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirectionsAllowed"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctRatePolicingConfigGroup = ctRatePolicingConfigGroup.setStatus('current')
ctRatePolicingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2, 1)).setObjects(("CTRON-RATE-POLICING-MIB", "ctRatePolicingConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctRatePolicingCompliance = ctRatePolicingCompliance.setStatus('current')
mibBuilder.exportSymbols("CTRON-RATE-POLICING-MIB", CtPriList=CtPriList, ctRatePolicingConfigGroup=ctRatePolicingConfigGroup, ctRatePolicingRuleStatus=ctRatePolicingRuleStatus, ctRatePolicingThreshHoldMin=ctRatePolicingThreshHoldMin, ctRatePolicingPriorityList=ctRatePolicingPriorityList, ctRatePolicingDirectionsAllowed=ctRatePolicingDirectionsAllowed, ctRatePolicingAction=ctRatePolicingAction, ctRatePolicingCompliance=ctRatePolicingCompliance, ctRatePolicingResourceIndex=ctRatePolicingResourceIndex, ctRatePolicingDirection=ctRatePolicingDirection, ctRatePolicingConformance=ctRatePolicingConformance, ctRatePolicingConfigLastChange=ctRatePolicingConfigLastChange, ctRatePolicingObjects=ctRatePolicingObjects, ctRatePolicingThreshHold=ctRatePolicingThreshHold, PYSNMP_MODULE_ID=ctRatePolicing, ctRatePolicingActionsTaken=ctRatePolicingActionsTaken, ctRatePolicingConfigTable=ctRatePolicingConfigTable, CtRatePolActionList=CtRatePolActionList, ctRatePolicingAdminStatus=ctRatePolicingAdminStatus, ctRatePolicingGroups=ctRatePolicingGroups, ctRatePolicingConfigEntry=ctRatePolicingConfigEntry, CtRatePolDirectionList=CtRatePolDirectionList, ctRatePolicingActionsAllowed=ctRatePolicingActionsAllowed, ctRatePolicingCompliances=ctRatePolicingCompliances, ctRatePolicing=ctRatePolicing)
