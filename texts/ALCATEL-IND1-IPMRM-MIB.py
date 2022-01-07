#
# PySNMP MIB module ALCATEL-IND1-IPMRM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-IPMRM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:00:01 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
routingIND1Ipmrm, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ipmrm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, iso, Counter32, Counter64, ObjectIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, TimeTicks, NotificationType, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter32", "Counter64", "ObjectIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1IPMRMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1))
alcatelIND1IPMRMMIB.setRevisions(('2012-04-03 00:00', '2014-12-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setRevisionsDescriptions(('The latest version of this MIB Module.', 'Add failover holddown object..',))
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setLastUpdated('201412040000Z')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n         version of this document is used with the products in question:\n\n                    Alcatel-Lucent, Enterprise Solutions Division\n                   (Formerly Alcatel Internetworking, Incorporated)\n                           26801 West Agoura Road\n                        Agoura Hills, CA  91301-5122\n                          United States Of America\n\n        Telephone:               North America  +1 800 995 2696\n                                 Latin America  +1 877 919 9526\n                                 Europe         +31 23 556 0100\n                                 Asia           +65 394 7933\n                                 All Other      +1 818 878 4507\n\n        Electronic Mail:         support@ind.alcatel.com\n        World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n        File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1IPMRMMIB.setDescription('This module describes an authoritative enterprise-specific Simple\n         Network Management Protocol (SNMP) Management Information Base (MIB):\n\n             This proprietary MIB contains management information for \n             the configuration of IPMRM (IP Multicast Route Manager)\n             global configuration parameters.\n\n         The right to make changes in specification and other information\n         contained in this document without prior notice is reserved.\n\n         No liability shall be assumed for any incidental, indirect, special, or\n         consequential damages whatsoever arising from or related to this\n         document or the information contained herein.\n\n         Vendors, end-users, and other interested parties are granted\n         non-exclusive license to use this specification in connection with\n         management of the products for which it is intended to be used.\n\n                     Copyright (C) 1995-2007 Alcatel-Lucent\n                         ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1IPMRMMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1))
alaIpmrmGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1))
alaIpmrmMbrStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmMbrStatus.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmMbrStatus.setDescription('Administratively enables/disables the Multicast\n                Border Router (MBR) functionality on this router.')
alaIpmrmMbrProtocolApps = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("dvmrp", 0), ("pim", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaIpmrmMbrProtocolApps.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmMbrProtocolApps.setDescription('Bit map object to reflect the multicast protocols that\n                are currently registered with IPMRM.  Bits 0 - 1 are \n                currently in use, and if set, indicate that the respective \n                application is currently active:\n                     bit 0 - DVMRP\n                     bit 1 - PIM ')
alaIpmrmFailoverHolddown = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(80)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmFailoverHolddown.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmFailoverHolddown.setDescription('This is the period (in seconds) during a failover\n                in which the multicast routing tables will be kept in\n                holddown (or frozen) to allow for the unicast and multicast \n                routing protocols to converge before updating the \n                forwarding tables.\n\n                A value of 0 indicates that multicast routing will not\n                not be frozen during a failover.')
alaIpmrmExtendedBoundaryStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaIpmrmExtendedBoundaryStatus.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmExtendedBoundaryStatus.setDescription('Administratively enables/disables the Multicast\n                 Route Boundary Expand functionality on this router.')
alcatelIND1IPMRMMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2))
alcatelIND1IPMRMMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1))
alcatelIND1IPMRMMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2))
alaIpmrmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmCompliance = alaIpmrmCompliance.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmCompliance.setDescription('The compliance statement for routers running IP Multicast\n             and implementing the ALCATEL-IND1-IPMRM MIB.')
alaIpmrmConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrStatus"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmMbrProtocolApps"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmFailoverHolddown"), ("ALCATEL-IND1-IPMRM-MIB", "alaIpmrmExtendedBoundaryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaIpmrmConfigMIBGroup = alaIpmrmConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaIpmrmConfigMIBGroup.setDescription('A collection of objects to support management of global\n            configuration parameters for IP Multicast Routing')
mibBuilder.exportSymbols("ALCATEL-IND1-IPMRM-MIB", alaIpmrmFailoverHolddown=alaIpmrmFailoverHolddown, alaIpmrmGlobalConfig=alaIpmrmGlobalConfig, PYSNMP_MODULE_ID=alcatelIND1IPMRMMIB, alaIpmrmConfigMIBGroup=alaIpmrmConfigMIBGroup, alaIpmrmCompliance=alaIpmrmCompliance, alcatelIND1IPMRMMIBConformance=alcatelIND1IPMRMMIBConformance, alcatelIND1IPMRMMIBGroups=alcatelIND1IPMRMMIBGroups, alaIpmrmMbrProtocolApps=alaIpmrmMbrProtocolApps, alcatelIND1IPMRMMIBCompliances=alcatelIND1IPMRMMIBCompliances, alaIpmrmMbrStatus=alaIpmrmMbrStatus, alaIpmrmExtendedBoundaryStatus=alaIpmrmExtendedBoundaryStatus, alcatelIND1IPMRMMIB=alcatelIND1IPMRMMIB, alcatelIND1IPMRMMIBObjects=alcatelIND1IPMRMMIBObjects)
