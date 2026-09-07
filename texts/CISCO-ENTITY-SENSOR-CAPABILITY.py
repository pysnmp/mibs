#
# PySNMP MIB module CISCO-ENTITY-SENSOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-SENSOR-CAPABILITY
# Source digest sha256:dcad9392d8d4018f3c403a65a2fb2540b7cd4b0aca9cf497754c81f0d7239864
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntitySensorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 350))
ciscoEntitySensorCapability.setRevisions(('2011-02-03 00:00', '2008-10-06 00:00', '2007-07-09 00:00', '2007-06-29 00:00', '2006-06-29 00:00', '2005-09-15 00:00', '2005-04-22 00:00', '2004-09-09 00:00', '2003-08-12 00:00', '2003-03-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorCapability.setRevisionsDescriptions(('Added capability statement\n        cEntitySensorCapV12R0250SYPCat6K.', 'Added capability statement\n        cEntitySensorCapV12R0250SE.', '* Added capability statement\n           cEntitySensorCapMDS3R1: entSensorThresholdSeverity, \n           entSensorThresholdRelation, entSensorThresholdValue \n           are read-only objects for cEntitySensorCapMDS3R1.\n         * Added capability statement\n           cEntitySensorCapDCOSNEXUS.\n           entSensorThresholdSeverity, \n           entSensorThresholdRelation, entSensorThresholdValue \n           are read-only objects for \n           cEntitySensorCapDCOSNEXUS.', 'The capability statement cEntitySensorCapIOSXRV3R06CRS1\n        has been added.', 'Added capability statement\n        cEntitySensorCapCatOSV08R0601.', 'entSensorThresholdSeverity, entSensorThresholdRelation\n        , entSensorThresholdValue are read-only objects for\n        cEntitySensorCapV12R0119ECat6K,\n        cEntitySensorCapV12R0214SXCat6K,\n        cEntitySensorCapCatOSV08R0101.', 'Added capability statement\n        cEntitySensorCapMDS3R0.', 'Added cEntitySensorCapabilityV5R015 for\n        MGX8850 release 5.0.15.', '- Added cEntitySensorCapV12R0119ECat6K for IOS\n        12.1(19)E on Catalyst 6000/6500 and Cisco\n        7600 series devices.\n        - Added cEntitySensorCapV12R0214SXCat6K for IOS\n        12.2(14)SX on Catalyst 6000/6500 and Cisco\n        7600 series devices.\n        - Added ciscoEsCapabilityCatOSV81R1 for\n        Cisco CatOS 8.1(1).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setLastUpdated('2011-02-03 00:00')
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-wanatm@cisco.com\n            cs-lan-switch-snmp@cisco.com\n            cs-core-mibs@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorCapability.setDescription('The Agent capabilities for CISCO-ENTITY-SENSOR-MIB.')
ciscoEntitySensorCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorCapabilityV5R000 = ciscoEntitySensorCapabilityV5R000.setProductRelease('MGX8850 Release 5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEntitySensorCapabilityV5R000 = ciscoEntitySensorCapabilityV5R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEntitySensorCapabilityV5R000.setDescription('Agent capabilities for CISCO-ENTITY-SENSOR-MIB\n        of Voice Switch Service Module(VXSM) in \n        Release 5.0.0.')
cEntitySensorCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0119ECat6K = cEntitySensorCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0119ECat6K = cEntitySensorCapV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapV12R0119ECat6K.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0214SXCat6K = cEntitySensorCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0214SXCat6K = cEntitySensorCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapV12R0214SXCat6K.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0101 = cEntitySensorCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0101 = cEntitySensorCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapCatOSV08R0101.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapabilityV5R015 = cEntitySensorCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapabilityV5R015 = cEntitySensorCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapabilityV5R015.setDescription('Agent capabilities for CISCO-ENTITY-SENSOR-MIB\n        of Voice Switch Service Module(VXSM) in \n        Release 5.0.15.')
cEntitySensorCapMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R0 = cEntitySensorCapMDS3R0.setProductRelease('Cisco MDS 3.0(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R0 = cEntitySensorCapMDS3R0.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapMDS3R0.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0601 = cEntitySensorCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapCatOSV08R0601 = cEntitySensorCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapCatOSV08R0601.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapIOSXRV3R06CRS1 = cEntitySensorCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapIOSXRV3R06CRS1 = cEntitySensorCapIOSXRV3R06CRS1.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapIOSXRV3R06CRS1.setDescription('Agent capabilities for IOS-XR\n        Release 3.6 for CRS-1.')
cEntitySensorCapMDS3R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R1 = cEntitySensorCapMDS3R1.setProductRelease('Cisco MDS Series Storage switches\n                         Release 3.1 onwards.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapMDS3R1 = cEntitySensorCapMDS3R1.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapMDS3R1.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapDCOSNEXUS = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapDCOSNEXUS = cEntitySensorCapDCOSNEXUS.setProductRelease('Cisco Nexus7000 Series Storage switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapDCOSNEXUS = cEntitySensorCapDCOSNEXUS.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapDCOSNEXUS.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
cEntitySensorCapV12R0250SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SE = cEntitySensorCapV12R0250SE.setProductRelease('Cisco IOS 12.2(50)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SE = cEntitySensorCapV12R0250SE.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapV12R0250SE.setDescription('MIB Capability from IOS release 12.2(50)SE.')
cEntitySensorCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 350, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SYPCat6K = cEntitySensorCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntitySensorCapV12R0250SYPCat6K = cEntitySensorCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cEntitySensorCapV12R0250SYPCat6K.setDescription('CISCO-ENTITY-SENSOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntitySensorCapability, cEntitySensorCapCatOSV08R0101=cEntitySensorCapCatOSV08R0101, cEntitySensorCapCatOSV08R0601=cEntitySensorCapCatOSV08R0601, cEntitySensorCapDCOSNEXUS=cEntitySensorCapDCOSNEXUS, cEntitySensorCapIOSXRV3R06CRS1=cEntitySensorCapIOSXRV3R06CRS1, cEntitySensorCapMDS3R0=cEntitySensorCapMDS3R0, cEntitySensorCapMDS3R1=cEntitySensorCapMDS3R1, cEntitySensorCapV12R0119ECat6K=cEntitySensorCapV12R0119ECat6K, cEntitySensorCapV12R0214SXCat6K=cEntitySensorCapV12R0214SXCat6K, cEntitySensorCapV12R0250SE=cEntitySensorCapV12R0250SE, cEntitySensorCapV12R0250SYPCat6K=cEntitySensorCapV12R0250SYPCat6K, cEntitySensorCapabilityV5R015=cEntitySensorCapabilityV5R015, ciscoEntitySensorCapability=ciscoEntitySensorCapability, ciscoEntitySensorCapabilityV5R000=ciscoEntitySensorCapabilityV5R000)
