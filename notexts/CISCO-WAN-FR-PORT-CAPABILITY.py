#
# PySNMP MIB module CISCO-WAN-FR-PORT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-FR-PORT-CAPABILITY
# Source digest sha256:6099611452f8beae7362f8dd60026878feb32082347619a755c3d7b67a94a2f2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanFrPortCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 359))
ciscoWanFrPortCapability.setRevisions(('2002-03-27 00:00',))
if mibBuilder.loadTexts: ciscoWanFrPortCapability.setLastUpdated('2002-03-27 00:00')
if mibBuilder.loadTexts: ciscoWanFrPortCapability.setOrganization('Cisco Systems, Inc.')
cwFrPortCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrPortCapabilityFrsm12V3R00 = cwFrPortCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrPortCapabilityFrsm12V3R00 = cwFrPortCapabilityFrsm12V3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-FR-PORT-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanFrPortCapability, ciscoWanFrPortCapability=ciscoWanFrPortCapability, cwFrPortCapabilityFrsm12V3R00=cwFrPortCapabilityFrsm12V3R00)
