#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:37:03 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, MibIdentifier, NotificationType, Counter32, IpAddress, ObjectIdentity, Bits, ModuleIdentity, Gauge32, Integer32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "MibIdentifier", "NotificationType", "Counter32", "IpAddress", "ObjectIdentity", "Bits", "ModuleIdentity", "Gauge32", "Integer32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatelIND1SNMPAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1))
alcatelIND1SNMPAgentMIB.setRevisions(('2014-07-15 00:00',))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setLastUpdated('201407150000Z')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setOrganization('Alcatel-Lucent')
alcatelIND1SNMPAgentMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setStatus('current')
alcatelIND1SNMPAgentMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setStatus('current')
alcatelIND1SNMPAgentMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setStatus('current')
alcatelIND1SNMPAgentMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setStatus('current')
snmpAgtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1))
class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noSec", 1), ("authSet", 2), ("authAll", 3), ("privSet", 4), ("privAll", 5), ("trapOnly", 6))

snmpAgtSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 1), SnmpAgtSecurityLevel().clone('noSec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setStatus('current')
snmpAgtCommunityMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtCommunityMode.setStatus('current')
snmpAgtCtlFiles = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: snmpAgtCtlFiles.setStatus('current')
snmpAgtSourceIpConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("noLoopback0", 2), ("ipInterface", 3))).clone('default')).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setStatus('deprecated')
snmpAgtSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpAgtSourceIp.setStatus('deprecated')
alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SNMPAgentMIBCompliance = alcatelIND1SNMPAgentMIBCompliance.setStatus('current')
snmpAgtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtConfigGroup = snmpAgtConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, snmpAgtCtlFiles=snmpAgtCtlFiles, snmpAgtSourceIp=snmpAgtSourceIp, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, snmpAgtSecurityLevel=snmpAgtSecurityLevel, snmpAgtCommunityMode=snmpAgtCommunityMode, PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, snmpAgtConfig=snmpAgtConfig, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, snmpAgtConfigGroup=snmpAgtConfigGroup, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, snmpAgtSourceIpConfig=snmpAgtSourceIpConfig)
