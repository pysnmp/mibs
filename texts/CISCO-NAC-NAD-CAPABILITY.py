#
# PySNMP MIB module CISCO-NAC-NAD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NAC-NAD-CAPABILITY
# Source digest sha256:a63a4ed8a901966b5358356a3cd7930c509eb834e6299d035a3cb59ad29d6af9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoNacNadCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 440))
ciscoNacNadCapability.setRevisions(('2008-11-10 00:00', '2008-07-17 00:00', '2006-12-12 00:00', '2005-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNacNadCapability.setRevisionsDescriptions(('Updated capabilities statement CISCO-NAC-NAD-MIB for 3750.', 'Added capability statement ciscoNacNadCapCatOSV08R0701.', 'Added capability statement ciscoNacNadCapCatOSV08R0601.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNacNadCapability.setLastUpdated('2008-11-10 00:00')
if mibBuilder.loadTexts: ciscoNacNadCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNacNadCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-nac@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNacNadCapability.setDescription('The capabilities description of CISCO-NAC-NAD-MIB.')
ciscoNacNadCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0501.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0601.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0701.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapV12R0246SECat3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setProductRelease('Cisco IOS 12.2(46)SE on Catalyst 3750.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapV12R0246SECat3k.setDescription('CISCO-NAC-NAD-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-NAC-NAD-CAPABILITY", PYSNMP_MODULE_ID=ciscoNacNadCapability, ciscoNacNadCapCatOSV08R0501=ciscoNacNadCapCatOSV08R0501, ciscoNacNadCapCatOSV08R0601=ciscoNacNadCapCatOSV08R0601, ciscoNacNadCapCatOSV08R0701=ciscoNacNadCapCatOSV08R0701, ciscoNacNadCapV12R0246SECat3k=ciscoNacNadCapV12R0246SECat3k, ciscoNacNadCapability=ciscoNacNadCapability)
