#
# PySNMP MIB module CISCO-GPRS-CHARGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GPRS-CHARGING-CAPABILITY
# Source digest sha256:27369eb819f69fb86d3906447688fffe5c8830775c9e53c5aa22a7ae146481ce
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprschargingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 297))
ciscoGprschargingCapability.setRevisions(('2004-02-03 22:30', '2003-04-08 17:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGprschargingCapability.setRevisionsDescriptions(('Added variations for cgprsCgAlarmHistType to\n                cGprschargingCapabilityV12R2M8YW and also added\n                a variations for new version\n                cGprschargingCapabilityV12R3M2XB1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGprschargingCapability.setLastUpdated('2004-02-03 22:30')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setDescription('Agent capabilities for CISCO-GPRS-CHARGING-MIB')
cGprschargingCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YD.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YY1.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YW.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R3M2XB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setProductRelease('Cisco IOS 12.3(2)XB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R3M2XB1.setDescription('Cisco GPRS CHARGING MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-CHARGING-CAPABILITY", PYSNMP_MODULE_ID=ciscoGprschargingCapability, cGprschargingCapabilityV12R2M8YD=cGprschargingCapabilityV12R2M8YD, cGprschargingCapabilityV12R2M8YW=cGprschargingCapabilityV12R2M8YW, cGprschargingCapabilityV12R2M8YY1=cGprschargingCapabilityV12R2M8YY1, cGprschargingCapabilityV12R3M2XB1=cGprschargingCapabilityV12R3M2XB1, ciscoGprschargingCapability=ciscoGprschargingCapability)
