#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source APAGENTCAP2-MIB
# Source digest sha256:73bd9dc5b56e71320862ed998b413f306fdd0934fecf3bdf1a0e1c6f5a7f4b50
# Produced by pysmi-2.3.0
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso, mib_2, snmpModules = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso", "mib-2", "snmpModules")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
apAgentCap2Module.setRevisions(('2020-10-26 00:00', '2021-07-06 00:00', '2022-02-16 00:00', '2022-03-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apAgentCap2Module.setRevisionsDescriptions(('Added apStirCap', 'Added apStirCap2', 'Added new capability objects apSipMSRPKPIStatsCap for MSRP statistics.', 'Added apNSEPRealmKPIStatsCap and apSmgmtNSEPOutboundSession.',))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('2022-03-24 00:00')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apAgentCap2Module.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apAgentCap2Module.setDescription(' Agent capability2 MIB for Oracle Communications Acme Packet SBCs.')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
if mibBuilder.loadTexts: apIpForwardCap.setDescription('Acme Packet Agent Capability IP-FORWARD support.')
apAppsStirMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2))
apStirCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setStatus('current')
if mibBuilder.loadTexts: apStirCap.setDescription('Acme Packet Agent Capability Stir MIB support.')
apStirCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setStatus('current')
if mibBuilder.loadTexts: apStirCap2.setDescription('Acme Packet Agent Capability Stir Agent MIB support.')
apMSRPKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3))
apMSRPKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setStatus('current')
if mibBuilder.loadTexts: apMSRPKPIStatsCap.setDescription('Acme Packet Agent Capability for MSRP KPI statistics  MIB.')
apNSEPRealmKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4))
apNSEPRealmKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setStatus('current')
if mibBuilder.loadTexts: apNSEPRealmKPIStatsCap.setDescription('Acme Packet Agent Capability for NSEP Realm\n                                KPI statistics MIB.')
apNSEPOutboundSessionMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5))
apSmgmtNSEPOutboundSession = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNSEPOutboundSession.setDescription('Acme Packet Agent Capability for NSEP\n                                Outbound KPI statistics MIB.')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", PYSNMP_MODULE_ID=apAgentCap2Module, apAgentCap2Module=apAgentCap2Module, apAppsStirMibCapabilities=apAppsStirMibCapabilities, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apIpForwardCap=apIpForwardCap, apMSRPKPIMibCapabilities=apMSRPKPIMibCapabilities, apMSRPKPIStatsCap=apMSRPKPIStatsCap, apNSEPOutboundSessionMibCapabilities=apNSEPOutboundSessionMibCapabilities, apNSEPRealmKPIMibCapabilities=apNSEPRealmKPIMibCapabilities, apNSEPRealmKPIStatsCap=apNSEPRealmKPIStatsCap, apSmgmtNSEPOutboundSession=apSmgmtNSEPOutboundSession, apStirCap2=apStirCap2, apStirCap=apStirCap)
