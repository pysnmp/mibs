#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-RATE-LIMITER-CAPABILITY
# Source digest sha256:81c5d2f1e27b05790cf283f8a7f55feda27fb4a3a7a937f6283129f38c6ff6d4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchRateLimiterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 606))
ciscoSwitchRateLimiterCapability.setRevisions(('2011-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setLastUpdated('2011-07-27 00:00')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-RATE-LIMITER-MIB.')
ciscoRateLimiterCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 606, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoRateLimiterCapNxOSV05R0201PN7k.setDescription('CISCO-SWITCH-RATE-LIMITER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchRateLimiterCapability, ciscoRateLimiterCapNxOSV05R0201PN7k=ciscoRateLimiterCapNxOSV05R0201PN7k, ciscoSwitchRateLimiterCapability=ciscoSwitchRateLimiterCapability)
