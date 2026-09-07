#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HARDWARE-IP-VERIFY-CAPABILITY
# Source digest sha256:d2691d0756be44afe6a81d1c152f5df21fae33c8f3646865c1703a8e52a1f718
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHardwareIpVerifyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 623))
ciscoHardwareIpVerifyCapability.setRevisions(('2013-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setLastUpdated('2013-07-26 00:00')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setDescription('Agent capabilities for CISCO-HARDWARE-IP-VERIFY-MIB.')
chivCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 623, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus \n                        7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: chivCapNxOSV06R0104PN7k.setDescription('CISCO-HARDWARE-IP-VERIFY-MIB\n        agent capabilities.')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-CAPABILITY", PYSNMP_MODULE_ID=ciscoHardwareIpVerifyCapability, chivCapNxOSV06R0104PN7k=chivCapNxOSV06R0104PN7k, ciscoHardwareIpVerifyCapability=ciscoHardwareIpVerifyCapability)
