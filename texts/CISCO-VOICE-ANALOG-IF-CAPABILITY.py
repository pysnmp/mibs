#
# PySNMP MIB module CISCO-VOICE-ANALOG-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-ANALOG-IF-CAPABILITY
# Source digest sha256:4eb4d1ed776583cb64ad269338d55b1f10c331f2c962019ef21654b51a3d18b6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceAnalogIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 82))
ciscoVoiceAnalogIfCapability.setRevisions(('2003-04-28 00:00', '1997-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setRevisionsDescriptions(('cvaIfEMCfgLmrMCap & cvaIfEMCfgLmrECap are\n\t\t readonly', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setLastUpdated('2003-04-28 00:00')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setDescription('Agent capabilities for CISCO-VOICE-ANALOG-IF-MIB')
ciscoVoiceAnalogIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 82, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapabilityV11R03.setDescription('Cisco Voice Analog Interface MIB capabilities')
mibBuilder.exportSymbols("CISCO-VOICE-ANALOG-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapability=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapabilityV11R03=ciscoVoiceAnalogIfCapabilityV11R03)
