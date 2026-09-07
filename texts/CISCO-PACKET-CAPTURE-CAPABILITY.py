#
# PySNMP MIB module CISCO-PACKET-CAPTURE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PACKET-CAPTURE-CAPABILITY
# Source digest sha256:b6016fc4155801b1dabdde4d53d33d490d689a850c372bdbd125a2b4cbbffbbc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPacketCaptureCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 527))
ciscoPacketCaptureCapability.setRevisions(('2008-10-23 00:00', '2007-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setRevisionsDescriptions(('Added capability statement cpcCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setLastUpdated('2008-10-23 00:00')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPacketCaptureCapability.setDescription('The capabilities description of\n        CISCO-PACKET-CAPTURE-MIB.')
ciscoPacketCaptureCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on devices with\n                    Supervisor 720 or Supervisor 32 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPacketCaptureCatOSV08R0601 = ciscoPacketCaptureCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoPacketCaptureCatOSV08R0601.setDescription('CISCO-PACKET-CAPTURE-MIB capabilities.')
cpcCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 527, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpcCapV12R0233SXIPCat6K = cpcCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cpcCapV12R0233SXIPCat6K.setDescription('CISCO-PACKET-CAPTURE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PACKET-CAPTURE-CAPABILITY", PYSNMP_MODULE_ID=ciscoPacketCaptureCapability, ciscoPacketCaptureCapability=ciscoPacketCaptureCapability, ciscoPacketCaptureCatOSV08R0601=ciscoPacketCaptureCatOSV08R0601, cpcCapV12R0233SXIPCat6K=cpcCapV12R0233SXIPCat6K)
