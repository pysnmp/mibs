#
# PySNMP MIB module CISCO-ERM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ERM-CAPABILITY
# Source digest sha256:2a854eed53d5c90e0509b1994976a4edacb108d0cb1d91fad27a2513c20ce57d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoErmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 492))
ciscoErmCapability.setRevisions(('2006-03-09 00:00',))
if mibBuilder.loadTexts: ciscoErmCapability.setLastUpdated('2006-03-09 00:00')
if mibBuilder.loadTexts: ciscoErmCapability.setOrganization('Cisco Systems, Inc.')
ciscoErmCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 492, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERM-CAPABILITY", PYSNMP_MODULE_ID=ciscoErmCapability, ciscoErmCapability=ciscoErmCapability, ciscoErmCapabilityV12R02SR=ciscoErmCapabilityV12R02SR)
