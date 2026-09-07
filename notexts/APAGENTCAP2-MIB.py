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
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('2022-03-24 00:00')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
apAppsStirMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2))
apStirCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap = apStirCap.setStatus('current')
apStirCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apStirCap2 = apStirCap2.setStatus('current')
apMSRPKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3))
apMSRPKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apMSRPKPIStatsCap = apMSRPKPIStatsCap.setStatus('current')
apNSEPRealmKPIMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4))
apNSEPRealmKPIStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apNSEPRealmKPIStatsCap = apNSEPRealmKPIStatsCap.setStatus('current')
apNSEPOutboundSessionMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5))
apSmgmtNSEPOutboundSession = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPOutboundSession = apSmgmtNSEPOutboundSession.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", PYSNMP_MODULE_ID=apAgentCap2Module, apAgentCap2Module=apAgentCap2Module, apAppsStirMibCapabilities=apAppsStirMibCapabilities, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apIpForwardCap=apIpForwardCap, apMSRPKPIMibCapabilities=apMSRPKPIMibCapabilities, apMSRPKPIStatsCap=apMSRPKPIStatsCap, apNSEPOutboundSessionMibCapabilities=apNSEPOutboundSessionMibCapabilities, apNSEPRealmKPIMibCapabilities=apNSEPRealmKPIMibCapabilities, apNSEPRealmKPIStatsCap=apNSEPRealmKPIStatsCap, apSmgmtNSEPOutboundSession=apSmgmtNSEPOutboundSession, apStirCap2=apStirCap2, apStirCap=apStirCap)
