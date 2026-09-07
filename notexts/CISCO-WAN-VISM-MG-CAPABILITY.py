#
# PySNMP MIB module CISCO-WAN-VISM-MG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-MG-CAPABILITY
# Source digest sha256:ad99594399573cfc05e0a29771101126be337396ab3ab3e4866fbc31c779a7e8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 320))
ciscoWanVismMgCapability.setRevisions(('2000-07-17 00:00', '2000-03-17 00:00',))
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setLastUpdated('2000-03-17 00:00')
if mibBuilder.loadTexts: ciscoWanVismMgCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanVismMgCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setProductRelease('VISM Release1.5,VISM Release2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R00 = ciscoWanVismMgCapabilityV2R00.setStatus('current')
ciscoWanVismMgCapabilityV2R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setProductRelease('VISM Release2.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgCapabilityV2R02 = ciscoWanVismMgCapabilityV2R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MG-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismMgCapability, ciscoWanVismMgCapability=ciscoWanVismMgCapability, ciscoWanVismMgCapabilityV2R00=ciscoWanVismMgCapabilityV2R00, ciscoWanVismMgCapabilityV2R02=ciscoWanVismMgCapabilityV2R02)
