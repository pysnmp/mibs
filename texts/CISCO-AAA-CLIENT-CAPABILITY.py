#
# PySNMP MIB module CISCO-AAA-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AAA-CLIENT-CAPABILITY
# Source digest sha256:170861551c0aaa667760373497770910a02b3367a2660b4f2fcf5311a529f256
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoAaaClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 322))
ciscoAaaClientCapability.setRevisions(('2004-02-03 00:00', '2003-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAaaClientCapability.setRevisionsDescriptions(('Added VARIATION for cacEnable and cacPrimaryMethod.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAaaClientCapability.setLastUpdated('2004-02-03 00:00')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setDescription('The capabilities description of CISCO-AAA-CLIENT-MIB.')
ciscoAaaClientCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoAaaClientCapCatOSV08R0101.setDescription('CISCO-AAA-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoAaaClientCapability, ciscoAaaClientCapCatOSV08R0101=ciscoAaaClientCapCatOSV08R0101, ciscoAaaClientCapability=ciscoAaaClientCapability)
