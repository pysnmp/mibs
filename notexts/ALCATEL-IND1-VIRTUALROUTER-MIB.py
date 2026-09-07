#
# PySNMP MIB module ALCATEL-IND1-VIRTUALROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-VIRTUALROUTER-MIB
# Source digest sha256:024773eb8e5006b5d00f87f38e2445f52ea79aa5cb2f3e5d656d993629d72765
# Produced by pysmi-2.3.0
#
routingIND1Vrf, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Vrf")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
alcatelIND1VirtualRouterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1))
alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setLastUpdated('2007-04-03 00:00')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setOrganization('Alcatel-Lucent')
alcatelIND1VirtualRouterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1))
alaVirtualRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1))
alaVirtualRouterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setStatus('current')
alaVirtualRouterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"))
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setStatus('current')
alaVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaVirtualRouterName.setStatus('current')
alaVirtualRouterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setStatus('current')
alaVirtualRouterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setStatus('current')
alcatelIND1VirtualRouterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2))
alcatelIND1VirtualRouterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1))
alcatelIND1VirtualRouterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2))
alaVirtualRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterCompliance = alaVirtualRouterCompliance.setStatus('current')
alaVirtualRouterConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterConfigMIBGroup = alaVirtualRouterConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alaVirtualRouterCompliance=alaVirtualRouterCompliance, alaVirtualRouterConfig=alaVirtualRouterConfig, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alaVirtualRouterName=alaVirtualRouterName, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects)
