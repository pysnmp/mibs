#
# PySNMP MIB module CISCO-HC-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-HC-RMON-CAPABILITY
# Source digest sha256:d1eac32669b932f2374ce466fdfbcedecabb7913f2f9dbc875f3b66e5936010d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHcRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 358))
ciscoHcRmonCapability.setRevisions(('2003-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHcRmonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHcRmonCapability.setLastUpdated('2003-09-30 00:00')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-rmon@cisco.com')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setDescription('The capabilities description of \n                 HC-RMON-MIB.')
ciscoHcRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoHcRmonCapCatOSV08R0101.setDescription('HC-RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-HC-RMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoHcRmonCapability, ciscoHcRmonCapCatOSV08R0101=ciscoHcRmonCapCatOSV08R0101, ciscoHcRmonCapability=ciscoHcRmonCapability)
