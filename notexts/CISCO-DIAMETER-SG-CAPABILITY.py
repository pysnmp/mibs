#
# PySNMP MIB module CISCO-DIAMETER-SG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DIAMETER-SG-CAPABILITY
# Source digest sha256:6456bd32650edfc341f6e90f33ee5a7b723ad2981459093d1b60d376b201f6b1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDiameterSGCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 518))
ciscoDiameterSGCapability.setRevisions(('2006-09-07 00:00',))
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setLastUpdated('2006-09-07 00:00')
if mibBuilder.loadTexts: ciscoDiameterSGCapability.setOrganization('Cisco Systems, Inc.')
ciscoDiameterSGCapabilityV12R0409XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 518, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGCapabilityV12R0409XG = ciscoDiameterSGCapabilityV12R0409XG.setProductRelease('Cisco IOS 12.4(9)XG.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDiameterSGCapabilityV12R0409XG = ciscoDiameterSGCapabilityV12R0409XG.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIAMETER-SG-CAPABILITY", PYSNMP_MODULE_ID=ciscoDiameterSGCapability, ciscoDiameterSGCapability=ciscoDiameterSGCapability, ciscoDiameterSGCapabilityV12R0409XG=ciscoDiameterSGCapabilityV12R0409XG)
