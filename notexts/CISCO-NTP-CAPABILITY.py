#
# PySNMP MIB module CISCO-NTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NTP-CAPABILITY
# Source digest sha256:e8c306a37b35cc90bf494c55b97a01d44f499e185875a59375f786aaa8fc96c3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoNtpCapability.setRevisions(('2006-04-05 00:00', '2005-06-22 00:00', '2003-04-08 00:00',))
if mibBuilder.loadTexts: ciscoNtpCapability.setLastUpdated('2006-04-05 00:00')
if mibBuilder.loadTexts: ciscoNtpCapability.setOrganization('Cisco Systems, Inc.')
ciscoNtpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,BPX SES Release ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setStatus('current')
ciscoNtpCapabilitySANOSV3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setProductRelease('SAN-OS 3.0(1) ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setStatus('current')
ciscoNtpCapabilityIOS124 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setProductRelease('IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setStatus('current')
mibBuilder.exportSymbols("CISCO-NTP-CAPABILITY", PYSNMP_MODULE_ID=ciscoNtpCapability, ciscoNtpCapability=ciscoNtpCapability, ciscoNtpCapabilityIOS124=ciscoNtpCapabilityIOS124, ciscoNtpCapabilitySANOSV3R0001=ciscoNtpCapabilitySANOSV3R0001, ciscoNtpCapabilityV3R00=ciscoNtpCapabilityV3R00)
