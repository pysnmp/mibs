#
# PySNMP MIB module CISCO-ITP-MSU-RATES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-MSU-RATES-CAPABILITY
# Source digest sha256:45ea4bd15967f10395d589c7373c649f7bb2f674ce9641058ea96513d21d7c80
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpMsuRatesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 537))
ciscoItpMsuRatesCapability.setRevisions(('2007-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setLastUpdated('2007-03-20 00:00')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-itp@cisco.com')
if mibBuilder.loadTexts: ciscoItpMsuRatesCapability.setDescription('Agent capabilities for the CISCO-ITP-MSU-RATES-MIB.')
ciscoItpMsuCapabilityV12R0225SW7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setProductRelease('Cisco IOS 12.2(25)SW7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0225SW7 = ciscoItpMsuCapabilityV12R0225SW7.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0225SW7.setDescription('Cisco IOS 12.2(25)SW7 CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0218IXB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setProductRelease('Cisco IOS 12.2(18)IXB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0218IXB = ciscoItpMsuCapabilityV12R0218IXB.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0218IXB.setDescription('Cisco IOS 12.2(18)IXB CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
ciscoItpMsuCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 537, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMsuCapabilityV12R0411SW = ciscoItpMsuCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMsuCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-MSU-RATES-MIB.my User\n        Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MSU-RATES-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpMsuRatesCapability, ciscoItpMsuCapabilityV12R0218IXB=ciscoItpMsuCapabilityV12R0218IXB, ciscoItpMsuCapabilityV12R0225SW7=ciscoItpMsuCapabilityV12R0225SW7, ciscoItpMsuCapabilityV12R0411SW=ciscoItpMsuCapabilityV12R0411SW, ciscoItpMsuRatesCapability=ciscoItpMsuRatesCapability)
