#
# PySNMP MIB module ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:44:36 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1Aip, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Aip")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, IpAddress, iso, ModuleIdentity, MibIdentifier, Counter64, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "IpAddress", "iso", "ModuleIdentity", "MibIdentifier", "Counter64", "NotificationType", "Bits")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
alcatelIND1InterswitchProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1))
alcatelIND1InterswitchProtocolMIB.setRevisions(('2010-05-13 00:00', '2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setRevisionsDescriptions(('Fixed the Notifications to use MIB Module OID.0 as Notifications root.', 'Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setLastUpdated('201005130000Z')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n             version of this document is used with the products in question:\n\n                        Alcatel-Lucent, Enterprise Solutions Division\n                       (Formerly Alcatel Internetworking, Incorporated)\n                               26801 West Agoura Road\n                            Agoura Hills, CA  91301-5122\n                              United States Of America\n\n            Telephone:               North America  +1 800 995 2696\n                                     Latin America  +1 877 919 9526\n                                     Europe         +31 23 556 0100\n                                     Asia           +65 394 7933\n                                     All Other      +1 818 878 4507\n\n            Electronic Mail:         support@ind.alcatel.com\n            World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n            File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setDescription('This module describes an authoritative enterprise-specific Simple\n             Network Management Protocol (SNMP) Management Information Base (MIB):\n\n                 For the Birds Of Prey Product Line\n                 Health Monitoring for dissemination of resource consumption information.\n\n             The right to make changes in specification and other information\n             contained in this document without prior notice is reserved.\n\n             No liability shall be assumed for any incidental, indirect, special, or\n             consequential damages whatsoever arising from or related to this\n             document or the information contained herein.\n\n             Vendors, end-users, and other interested parties are granted\n             non-exclusive license to use this specification in connection with\n             management of the products for which it is intended to be used.\n\n                         Copyright (C) 1995-2010 Alcatel-Lucent\n                             ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1InterswitchProtocolMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 0))
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIBNotifications.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIBNotifications.setDescription('Branch For Inter Switch Protocol MIB Subsystem Notifications.')
alcatelIND1InterswitchProtocolMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1))
aipLLDPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1))
alcatelIND1InterswitchProtocolMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2))
aipLLDPConfigManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1), )
if mibBuilder.loadTexts: aipLLDPConfigManAddrTable.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfigManAddrTable.setDescription('The table that controls selection of LLDP management address\n            TLV instances to be transmitted on individual ports.')
aipLLDPConfigManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrPortNum"))
if mibBuilder.loadTexts: aipLLDPConfigManAddrEntry.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfigManAddrEntry.setDescription('LLDP configuration information for a particular port\n             on which the local system management address instance will be transmitted.')
aipLLDPConfigManAddrPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aipLLDPConfigManAddrPortNum.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfigManAddrPortNum.setDescription('The  port ifindex of the port associated with this entry.')
aipLLDPConfigManAddrTlvTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aipLLDPConfigManAddrTlvTxEnable.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfigManAddrTlvTxEnable.setDescription(' This object controls, on a per port basis, whether or not\n              management address TLV instances are transmitted. The value\n              true(1) means that management address TLVs are transmitted ;\n              the value false(2) means that they are not.The default value\n              for this object is false(2). ')
aipLLDPConfigNearestEdgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aipLLDPConfigNearestEdgeEnable.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfigNearestEdgeEnable.setDescription(' This global object specifies, whether or not NearestEdge\n              is enabled. The value true(1) means that it is enabled;\n              the value false(2) means that they are not.The default value\n              for this object is false(2). ')
alcatelIND1InterswitchProtocolMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1))
alcatelIND1InterswitchProtocolMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2))
aipLLDPConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrTlvTxEnable"), ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigNearestEdgeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aipLLDPConfGroup = aipLLDPConfGroup.setStatus('current')
if mibBuilder.loadTexts: aipLLDPConfGroup.setDescription('A collection of objects providing information about LLDP.')
alcatelIND1InterswitchProtocolMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1InterswitchProtocolMIBCompliance = alcatelIND1InterswitchProtocolMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIBCompliance.setDescription('The compliance statement for device support of AIP.')
mibBuilder.exportSymbols("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", alcatelIND1InterswitchProtocolMIBNotifications=alcatelIND1InterswitchProtocolMIBNotifications, aipLLDPConfig=aipLLDPConfig, aipLLDPConfigManAddrTable=aipLLDPConfigManAddrTable, PYSNMP_MODULE_ID=alcatelIND1InterswitchProtocolMIB, aipLLDPConfigManAddrPortNum=aipLLDPConfigManAddrPortNum, aipLLDPConfigManAddrTlvTxEnable=aipLLDPConfigManAddrTlvTxEnable, aipLLDPConfigNearestEdgeEnable=aipLLDPConfigNearestEdgeEnable, aipLLDPConfGroup=aipLLDPConfGroup, alcatelIND1InterswitchProtocolMIBCompliance=alcatelIND1InterswitchProtocolMIBCompliance, alcatelIND1InterswitchProtocolMIBCompliances=alcatelIND1InterswitchProtocolMIBCompliances, aipLLDPConfigManAddrEntry=aipLLDPConfigManAddrEntry, alcatelIND1InterswitchProtocolMIBObjects=alcatelIND1InterswitchProtocolMIBObjects, alcatelIND1InterswitchProtocolMIBConformance=alcatelIND1InterswitchProtocolMIBConformance, alcatelIND1InterswitchProtocolMIB=alcatelIND1InterswitchProtocolMIB, alcatelIND1InterswitchProtocolMIBGroups=alcatelIND1InterswitchProtocolMIBGroups)
