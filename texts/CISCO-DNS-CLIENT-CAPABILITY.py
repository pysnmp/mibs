#
# PySNMP MIB module CISCO-DNS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DNS-CLIENT-CAPABILITY
# Source digest sha256:5c0fe5845400e092f2576b1348d74923a897ee3dac9f45d974cb903d9f677a6f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDNSClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 888))
ciscoDNSClientCapability.setRevisions(('2004-11-25 00:00', '2004-08-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDNSClientCapability.setRevisionsDescriptions(("Added the agent capabilities \n                 'cDNSClientCapSanOSV20R1MDS9000' for\n                 SanOS 2.0(1) on Cisco MDS 9000 series devices.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDNSClientCapability.setLastUpdated('2004-11-25 00:00')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoDNSClientCapability.setDescription('The capabilities description of\n                CISCO-DNS-CLIENT-MIB.')
cDNSClientCapSanOSV20R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 888, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setProductRelease('Cisco SanOS 2.0(1) on Cisco MDS 9000\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDNSClientCapSanOSV20R1MDS9000 = cDNSClientCapSanOSV20R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cDNSClientCapSanOSV20R1MDS9000.setDescription('Cisco DNS Client MIB capabilities')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDNSClientCapability, cDNSClientCapSanOSV20R1MDS9000=cDNSClientCapSanOSV20R1MDS9000, ciscoDNSClientCapability=ciscoDNSClientCapability)
