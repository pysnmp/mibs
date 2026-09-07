#
# PySNMP MIB module CISCO-DOT11-WIDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-WIDS-CAPABILITY
# Source digest sha256:3fc656a123f7e0aa5f45494ee678529c80292bbbdb8ef1f3b14cee399584a48f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDot11WidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 426))
if mibBuilder.loadTexts: cDot11WidsCapability.setLastUpdated('2005-01-24 00:00')
if mibBuilder.loadTexts: cDot11WidsCapability.setOrganization('Cisco Systems, Inc.')
cDot11WidsCapabilityV12R0304JA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 426, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-WIDS-CAPABILITY", PYSNMP_MODULE_ID=cDot11WidsCapability, cDot11WidsCapability=cDot11WidsCapability, cDot11WidsCapabilityV12R0304JA=cDot11WidsCapabilityV12R0304JA)
