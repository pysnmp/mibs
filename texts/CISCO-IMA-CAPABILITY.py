#
# PySNMP MIB module CISCO-IMA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IMA-CAPABILITY
# Source digest sha256:43e46c24ff568adc78c1f0841ccd7c7013c70b140e085bf9877ba72f247dd73d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
MilliSeconds, = mibBuilder.importSymbols("IMA-MIB", "MilliSeconds")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 257))
ciscoImaCapability.setRevisions(('2002-08-15 00:00', '2002-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImaCapability.setRevisionsDescriptions(('Added ciscoImaAxsmeCapabilityV3R00 for \n     Enhanced ATM Switch Service Module(AXSM-E), and\n     Enhanced Processor Switch Module 1(PXM1E) uplink.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImaCapability.setLastUpdated('2002-08-15 00:00')
if mibBuilder.loadTexts: ciscoImaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImaCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoImaCapability.setDescription('This file defines agent capabilities for IMA-MIB.')
ciscoImaAxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 257, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImaAxsmeCapabilityV3R00 = ciscoImaAxsmeCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoImaAxsmeCapabilityV3R00.setDescription('IMA-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IMA-CAPABILITY", PYSNMP_MODULE_ID=ciscoImaCapability, ciscoImaAxsmeCapabilityV3R00=ciscoImaAxsmeCapabilityV3R00, ciscoImaCapability=ciscoImaCapability)
