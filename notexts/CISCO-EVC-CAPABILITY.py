#
# PySNMP MIB module CISCO-EVC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-EVC-CAPABILITY
# Source digest sha256:1265787c6a0442f81207b485a47d29cb831c3c6f8b09717fffa1ba573356decc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEvcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 568))
ciscoEvcCapability.setRevisions(('2008-08-26 00:00',))
if mibBuilder.loadTexts: ciscoEvcCapability.setLastUpdated('2008-08-26 00:00')
if mibBuilder.loadTexts: ciscoEvcCapability.setOrganization('Cisco Systems, Inc.')
ciscoEvcCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2 SR Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02SR = ciscoEvcCapabilityV12R02SR.setStatus('current')
ciscoEvcCapabilityV12R02XO = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 568, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setProductRelease('Cisco IOS 12.2 XO Release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEvcCapabilityV12R02XO = ciscoEvcCapabilityV12R02XO.setStatus('current')
mibBuilder.exportSymbols("CISCO-EVC-CAPABILITY", PYSNMP_MODULE_ID=ciscoEvcCapability, ciscoEvcCapability=ciscoEvcCapability, ciscoEvcCapabilityV12R02SR=ciscoEvcCapabilityV12R02SR, ciscoEvcCapabilityV12R02XO=ciscoEvcCapabilityV12R02XO)
