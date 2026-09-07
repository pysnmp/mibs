#
# PySNMP MIB module CISCO-DOT11-HT-MAC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-HT-MAC-CAPABILITY
# Source digest sha256:ab8ad506283292e29495c3a178012bea98072b90ea21d988690171fe20c2e3a9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
cDot11HtMacCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 550))
cDot11HtMacCapability.setRevisions(('2007-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDot11HtMacCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: cDot11HtMacCapability.setLastUpdated('2007-07-26 00:00')
if mibBuilder.loadTexts: cDot11HtMacCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11HtMacCapability.setContactInfo('            Cisco Systems\n                             Customer Service\n\n                             Postal: 170 W Tasman Drive\n                             San Jose, CA  95134\n                             USA\n  \n                             Tel: +1 800 553-NETS\n \n                             E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: cDot11HtMacCapability.setDescription('Agent capabilities for CISCO-DOT11-HT-MAC-MIB')
cDot11HtMacCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 550, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setStatus('current')
if mibBuilder.loadTexts: cDot11HtMacCapabilityV12R0410BJA.setDescription('Cisco DOT11 HT MAC MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-HT-MAC-CAPABILITY", PYSNMP_MODULE_ID=cDot11HtMacCapability, cDot11HtMacCapability=cDot11HtMacCapability, cDot11HtMacCapabilityV12R0410BJA=cDot11HtMacCapabilityV12R0410BJA)
