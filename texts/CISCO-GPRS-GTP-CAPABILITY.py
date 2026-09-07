#
# PySNMP MIB module CISCO-GPRS-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GPRS-GTP-CAPABILITY
# Source digest sha256:46bcceb774f4554c848afd3ef90e118eee36fed9fc07dfa8118cfba038ae6365
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cgprsGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 212))
cgprsGtpCapability.setRevisions(('2001-12-20 16:00', '2001-06-05 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsGtpCapability.setRevisionsDescriptions(('Updated information for cgprsGtpDroppedPktsMonTime.\n                ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsGtpCapability.setLastUpdated('2001-12-20 16:00')
if mibBuilder.loadTexts: cgprsGtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsGtpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                                Tel: +1 800 553-NETS\n\n                        E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsGtpCapability.setDescription('Agent capabilities for CISCO-GPRS-GTP-MIB')
cgprsGtpCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R01.setDescription('Cisco GPRS GTP MIB capabilities.')
cgprsGtpCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setProductRelease('Cisco IOS 12.2(7)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R02.setDescription('Cisco GPRS GTP MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-GTP-CAPABILITY", PYSNMP_MODULE_ID=cgprsGtpCapability, cgprsGtpCapability=cgprsGtpCapability, cgprsGtpCapabilityV12R01=cgprsGtpCapabilityV12R01, cgprsGtpCapabilityV12R02=cgprsGtpCapabilityV12R02)
