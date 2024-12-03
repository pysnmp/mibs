#
# PySNMP MIB module APAGENTCAP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP2-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:10:01 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, Counter64, TimeTicks, ObjectIdentity, mib_2, snmpModules, Integer32, iso, Gauge32, IpAddress, Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter64", "TimeTicks", "ObjectIdentity", "mib-2", "snmpModules", "Integer32", "iso", "Gauge32", "IpAddress", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apAgentCap2Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 2))
if mibBuilder.loadTexts: apAgentCap2Module.setLastUpdated('201509200000Z')
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
mibBuilder.exportSymbols("APAGENTCAP2-MIB", apAgentCap2Module=apAgentCap2Module, apIpForwardCap=apIpForwardCap, PYSNMP_MODULE_ID=apAgentCap2Module, apIPForwardMibCapabilities=apIPForwardMibCapabilities)
