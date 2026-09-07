#
# PySNMP MIB module CISCO-IP-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-IF-CAPABILITY
# Source digest sha256:a6bd22bf229c846b881a5b5e66ee1433f75f0f5840cdc04b0e626e841203ec8d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 324))
ciscoIPIfCapability.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPIfCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIPIfCapability.setLastUpdated('2004-04-19 00:00')
if mibBuilder.loadTexts: ciscoIPIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPIfCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIPIfCapability.setDescription('The capabilities description of CISCO-IP-IF-MIB.')
ciscoIpIfCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 324, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpIfCapCatOSV08R0101 = ciscoIpIfCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpIfCapCatOSV08R0101 = ciscoIpIfCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoIpIfCapCatOSV08R0101.setDescription('CISCO-IP-IF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoIPIfCapability, ciscoIPIfCapability=ciscoIPIfCapability, ciscoIpIfCapCatOSV08R0101=ciscoIpIfCapCatOSV08R0101)
