#
# PySNMP MIB module CISCO-CAT6k-NAT-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CAT6k-NAT-STAT-MIB
# Source digest sha256:013cba2fd598f546bef4c689317bbd2f7ad2a16ed42ec62d0b63821f61720700
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCat6kNatStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 861))
ciscoCat6kNatStatMIB.setRevisions(('2019-06-11 00:00',))
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setLastUpdated('2019-06-11 00:00')
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setOrganization('Cisco Systems, Inc.')
ciscoCat6kNatStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 1))
ciscoCat6kNatStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2))
ciscoCat6kNatStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2))
ciscoCat6kNatStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1))
ciscoCat6kNatStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2))
ciscoCat6kNatStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2, 1)).setObjects(("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatType"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatNetFlowType"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatFlowRecord"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatDynamicEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStaticEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatOtherEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatTotalEntryCount"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatResourceUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCat6kNatStatGroup = ciscoCat6kNatStatGroup.setStatus('current')
ciscoCat6kNatStatMIBComplianceVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1, 1)).setObjects(("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCat6kNatStatMIBComplianceVer1 = ciscoCat6kNatStatMIBComplianceVer1.setStatus('current')
class NatType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("static", 1), ("dynamic", 2), ("mixed", 3), ("other", 4))

class NetFlowType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("layer3", 1), ("mixed", 2))

class NatBool(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

ciscoCat6kNatType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 1), NatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatType.setStatus('current')
ciscoCat6kNatNetFlowType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 2), NetFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatNetFlowType.setStatus('current')
ciscoCat6kNatFlowRecord = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 3), NatBool()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatFlowRecord.setStatus('current')
ciscoCat6kNatDynamicEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatDynamicEntryUtilization.setStatus('current')
ciscoCat6kNatStaticEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatStaticEntryUtilization.setStatus('current')
ciscoCat6kNatOtherEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatOtherEntryUtilization.setStatus('current')
ciscoCat6kNatTotalEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatTotalEntryCount.setStatus('current')
ciscoCat6kNatResourceUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatResourceUtilization.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAT6k-NAT-STAT-MIB", NatBool=NatBool, NatType=NatType, NetFlowType=NetFlowType, PYSNMP_MODULE_ID=ciscoCat6kNatStatMIB, ciscoCat6kNatDynamicEntryUtilization=ciscoCat6kNatDynamicEntryUtilization, ciscoCat6kNatFlowRecord=ciscoCat6kNatFlowRecord, ciscoCat6kNatNetFlowType=ciscoCat6kNatNetFlowType, ciscoCat6kNatOtherEntryUtilization=ciscoCat6kNatOtherEntryUtilization, ciscoCat6kNatResourceUtilization=ciscoCat6kNatResourceUtilization, ciscoCat6kNatStatGroup=ciscoCat6kNatStatGroup, ciscoCat6kNatStatMIB=ciscoCat6kNatStatMIB, ciscoCat6kNatStatMIBComplianceVer1=ciscoCat6kNatStatMIBComplianceVer1, ciscoCat6kNatStatMIBCompliances=ciscoCat6kNatStatMIBCompliances, ciscoCat6kNatStatMIBConformance=ciscoCat6kNatStatMIBConformance, ciscoCat6kNatStatMIBGroups=ciscoCat6kNatStatMIBGroups, ciscoCat6kNatStatMIBObjects=ciscoCat6kNatStatMIBObjects, ciscoCat6kNatStaticEntryUtilization=ciscoCat6kNatStaticEntryUtilization, ciscoCat6kNatStatus=ciscoCat6kNatStatus, ciscoCat6kNatTotalEntryCount=ciscoCat6kNatTotalEntryCount, ciscoCat6kNatType=ciscoCat6kNatType)
