#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 13:53:30 2024
# On host fv-az1490-927 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
enterprises, NotificationType, Unsigned32, IpAddress, Gauge32, Counter64, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Counter32, iso, snmpModules, Bits, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Unsigned32", "IpAddress", "Gauge32", "Counter64", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Counter32", "iso", "snmpModules", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks")
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
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apIPForwardMibCapabilities=apIPForwardMibCapabilities, apAgentCap2Module=apAgentCap2Module, apIpForwardCap=apIpForwardCap, PYSNMP_MODULE_ID=apAgentCap2Module)
