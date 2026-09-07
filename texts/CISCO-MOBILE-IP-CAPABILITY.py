#
# PySNMP MIB module CISCO-MOBILE-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MOBILE-IP-CAPABILITY
# Source digest sha256:799b9c0338239c1d55bb58b2053e21ea2e150a2ba55c45080fae835ebb84eb74
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMobileIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 449))
ciscoMobileIPCapability.setRevisions(('2005-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMobileIPCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMobileIPCapability.setLastUpdated('2005-09-09 00:00')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setContactInfo('       Cisco Systems\n                         Customer Service\n                        \n                 Postal: 170 West Tasman Drive\n                         San Jose, CA  95134\n                         USA\n                        \n                    Tel: +1 800 553-NETS\n                        \n                 E-mail: cs-mobileip@cisco.com')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setDescription('Agent capabilities for CISCO-MOBILE-IP-MIB \n                 (MobileIP MIB).')
ciscoMobileIPCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 449, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setProductRelease('Cisco IOS 12.4(3)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoMobileIPCapabilityV12R04.setDescription('Cisco MobileIP mib capabilities')
mibBuilder.exportSymbols("CISCO-MOBILE-IP-CAPABILITY", PYSNMP_MODULE_ID=ciscoMobileIPCapability, ciscoMobileIPCapability=ciscoMobileIPCapability, ciscoMobileIPCapabilityV12R04=ciscoMobileIPCapabilityV12R04)
