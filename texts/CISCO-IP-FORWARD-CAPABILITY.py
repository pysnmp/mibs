#
# PySNMP MIB module CISCO-IP-FORWARD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-FORWARD-CAPABILITY
# Source digest sha256:5d68f67cffe62f8689a0303bdf312cbec4d426860483241aacd2c9d9657a4b42
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpForwardCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 595))
ciscoIpForwardCapability.setRevisions(('2010-09-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpForwardCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpForwardCapability.setLastUpdated('2010-09-23 00:00')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ipv6@cisco.com')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setDescription('The capabilities description of IP-FORWARD-MIB.')
ciscoIpForwardCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 595, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIpForwardCapabilityV12R2SE.setDescription('IP-FORWARD-MIB capabilities for Catalyst 2k/3k.')
mibBuilder.exportSymbols("CISCO-IP-FORWARD-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpForwardCapability, ciscoIpForwardCapability=ciscoIpForwardCapability, ciscoIpForwardCapabilityV12R2SE=ciscoIpForwardCapabilityV12R2SE)
