#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:06:50 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Unsigned32, NotificationType, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ModuleIdentity, Integer32, TimeTicks, enterprises, mib_2, Counter32, Counter64, ObjectIdentity, snmpModules, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ModuleIdentity", "Integer32", "TimeTicks", "enterprises", "mib-2", "Counter32", "Counter64", "ObjectIdentity", "snmpModules", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('201509200000Z')
if mibBuilder.loadTexts: apAgentCap2Module.setOrganization('Oracle Communications')
apIPForwardMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1))
apIpForwardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpForwardCap = apIpForwardCap.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apIpForwardCap=apIpForwardCap, apAgentCap2Module=apAgentCap2Module, apIPForwardMibCapabilities=apIPForwardMibCapabilities, PYSNMP_MODULE_ID=apAgentCap2Module)
