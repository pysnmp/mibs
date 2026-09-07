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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setLastUpdated('2007-04-03 00:00')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n         version of this document is used with the products in question:\n\n                    Alcatel-Lucent, Enterprise Solutions Division\n                   (Formerly Alcatel Internetworking, Incorporated)\n                           26801 West Agoura Road\n                        Agoura Hills, CA  91301-5122\n                          United States Of America\n\n        Telephone:               North America  +1 800 995 2696\n                                 Latin America  +1 877 919 9526\n                                 Europe         +31 23 556 0100\n                                 Asia           +65 394 7933\n                                 All Other      +1 818 878 4507\n\n        Electronic Mail:         support@ind.alcatel.com\n        World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n        File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setDescription('This module describes an authoritative enterprise-specific Simple\n         Network Management Protocol (SNMP) Management Information Base (MIB):\n\n             This proprietary MIB contains management information for\n             the configuration of IP Route Maps global configuration\n             parameters.\n\n         The right to make changes in specification and other information\n         contained in this document without prior notice is reserved.\n\n         No liability shall be assumed for any incidental, indirect, special, or\n         consequential damages whatsoever arising from or related to this\n         document or the information contained herein.\n\n         Vendors, end-users, and other interested parties are granted\n         non-exclusive license to use this specification in connection with\n         management of the products for which it is intended to be used.\n\n                     Copyright (C) 1995-2006 Alcatel-Lucent\n                         ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1VirtualRouterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1))
alaVirtualRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1))
alaVirtualRouterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setDescription('Table containing Virtual Router Name to Virtual Router Index bindings.')
alaVirtualRouterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"))
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setDescription('Each entry binds a Virtual Router Name to a Virtual Router index.')
alaVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: alaVirtualRouterName.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterName.setDescription('The name of a Virtual Router.')
alaVirtualRouterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setDescription('The index associated with the Virtual Router name.')
alaVirtualRouterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setDescription('Controls creation and deletion of Row Status entries.')
alcatelIND1VirtualRouterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2))
alcatelIND1VirtualRouterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1))
alcatelIND1VirtualRouterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2))
alaVirtualRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterCompliance = alaVirtualRouterCompliance.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterCompliance.setDescription('The compliance statement for routers running Route Maps\n            and implementing the ALCATEL-IND1-VIRTUALROUTER MIB.')
alaVirtualRouterConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 15, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterConfigMIBGroup = alaVirtualRouterConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterConfigMIBGroup.setDescription('A collection of objects to support management of global\n            configuration parameters of the Virtual Router Module.')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alaVirtualRouterCompliance=alaVirtualRouterCompliance, alaVirtualRouterConfig=alaVirtualRouterConfig, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alaVirtualRouterName=alaVirtualRouterName, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects)
