#
# PySNMP MIB module ALCATEL-IND1-VIRTUAL-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-VIRTUAL-CHASSIS-MIB
# Source digest sha256:ed25bf75180dd0f0ddb1a2664633a07a23e18f019abaef932c8e28449674b905
# Produced by pysmi-2.3.0
#
softentIND1VirtualChassisManager, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1VirtualChassisManager")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
alcatelIND1VirtualChassisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1))
alcatelIND1VirtualChassisMIB.setRevisions(('2019-11-27 00:00', '2011-05-25 00:00',))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setLastUpdated('2019-11-27 00:00')
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIB.setOrganization('ALE USA Inc.')
alcatelIND1VirtualChassisMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBNotifications.setStatus('current')
alcatelIND1VirtualChassisMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBObjects.setStatus('current')
alcatelIND1VirtualChassisMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBConformance.setStatus('current')
alcatelIND1VirtualChassisMIBVCSP = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBVCSP.setStatus('current')
alcatelIND1VirtualChassisMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBGroups.setStatus('current')
alcatelIND1VirtualChassisMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1VirtualChassisMIBCompliances.setStatus('current')
class VirtualOperChassisId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualConfigChassisId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 8)

class VirtualChassisHelloInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class VirtualChassisControlVlan(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 4094)

class VirtualChassisCmmSlot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 65, 66))
    namedValues = NamedValues(("notPresent", 0), ("cmmSlot1", 65), ("cmmSlot2", 66))

class VirtualChassisNiSlot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 8)

class VirtualChassisVflId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VirtualChassisConsistency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("inconsistent", 0), ("consistent", 1), ("na", 2), ("disabled", 3))

class VirtualChassisRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unassigned", 0), ("master", 1), ("slave", 2), ("inconsistent", 3), ("startuperror", 4))

class VirtualChassisStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("init", 0), ("running", 1), ("invalidChassisId", 2), ("helloDown", 3), ("duplicateChassisId", 4), ("mismatchImage", 5), ("mismatchChassisType", 6), ("mismatchHelloInterval", 7), ("mismatchControlVlan", 8), ("mismatchGroup", 9), ("mismatchLicenseConfig", 10), ("invalidLicense", 11), ("splitTopology", 12), ("commandShutdown", 13), ("failureShutdown", 14), ("mismatchTableMode", 15), ("unavailable", 16), ("rebootNotJoined", 17), ("rebootAdded", 18), ("runtimeLeft", 19), ("runtimeJoined", 20))

class VirtualChassisGroup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualChassisPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class VirtualChassisSlotResetStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("supported", 0), ("split", 1))

class VirtualChassisType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("invalid", 0), ("rushmore", 1), ("tor", 2), ("shasta", 3), ("medora", 4), ("everest", 5), ("nandi", 6), ("vindhya", 7), ("yukon", 8), ("shastaN", 9), ("aravalli", 10), ("whitney", 11), ("kailash", 12), ("dronagiri", 13))

class VirtualChassisVflSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unassigned", 0), ("unknown", 1), ("mismatch", 2), ("tenGB", 3), ("fortyGB", 4), ("twentyOneGB", 5), ("fiftyGB", 6), ("oneHundredGB", 7), ("twentyGB", 8), ("oneGB", 9), ("twentyFiveGB", 10), ("twoHundredGB", 11))

class VirtualChassisVflMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("auto", 2))

class VirtualChassisTopologyChassisIDs(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("chassis1", 0), ("chassis2", 1), ("chassis3", 2), ("chassis4", 3), ("chassis5", 4), ("chassis6", 5), ("chassis7", 6), ("chassis8", 7))

virtualChassisLocalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1))
virtualChassisLocalInfoChasId = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 1, 1), VirtualOperChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLocalInfoChasId.setStatus('current')
virtualChassisGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisGlobalTable.setStatus('current')
virtualChassisGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"))
if mibBuilder.loadTexts: virtualChassisGlobalEntry.setStatus('current')
virtualChassisOperChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 1), VirtualOperChassisId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: virtualChassisOperChasId.setStatus('current')
virtualChassisConfigChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 2), VirtualConfigChassisId().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigChassisId.setStatus('current')
virtualChassisRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 3), VirtualChassisRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisRole.setStatus('current')
virtualChassisPreviousRole = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 4), VirtualChassisRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisPreviousRole.setStatus('current')
virtualChassisStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 5), VirtualChassisStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisStatus.setStatus('current')
virtualChassisOperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 6), VirtualChassisPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperPriority.setStatus('current')
virtualChassisConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 7), VirtualChassisPriority().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigPriority.setStatus('current')
virtualChassisGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 8), VirtualChassisGroup().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisGroup.setStatus('current')
virtualChassisMac = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisMac.setStatus('current')
virtualChassisUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisUpTime.setStatus('current')
virtualChassisDesigNI = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 11), VirtualChassisNiSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisDesigNI.setStatus('current')
virtualChassisPriCmm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 12), VirtualChassisCmmSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisPriCmm.setStatus('current')
virtualChassisSecCmm = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 13), VirtualChassisCmmSlot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisSecCmm.setStatus('current')
virtualChassisOperHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 14), VirtualChassisHelloInterval().clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisOperHelloInterval.setStatus('current')
virtualChassisOperControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 15), VirtualChassisControlVlan()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperControlVlan.setStatus('current')
virtualChassisConfigHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 16), VirtualChassisHelloInterval().clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigHelloInterval.setStatus('deprecated')
virtualChassisConfigControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 17), VirtualChassisControlVlan().clone(4094)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisConfigControlVlan.setStatus('current')
virtualChassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 18), VirtualChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisType.setStatus('current')
virtualChassisLicense = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 19), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLicense.setStatus('current')
virtualChassisOperChasIdConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 20), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperChasIdConsis.setStatus('current')
virtualChassisConfigChasIdConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 21), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigChasIdConsis.setStatus('current')
virtualChassisOperControlVlanConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 22), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperControlVlanConsis.setStatus('current')
virtualChassisConfigControlVlanConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 23), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigControlVlanConsis.setStatus('current')
virtualChassisOperHelloIntervalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 24), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisOperHelloIntervalConsis.setStatus('current')
virtualChassisConfigHelloIntervalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 25), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisConfigHelloIntervalConsis.setStatus('deprecated')
virtualChassisChassisTypeConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 26), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisChassisTypeConsis.setStatus('current')
virtualChassisGroupConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 27), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisGroupConsis.setStatus('current')
virtualChassisLicenseConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 28), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisLicenseConsis.setStatus('current')
virtualChassisGlobalConsis = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 29), VirtualChassisConsistency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisGlobalConsis.setStatus('current')
virtualChassisNumOfNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNumOfNeighbor.setStatus('current')
virtualChassisNumOfDirectNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNumOfDirectNeighbor.setStatus('current')
virtualChassisVflMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 32), VirtualChassisVflMode().clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: virtualChassisVflMode.setStatus('current')
virtualChassisTopologyMissingChassisIDs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 2, 1, 33), VirtualChassisTopologyChassisIDs()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisTopologyMissingChassisIDs.setStatus('current')
virtualChassisNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisNeighborTable.setStatus('current')
virtualChassisNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborChasId"))
if mibBuilder.loadTexts: virtualChassisNeighborEntry.setStatus('current')
virtualChassisNeighborChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 1), VirtualOperChassisId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisNeighborChasId.setStatus('current')
virtualChassisNeighborShortestPath = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNeighborShortestPath.setStatus('current')
virtualChassisNeighborIsDirect = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisNeighborIsDirect.setStatus('current')
virtualChassisChassisResetListTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisChassisResetListTable.setStatus('current')
virtualChassisChassisResetListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"))
if mibBuilder.loadTexts: virtualChassisChassisResetListEntry.setStatus('current')
virtualChassisChassisResetList = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisChassisResetList.setStatus('current')
virtualChassisSlotResetStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisSlotResetStatusTable.setStatus('current')
virtualChassisSlotResetStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotNum"))
if mibBuilder.loadTexts: virtualChassisSlotResetStatusEntry.setStatus('current')
virtualChassisSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 1), VirtualChassisNiSlot()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisSlotNum.setStatus('current')
virtualChassisSlotResetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 5, 1, 2), VirtualChassisSlotResetStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisSlotResetStatus.setStatus('current')
virtualChassisVflTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisVflTable.setStatus('current')
virtualChassisVflEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"))
if mibBuilder.loadTexts: virtualChassisVflEntry.setStatus('current')
virtualChassisVflId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 1), VirtualChassisVflId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: virtualChassisVflId.setStatus('current')
virtualChassisVflDefaultVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflDefaultVlan.setStatus('deprecated')
virtualChassisVflOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflOperStatus.setStatus('current')
virtualChassisVflPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflPrimaryPort.setStatus('current')
virtualChassisVflActivePortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflActivePortNum.setStatus('current')
virtualChassisVflConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflConfigPortNum.setStatus('current')
virtualChassisVflRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflRowStatus.setStatus('current')
virtualChassisVflDirectNeighborChasId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 8), VirtualOperChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflDirectNeighborChasId.setStatus('current')
virtualChassisVflSpeedType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 6, 1, 9), VirtualChassisVflSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflSpeedType.setStatus('current')
virtualChassisVflMemberPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisVflMemberPortTable.setStatus('current')
virtualChassisVflMemberPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), (0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortEntry.setStatus('current')
virtualChassisVflMemberPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 1), InterfaceIndex()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: virtualChassisVflMemberPortIfindex.setStatus('current')
virtualChassisVflMemberPortIsPrimay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflMemberPortIsPrimay.setStatus('current')
virtualChassisVflMemberPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisVflMemberPortOperStatus.setStatus('current')
virtualChassisVflMemberPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisVflMemberPortRowStatus.setStatus('current')
virtualChassisTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8))
virtualChassisDiagnostic = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("duplexMode", 1), ("speed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisDiagnostic.setStatus('current')
virtualChassisUpgradeCompleteStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisUpgradeCompleteStatus.setStatus('current')
virtualChassisAutoVflPortTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisAutoVflPortTable.setStatus('current')
virtualChassisAutoVflPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortIfindex"))
if mibBuilder.loadTexts: virtualChassisAutoVflPortEntry.setStatus('current')
virtualChassisAutoVflPortIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: virtualChassisAutoVflPortIfindex.setStatus('current')
virtualChassisAutoVflIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisAutoVflIfindex.setStatus('current')
virtualChassisAutoVflPortMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unassigned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: virtualChassisAutoVflPortMemberStatus.setStatus('current')
virtualChassisAutoVflPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 1, 9, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: virtualChassisAutoVflPortRowStatus.setStatus('current')
virtualChassisStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"))
if mibBuilder.loadTexts: virtualChassisStatusChange.setStatus('current')
virtualChassisRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 2)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"))
if mibBuilder.loadTexts: virtualChassisRoleChange.setStatus('current')
virtualChassisVflStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 3)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"))
if mibBuilder.loadTexts: virtualChassisVflStatusChange.setStatus('current')
virtualChassisVflMemberPortStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 4)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortStatusChange.setStatus('deprecated')
virtualChassisVflMemberPortJoinFailure = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 5)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"))
if mibBuilder.loadTexts: virtualChassisVflMemberPortJoinFailure.setStatus('current')
virtualChassisUpgradeComplete = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 6)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus"))
if mibBuilder.loadTexts: virtualChassisUpgradeComplete.setStatus('current')
virtualChassisVflSpeedTypeChange = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 0, 7)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
if mibBuilder.loadTexts: virtualChassisVflSpeedTypeChange.setStatus('current')
alcatelIND1VirtualChassisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLocalInfoGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGlobalGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisResetListGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotRestStatusGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1VirtualChassisMIBCompliance = alcatelIND1VirtualChassisMIBCompliance.setStatus('current')
virtualChassisLocalInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLocalInfoChasId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisLocalInfoGroup = virtualChassisLocalInfoGroup.setStatus('current')
virtualChassisGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChassisId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRole"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPreviousRole"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperPriority"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigPriority"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroup"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisMac"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpTime"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDesigNI"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisPriCmm"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSecCmm"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloInterval"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloInterval"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisType"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicense"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperChasIdConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigChasIdConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperControlVlanConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigControlVlanConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisOperHelloIntervalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisConfigHelloIntervalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisTypeConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGroupConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisLicenseConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisGlobalConsis"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfNeighbor"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNumOfDirectNeighbor"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMode"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisTopologyMissingChassisIDs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisGlobalGroup = virtualChassisGlobalGroup.setStatus('current')
virtualChassisNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborShortestPath"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisNeighborIsDirect"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisNeighborGroup = virtualChassisNeighborGroup.setStatus('current')
virtualChassisChassisResetListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisChassisResetList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisChassisResetListGroup = virtualChassisChassisResetListGroup.setStatus('current')
virtualChassisSlotRestStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisSlotResetStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisSlotRestStatusGroup = virtualChassisSlotRestStatusGroup.setStatus('current')
virtualChassisVflGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDefaultVlan"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflOperStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflPrimaryPort"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflActivePortNum"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflConfigPortNum"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflRowStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflDirectNeighborChasId"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisVflGroup = virtualChassisVflGroup.setStatus('current')
virtualChassisVflMemberPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortIsPrimay"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortOperStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisVflMemberPortGroup = virtualChassisVflMemberPortGroup.setStatus('current')
virtualChassisTrapInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 8)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisDiagnostic"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeCompleteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisTrapInfoGroup = virtualChassisTrapInfoGroup.setStatus('current')
virtualChassisTrapOBJGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 9)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisRoleChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortStatusChange"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflMemberPortJoinFailure"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisUpgradeComplete"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisVflSpeedTypeChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisTrapOBJGroup = virtualChassisTrapOBJGroup.setStatus('current')
virtualChassisAutoVflPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 2, 1, 10)).setObjects(("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflIfindex"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortMemberStatus"), ("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", "virtualChassisAutoVflPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    virtualChassisAutoVflPortGroup = virtualChassisAutoVflPortGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUAL-CHASSIS-MIB", PYSNMP_MODULE_ID=alcatelIND1VirtualChassisMIB, VirtualChassisCmmSlot=VirtualChassisCmmSlot, VirtualChassisConsistency=VirtualChassisConsistency, VirtualChassisControlVlan=VirtualChassisControlVlan, VirtualChassisGroup=VirtualChassisGroup, VirtualChassisHelloInterval=VirtualChassisHelloInterval, VirtualChassisNiSlot=VirtualChassisNiSlot, VirtualChassisPriority=VirtualChassisPriority, VirtualChassisRole=VirtualChassisRole, VirtualChassisSlotResetStatus=VirtualChassisSlotResetStatus, VirtualChassisStatus=VirtualChassisStatus, VirtualChassisTopologyChassisIDs=VirtualChassisTopologyChassisIDs, VirtualChassisType=VirtualChassisType, VirtualChassisVflId=VirtualChassisVflId, VirtualChassisVflMode=VirtualChassisVflMode, VirtualChassisVflSpeedType=VirtualChassisVflSpeedType, VirtualConfigChassisId=VirtualConfigChassisId, VirtualOperChassisId=VirtualOperChassisId, alcatelIND1VirtualChassisMIB=alcatelIND1VirtualChassisMIB, alcatelIND1VirtualChassisMIBCompliance=alcatelIND1VirtualChassisMIBCompliance, alcatelIND1VirtualChassisMIBCompliances=alcatelIND1VirtualChassisMIBCompliances, alcatelIND1VirtualChassisMIBConformance=alcatelIND1VirtualChassisMIBConformance, alcatelIND1VirtualChassisMIBGroups=alcatelIND1VirtualChassisMIBGroups, alcatelIND1VirtualChassisMIBNotifications=alcatelIND1VirtualChassisMIBNotifications, alcatelIND1VirtualChassisMIBObjects=alcatelIND1VirtualChassisMIBObjects, alcatelIND1VirtualChassisMIBVCSP=alcatelIND1VirtualChassisMIBVCSP, virtualChassisAutoVflIfindex=virtualChassisAutoVflIfindex, virtualChassisAutoVflPortEntry=virtualChassisAutoVflPortEntry, virtualChassisAutoVflPortGroup=virtualChassisAutoVflPortGroup, virtualChassisAutoVflPortIfindex=virtualChassisAutoVflPortIfindex, virtualChassisAutoVflPortMemberStatus=virtualChassisAutoVflPortMemberStatus, virtualChassisAutoVflPortRowStatus=virtualChassisAutoVflPortRowStatus, virtualChassisAutoVflPortTable=virtualChassisAutoVflPortTable, virtualChassisChassisResetList=virtualChassisChassisResetList, virtualChassisChassisResetListEntry=virtualChassisChassisResetListEntry, virtualChassisChassisResetListGroup=virtualChassisChassisResetListGroup, virtualChassisChassisResetListTable=virtualChassisChassisResetListTable, virtualChassisChassisTypeConsis=virtualChassisChassisTypeConsis, virtualChassisConfigChasIdConsis=virtualChassisConfigChasIdConsis, virtualChassisConfigChassisId=virtualChassisConfigChassisId, virtualChassisConfigControlVlan=virtualChassisConfigControlVlan, virtualChassisConfigControlVlanConsis=virtualChassisConfigControlVlanConsis, virtualChassisConfigHelloInterval=virtualChassisConfigHelloInterval, virtualChassisConfigHelloIntervalConsis=virtualChassisConfigHelloIntervalConsis, virtualChassisConfigPriority=virtualChassisConfigPriority, virtualChassisDesigNI=virtualChassisDesigNI, virtualChassisDiagnostic=virtualChassisDiagnostic, virtualChassisGlobalConsis=virtualChassisGlobalConsis, virtualChassisGlobalEntry=virtualChassisGlobalEntry, virtualChassisGlobalGroup=virtualChassisGlobalGroup, virtualChassisGlobalTable=virtualChassisGlobalTable, virtualChassisGroup=virtualChassisGroup, virtualChassisGroupConsis=virtualChassisGroupConsis, virtualChassisLicense=virtualChassisLicense, virtualChassisLicenseConsis=virtualChassisLicenseConsis, virtualChassisLocalInfo=virtualChassisLocalInfo, virtualChassisLocalInfoChasId=virtualChassisLocalInfoChasId, virtualChassisLocalInfoGroup=virtualChassisLocalInfoGroup, virtualChassisMac=virtualChassisMac, virtualChassisNeighborChasId=virtualChassisNeighborChasId, virtualChassisNeighborEntry=virtualChassisNeighborEntry, virtualChassisNeighborGroup=virtualChassisNeighborGroup, virtualChassisNeighborIsDirect=virtualChassisNeighborIsDirect, virtualChassisNeighborShortestPath=virtualChassisNeighborShortestPath, virtualChassisNeighborTable=virtualChassisNeighborTable, virtualChassisNumOfDirectNeighbor=virtualChassisNumOfDirectNeighbor, virtualChassisNumOfNeighbor=virtualChassisNumOfNeighbor, virtualChassisOperChasId=virtualChassisOperChasId, virtualChassisOperChasIdConsis=virtualChassisOperChasIdConsis, virtualChassisOperControlVlan=virtualChassisOperControlVlan, virtualChassisOperControlVlanConsis=virtualChassisOperControlVlanConsis, virtualChassisOperHelloInterval=virtualChassisOperHelloInterval, virtualChassisOperHelloIntervalConsis=virtualChassisOperHelloIntervalConsis, virtualChassisOperPriority=virtualChassisOperPriority, virtualChassisPreviousRole=virtualChassisPreviousRole, virtualChassisPriCmm=virtualChassisPriCmm, virtualChassisRole=virtualChassisRole, virtualChassisRoleChange=virtualChassisRoleChange, virtualChassisSecCmm=virtualChassisSecCmm, virtualChassisSlotNum=virtualChassisSlotNum, virtualChassisSlotResetStatus=virtualChassisSlotResetStatus, virtualChassisSlotResetStatusEntry=virtualChassisSlotResetStatusEntry, virtualChassisSlotResetStatusTable=virtualChassisSlotResetStatusTable, virtualChassisSlotRestStatusGroup=virtualChassisSlotRestStatusGroup, virtualChassisStatus=virtualChassisStatus, virtualChassisStatusChange=virtualChassisStatusChange, virtualChassisTopologyMissingChassisIDs=virtualChassisTopologyMissingChassisIDs, virtualChassisTrapInfo=virtualChassisTrapInfo, virtualChassisTrapInfoGroup=virtualChassisTrapInfoGroup, virtualChassisTrapOBJGroup=virtualChassisTrapOBJGroup, virtualChassisType=virtualChassisType, virtualChassisUpTime=virtualChassisUpTime, virtualChassisUpgradeComplete=virtualChassisUpgradeComplete, virtualChassisUpgradeCompleteStatus=virtualChassisUpgradeCompleteStatus, virtualChassisVflActivePortNum=virtualChassisVflActivePortNum, virtualChassisVflConfigPortNum=virtualChassisVflConfigPortNum, virtualChassisVflDefaultVlan=virtualChassisVflDefaultVlan, virtualChassisVflDirectNeighborChasId=virtualChassisVflDirectNeighborChasId, virtualChassisVflEntry=virtualChassisVflEntry, virtualChassisVflGroup=virtualChassisVflGroup, virtualChassisVflId=virtualChassisVflId, virtualChassisVflMemberPortEntry=virtualChassisVflMemberPortEntry, virtualChassisVflMemberPortGroup=virtualChassisVflMemberPortGroup, virtualChassisVflMemberPortIfindex=virtualChassisVflMemberPortIfindex, virtualChassisVflMemberPortIsPrimay=virtualChassisVflMemberPortIsPrimay, virtualChassisVflMemberPortJoinFailure=virtualChassisVflMemberPortJoinFailure, virtualChassisVflMemberPortOperStatus=virtualChassisVflMemberPortOperStatus, virtualChassisVflMemberPortRowStatus=virtualChassisVflMemberPortRowStatus, virtualChassisVflMemberPortStatusChange=virtualChassisVflMemberPortStatusChange, virtualChassisVflMemberPortTable=virtualChassisVflMemberPortTable, virtualChassisVflMode=virtualChassisVflMode, virtualChassisVflOperStatus=virtualChassisVflOperStatus, virtualChassisVflPrimaryPort=virtualChassisVflPrimaryPort, virtualChassisVflRowStatus=virtualChassisVflRowStatus, virtualChassisVflSpeedType=virtualChassisVflSpeedType, virtualChassisVflSpeedTypeChange=virtualChassisVflSpeedTypeChange, virtualChassisVflStatusChange=virtualChassisVflStatusChange, virtualChassisVflTable=virtualChassisVflTable)
