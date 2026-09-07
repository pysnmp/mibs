#
# PySNMP MIB module CISCO-VOIP-TAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOIP-TAP-CAPABILITY
# Source digest sha256:ea57da9c2a5c533af4890a80cba19f144dc3d986dc2d0a9195d64c223cb01da3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoipTapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 593))
ciscoVoipTapCapability.setRevisions(('2010-08-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoipTapCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoipTapCapability.setLastUpdated('2010-08-24 00:00')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setDescription('The capabilities description of CISCO-VOIP-TAP-MIB.')
ciscoVoipTapCapV15R01SXE31ASR1K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 593, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setProductRelease('Cisco IOS XE 15.0(01)SXE31 on ASR 1000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setStatus('current')
if mibBuilder.loadTexts: ciscoVoipTapCapV15R01SXE31ASR1K.setDescription('CISCO-VOIP-TAP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoipTapCapability, ciscoVoipTapCapV15R01SXE31ASR1K=ciscoVoipTapCapV15R01SXE31ASR1K, ciscoVoipTapCapability=ciscoVoipTapCapability)
