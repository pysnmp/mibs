#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-CAS-MODULE-CAPABILITY
# Source digest sha256:083495059f87452794b90db1800f95966e1a717c8f91af1dbe58e0da4cb7f1cc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceCasModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 401))
ciscoVoiceCasModuleCapability.setRevisions(('2004-03-29 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setLastUpdated('2004-03-29 00:00')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setOrganization('Cisco Systems, Inc.')
cvcmCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 401, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceCasModuleCapability, ciscoVoiceCasModuleCapability=ciscoVoiceCasModuleCapability, cvcmCapabilityV321=cvcmCapabilityV321)
