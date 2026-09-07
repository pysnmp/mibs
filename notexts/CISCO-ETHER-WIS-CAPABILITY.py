#
# PySNMP MIB module CISCO-ETHER-WIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ETHER-WIS-CAPABILITY
# Source digest sha256:4a348217d2d502fe8176dcf2febac962870126fe58d8c20bc6925c2d2eb239a4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherWisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 531))
ciscoEtherWisCapability.setRevisions(('2007-01-23 12:00',))
if mibBuilder.loadTexts: ciscoEtherWisCapability.setLastUpdated('2007-01-23 12:00')
if mibBuilder.loadTexts: ciscoEtherWisCapability.setOrganization('Cisco Systems, Inc.')
ciscoEtherWisCapabilityV120S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 531, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setProductRelease('Cisco IOS 12.0S for GSR.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHER-WIS-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherWisCapability, ciscoEtherWisCapability=ciscoEtherWisCapability, ciscoEtherWisCapabilityV120S=ciscoEtherWisCapabilityV120S)
