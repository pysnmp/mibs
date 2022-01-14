#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:55:51 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, ObjectIdentity, IpAddress, Bits, NotificationType, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "Bits", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "iso")
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
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", snmpAgtConfig=snmpAgtConfig, snmpAgtConfigGroup=snmpAgtConfigGroup, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, snmpAgtSourceIp=snmpAgtSourceIp, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, snmpAgtSecurityLevel=snmpAgtSecurityLevel, snmpAgtCommunityMode=snmpAgtCommunityMode, snmpAgtCtlFiles=snmpAgtCtlFiles, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects)
