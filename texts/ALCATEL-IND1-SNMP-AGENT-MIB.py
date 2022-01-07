#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:15:06 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, ModuleIdentity, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Gauge32, Counter32, NotificationType, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Gauge32", "Counter32", "NotificationType", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SNMPAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1))
alcatelIND1SNMPAgentMIB.setRevisions(('2014-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setRevisionsDescriptions(('Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setLastUpdated('201407150000Z')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n             version of this document is used with the products in question:\n\n                        Alcatel-Lucent, Enterprise Solutions Division\n                       (Formerly Alcatel Internetworking, Incorporated)\n                               26801 West Agoura Road\n                            Agoura Hills, CA  91301-5122\n                              United States Of America\n\n            Telephone:               North America  +1 800 995 2696\n                                     Latin America  +1 877 919 9526\n                                     Europe         +31 23 556 0100\n                                     Asia           +65 394 7933\n                                     All Other      +1 818 878 4507\n\n            Electronic Mail:         support@ind.alcatel.com\n            World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n            File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setDescription('This module describes an authoritative enterprise-specific Simple\n             Network Management Protocol (SNMP) Management Information Base (MIB):\n\n                 For the Birds Of Prey Product Line\n                 SNMP Agent Subsystem.\n\n             The right to make changes in specification and other information\n             contained in this document without prior notice is reserved.\n\n             No liability shall be assumed for any incidental, indirect, special, or\n             consequential damages whatsoever arising from or related to this\n             document or the information contained herein.\n\n             Vendors, end-users, and other interested parties are granted\n             non-exclusive license to use this specification in connection with\n             management of the products for which it is intended to be used.\n\n                         Copyright (C) 1995-2007 Alcatel-Lucent\n                             ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1SNMPAgentMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setDescription('Branch For SNMP Agent Subsystem Managed Objects.')
alcatelIND1SNMPAgentMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setDescription('Branch For SNMP Agent Subsystem Conformance Information.')
alcatelIND1SNMPAgentMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setDescription('Branch For SNMP Agent Subsystem Units Of Conformance.')
alcatelIND1SNMPAgentMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setDescription('Branch For SNMP Agent Subsystem Compliance Statements.')
snmpAgtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1))
class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    description = 'The switch security level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noSec", 1), ("authSet", 2), ("authAll", 3), ("privSet", 4), ("privAll", 5), ("trapOnly", 6))

snmpAgtSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 1), SnmpAgtSecurityLevel().clone('noSec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setStatus('current')
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setDescription('Level of security required for SNMP get or SET.\n         noSec: no security; all the PDU with a known user id\n                are accepted\n         authSet: authentication required for set; all GET\n                are accepted, but not authenticated SET are\n                rejected.\n         authAll: authentication required for SET and GET; not\n                authenticated SET and GET are rejected.\n         privSet: authentication required for GET and encryption\n                required for SET.\n         privAll: encryption required for SET and GET.\n         trapOnly: no SNMP GET or SET are accepted.')
snmpAgtCommunityMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtCommunityMode.setStatus('current')
if mibBuilder.loadTexts: snmpAgtCommunityMode.setDescription('If the community mode is enabled,\n                 the SNMPv1/v2 packets must use\n                 the community names.')
snmpAgtCtlFiles = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: snmpAgtCtlFiles.setStatus('current')
if mibBuilder.loadTexts: snmpAgtCtlFiles.setDescription('MIB entity on which to attach the MODULE-IDENTITY for the\n        Epilogue(R) control files.')
snmpAgtSourceIpConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("noLoopback0", 2), ("ipInterface", 3))).clone('default')).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setStatus('deprecated')
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setDescription('The SNMP Agent Configuration\n              1 -- Default(Loopback0 or closest IP)\n              2 -- No Loopback0\n              3 -- Interface IP Specified by User\n              NOTE: this configuration option has been deprecated.\n              Please see alaIpServiceSourceIpTable for SNMP Source\n              IP Preferred Configuration (in ALCATEL-IND1-IP-MIB).')
snmpAgtSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpAgtSourceIp.setStatus('deprecated')
if mibBuilder.loadTexts: snmpAgtSourceIp.setDescription('The Source IP of SNMP Packets.\n               NOTE: this configuration option has been deprecated.\n               Please see alaIpServiceSourceIpTable for SNMP Source\n               IP Preferred Configuration (in ALCATEL-IND1-IP-MIB).')
alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SNMPAgentMIBCompliance = alcatelIND1SNMPAgentMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliance.setDescription('Compliance statement for SNMP Agent Subsystem.')
snmpAgtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtConfigGroup = snmpAgtConfigGroup.setStatus('current')
if mibBuilder.loadTexts: snmpAgtConfigGroup.setDescription('Collection of objects for SNMP Agent configuration.')
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", snmpAgtSourceIp=snmpAgtSourceIp, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, snmpAgtConfig=snmpAgtConfig, PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, snmpAgtConfigGroup=snmpAgtConfigGroup, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, snmpAgtSecurityLevel=snmpAgtSecurityLevel, snmpAgtCtlFiles=snmpAgtCtlFiles, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, snmpAgtCommunityMode=snmpAgtCommunityMode)
