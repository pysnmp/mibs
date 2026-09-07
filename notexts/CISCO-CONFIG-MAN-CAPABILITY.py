#
# PySNMP MIB module CISCO-CONFIG-MAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CONFIG-MAN-CAPABILITY
# Source digest sha256:978bbe5deeae2ad0e9cc996bba1813af4d35a774390dc73f08f07bcca8b0ab0d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cconfigManCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 469))
cconfigManCapability.setRevisions(('2005-12-29 00:00',))
if mibBuilder.loadTexts: cconfigManCapability.setLastUpdated('2005-12-29 00:00')
if mibBuilder.loadTexts: cconfigManCapability.setOrganization('Cisco Systems, Inc.')
cconfigManCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 469, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-CAPABILITY", PYSNMP_MODULE_ID=cconfigManCapability, cconfigManCapability=cconfigManCapability, cconfigManCapabilityIOSXRV2R0CRS1=cconfigManCapabilityIOSXRV2R0CRS1)
