#
# PySNMP MIB module CISCO-SCTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SCTP-CAPABILITY
# Source digest sha256:e500cabafa57df3f62023f0188101dabc34fc62b3851373675707c6ab0942cef
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ceSctpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 190))
ceSctpCapability.setRevisions(('2001-06-05 00:00',))
if mibBuilder.loadTexts: ceSctpCapability.setLastUpdated('2001-06-05 00:00')
if mibBuilder.loadTexts: ceSctpCapability.setOrganization('Cisco Systems, Inc.')
ceSctpCapabilityV12R021MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 190, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceSctpCapabilityV12R021MB1 = ceSctpCapabilityV12R021MB1.setProductRelease('Cisco IOS 12.2(1)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceSctpCapabilityV12R021MB1 = ceSctpCapabilityV12R021MB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-SCTP-CAPABILITY", PYSNMP_MODULE_ID=ceSctpCapability, ceSctpCapability=ceSctpCapability, ceSctpCapabilityV12R021MB1=ceSctpCapabilityV12R021MB1)
