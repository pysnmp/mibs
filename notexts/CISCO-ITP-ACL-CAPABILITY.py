#
# PySNMP MIB module CISCO-ITP-ACL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-ACL-CAPABILITY
# Source digest sha256:2ce012eddc950ddea952c263ad4fa4572b2975b9cc71b3f1e25f259178071457
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpAclCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 214))
ciscoItpAclCapability.setRevisions(('2001-10-24 00:00',))
if mibBuilder.loadTexts: ciscoItpAclCapability.setLastUpdated('2001-10-24 00:00')
if mibBuilder.loadTexts: ciscoItpAclCapability.setOrganization('Cisco Systems, Inc.')
ciscoItpAclCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 214, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-ACL-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpAclCapability, ciscoItpAclCapability=ciscoItpAclCapability, ciscoItpAclCapabilityV12R024MB1=ciscoItpAclCapabilityV12R024MB1)
