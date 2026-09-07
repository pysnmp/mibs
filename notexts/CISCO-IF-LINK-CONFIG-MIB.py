#
# PySNMP MIB module CISCO-IF-LINK-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-LINK-CONFIG-MIB
# Source digest sha256:b8504ddc340ac8f1a4e26cc1f6f9feb24622c6725dfedf536b84c5b53eb8a03e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoLocationSpecifier, = mibBuilder.importSymbols("CISCO-TC", "CiscoLocationSpecifier")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoIfLinkConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 175))
ciscoIfLinkConfigMIB.setRevisions(('2001-10-05 00:00', '2000-09-14 00:00',))
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setLastUpdated('2001-10-05 00:00')
if mibBuilder.loadTexts: ciscoIfLinkConfigMIB.setOrganization('Cisco Systems, Inc.')
cilConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1))
cilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1))
cilConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cilConfTable.setStatus('current')
cilConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"))
if mibBuilder.loadTexts: cilConfEntry.setStatus('current')
cilSourceInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cilSourceInterface.setStatus('current')
cilTargetModuleInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2), CiscoLocationSpecifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleInterface.setStatus('current')
cilRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilRowStatus.setStatus('current')
cilTargetModuleFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("dsx1D4", 2), ("dsx1ESF", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cilTargetModuleFramingType.setStatus('current')
cilConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3))
cilConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1))
cilConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2))
cilConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBCompliance = cilConfigMIBCompliance.setStatus('deprecated')
cilConfigMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilConfMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfigMIBComplianceRev1 = cilConfigMIBComplianceRev1.setStatus('current')
cilConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroup = cilConfMIBGroup.setStatus('deprecated')
cilConfMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)).setObjects(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"), ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"), ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cilConfMIBGroupRev1 = cilConfMIBGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-LINK-CONFIG-MIB", PYSNMP_MODULE_ID=ciscoIfLinkConfigMIB, cilConfEntry=cilConfEntry, cilConfMIBGroup=cilConfMIBGroup, cilConfMIBGroupRev1=cilConfMIBGroupRev1, cilConfTable=cilConfTable, cilConfig=cilConfig, cilConfigMIBCompliance=cilConfigMIBCompliance, cilConfigMIBComplianceRev1=cilConfigMIBComplianceRev1, cilConfigMIBCompliances=cilConfigMIBCompliances, cilConfigMIBConformance=cilConfigMIBConformance, cilConfigMIBGroups=cilConfigMIBGroups, cilConfigMIBObjects=cilConfigMIBObjects, cilRowStatus=cilRowStatus, cilSourceInterface=cilSourceInterface, cilTargetModuleFramingType=cilTargetModuleFramingType, cilTargetModuleInterface=cilTargetModuleInterface, ciscoIfLinkConfigMIB=ciscoIfLinkConfigMIB)
