#
# PySNMP MIB module CISCO-VLAN-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VLAN-GROUP-MIB
# Source digest sha256:6072951f99fef70d1d27c9f2d8419e14950685f3ee563a3c0768592bdfe8ff5e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Cisco2KVlanList, = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention")
ciscoVlanGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 709))
ciscoVlanGroupMIB.setRevisions(('2011-03-22 00:00', '2009-11-20 00:00',))
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setLastUpdated('2011-03-22 00:00')
if mibBuilder.loadTexts: ciscoVlanGroupMIB.setOrganization('Cisco Systems, Inc.')
ciscoVlanGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 0))
ciscoVlanGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 1))
ciscoVlanGroupMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2))
cvgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvgConfigTable.setStatus('current')
cvgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VLAN-GROUP-MIB", "cvgConfigGroupName"))
if mibBuilder.loadTexts: cvgConfigEntry.setStatus('current')
cvgConfigGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvgConfigGroupName.setStatus('current')
cvgConfigVlansFirst2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 2), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansFirst2K.setStatus('current')
cvgConfigVlansSecond2K = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 3), Cisco2KVlanList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigVlansSecond2K.setStatus('current')
cvgConfigStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 4), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigStorageType.setStatus('current')
cvgConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvgConfigRowStatus.setStatus('current')
cvgConfigTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvgConfigTableSize.setStatus('current')
ciscoVlanGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1))
ciscoVlanGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2))
ciscoVlanGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance = ciscoVlanGroupMIBCompliance.setStatus('deprecated')
ciscoVlanGroupMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "ciscoVlanGroupConfigGroup"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupMIBCompliance2 = ciscoVlanGroupMIBCompliance2.setStatus('current')
ciscoVlanGroupConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 1)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansFirst2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansSecond2K"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigRowStatus"), ("CISCO-VLAN-GROUP-MIB", "cvgConfigStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanGroupConfigGroup = ciscoVlanGroupConfigGroup.setStatus('current')
cvgConfigTableSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 2)).setObjects(("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvgConfigTableSizeGroup = cvgConfigTableSizeGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-GROUP-MIB", PYSNMP_MODULE_ID=ciscoVlanGroupMIB, ciscoVlanGroupConfigGroup=ciscoVlanGroupConfigGroup, ciscoVlanGroupMIB=ciscoVlanGroupMIB, ciscoVlanGroupMIBCompliance2=ciscoVlanGroupMIBCompliance2, ciscoVlanGroupMIBCompliance=ciscoVlanGroupMIBCompliance, ciscoVlanGroupMIBCompliances=ciscoVlanGroupMIBCompliances, ciscoVlanGroupMIBConform=ciscoVlanGroupMIBConform, ciscoVlanGroupMIBGroups=ciscoVlanGroupMIBGroups, ciscoVlanGroupMIBNotifs=ciscoVlanGroupMIBNotifs, ciscoVlanGroupMIBObjects=ciscoVlanGroupMIBObjects, cvgConfigEntry=cvgConfigEntry, cvgConfigGroupName=cvgConfigGroupName, cvgConfigRowStatus=cvgConfigRowStatus, cvgConfigStorageType=cvgConfigStorageType, cvgConfigTable=cvgConfigTable, cvgConfigTableSize=cvgConfigTableSize, cvgConfigTableSizeGroup=cvgConfigTableSizeGroup, cvgConfigVlansFirst2K=cvgConfigVlansFirst2K, cvgConfigVlansSecond2K=cvgConfigVlansSecond2K)
