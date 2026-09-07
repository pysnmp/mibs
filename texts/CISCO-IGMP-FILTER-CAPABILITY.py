#
# PySNMP MIB module CISCO-IGMP-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IGMP-FILTER-CAPABILITY
# Source digest sha256:885b4fccb0e9caf5ab12aef3a81ad1c98e31d8397d62684cbeaf7ea7c28748d8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIgmpFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 331))
ciscoIgmpFilterCapability.setRevisions(('2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setLastUpdated('2004-03-30 00:00')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIgmpFilterCapability.setDescription('The capabilities description of\n                 CISCO-IGMP-FILTER-MIB.')
cIgmpFilterCapCatOSV07R0101Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 331, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setProductRelease('Cisco CatOS 7.1(1) on Catalyst 4000/4500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIgmpFilterCapCatOSV07R0101Cat4k = cIgmpFilterCapCatOSV07R0101Cat4k.setStatus('current')
if mibBuilder.loadTexts: cIgmpFilterCapCatOSV07R0101Cat4k.setDescription('CISCO-IGMP-FILTER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IGMP-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIgmpFilterCapability, cIgmpFilterCapCatOSV07R0101Cat4k=cIgmpFilterCapCatOSV07R0101Cat4k, ciscoIgmpFilterCapability=ciscoIgmpFilterCapability)
