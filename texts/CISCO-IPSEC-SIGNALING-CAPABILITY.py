#
# PySNMP MIB module CISCO-IPSEC-SIGNALING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IPSEC-SIGNALING-CAPABILITY
# Source digest sha256:e00b598018752702b098c41dd66a975467e1058e073107c1ebd377bde83f6ebc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPsecSigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 488))
ciscoIPsecSigCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecSigCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setDescription('Agent capabilities for\n                 CISCO-IPSEC-SIGNALING-MIB')
cIPsecSigCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 488, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIPsecSigCapSanOSV30R1MDS9000.setDescription('Cisco Generic IPsec/FC-SP Signaling\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSEC-SIGNALING-CAPABILITY", PYSNMP_MODULE_ID=ciscoIPsecSigCapability, cIPsecSigCapSanOSV30R1MDS9000=cIPsecSigCapSanOSV30R1MDS9000, ciscoIPsecSigCapability=ciscoIPsecSigCapability)
