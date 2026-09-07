#
# PySNMP MIB module CISCO-CONFIG-COPY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CONFIG-COPY-CAPABILITY
# Source digest sha256:c16756511568f48ae91d37580ae77f7bd088ccd77f033ae4e01c34852a242491
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ConfigCopyFailCause, ConfigCopyProtocol, ConfigCopyState, ConfigFileType = mibBuilder.importSymbols("CISCO-CONFIG-COPY-MIB", "ConfigCopyFailCause", "ConfigCopyProtocol", "ConfigCopyState", "ConfigFileType")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoConfigCopyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 128))
ciscoConfigCopyCapability.setRevisions(('2006-02-08 00:00', '2005-05-24 00:00', '2004-06-08 00:00', '2004-03-17 00:00', '2002-04-29 00:00', '2000-09-06 00:00', '1999-10-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoConfigCopyCapability.setRevisionsDescriptions(('Added Agent Capability statement\n                 ciscoConfigCopyCapIOSXRV2R0CRS1.', 'Added capability statement \n                 ciscoConfigCopyCapMDS3R0.', 'Added capability statement \n                 ciscoConfigCopyCapCatOSV08R0401.', 'Adding new varbind for ccCopyCompletion \n                 Notification.', 'Added ciscoConfigCopyCapabilityV2R0175\n                 for RPM-PR module in MGX8850.', 'Added VARIATION clauses to \n                 ccCopySourceFileType and ccCopyDestFileType.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setLastUpdated('2006-02-08 00:00')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com\n                        cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoConfigCopyCapability.setDescription('This is the Agent Capabilities for\n                 CISCO-CONFIG-COPY-MIB.')
ciscoConfigCopyCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R00 = ciscoConfigCopyCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R00.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R01 = ciscoConfigCopyCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R01.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapabilityV2R0175 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setProductRelease('MGX8850 Release 2.1.75')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV2R0175 = ciscoConfigCopyCapabilityV2R0175.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV2R0175.setDescription('CISCO-CONFIG-COPY-MIB Capabilities\n                         for RPM-PR(Router Module).')
ciscoConfigCopyCapabilityV12R30S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setProductRelease('Cisco IOS 12.30S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapabilityV12R30S = ciscoConfigCopyCapabilityV12R30S.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapabilityV12R30S.setDescription('CONFIG-COPY MIB capabilities')
ciscoConfigCopyCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapCatOSV08R0401 = ciscoConfigCopyCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapCatOSV08R0401.setDescription('CISCO-CONFIG-COPY-MIB capabilities.')
ciscoConfigCopyCapMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setProductRelease('Cisco MDS 3.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapMDS3R0 = ciscoConfigCopyCapMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapMDS3R0.setDescription('CISCO-CONFIG-COPY-MIB capabilities.')
ciscoConfigCopyCapIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 128, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConfigCopyCapIOSXRV2R0CRS1 = ciscoConfigCopyCapIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoConfigCopyCapIOSXRV2R0CRS1.setDescription('CISCO-CONFIG-COPY-MIB Capabilities\n                         for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-CONFIG-COPY-CAPABILITY", PYSNMP_MODULE_ID=ciscoConfigCopyCapability, ciscoConfigCopyCapCatOSV08R0401=ciscoConfigCopyCapCatOSV08R0401, ciscoConfigCopyCapIOSXRV2R0CRS1=ciscoConfigCopyCapIOSXRV2R0CRS1, ciscoConfigCopyCapMDS3R0=ciscoConfigCopyCapMDS3R0, ciscoConfigCopyCapability=ciscoConfigCopyCapability, ciscoConfigCopyCapabilityV12R00=ciscoConfigCopyCapabilityV12R00, ciscoConfigCopyCapabilityV12R01=ciscoConfigCopyCapabilityV12R01, ciscoConfigCopyCapabilityV12R30S=ciscoConfigCopyCapabilityV12R30S, ciscoConfigCopyCapabilityV2R0175=ciscoConfigCopyCapabilityV2R0175)
