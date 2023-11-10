#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:26:44 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, NotificationType, Bits, enterprises, Counter64, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter32, TimeTicks, mib_2, snmpModules, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "NotificationType", "Bits", "enterprises", "Counter64", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "TimeTicks", "mib-2", "snmpModules", "ModuleIdentity")
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
mibBuilder.exportSymbols("APAGENTCAP2-MIB", PYSNMP_MODULE_ID=apAgentCap2Module, apAgentCap2Module=apAgentCap2Module, apIPForwardMibCapabilities=apIPForwardMibCapabilities, apIpForwardCap=apIpForwardCap)
