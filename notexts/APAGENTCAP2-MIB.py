#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.8 at Mon Feb  6 14:30:27 2023
# On host fv-az442-130 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Integer32, enterprises, Counter64, Gauge32, Counter32, mib_2, Bits, MibIdentifier, ObjectIdentity, snmpModules, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Integer32", "enterprises", "Counter64", "Gauge32", "Counter32", "mib-2", "Bits", "MibIdentifier", "ObjectIdentity", "snmpModules", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('201509200000Z')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apAgentCap2Module=apAgentCap2Module, apIpForwardCap=apIpForwardCap, PYSNMP_MODULE_ID=apAgentCap2Module, apIPForwardMibCapabilities=apIPForwardMibCapabilities)
