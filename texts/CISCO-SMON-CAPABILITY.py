#
# PySNMP MIB module CISCO-SMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SMON-CAPABILITY
# Source digest sha256:5f31f790c964d5ed6193b6da57edfdaca31bc5ea56cb9c43f71d9bcc78306113
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 381))
ciscoSmonCapability.setRevisions(('2004-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSmonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSmonCapability.setLastUpdated('2004-01-22 00:00')
if mibBuilder.loadTexts: ciscoSmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSmonCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSmonCapability.setDescription('Agent capabilities for SMON-MIB.')
csCapV12R0214SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 3 (PFC 3).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: csCapV12R0214SXCat6KPfc3.setDescription('SMON-MIB agent capabilities.')
csCapV12R0113ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: csCapV12R0113ECat6KPfc2.setDescription('SMON-MIB agent capabilities.')
csCapCatOSV07R0102Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setProductRelease('Cisco CatOS 7.1(2) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: csCapCatOSV07R0102Cat6KPfc2.setDescription('SMON-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-SMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoSmonCapability, ciscoSmonCapability=ciscoSmonCapability, csCapCatOSV07R0102Cat6KPfc2=csCapCatOSV07R0102Cat6KPfc2, csCapV12R0113ECat6KPfc2=csCapV12R0113ECat6KPfc2, csCapV12R0214SXCat6KPfc3=csCapV12R0214SXCat6KPfc3)
