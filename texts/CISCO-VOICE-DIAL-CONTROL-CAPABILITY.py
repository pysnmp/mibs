#
# PySNMP MIB module CISCO-VOICE-DIAL-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-DIAL-CONTROL-CAPABILITY
# Source digest sha256:fc80ef7eafccb417c75dbd8246297d71e37071e781a15f415e3a8889c00c9745
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoVoiceDialControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 83))
ciscoVoiceDialControlCapability.setRevisions(('2009-03-31 00:00', '2006-11-16 00:00', '2005-07-25 00:00', '1999-07-12 00:00', '1998-01-09 00:00', '1997-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setRevisionsDescriptions(('Added ciscoVoiceDialControlCapV12R04Rev1 for IOS 12.4T', 'Added ciscoVoiceDialControlCapV12R04 for IOS 12.4.', 'Add GSM AMR-NB bit rate mode supports.', 'Add new codec types supports.', 'Add DNIS, DID, Max connections supports.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setLastUpdated('2009-03-31 00:00')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W. Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:    +1 800 553-NETS\n\n            E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setDescription('Agent capabilities for CISCO-VOICE-DIAL-CONTROL-MIB.')
ciscoVoiceDialControlCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapabilityV11R03.setDescription('Cisco Voice Dial Control MIB capabilities.')
ciscoVoiceDialControlCapabilityV11R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapabilityV11R03Rev1.setDescription('Cisco Voice Dial Control MIB capabilities.')
ciscoVoiceDialControlCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapabilityV12R00.setDescription('Cisco Voice Dial Control MIB capabilities.')
ciscoVoiceDialControlCapabilityV12R00Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapabilityV12R00Rev1.setDescription('Cisco Voice Dial Control MIB capabilities.')
ciscoVoiceDialControlCapabilityV124R03T5400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setProductRelease('Cisco IOS 12.4(3)T on AS5400')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapabilityV124R03T5400.setDescription('Cisco Voice Dial Control MIB capabilities\n        supporting GSM AMR-NB codec.')
ciscoVoiceDialControlCapV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setProductRelease('Cisco IOS 12.4 for all platforms except IAD2420')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapV12R04.setDescription('Cisco Voice Dial Control MIB capabilities.')
ciscoVoiceDialControlCapV12R04Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setProductRelease('Cisco IOS 12.4T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapV12R04Rev1.setDescription('Cisco Voice Dial Control MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VOICE-DIAL-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapV12R04=ciscoVoiceDialControlCapV12R04, ciscoVoiceDialControlCapV12R04Rev1=ciscoVoiceDialControlCapV12R04Rev1, ciscoVoiceDialControlCapability=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapabilityV11R03=ciscoVoiceDialControlCapabilityV11R03, ciscoVoiceDialControlCapabilityV11R03Rev1=ciscoVoiceDialControlCapabilityV11R03Rev1, ciscoVoiceDialControlCapabilityV124R03T5400=ciscoVoiceDialControlCapabilityV124R03T5400, ciscoVoiceDialControlCapabilityV12R00=ciscoVoiceDialControlCapabilityV12R00, ciscoVoiceDialControlCapabilityV12R00Rev1=ciscoVoiceDialControlCapabilityV12R00Rev1)
