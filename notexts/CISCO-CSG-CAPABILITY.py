#
# PySNMP MIB module CISCO-CSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CSG-CAPABILITY
# Source digest sha256:1c837d150f155fede4f2571eb26481d2c9673075b8e22da287c8457212293ed6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoCsgCapability.setRevisions(('2003-05-01 00:00',))
if mibBuilder.loadTexts: ciscoCsgCapability.setLastUpdated('2003-05-01 00:00')
if mibBuilder.loadTexts: ciscoCsgCapability.setOrganization('Cisco Systems, Inc.')
ciscoCsgCapabilityV14R02ZA1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setProductRelease('Cisco IOS 12.2(14)ZA1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCsgCapabilityV14R02ZA1 = ciscoCsgCapabilityV14R02ZA1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CSG-CAPABILITY", PYSNMP_MODULE_ID=ciscoCsgCapability, ciscoCsgCapability=ciscoCsgCapability, ciscoCsgCapabilityV14R02ZA1=ciscoCsgCapabilityV14R02ZA1)
