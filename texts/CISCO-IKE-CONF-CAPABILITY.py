#
# PySNMP MIB module CISCO-IKE-CONF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IKE-CONF-CAPABILITY
# Source digest sha256:c3e8af941b55a47a1b0ab76019faf345b59ed4eb6eb165e33d9e2adac41f3fda
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCicIkeCfgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 489))
ciscoCicIkeCfgCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setLastUpdated('2006-02-02 00:00')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setDescription('Agent capabilities for\n                 CISCO-IKE-CONFIGURATION-MIB')
cCicIkeCfgCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 489, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cCicIkeCfgCapSanOSV30R1MDS9000.setDescription('Cisco IKE Configuration \n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-CONF-CAPABILITY", PYSNMP_MODULE_ID=ciscoCicIkeCfgCapability, cCicIkeCfgCapSanOSV30R1MDS9000=cCicIkeCfgCapSanOSV30R1MDS9000, ciscoCicIkeCfgCapability=ciscoCicIkeCfgCapability)
