#
# PySNMP MIB module CISCO-RMON2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-RMON2-CAPABILITY
# Source digest sha256:2e07b926242f8e0291aa432b20720d2ff44a2d1ed67cffc43096401db25eef84
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRmon2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 361))
ciscoRmon2Capability.setRevisions(('2003-10-01 00:00',))
if mibBuilder.loadTexts: ciscoRmon2Capability.setLastUpdated('2003-10-01 00:00')
if mibBuilder.loadTexts: ciscoRmon2Capability.setOrganization('Cisco Systems, Inc.')
ciscoRmon2CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 361, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON2-CAPABILITY", PYSNMP_MODULE_ID=ciscoRmon2Capability, ciscoRmon2CapCatOSV08R0101=ciscoRmon2CapCatOSV08R0101, ciscoRmon2Capability=ciscoRmon2Capability)
