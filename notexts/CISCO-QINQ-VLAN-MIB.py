#
# PySNMP MIB module CISCO-QINQ-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-QINQ-VLAN-MIB
# Source digest sha256:666ad122a4e4f2a34d8637bd5ddd4a5e759280a09894d8b55451c0c68cc0aae0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoQinqVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 445))
ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setLastUpdated('2004-11-29 00:00')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setOrganization('Cisco Systems, Inc.')
ciscoQinqVlanMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 0))
ciscoQinqVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1))
ciscoQinqVlanMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2))
cqvTermination = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1))
cqvTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2))
class CqvVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC-2674, Bridge MIB Extensions, August 1999, Q-BRIDGE-MIB, E. Bell.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class CqvEncapsulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isl", 1), ("dot1Q", 2))

cqvTerminationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationTable.setStatus('current')
cqvTerminationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"))
if mibBuilder.loadTexts: cqvTerminationEntry.setStatus('current')
cqvTerminationPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setStatus('current')
cqvTerminationCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2), VlanId()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setStatus('current')
cqvTerminationPeEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3), CqvEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationPeEncap.setStatus('current')
cqvTerminationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationRowStatus.setStatus('current')
cqvTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationTable.setStatus('current')
cqvTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"))
if mibBuilder.loadTexts: cqvTranslationEntry.setStatus('current')
cqvTranslationInternalPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1), CqvVlanIdOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setStatus('current')
cqvTranslationInternalCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2), CqvVlanIdOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setStatus('current')
cqvTranslationTrunkPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setStatus('current')
cqvTranslationTrunkCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setStatus('current')
cqvTranslationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doubleToSingle", 1), ("doubleToDouble", 2), ("doubleToDoubleOutOfRange", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationType.setStatus('current')
cqvTranslationCosPBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyFromOuterTag", 1), ("copyFromInnerTag", 2))).clone('copyFromOuterTag')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationCosPBits.setStatus('current')
cqvTranslationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationRowStatus.setStatus('current')
ciscoQinqVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1))
ciscoQinqVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2))
ciscoQinQVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTerminationGroup"), ("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinQVlanMIBCompliance = ciscoQinQVlanMIBCompliance.setStatus('current')
ciscoQinqVlanTerminationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"), ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTerminationGroup = ciscoQinqVlanTerminationGroup.setStatus('current')
ciscoQinqVlanTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTranslationGroup = ciscoQinqVlanTranslationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QINQ-VLAN-MIB", CqvEncapsulationType=CqvEncapsulationType, CqvVlanIdOrZero=CqvVlanIdOrZero, PYSNMP_MODULE_ID=ciscoQinqVlanMIB, ciscoQinQVlanMIBCompliance=ciscoQinQVlanMIBCompliance, ciscoQinqVlanMIB=ciscoQinqVlanMIB, ciscoQinqVlanMIBCompliances=ciscoQinqVlanMIBCompliances, ciscoQinqVlanMIBConform=ciscoQinqVlanMIBConform, ciscoQinqVlanMIBGroups=ciscoQinqVlanMIBGroups, ciscoQinqVlanMIBNotifs=ciscoQinqVlanMIBNotifs, ciscoQinqVlanMIBObjects=ciscoQinqVlanMIBObjects, ciscoQinqVlanTerminationGroup=ciscoQinqVlanTerminationGroup, ciscoQinqVlanTranslationGroup=ciscoQinqVlanTranslationGroup, cqvTermination=cqvTermination, cqvTerminationCeVlanId=cqvTerminationCeVlanId, cqvTerminationEntry=cqvTerminationEntry, cqvTerminationPeEncap=cqvTerminationPeEncap, cqvTerminationPeVlanId=cqvTerminationPeVlanId, cqvTerminationRowStatus=cqvTerminationRowStatus, cqvTerminationTable=cqvTerminationTable, cqvTranslation=cqvTranslation, cqvTranslationCosPBits=cqvTranslationCosPBits, cqvTranslationEntry=cqvTranslationEntry, cqvTranslationInternalCeVlanId=cqvTranslationInternalCeVlanId, cqvTranslationInternalPeVlanId=cqvTranslationInternalPeVlanId, cqvTranslationRowStatus=cqvTranslationRowStatus, cqvTranslationTable=cqvTranslationTable, cqvTranslationTrunkCeVlanId=cqvTranslationTrunkCeVlanId, cqvTranslationTrunkPeVlanId=cqvTranslationTrunkPeVlanId, cqvTranslationType=cqvTranslationType)
