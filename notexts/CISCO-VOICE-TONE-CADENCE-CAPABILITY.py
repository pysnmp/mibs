#
# PySNMP MIB module CISCO-VOICE-TONE-CADENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-TONE-CADENCE-CAPABILITY
# Source digest sha256:475a14285f457a73b7e4c08eb73fe79bb0065147cbd94464b710f59ebb215148
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceToneCadenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 387))
ciscoVoiceToneCadenceCapability.setRevisions(('2004-02-02 00:00',))
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setLastUpdated('2004-02-02 00:00')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setOrganization('Cisco Systems, Inc.')
cVoiceToneCadenceCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 387, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-TONE-CADENCE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceToneCadenceCapability, cVoiceToneCadenceCapV5R00=cVoiceToneCadenceCapV5R00, ciscoVoiceToneCadenceCapability=ciscoVoiceToneCadenceCapability)
