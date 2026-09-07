#
# PySNMP MIB module CISCO-VDC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VDC-CAPABILITY
# Source digest sha256:33cde3669b4a0e0fd6d52a85b5550c5cbe7e29b04b557186349c470e3d913d99
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVdcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 621))
ciscoVdcCapability.setRevisions(('2013-07-26 00:00',))
if mibBuilder.loadTexts: ciscoVdcCapability.setLastUpdated('2013-07-26 00:00')
if mibBuilder.loadTexts: ciscoVdcCapability.setOrganization('Cisco Systems, Inc.')
ciscoVdcCapNxOSV06R0202PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 621, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVdcCapNxOSV06R0202PN7k = ciscoVdcCapNxOSV06R0202PN7k.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVdcCapNxOSV06R0202PN7k = ciscoVdcCapNxOSV06R0202PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-VDC-CAPABILITY", PYSNMP_MODULE_ID=ciscoVdcCapability, ciscoVdcCapNxOSV06R0202PN7k=ciscoVdcCapNxOSV06R0202PN7k, ciscoVdcCapability=ciscoVdcCapability)
