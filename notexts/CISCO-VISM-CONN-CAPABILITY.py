#
# PySNMP MIB module CISCO-VISM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VISM-CONN-CAPABILITY
# Source digest sha256:0d89090820110edd2cdf4f414659a0870c330884915cf10b2c5b56b9c4a1dc85
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 400))
ciscoVismConnCapability.setRevisions(('2004-03-17 00:00',))
if mibBuilder.loadTexts: ciscoVismConnCapability.setLastUpdated('2004-03-17 00:00')
if mibBuilder.loadTexts: ciscoVismConnCapability.setOrganization('Cisco Systems, Inc.')
cVismConnCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 400, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-CONN-CAPABILITY", PYSNMP_MODULE_ID=ciscoVismConnCapability, cVismConnCapabilityV321=cVismConnCapabilityV321, ciscoVismConnCapability=ciscoVismConnCapability)
