#
# PySNMP MIB module CISCO-IVR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IVR-CAPABILITY
# Source digest sha256:1ea577d1e11d89568a6d41f49a7282823b5814e6502a6e2f95ae272ccdffd57b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIvrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 491))
ciscoIvrCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIvrCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIvrCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoIvrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIvrCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIvrCapability.setDescription('Agent capabilities for\n                 CISCO-IVR-MIB')
ciscoIvrCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 491, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIvrCapSanOSV30R1MDS9000 = ciscoIvrCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIvrCapSanOSV30R1MDS9000.setDescription('Cisco Inter Virutal Storage Area\n                     Network (Inter-VSAN) Routing\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IVR-CAPABILITY", PYSNMP_MODULE_ID=ciscoIvrCapability, ciscoIvrCapSanOSV30R1MDS9000=ciscoIvrCapSanOSV30R1MDS9000, ciscoIvrCapability=ciscoIvrCapability)
