#
# PySNMP MIB module APAGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan 13 14:03:19 2023
# On host fv-az178-827 platform Linux version 5.15.0-1030-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, ModuleIdentity, snmpModules, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Gauge32, mib_2, iso, Integer32, enterprises, TimeTicks, IpAddress, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "snmpModules", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Gauge32", "mib-2", "iso", "Integer32", "enterprises", "TimeTicks", "IpAddress", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apAgentCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 1))
apAgentCapModule.setRevisions(('2001-08-01 00:00', '2004-11-18 00:00', '2006-05-01 00:00', '2007-05-07 00:00', '1920-12-15 00:00', '2012-03-07 00:00', '2012-07-16 00:00', '2014-02-26 00:00', '2014-06-20 00:00', '2014-06-26 00:00', '2017-02-09 00:00', '2017-10-18 00:00', '2017-11-24 00:00', '2017-12-14 00:00', '2018-04-10 00:00', '2018-04-27 00:00', '2019-04-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apAgentCapModule.setRevisionsDescriptions((' The initial version.', ' Add agent capacity for release 2.0. ', ' Add agent capability for SD9000 series', ' Add agent capability for SD9000 series', ' Add agent capability for ap-dd.mib', ' Add agent capability for ap-apps.mib', 'Updated contact information.', 'Added new capability object apIfMibVHCCap.', ' Added new capability object, apSmgmtCPULoadAvgCap', 'Updated Organization and Contact info.', 'Updated capabiltiy information for diameter authentication notification', ' Added new capability object apSecurityTacacsDownLocalAuthCap', 'Added new capability object apSipVoLTECountersCap for SRVCC,\n                         Diameter Rx Policy Server, IKE SA, IMS-AKA SA and SRTP SA,\n                         licensed codec session stats, TCU Load Statistics,\n                         and licensed codec capaciites.', 'Added new capability objects apSmgmtSipMethodStatsCap, apSipCallInformationCap', 'Added new capability object apSipSRVCCPreAlertingStatsCap for SRVCC Pre-Alerting stats', 'Added new capability objects apSipRegEvtSubscriptionCap for SIP Reg Event Subscriptions.', 'Added new capability objects apSipMSRPStatsCap for MSRP statistics.',))
if mibBuilder.loadTexts: apAgentCapModule.setLastUpdated('201904240000Z')
if mibBuilder.loadTexts: apAgentCapModule.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apAgentCapModule.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apAgentCapModule.setDescription(' Agent capability MIB for Oracle Communications Acme Packet SBCs.')
apSnmpMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1))
apIfMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2))
apIPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3))
apTCPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4))
apUDPMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5))
apEntityCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6))
apSlogMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7))
apSmgmtMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8))
apEnvMonitorMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9))
apSwinventoryMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10))
apLicenseMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11))
apAmiMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12))
apCodecMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13))
apSecurityMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14))
apH323MibCapabilites = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15))
apSLBMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16))
apDiamMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17))
apDDMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18))
apDNSALGMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19))
apAppsMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20))
apSipMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21))
apUsbcSysMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22))
apRadiusMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23))
apCoreLbMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 24))
apUsbcSysDPDKMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 25))
apUsbcSysScalingMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 26))
apUsbcSysThreadMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 27))
apUsbcSysThreadMibCapabilities2 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 28))
apUsbcSysSmMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 29))
apUsbcSysThreadMibCapabilities3 = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 30))
apAclDropMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 31))
apCsvConfigMibCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 2, 1, 32))
apSnmpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpCap = apSnmpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpCap = apSnmpCap.setStatus('current')
if mibBuilder.loadTexts: apSnmpCap.setDescription('Acme Packet Agent Capability for SNMPv2-MIB.')
apSnmpv3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setStatus('current')
if mibBuilder.loadTexts: apSnmpv3Cap.setDescription('Acme Packet Agent Capability for SNMPv3 MIBs.')
apInterfacesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setStatus('current')
if mibBuilder.loadTexts: apInterfacesCap.setDescription('Acme Packet Agent Capability for interfaces.')
apIfMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setStatus('current')
if mibBuilder.loadTexts: apIfMibCap.setDescription('Acme Packet Agent Capability IfMib support.')
apIfMibHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setStatus('current')
if mibBuilder.loadTexts: apIfMibHCCap.setDescription('Acme Packet Agent Capability for interfaces.')
apIfMibVHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibVHCCap = apIfMibVHCCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibVHCCap = apIfMibVHCCap.setStatus('current')
if mibBuilder.loadTexts: apIfMibVHCCap.setDescription('Acme Packet Agent Capability for interfaces.')
apIpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setStatus('current')
if mibBuilder.loadTexts: apIpCap.setDescription('Acme Packet Agent Capability IP support.')
apIpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap2 = apIpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap2 = apIpCap2.setStatus('current')
if mibBuilder.loadTexts: apIpCap2.setDescription('Acme Packet Agent Capability IP support.')
apIcmpStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIcmpStatsCap = apIcmpStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIcmpStatsCap = apIcmpStatsCap.setStatus('current')
if mibBuilder.loadTexts: apIcmpStatsCap.setDescription('Acme Packet Agent Capability IP-FORWARD support.')
apTcpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setStatus('current')
if mibBuilder.loadTexts: apTcpCap.setDescription('Acme Packet Agent Capability TCP support.')
apTcpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap2 = apTcpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap2 = apTcpCap2.setStatus('current')
if mibBuilder.loadTexts: apTcpCap2.setDescription('Acme Packet Agent Capability TCP support.')
apUdpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setStatus('current')
if mibBuilder.loadTexts: apUdpCap.setDescription('Acme Packet Agent Capability UDP support.')
apUdpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap2 = apUdpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap2 = apUdpCap2.setStatus('current')
if mibBuilder.loadTexts: apUdpCap2.setDescription('Acme Packet Agent Capability UDP support.')
apEntityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setProductRelease('Acme Packet for Relase 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setStatus('current')
if mibBuilder.loadTexts: apEntityCap.setDescription('Acme Packet Agent Capability for entity MIB.')
apSyslogCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setStatus('current')
if mibBuilder.loadTexts: apSyslogCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 syslog MIB.')
apCsvConfigSaveCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCsvConfigSaveCap = apCsvConfigSaveCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCsvConfigSaveCap = apCsvConfigSaveCap.setStatus('current')
if mibBuilder.loadTexts: apCsvConfigSaveCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 CSV Config mamgerment MIB.')
apSmgmtCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap2.setDescription('Acme Packet Agent Capability for enterprise \n                                 system management MIB.')
apSmgmtCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap3.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap4.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap5.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCap6.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtNSEPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNSEPCap.setDescription('Acme Packet Agent Capability for enterprise \n                         system mamgerment MIB.')
apSmgmtCtrlStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCtrlStatsCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtLDAPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtLDAPCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtHDRCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtHDRCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtMediaSuperCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtMediaSuperCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtH248Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH248Cap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtRFactorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRFactorCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtSipRejectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSipRejectCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDOSNotifyCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtRegNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegNotifyCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtNTPNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtNTPNotifyCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtCollectorPushSuccessNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCollectorPushSuccessNotifyCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtExtSigRealmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtExtSigRealmCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtClockNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtClockNotifyCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtRegistrationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRegistrationCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap2.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegCacheLimCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtShortSessionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtShortSessionCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSystemManagementGatewaySynchronizedMonitorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setStatus('current')
if mibBuilder.loadTexts: apSystemManagementGatewaySynchronizedMonitorCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRegistrationCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRegistrationCap3.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtCallRecordingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCallRecordingCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtH323AdditionsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH323AdditionsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtENUMCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtENUMCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtExtSipCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtExtSipCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRealmIcmpFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmIcmpFailureCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtTrapTableObjectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtTrapTableObjectCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtCDRPushReceiverFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCDRPushReceiverFailureCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRealmStatsQoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmStatsQoSCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtInetAddrDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtInetAddrDOSNotifyCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system mamgerment MIB.')
apSmgmtApplicationCPUUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtApplicationCPUUsageCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtRegistrationCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setStatus('obsolete')
if mibBuilder.loadTexts: apSmgmtRegistrationCapacityCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtRejectedMessagesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRejectedMessagesCap.setDescription('Acme Packet Agent Capability for enterprise \n                                 system management MIB.')
apSmgmtEndPtDemotionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtEndPtDemotionCap.setDescription('Acme Packet Agent Capability for enterprise\n\t                         system management MIB.')
apSmgmtAdminCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtAdminCap.setDescription('Acme Packet Agent Capability for enterprise\n\t                         system management MIB.')
apSmgmtLPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtLPCap.setDescription('Acme Packet Agent Capability for enterprise\n\t                         system management MIB.')
apSmgmtPhyUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtPhyUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtStorageSpaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtStorageSpaceCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtCtrlStatsCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCtrlStatsCap2.setDescription('Acme Packet Agent Capability for enterprise \n                                system mamgerment MIB.')
apSmgmtDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDatabaseRegCap.setDescription('Acme Packet Agent Capability for enterprise \n                                system mamgerment MIB.')
apSmgmtCallsRejectedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtCallsRejectedCap.setDescription('Acme Packet Agent Capability for enterprise \n                                system mamgerment MIB.')
apSmgmtSipInterfaceRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSipInterfaceRegCacheLimCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtRealmRegCacheSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtRealmRegCacheSummaryCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtSubscriptionSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSubscriptionSummaryCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtH248PortMapUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtH248PortMapUsageCap.setDescription('Acme Packet Agent Capability for enterprise\n\t                           system management MIB.')
apSmgmtDOSNotifyTrustedtoUntrustedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtDOSNotifyTrustedtoUntrustedCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSysMgmtETCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSysMgmtETCUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtXCodeEVRCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 53))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCUtilCap = apSmgmtXCodeEVRCUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCUtilCap = apSmgmtXCodeEVRCUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeEVRCUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtXCodeG729UtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 54))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeG729UtilCap = apSmgmtXCodeG729UtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeG729UtilCap = apSmgmtXCodeG729UtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeG729UtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtCPULoadAvgCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 55))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCPULoadAvgCap = apSmgmtCPULoadAvgCap.setProductRelease('Acme-Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCPULoadAvgCap = apSmgmtCPULoadAvgCap.setStatus('obsolete')
if mibBuilder.loadTexts: apSmgmtCPULoadAvgCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtXCodeOpusUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 56))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeOpusUtilCap = apSmgmtXCodeOpusUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeOpusUtilCap = apSmgmtXCodeOpusUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeOpusUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtXCodeSILKUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 57))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeSILKUtilCap = apSmgmtXCodeSILKUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeSILKUtilCap = apSmgmtXCodeSILKUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeSILKUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system mamgerment MIB.')
apSmgmtXCodeEVRCNWUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 58))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCNWUtilCap = apSmgmtXCodeEVRCNWUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCNWUtilCap = apSmgmtXCodeEVRCNWUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeEVRCNWUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apSmgmtXCodeEVSUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 59))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVSUtilCap = apSmgmtXCodeEVSUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVSUtilCap = apSmgmtXCodeEVSUtilCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtXCodeEVSUtilCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 system management MIB.')
apEnvMonCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tEnvironmental Monitor MIB.')
apEnvMonCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap2.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tEnvironmental Monitor MIB.')
apEnvMonPortChangeCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setStatus('current')
if mibBuilder.loadTexts: apEnvMonPortChangeCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tEnvironmental Monitor MIB.')
apEnvMonCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCap4.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tEnvironmental Monitor MIB.')
apEnvMonCardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardCap = apEnvMonCardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardCap = apEnvMonCardCap.setStatus('current')
if mibBuilder.loadTexts: apEnvMonCardCap.setDescription('Acme Packet Agent Capability for apEnvMonCardOnlyGroup \n\t\t\t\tEnvironmental Monitor MIB.')
apSwInventoryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setStatus('current')
if mibBuilder.loadTexts: apSwInventoryCap.setDescription('Acme Packet Agent Capability for\n                                 enterprise software inventory MIB.')
apLicenseCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tLicense MIB.')
apLicenseDBRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDBRegCap = apLicenseDBRegCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDBRegCap = apLicenseDBRegCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseDBRegCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tLicense MIB.')
apLicenseExpirationWarnCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setStatus('current')
if mibBuilder.loadTexts: apLicenseExpirationWarnCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tLicense MIB.')
apAmiCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setStatus('current')
if mibBuilder.loadTexts: apAmiCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tAMI MIB.')
apCodecRealmCodecCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB.')
apCodecMediaProcessingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setStatus('current')
if mibBuilder.loadTexts: apCodecMediaProcessingCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB.')
apCodecRealmCodecCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap2.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecTranscodingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setStatus('current')
if mibBuilder.loadTexts: apCodecTranscodingStatsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap3 = apCodecRealmCodecCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap3 = apCodecRealmCodecCap3.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap3.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap4 = apCodecRealmCodecCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap4 = apCodecRealmCodecCap4.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap4.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap5 = apCodecRealmCodecCap5.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap5 = apCodecRealmCodecCap5.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap5.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap6 = apCodecRealmCodecCap6.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap6 = apCodecRealmCodecCap6.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap6.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap7 = apCodecRealmCodecCap7.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap7 = apCodecRealmCodecCap7.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap7.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap8 = apCodecRealmCodecCap8.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap8 = apCodecRealmCodecCap8.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap8.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap9 = apCodecRealmCodecCap9.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap9 = apCodecRealmCodecCap9.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap9.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apCodecRealmCodecCap10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap10 = apCodecRealmCodecCap10.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap10 = apCodecRealmCodecCap10.setStatus('current')
if mibBuilder.loadTexts: apCodecRealmCodecCap10.setDescription('Acme Packet Agent Capability for enterprise\n                                 codec MIB. (Additional Codecs)')
apSecurityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tLicense MIB.')
apSecurityIPsecTunnelsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIPsecTunnelsCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityIkeInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityTacacsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTacacsCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityCertStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCertStatusCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityIkeDDoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeDDoSCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityCertificateCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityCertificateCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityGtpStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityGtpStatusCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityIkeInterfaceInfoCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceInfoCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityTacacsNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTacacsNotifCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityInetCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tLicense MIB.')
apSecurityIkeDDoSInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeDDoSInetCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityIkeIfcBlAuthIDErrorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeIfcBlAuthIDErrorCap = apSecurityIkeIfcBlAuthIDErrorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeIfcBlAuthIDErrorCap = apSecurityIkeIfcBlAuthIDErrorCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeIfcBlAuthIDErrorCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityDhcpInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityDhcpInterfaceCap = apSecurityDhcpInterfaceCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityDhcpInterfaceCap = apSecurityDhcpInterfaceCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityDhcpInterfaceCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityGtpProfileCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpProfileCap = apSecurityGtpProfileCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpProfileCap = apSecurityGtpProfileCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityGtpProfileCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityRekeyOnSNoverflowCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityRekeyOnSNoverflowCap = apSecurityRekeyOnSNoverflowCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityRekeyOnSNoverflowCap = apSecurityRekeyOnSNoverflowCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityRekeyOnSNoverflowCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB.')
apSecurityIkeInterfaceDpdStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceDpdStatsCap = apSecurityIkeInterfaceDpdStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceDpdStatsCap = apSecurityIkeInterfaceDpdStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceDpdStatsCap.setDescription('Acme Packet Agent Capability for enterprise \n                                Security MIB.')
apSecurityIkeInterfaceEapOnlyAuthStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapOnlyAuthStatsCap = apSecurityIkeInterfaceEapOnlyAuthStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapOnlyAuthStatsCap = apSecurityIkeInterfaceEapOnlyAuthStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceEapOnlyAuthStatsCap.setDescription('Acme Packet Agent Capability for enterprise \n                                Security MIB.')
apSecurityTscfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfCap = apSecurityTscfCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfCap = apSecurityTscfCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTscfCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityIkeInterfaceEapMethodsStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapMethodsStatsCap = apSecurityIkeInterfaceEapMethodsStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapMethodsStatsCap = apSecurityIkeInterfaceEapMethodsStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceEapMethodsStatsCap.setDescription('Acme Packet Agent Capability for enterprise \n                                Security MIB.')
apSecurityIkeInterfaceIkeErrorStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceIkeErrorStatsCap = apSecurityIkeInterfaceIkeErrorStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceIkeErrorStatsCap = apSecurityIkeInterfaceIkeErrorStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceIkeErrorStatsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityIkeInterfaceMobikeStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceMobikeStatsCap = apSecurityIkeInterfaceMobikeStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceMobikeStatsCap = apSecurityIkeInterfaceMobikeStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterfaceMobikeStatsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityTscfTimeoutCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfTimeoutCap = apSecurityTscfTimeoutCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfTimeoutCap = apSecurityTscfTimeoutCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTscfTimeoutCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityIkeInterface3GPPAuthErrorsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterface3GPPAuthErrorsCap = apSecurityIkeInterface3GPPAuthErrorsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterface3GPPAuthErrorsCap = apSecurityIkeInterface3GPPAuthErrorsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityIkeInterface3GPPAuthErrorsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityGtpCaviumStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpCaviumStatsCap = apSecurityGtpCaviumStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpCaviumStatsCap = apSecurityGtpCaviumStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityGtpCaviumStatsCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityTacacsDownLocalAuthCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsDownLocalAuthCap = apSecurityTacacsDownLocalAuthCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsDownLocalAuthCap = apSecurityTacacsDownLocalAuthCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTacacsDownLocalAuthCap.setDescription('Acme Packet Agent Capability for enterprise\n                                Security MIB.')
apSecurityTlsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTlsCap = apSecurityTlsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTlsCap = apSecurityTlsCap.setStatus('current')
if mibBuilder.loadTexts: apSecurityTlsCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB for TLS.')
apSecuritySrtpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecuritySrtpCap = apSecuritySrtpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecuritySrtpCap = apSecuritySrtpCap.setStatus('current')
if mibBuilder.loadTexts: apSecuritySrtpCap.setDescription('Acme Packet Agent Capability for enterprise \n\t\t\t\tSecurity MIB for SRTP.')
apH323StackCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setStatus('current')
if mibBuilder.loadTexts: apH323StackCap.setDescription('Acme Packet Agent Capability for H323 stack.')
apSLBEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setStatus('current')
if mibBuilder.loadTexts: apSLBEndpointCapacityCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 SLB MIB.')
apSLBUntrustedEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setStatus('current')
if mibBuilder.loadTexts: apSLBUntrustedEndpointCapacityCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 SLB MIB.')
apDiamMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setStatus('current')
if mibBuilder.loadTexts: apDiamMibCap.setDescription('Acme Packet Capability for AP-DIAMETER-MIB.')
apDiamNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamNotifCap = apDiamNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamNotifCap = apDiamNotifCap.setStatus('current')
if mibBuilder.loadTexts: apDiamNotifCap.setDescription('Acme Packet Capability for AP-DIAMETER-MIB.')
apDiamClfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamClfCap = apDiamClfCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamClfCap = apDiamClfCap.setStatus('current')
if mibBuilder.loadTexts: apDiamClfCap.setDescription('Acme Packet Capability for AP-DIAMETER-MIB.')
apDiamIntfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamIntfCap = apDiamIntfCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamIntfCap = apDiamIntfCap.setStatus('current')
if mibBuilder.loadTexts: apDiamIntfCap.setDescription('Acme Packet Capability for AP-DIAMETER-MIB.')
apDiamAuthCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthCap = apDiamAuthCap.setProductRelease('Oracle Communications Acme MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthCap = apDiamAuthCap.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthCap.setDescription('Acme Packet Capability for AP-DIAMETERAUTH-MIB.')
apDiamAuthNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthNotifyCap = apDiamAuthNotifyCap.setProductRelease('Oracle Communications Acme MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthNotifyCap = apDiamAuthNotifyCap.setStatus('current')
if mibBuilder.loadTexts: apDiamAuthNotifyCap.setDescription('Acme Packet Capability for AP-DIAMETERAUTH-MIB.')
apDDStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroupCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDDNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDDNotifGroupCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDDStatsGroup2Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroup2Cap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDDStatsGroup3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroup3Cap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDDSCTPNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDSCTPNotifGroupCap = apDDSCTPNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDSCTPNotifGroupCap = apDDSCTPNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDDSCTPNotifGroupCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDDStatsGroup4Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup4Cap = apDDStatsGroup4Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup4Cap = apDDStatsGroup4Cap.setStatus('current')
if mibBuilder.loadTexts: apDDStatsGroup4Cap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DD MIB.')
apDNSALGStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setProductRelease('Acme Packet DNS ALG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDNSALGStatsGroupCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DNSALG MIB.')
apDNSALGNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setProductRelease('Acme Packet PEC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDNSALGNotifGroupCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 DNSALG MIB.')
apDNSALGRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGRateGroupCap = apDNSALGRateGroupCap.setProductRelease('Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGRateGroupCap = apDNSALGRateGroupCap.setStatus('current')
if mibBuilder.loadTexts: apDNSALGRateGroupCap.setDescription('Acme Packet Agent Capability stats for\n                                 DNSALG MIB.')
apAppsENUMStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsENUMStatusGroupCap.setDescription('Acme Packet Agent Capability for APPS\n                                 ENUM server status group. ')
apAppsDNSStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsDNSStatusGroupCap.setDescription('Acme Packet Agent Capability for APPS\n                                 DNS server status group. ')
apAppsENUMSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsENUMSvrNotifGroupCap.setDescription('Acme Packet Agent Capability for APPS \n                                 ENUM Server Notif group.')
apAppsDNSSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsDNSSvrNotifGroupCap.setDescription('Acme Packet Agent Capability for APPS \n                                 DNS Server Notif group.')
apAppsENUMRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMRateGroupCap = apAppsENUMRateGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMRateGroupCap = apAppsENUMRateGroupCap.setStatus('current')
if mibBuilder.loadTexts: apAppsENUMRateGroupCap.setDescription('Acme Packet Agent Capability for APPS\n                                 ENUM server status group. ')
apCommMonitorNotificationGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCommMonitorNotificationGroupCap = apCommMonitorNotificationGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCommMonitorNotificationGroupCap = apCommMonitorNotificationGroupCap.setStatus('current')
if mibBuilder.loadTexts: apCommMonitorNotificationGroupCap.setDescription('Report an alarm when disconnect between \n                                 SBC and CommMonitor.')
apSipSecInterfaceRegNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipSecInterfaceRegNotifGroupCap.setDescription('Acme Packet Agent Capability for SIP\n                                 Secondary SIP Interface Registrations\n                                 Notif group.')
apSipSecInterfaceRegObjectsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipSecInterfaceRegObjectsGroupCap.setDescription('Acme Packet Agent Capability for SIP\n                                 Secondary SIP Interface Registrations\n                                 Object group.')
apSipSurvivabilityNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSurvivabilityNotificationsGroupCap = apSipSurvivabilityNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSurvivabilityNotificationsGroupCap = apSipSurvivabilityNotificationsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipSurvivabilityNotificationsGroupCap.setDescription('Acme Packet Agent Capability for SIP\n                                 Interface Survivability Mode\n                                 Notif group.')
apSipRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRateGroupCap = apSipRateGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRateGroupCap = apSipRateGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipRateGroupCap.setDescription('Acme Packet Agent Capability for SIP\n                                 Rate Stats group.')
apSipCACStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsGroupCap = apSipCACStatsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsGroupCap = apSipCACStatsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipCACStatsGroupCap.setDescription('A collection of objects providing\n                                 sip rate stats.')
apSipCACNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACNotificationsGroupCap = apSipCACNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACNotificationsGroupCap = apSipCACNotificationsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipCACNotificationsGroupCap.setDescription('Traps to montitor SIP CAC \n                                 utilizaton.')
apSipCACStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsCap = apSipCACStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsCap = apSipCACStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSipCACStatsCap.setDescription('A collection of objects providing\n                                 sip rate stats.')
apSipRecNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRecNotificationsGroupCap = apSipRecNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRecNotificationsGroupCap = apSipRecNotificationsGroupCap.setStatus('current')
if mibBuilder.loadTexts: apSipRecNotificationsGroupCap.setDescription('Traps to monitor SIPREC dialogs and sessions.')
apSipAudioVideoCallsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipAudioVideoCallsCap = apSipAudioVideoCallsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipAudioVideoCallsCap = apSipAudioVideoCallsCap.setStatus('current')
if mibBuilder.loadTexts: apSipAudioVideoCallsCap.setDescription('Acme Packet Agent Capability for SIP Audio \n                                Video Call counters MIB.')
apSipVoLTECountersCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipVoLTECountersCap = apSipVoLTECountersCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipVoLTECountersCap = apSipVoLTECountersCap.setStatus('current')
if mibBuilder.loadTexts: apSipVoLTECountersCap.setDescription('Acme Packet Agent Capability for SIP\n                                   VoLTE Counters MIB')
apSipCallInformationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCallInformationCap = apSipCallInformationCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCallInformationCap = apSipCallInformationCap.setStatus('current')
if mibBuilder.loadTexts: apSipCallInformationCap.setDescription('Acme Packet Agent Capability for SIP call drop and \n                                 call duuration information MIB.')
apSmgmtSipMethodStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipMethodStatsCap = apSmgmtSipMethodStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipMethodStatsCap = apSmgmtSipMethodStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSmgmtSipMethodStatsCap.setDescription('Acme Packet Agent Capability for system wide SIP method stats\n                                 system mamgerment MIB.')
apSipSRVCCPreAlertingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSRVCCPreAlertingStatsCap = apSipSRVCCPreAlertingStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSRVCCPreAlertingStatsCap = apSipSRVCCPreAlertingStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSipSRVCCPreAlertingStatsCap.setDescription('Acme Packet Agent Capability for SRVCC Pre-Alerting\n                                 stats MIB.')
apSipRegEvtSubscriptionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRegEvtSubscriptionCap = apSipRegEvtSubscriptionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRegEvtSubscriptionCap = apSipRegEvtSubscriptionCap.setStatus('current')
if mibBuilder.loadTexts: apSipRegEvtSubscriptionCap.setDescription('Acme Packet Agent Capability for SIP\n                                   Reg Event Subscrption Counters MIB')
apSipMSRPStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipMSRPStatsCap = apSipMSRPStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipMSRPStatsCap = apSipMSRPStatsCap.setStatus('current')
if mibBuilder.loadTexts: apSipMSRPStatsCap.setDescription('Acme Packet Agent Capability for MSRP statistics  MIB.')
apUsbcSysCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysCap.setDescription('Acme Packet Agent Capability for USBC\n                                 system mamgerment MIB.')
apUsbcSysDPDKCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysDPDKCap = apUsbcSysDPDKCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysDPDKCap = apUsbcSysDPDKCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysDPDKCap.setDescription('Acme Packet Agent Capability for USBC\n                                 DPDK system management MIB.')
apUsbcSysScalingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysScalingCap = apUsbcSysScalingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysScalingCap = apUsbcSysScalingCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysScalingCap.setDescription('Acme Packet Agent Capability for USBC\n                                 Scaling system management MIB.')
apUsbcSysThreadCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap = apUsbcSysThreadCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap = apUsbcSysThreadCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysThreadCap.setDescription('Acme Packet Agent Capability for USBC\n                                 Thread Usage and Event monitoring MIB.')
apUsbcSysFdCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysFdCap = apUsbcSysFdCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysFdCap = apUsbcSysFdCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysFdCap.setDescription('Acme Packet Agent Capability for USBC\n                                 system FD Count.')
apUsbcSysThreadCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap2 = apUsbcSysThreadCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap2 = apUsbcSysThreadCap2.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysThreadCap2.setDescription('Acme Packet Agent Capability for USBC\n                                 Thread Usage and Event monitoring MIB.')
apUsbcSysThreadCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap3 = apUsbcSysThreadCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap3 = apUsbcSysThreadCap3.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysThreadCap3.setDescription('Acme Packet Agent Capability for USBC\n                                 Thread Deadlock monitoring MIB.')
apUsbcSysThreadCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 27, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap4 = apUsbcSysThreadCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap4 = apUsbcSysThreadCap4.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysThreadCap4.setDescription('Acme Packet Agent Capability for USBC\n                                 Thread Usage and Event monitoring MIB.')
apUsbcSysSmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysSmCap = apUsbcSysSmCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysSmCap = apUsbcSysSmCap.setStatus('current')
if mibBuilder.loadTexts: apUsbcSysSmCap.setDescription('Acme Packet Agent Capability for USBC\n                                 SM monitoring MIB.')
apRadiusMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setStatus('current')
if mibBuilder.loadTexts: apRadiusMibCap.setDescription('Acme Packet Capability for AP-RADIUS-MIB.')
apRadiusServerStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setStatus('current')
if mibBuilder.loadTexts: apRadiusServerStatsCap.setDescription('Acme Packet Capability for AP-RADIUS-MIB.')
apCoreLBMemberStatusNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 24, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCoreLBMemberStatusNotifCap = apCoreLBMemberStatusNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCoreLBMemberStatusNotifCap = apCoreLBMemberStatusNotifCap.setStatus('current')
if mibBuilder.loadTexts: apCoreLBMemberStatusNotifCap.setDescription('Acme Packet Agent Capability for enterprise\n                                 CORELB MIB.')
apAclDropCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 31, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAclDropCap = apAclDropCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAclDropCap = apAclDropCap.setStatus('current')
if mibBuilder.loadTexts: apAclDropCap.setDescription('Acme Packet Agent Capability for ACL\n                                 drop monitoring MIB.')
mibBuilder.exportSymbols("APAGENTCAP-MIB", apDiamIntfCap=apDiamIntfCap, apSecurityGtpCaviumStatsCap=apSecurityGtpCaviumStatsCap, apDiamMibCap=apDiamMibCap, apAgentCapModule=apAgentCapModule, apSipCACStatsGroupCap=apSipCACStatsGroupCap, apDDNotifGroupCap=apDDNotifGroupCap, apH323StackCap=apH323StackCap, apSipCACNotificationsGroupCap=apSipCACNotificationsGroupCap, apSmgmtShortSessionCap=apSmgmtShortSessionCap, apSmgmtDatabaseRegCap=apSmgmtDatabaseRegCap, apSmgmtCap4=apSmgmtCap4, apSmgmtRealmIcmpFailureCap=apSmgmtRealmIcmpFailureCap, apSecurityDhcpInterfaceCap=apSecurityDhcpInterfaceCap, apUsbcSysFdCap=apUsbcSysFdCap, apH323MibCapabilites=apH323MibCapabilites, apAppsMibCapabilities=apAppsMibCapabilities, apSecurityTscfTimeoutCap=apSecurityTscfTimeoutCap, apIfMibVHCCap=apIfMibVHCCap, apSlogMibCapabilities=apSlogMibCapabilities, apSecurityIkeInterfaceCap=apSecurityIkeInterfaceCap, apSipCACStatsCap=apSipCACStatsCap, apRadiusMibCapabilities=apRadiusMibCapabilities, apSmgmtH248Cap=apSmgmtH248Cap, apSecurityCertStatusCap=apSecurityCertStatusCap, apIpCap2=apIpCap2, apSmgmtMibCapabilities=apSmgmtMibCapabilities, apCsvConfigMibCapabilities=apCsvConfigMibCapabilities, apUDPMibCapabilities=apUDPMibCapabilities, apSmgmtCPULoadAvgCap=apSmgmtCPULoadAvgCap, apSmgmtCallRecordingCap=apSmgmtCallRecordingCap, apLicenseCap=apLicenseCap, apCodecTranscodingStatsCap=apCodecTranscodingStatsCap, apUsbcSysThreadMibCapabilities2=apUsbcSysThreadMibCapabilities2, apAppsENUMStatusGroupCap=apAppsENUMStatusGroupCap, apDNSALGMibCapabilities=apDNSALGMibCapabilities, apDNSALGNotifGroupCap=apDNSALGNotifGroupCap, apSmgmtRFactorCap=apSmgmtRFactorCap, apSecuritySrtpCap=apSecuritySrtpCap, apSecurityIkeInterfaceDpdStatsCap=apSecurityIkeInterfaceDpdStatsCap, apSecurityIkeInterfaceInfoCap=apSecurityIkeInterfaceInfoCap, apUsbcSysThreadCap3=apUsbcSysThreadCap3, apSmgmtXCodeEVRCNWUtilCap=apSmgmtXCodeEVRCNWUtilCap, apSmgmtNSEPCap=apSmgmtNSEPCap, apEnvMonCap2=apEnvMonCap2, apDDStatsGroup4Cap=apDDStatsGroup4Cap, apSmgmtRealmStatsQoSCap=apSmgmtRealmStatsQoSCap, apDiamNotifCap=apDiamNotifCap, apLicenseDBRegCap=apLicenseDBRegCap, apCodecRealmCodecCap=apCodecRealmCodecCap, apDiamClfCap=apDiamClfCap, apSipRecNotificationsGroupCap=apSipRecNotificationsGroupCap, apCodecMibCapabilities=apCodecMibCapabilities, apCodecRealmCodecCap2=apCodecRealmCodecCap2, apUsbcSysThreadCap=apUsbcSysThreadCap, apSmgmtAdminCap=apSmgmtAdminCap, apSipCallInformationCap=apSipCallInformationCap, apSecurityCap=apSecurityCap, apSmgmtPhyUtilCap=apSmgmtPhyUtilCap, apSmgmtRegCacheLimCap=apSmgmtRegCacheLimCap, apEnvMonCap=apEnvMonCap, apUsbcSysMibCapabilities=apUsbcSysMibCapabilities, apDiamAuthNotifyCap=apDiamAuthNotifyCap, apIPMibCapabilities=apIPMibCapabilities, apSmgmtRegNotifyCap=apSmgmtRegNotifyCap, apSmgmtSipInterfaceRegCacheLimCap=apSmgmtSipInterfaceRegCacheLimCap, apSmgmtXCodeEVSUtilCap=apSmgmtXCodeEVSUtilCap, apCodecMediaProcessingCap=apCodecMediaProcessingCap, apSecurityIkeInterfaceEapOnlyAuthStatsCap=apSecurityIkeInterfaceEapOnlyAuthStatsCap, apAppsDNSSvrNotifGroupCap=apAppsDNSSvrNotifGroupCap, apEntityCapabilities=apEntityCapabilities, apUsbcSysThreadCap4=apUsbcSysThreadCap4, apUsbcSysSmCap=apUsbcSysSmCap, apSmgmtStorageSpaceCap=apSmgmtStorageSpaceCap, apSmgmtNTPNotifyCap=apSmgmtNTPNotifyCap, apAppsDNSStatusGroupCap=apAppsDNSStatusGroupCap, apSecurityIkeInterfaceIkeErrorStatsCap=apSecurityIkeInterfaceIkeErrorStatsCap, apEntityCap=apEntityCap, apSmgmtCtrlStatsCap=apSmgmtCtrlStatsCap, apSwInventoryCap=apSwInventoryCap, apSmgmtTrapTableObjectCap=apSmgmtTrapTableObjectCap, apLicenseExpirationWarnCap=apLicenseExpirationWarnCap, apSecurityTscfCap=apSecurityTscfCap, apRadiusMibCap=apRadiusMibCap, apSecurityInetCap=apSecurityInetCap, apSipMSRPStatsCap=apSipMSRPStatsCap, apSecurityGtpProfileCap=apSecurityGtpProfileCap, apUdpCap=apUdpCap, apSmgmtCap2=apSmgmtCap2, apSmgmtDOSNotifyTrustedtoUntrustedCap=apSmgmtDOSNotifyTrustedtoUntrustedCap, apTcpCap2=apTcpCap2, apLicenseMibCapabilities=apLicenseMibCapabilities, apSmgmtXCodeG729UtilCap=apSmgmtXCodeG729UtilCap, apSmgmtSipRejectCap=apSmgmtSipRejectCap, apSmgmtApplicationCPUUsageCap=apSmgmtApplicationCPUUsageCap, apSmgmtCap6=apSmgmtCap6, apSmgmtRegistrationCap2=apSmgmtRegistrationCap2, apSmgmtSipMethodStatsCap=apSmgmtSipMethodStatsCap, apSmgmtENUMCap=apSmgmtENUMCap, apCodecRealmCodecCap10=apCodecRealmCodecCap10, apAppsENUMSvrNotifGroupCap=apAppsENUMSvrNotifGroupCap, apDDMibCapabilities=apDDMibCapabilities, apSmgmtLDAPCap=apSmgmtLDAPCap, apUsbcSysThreadCap2=apUsbcSysThreadCap2, apIfMibCap=apIfMibCap, apSysMgmtETCUtilCap=apSysMgmtETCUtilCap, apSwinventoryMibCapabilities=apSwinventoryMibCapabilities, apAclDropCap=apAclDropCap, apSmgmtRealmRegCacheSummaryCap=apSmgmtRealmRegCacheSummaryCap, apIfMibHCCap=apIfMibHCCap, apSLBEndpointCapacityCap=apSLBEndpointCapacityCap, apCoreLBMemberStatusNotifCap=apCoreLBMemberStatusNotifCap, apInterfacesCap=apInterfacesCap, apSmgmtRegistrationCap=apSmgmtRegistrationCap, apAmiCap=apAmiCap, apDDStatsGroup3Cap=apDDStatsGroup3Cap, apSipRegEvtSubscriptionCap=apSipRegEvtSubscriptionCap, apSecurityTacacsCap=apSecurityTacacsCap, apSmgmtExtSipCap=apSmgmtExtSipCap, apUsbcSysSmMibCapabilities=apUsbcSysSmMibCapabilities, apUsbcSysDPDKCap=apUsbcSysDPDKCap, apSmgmtCap3=apSmgmtCap3, apSecurityRekeyOnSNoverflowCap=apSecurityRekeyOnSNoverflowCap, apSmgmtXCodeEVRCUtilCap=apSmgmtXCodeEVRCUtilCap, apIcmpStatsCap=apIcmpStatsCap, apSmgmtMediaSuperCap=apSmgmtMediaSuperCap, apSmgmtCallsRejectedCap=apSmgmtCallsRejectedCap, apSipSurvivabilityNotificationsGroupCap=apSipSurvivabilityNotificationsGroupCap, apDNSALGStatsGroupCap=apDNSALGStatsGroupCap, apSecurityIkeInterfaceEapMethodsStatsCap=apSecurityIkeInterfaceEapMethodsStatsCap, apSmgmtCap5=apSmgmtCap5, apDDStatsGroup2Cap=apDDStatsGroup2Cap, apDiamMibCapabilities=apDiamMibCapabilities, apSystemManagementGatewaySynchronizedMonitorCap=apSystemManagementGatewaySynchronizedMonitorCap, apSecurityTacacsNotifCap=apSecurityTacacsNotifCap, apSmgmtExtSigRealmCap=apSmgmtExtSigRealmCap, apSecurityIkeDDoSInetCap=apSecurityIkeDDoSInetCap, apAppsENUMRateGroupCap=apAppsENUMRateGroupCap, apRadiusServerStatsCap=apRadiusServerStatsCap, apCodecRealmCodecCap3=apCodecRealmCodecCap3, apDDStatsGroupCap=apDDStatsGroupCap, apEnvMonitorMibCapabilities=apEnvMonitorMibCapabilities, apSnmpCap=apSnmpCap, apEnvMonCardCap=apEnvMonCardCap, apSecurityIkeInterfaceMobikeStatsCap=apSecurityIkeInterfaceMobikeStatsCap, apSipRateGroupCap=apSipRateGroupCap, apTCPMibCapabilities=apTCPMibCapabilities, apSipSRVCCPreAlertingStatsCap=apSipSRVCCPreAlertingStatsCap, apSmgmtXCodeOpusUtilCap=apSmgmtXCodeOpusUtilCap, apCommMonitorNotificationGroupCap=apCommMonitorNotificationGroupCap, apSnmpMibCapabilities=apSnmpMibCapabilities, apCodecRealmCodecCap9=apCodecRealmCodecCap9, apSmgmtRejectedMessagesCap=apSmgmtRejectedMessagesCap, apSmgmtCap=apSmgmtCap, apSecurityMibCapabilities=apSecurityMibCapabilities, apUdpCap2=apUdpCap2, apIpCap=apIpCap, apDNSALGRateGroupCap=apDNSALGRateGroupCap, apCodecRealmCodecCap8=apCodecRealmCodecCap8, apSmgmtCollectorPushSuccessNotifyCap=apSmgmtCollectorPushSuccessNotifyCap, apUsbcSysThreadMibCapabilities3=apUsbcSysThreadMibCapabilities3, apIfMibCapabilities=apIfMibCapabilities, apSipAudioVideoCallsCap=apSipAudioVideoCallsCap, apCodecRealmCodecCap4=apCodecRealmCodecCap4, apSipMibCapabilities=apSipMibCapabilities, apSecurityTacacsDownLocalAuthCap=apSecurityTacacsDownLocalAuthCap, apSmgmtRegistrationCapacityCap=apSmgmtRegistrationCapacityCap, apDiamAuthCap=apDiamAuthCap, apSipSecInterfaceRegNotifGroupCap=apSipSecInterfaceRegNotifGroupCap, apSmgmtHDRCap=apSmgmtHDRCap, apUsbcSysCap=apUsbcSysCap, apCodecRealmCodecCap5=apCodecRealmCodecCap5, apSmgmtSubscriptionSummaryCap=apSmgmtSubscriptionSummaryCap, apEnvMonPortChangeCap=apEnvMonPortChangeCap, apSipVoLTECountersCap=apSipVoLTECountersCap, apSmgmtEndPtDemotionCap=apSmgmtEndPtDemotionCap, apSnmpv3Cap=apSnmpv3Cap, apSecurityCertificateCap=apSecurityCertificateCap, apCsvConfigSaveCap=apCsvConfigSaveCap, apSmgmtLPCap=apSmgmtLPCap, apCodecRealmCodecCap7=apCodecRealmCodecCap7, apSyslogCap=apSyslogCap, PYSNMP_MODULE_ID=apAgentCapModule, apSmgmtXCodeSILKUtilCap=apSmgmtXCodeSILKUtilCap, apSecurityTlsCap=apSecurityTlsCap, apSmgmtClockNotifyCap=apSmgmtClockNotifyCap, apUsbcSysScalingCap=apUsbcSysScalingCap, apSecurityGtpStatusCap=apSecurityGtpStatusCap, apSecurityIkeDDoSCap=apSecurityIkeDDoSCap, apSecurityIkeInterface3GPPAuthErrorsCap=apSecurityIkeInterface3GPPAuthErrorsCap, apSmgmtH323AdditionsCap=apSmgmtH323AdditionsCap, apSecurityIkeIfcBlAuthIDErrorCap=apSecurityIkeIfcBlAuthIDErrorCap, apUsbcSysThreadMibCapabilities=apUsbcSysThreadMibCapabilities, apCodecRealmCodecCap6=apCodecRealmCodecCap6, apSLBUntrustedEndpointCapacityCap=apSLBUntrustedEndpointCapacityCap, apSmgmtCDRPushReceiverFailureCap=apSmgmtCDRPushReceiverFailureCap, apSmgmtInetAddrDOSNotifyCap=apSmgmtInetAddrDOSNotifyCap, apUsbcSysScalingMibCapabilities=apUsbcSysScalingMibCapabilities, apSmgmtCtrlStatsCap2=apSmgmtCtrlStatsCap2, apDDSCTPNotifGroupCap=apDDSCTPNotifGroupCap, apSipSecInterfaceRegObjectsGroupCap=apSipSecInterfaceRegObjectsGroupCap, apSecurityIPsecTunnelsCap=apSecurityIPsecTunnelsCap, apSLBMibCapabilities=apSLBMibCapabilities, apCoreLbMibCapabilities=apCoreLbMibCapabilities, apSmgmtH248PortMapUsageCap=apSmgmtH248PortMapUsageCap, apEnvMonCap4=apEnvMonCap4, apAclDropMibCapabilities=apAclDropMibCapabilities, apTcpCap=apTcpCap, apAmiMibCapabilities=apAmiMibCapabilities, apSmgmtDOSNotifyCap=apSmgmtDOSNotifyCap, apSmgmtRegistrationCap3=apSmgmtRegistrationCap3, apUsbcSysDPDKMibCapabilities=apUsbcSysDPDKMibCapabilities)
