#
# PySNMP MIB module ALCATEL-IND1-SNMP-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-SNMP-AGENT-MIB
# Source digest sha256:8f8fe0ffd1015f7a185022744c09b327b0265dd5cc80dd4326ce66d2f550c3eb
# Produced by pysmi-2.3.0
#
softentIND1SnmpAgt, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1SnmpAgt")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SNMPAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1))
alcatelIND1SNMPAgentMIB.setRevisions(('2019-10-07 00:00',))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setLastUpdated('2019-10-07 00:00')
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIB.setOrganization('ALE USA Inc')
alcatelIND1SNMPAgentMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBObjects.setStatus('current')
alcatelIND1SNMPAgentMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBConformance.setStatus('current')
alcatelIND1SNMPAgentMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBGroups.setStatus('current')
alcatelIND1SNMPAgentMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SNMPAgentMIBCompliances.setStatus('current')
snmpAgtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1))
class SnmpAgtSecurityLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noSec", 1), ("authSet", 2), ("authAll", 3), ("privSet", 4), ("privAll", 5), ("trapOnly", 6))

snmpAgtSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 1), SnmpAgtSecurityLevel().clone('noSec')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSecurityLevel.setStatus('current')
snmpAgtCommunityMode = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtCommunityMode.setStatus('current')
snmpAgtCtlFiles = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 3))
if mibBuilder.loadTexts: snmpAgtCtlFiles.setStatus('current')
snmpAgtSourceIpConfig = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("default", 1), ("noLoopback0", 2), ("ipInterface", 3))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIpConfig.setStatus('current')
snmpAgtSourceIp = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpAgtSourceIp.setStatus('current')
alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtConfigGroup"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCtlFilesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SNMPAgentMIBCompliance = alcatelIND1SNMPAgentMIBCompliance.setStatus('current')
snmpAgtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtConfigGroup = snmpAgtConfigGroup.setStatus('current')
snmpAgtCtlFilesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"), ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpAgtCtlFilesGroup = snmpAgtCtlFilesGroup.setStatus('current')
snmpAgtViewMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6))
snmpAgtViewTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: snmpAgtViewTable.setStatus('current')
snmpAgtViewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtViewName"), (0, "ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtViewTableID"))
if mibBuilder.loadTexts: snmpAgtViewEntry.setStatus('current')
snmpAgtViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: snmpAgtViewName.setStatus('current')
snmpAgtViewTableID = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: snmpAgtViewTableID.setStatus('current')
snmpAgtViewType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 1, 1, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: snmpAgtViewType.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SNMP-AGENT-MIB", PYSNMP_MODULE_ID=alcatelIND1SNMPAgentMIB, SnmpAgtSecurityLevel=SnmpAgtSecurityLevel, alcatelIND1SNMPAgentMIB=alcatelIND1SNMPAgentMIB, alcatelIND1SNMPAgentMIBCompliance=alcatelIND1SNMPAgentMIBCompliance, alcatelIND1SNMPAgentMIBCompliances=alcatelIND1SNMPAgentMIBCompliances, alcatelIND1SNMPAgentMIBConformance=alcatelIND1SNMPAgentMIBConformance, alcatelIND1SNMPAgentMIBGroups=alcatelIND1SNMPAgentMIBGroups, alcatelIND1SNMPAgentMIBObjects=alcatelIND1SNMPAgentMIBObjects, snmpAgtCommunityMode=snmpAgtCommunityMode, snmpAgtConfig=snmpAgtConfig, snmpAgtConfigGroup=snmpAgtConfigGroup, snmpAgtCtlFiles=snmpAgtCtlFiles, snmpAgtCtlFilesGroup=snmpAgtCtlFilesGroup, snmpAgtSecurityLevel=snmpAgtSecurityLevel, snmpAgtSourceIp=snmpAgtSourceIp, snmpAgtSourceIpConfig=snmpAgtSourceIpConfig, snmpAgtViewEntry=snmpAgtViewEntry, snmpAgtViewMIB=snmpAgtViewMIB, snmpAgtViewName=snmpAgtViewName, snmpAgtViewTable=snmpAgtViewTable, snmpAgtViewTableID=snmpAgtViewTableID, snmpAgtViewType=snmpAgtViewType)
