#
# PySNMP MIB module CISCO-VOICE-AALX-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-AALX-PROFILE-CAPABILITY
# Source digest sha256:a6a509180309f8d59d8f4d5ccb8317dcfbd0a222d8fe689232f1e690a098cf20
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceAalxProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 352))
ciscoVoiceAalxProfileCapability.setRevisions(('2004-02-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setLastUpdated('2004-02-07 00:00')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setDescription('The agent capabilities for CISCO-VOICE-AALX-PROFILE-MIB.')
cVoiceAalxProfileCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 352, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setStatus('current')
if mibBuilder.loadTexts: cVoiceAalxProfileCapV5R00.setDescription('AALX Profile MIB capabilities for Voice \n                         Switch Service Module(VXSM) in \n                         release 5.0.0.')
mibBuilder.exportSymbols("CISCO-VOICE-AALX-PROFILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAalxProfileCapability, cVoiceAalxProfileCapV5R00=cVoiceAalxProfileCapV5R00, ciscoVoiceAalxProfileCapability=ciscoVoiceAalxProfileCapability)
