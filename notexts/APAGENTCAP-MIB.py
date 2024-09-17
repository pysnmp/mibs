#
# PySNMP MIB module APAGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/APAGENTCAP-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:06:14 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
acmepacketAgentCapability, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketAgentCapability")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, Integer32, Bits, mib_2, enterprises, iso, Counter32, NotificationType, Counter64, MibIdentifier, Unsigned32, ObjectIdentity, snmpModules, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Bits", "mib-2", "enterprises", "iso", "Counter32", "NotificationType", "Counter64", "MibIdentifier", "Unsigned32", "ObjectIdentity", "snmpModules", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
apAgentCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 2, 1))
apAgentCapModule.setRevisions(('2001-08-01 00:00', '2004-11-18 00:00', '2006-05-01 00:00', '2007-05-07 00:00', '1920-12-15 00:00', '2012-03-07 00:00', '2012-07-16 00:00', '2014-02-26 00:00', '2014-06-20 00:00', '2014-06-26 00:00', '2017-02-09 00:00', '2017-10-18 00:00', '2017-11-24 00:00', '2017-12-14 00:00', '2018-04-10 00:00', '2018-04-27 00:00', '2019-04-24 00:00',))
if mibBuilder.loadTexts: apAgentCapModule.setLastUpdated('201904240000Z')
if mibBuilder.loadTexts: apAgentCapModule.setOrganization('Oracle Communications')
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
apSnmpv3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSnmpv3Cap = apSnmpv3Cap.setStatus('current')
apInterfacesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apInterfacesCap = apInterfacesCap.setStatus('current')
apIfMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibCap = apIfMibCap.setStatus('current')
apIfMibHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibHCCap = apIfMibHCCap.setStatus('current')
apIfMibVHCCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibVHCCap = apIfMibVHCCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIfMibVHCCap = apIfMibVHCCap.setStatus('current')
apIpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap = apIpCap.setStatus('current')
apIpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap2 = apIpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIpCap2 = apIpCap2.setStatus('current')
apIcmpStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIcmpStatsCap = apIcmpStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apIcmpStatsCap = apIcmpStatsCap.setStatus('current')
apTcpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap = apTcpCap.setStatus('current')
apTcpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap2 = apTcpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apTcpCap2 = apTcpCap2.setStatus('current')
apUdpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap = apUdpCap.setStatus('current')
apUdpCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap2 = apUdpCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUdpCap2 = apUdpCap2.setStatus('current')
apEntityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setProductRelease('Acme Packet for Relase 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEntityCap = apEntityCap.setStatus('current')
apSyslogCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 7, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSyslogCap = apSyslogCap.setStatus('current')
apCsvConfigSaveCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 32, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCsvConfigSaveCap = apCsvConfigSaveCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCsvConfigSaveCap = apCsvConfigSaveCap.setStatus('current')
apSmgmtCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap = apSmgmtCap.setStatus('current')
apSmgmtCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap2 = apSmgmtCap2.setStatus('current')
apSmgmtCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap3 = apSmgmtCap3.setStatus('current')
apSmgmtCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap4 = apSmgmtCap4.setStatus('current')
apSmgmtCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap5 = apSmgmtCap5.setStatus('current')
apSmgmtCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCap6 = apSmgmtCap6.setStatus('current')
apSmgmtNSEPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNSEPCap = apSmgmtNSEPCap.setStatus('current')
apSmgmtCtrlStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap = apSmgmtCtrlStatsCap.setStatus('current')
apSmgmtLDAPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLDAPCap = apSmgmtLDAPCap.setStatus('current')
apSmgmtHDRCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtHDRCap = apSmgmtHDRCap.setStatus('current')
apSmgmtMediaSuperCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtMediaSuperCap = apSmgmtMediaSuperCap.setStatus('current')
apSmgmtH248Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248Cap = apSmgmtH248Cap.setStatus('current')
apSmgmtRFactorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRFactorCap = apSmgmtRFactorCap.setStatus('current')
apSmgmtSipRejectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipRejectCap = apSmgmtSipRejectCap.setStatus('current')
apSmgmtDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyCap = apSmgmtDOSNotifyCap.setStatus('current')
apSmgmtRegNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegNotifyCap = apSmgmtRegNotifyCap.setStatus('current')
apSmgmtNTPNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtNTPNotifyCap = apSmgmtNTPNotifyCap.setStatus('current')
apSmgmtCollectorPushSuccessNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCollectorPushSuccessNotifyCap = apSmgmtCollectorPushSuccessNotifyCap.setStatus('current')
apSmgmtExtSigRealmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSigRealmCap = apSmgmtExtSigRealmCap.setStatus('current')
apSmgmtClockNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtClockNotifyCap = apSmgmtClockNotifyCap.setStatus('current')
apSmgmtRegistrationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap = apSmgmtRegistrationCap.setStatus('current')
apSmgmtRegistrationCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap2 = apSmgmtRegistrationCap2.setStatus('current')
apSmgmtRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegCacheLimCap = apSmgmtRegCacheLimCap.setStatus('current')
apSmgmtShortSessionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtShortSessionCap = apSmgmtShortSessionCap.setStatus('current')
apSystemManagementGatewaySynchronizedMonitorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSystemManagementGatewaySynchronizedMonitorCap = apSystemManagementGatewaySynchronizedMonitorCap.setStatus('current')
apSmgmtRegistrationCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCap3 = apSmgmtRegistrationCap3.setStatus('current')
apSmgmtCallRecordingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallRecordingCap = apSmgmtCallRecordingCap.setStatus('current')
apSmgmtH323AdditionsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH323AdditionsCap = apSmgmtH323AdditionsCap.setStatus('current')
apSmgmtENUMCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 29))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtENUMCap = apSmgmtENUMCap.setStatus('current')
apSmgmtExtSipCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 30))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtExtSipCap = apSmgmtExtSipCap.setStatus('current')
apSmgmtRealmIcmpFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 31))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmIcmpFailureCap = apSmgmtRealmIcmpFailureCap.setStatus('current')
apSmgmtTrapTableObjectCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 32))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtTrapTableObjectCap = apSmgmtTrapTableObjectCap.setStatus('current')
apSmgmtCDRPushReceiverFailureCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 33))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCDRPushReceiverFailureCap = apSmgmtCDRPushReceiverFailureCap.setStatus('current')
apSmgmtRealmStatsQoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 34))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmStatsQoSCap = apSmgmtRealmStatsQoSCap.setStatus('current')
apSmgmtInetAddrDOSNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 35))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtInetAddrDOSNotifyCap = apSmgmtInetAddrDOSNotifyCap.setStatus('current')
apSmgmtApplicationCPUUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 36))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtApplicationCPUUsageCap = apSmgmtApplicationCPUUsageCap.setStatus('current')
apSmgmtRegistrationCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 37))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRegistrationCapacityCap = apSmgmtRegistrationCapacityCap.setStatus('obsolete')
apSmgmtRejectedMessagesCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 38))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRejectedMessagesCap = apSmgmtRejectedMessagesCap.setStatus('current')
apSmgmtEndPtDemotionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 39))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtEndPtDemotionCap = apSmgmtEndPtDemotionCap.setStatus('current')
apSmgmtAdminCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 40))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtAdminCap = apSmgmtAdminCap.setStatus('current')
apSmgmtLPCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 41))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtLPCap = apSmgmtLPCap.setStatus('current')
apSmgmtPhyUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 42))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtPhyUtilCap = apSmgmtPhyUtilCap.setStatus('current')
apSmgmtStorageSpaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 43))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtStorageSpaceCap = apSmgmtStorageSpaceCap.setStatus('current')
apSmgmtCtrlStatsCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 44))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCtrlStatsCap2 = apSmgmtCtrlStatsCap2.setStatus('current')
apSmgmtDatabaseRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 45))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDatabaseRegCap = apSmgmtDatabaseRegCap.setStatus('current')
apSmgmtCallsRejectedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 46))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCallsRejectedCap = apSmgmtCallsRejectedCap.setStatus('current')
apSmgmtSipInterfaceRegCacheLimCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 47))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipInterfaceRegCacheLimCap = apSmgmtSipInterfaceRegCacheLimCap.setStatus('current')
apSmgmtRealmRegCacheSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 48))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtRealmRegCacheSummaryCap = apSmgmtRealmRegCacheSummaryCap.setStatus('current')
apSmgmtSubscriptionSummaryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 49))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSubscriptionSummaryCap = apSmgmtSubscriptionSummaryCap.setStatus('current')
apSmgmtH248PortMapUsageCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 50))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtH248PortMapUsageCap = apSmgmtH248PortMapUsageCap.setStatus('current')
apSmgmtDOSNotifyTrustedtoUntrustedCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 51))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtDOSNotifyTrustedtoUntrustedCap = apSmgmtDOSNotifyTrustedtoUntrustedCap.setStatus('current')
apSysMgmtETCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 52))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSysMgmtETCUtilCap = apSysMgmtETCUtilCap.setStatus('current')
apSmgmtXCodeEVRCUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 53))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCUtilCap = apSmgmtXCodeEVRCUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCUtilCap = apSmgmtXCodeEVRCUtilCap.setStatus('current')
apSmgmtXCodeG729UtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 54))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeG729UtilCap = apSmgmtXCodeG729UtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeG729UtilCap = apSmgmtXCodeG729UtilCap.setStatus('current')
apSmgmtCPULoadAvgCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 55))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCPULoadAvgCap = apSmgmtCPULoadAvgCap.setProductRelease('Acme-Packet SD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtCPULoadAvgCap = apSmgmtCPULoadAvgCap.setStatus('obsolete')
apSmgmtXCodeOpusUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 56))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeOpusUtilCap = apSmgmtXCodeOpusUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeOpusUtilCap = apSmgmtXCodeOpusUtilCap.setStatus('current')
apSmgmtXCodeSILKUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 57))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeSILKUtilCap = apSmgmtXCodeSILKUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeSILKUtilCap = apSmgmtXCodeSILKUtilCap.setStatus('current')
apSmgmtXCodeEVRCNWUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 58))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCNWUtilCap = apSmgmtXCodeEVRCNWUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVRCNWUtilCap = apSmgmtXCodeEVRCNWUtilCap.setStatus('current')
apSmgmtXCodeEVSUtilCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 59))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVSUtilCap = apSmgmtXCodeEVSUtilCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtXCodeEVSUtilCap = apSmgmtXCodeEVSUtilCap.setStatus('current')
apEnvMonCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap = apEnvMonCap.setStatus('current')
apEnvMonCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap2 = apEnvMonCap2.setStatus('current')
apEnvMonPortChangeCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonPortChangeCap = apEnvMonPortChangeCap.setStatus('current')
apEnvMonCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCap4 = apEnvMonCap4.setStatus('current')
apEnvMonCardCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardCap = apEnvMonCardCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apEnvMonCardCap = apEnvMonCardCap.setStatus('current')
apSwInventoryCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryCap = apSwInventoryCap.setStatus('current')
apLicenseCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseCap = apLicenseCap.setStatus('current')
apLicenseDBRegCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDBRegCap = apLicenseDBRegCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseDBRegCap = apLicenseDBRegCap.setStatus('current')
apLicenseExpirationWarnCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apLicenseExpirationWarnCap = apLicenseExpirationWarnCap.setStatus('current')
apAmiCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAmiCap = apAmiCap.setStatus('current')
apCodecRealmCodecCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap = apCodecRealmCodecCap.setStatus('current')
apCodecMediaProcessingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecMediaProcessingCap = apCodecMediaProcessingCap.setStatus('current')
apCodecRealmCodecCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap2 = apCodecRealmCodecCap2.setStatus('current')
apCodecTranscodingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecTranscodingStatsCap = apCodecTranscodingStatsCap.setStatus('current')
apCodecRealmCodecCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap3 = apCodecRealmCodecCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap3 = apCodecRealmCodecCap3.setStatus('current')
apCodecRealmCodecCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap4 = apCodecRealmCodecCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap4 = apCodecRealmCodecCap4.setStatus('current')
apCodecRealmCodecCap5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap5 = apCodecRealmCodecCap5.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap5 = apCodecRealmCodecCap5.setStatus('current')
apCodecRealmCodecCap6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap6 = apCodecRealmCodecCap6.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap6 = apCodecRealmCodecCap6.setStatus('current')
apCodecRealmCodecCap7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap7 = apCodecRealmCodecCap7.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap7 = apCodecRealmCodecCap7.setStatus('current')
apCodecRealmCodecCap8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap8 = apCodecRealmCodecCap8.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap8 = apCodecRealmCodecCap8.setStatus('current')
apCodecRealmCodecCap9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap9 = apCodecRealmCodecCap9.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap9 = apCodecRealmCodecCap9.setStatus('current')
apCodecRealmCodecCap10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap10 = apCodecRealmCodecCap10.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCodecRealmCodecCap10 = apCodecRealmCodecCap10.setStatus('current')
apSecurityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCap = apSecurityCap.setStatus('current')
apSecurityIPsecTunnelsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIPsecTunnelsCap = apSecurityIPsecTunnelsCap.setStatus('current')
apSecurityIkeInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceCap = apSecurityIkeInterfaceCap.setStatus('current')
apSecurityTacacsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsCap = apSecurityTacacsCap.setStatus('current')
apSecurityCertStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertStatusCap = apSecurityCertStatusCap.setStatus('current')
apSecurityIkeDDoSCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSCap = apSecurityIkeDDoSCap.setStatus('current')
apSecurityCertificateCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityCertificateCap = apSecurityCertificateCap.setStatus('current')
apSecurityGtpStatusCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpStatusCap = apSecurityGtpStatusCap.setStatus('current')
apSecurityIkeInterfaceInfoCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceInfoCap = apSecurityIkeInterfaceInfoCap.setStatus('current')
apSecurityTacacsNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsNotifCap = apSecurityTacacsNotifCap.setStatus('current')
apSecurityInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityInetCap = apSecurityInetCap.setStatus('current')
apSecurityIkeDDoSInetCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeDDoSInetCap = apSecurityIkeDDoSInetCap.setStatus('current')
apSecurityIkeIfcBlAuthIDErrorCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeIfcBlAuthIDErrorCap = apSecurityIkeIfcBlAuthIDErrorCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeIfcBlAuthIDErrorCap = apSecurityIkeIfcBlAuthIDErrorCap.setStatus('current')
apSecurityDhcpInterfaceCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityDhcpInterfaceCap = apSecurityDhcpInterfaceCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityDhcpInterfaceCap = apSecurityDhcpInterfaceCap.setStatus('current')
apSecurityGtpProfileCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpProfileCap = apSecurityGtpProfileCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpProfileCap = apSecurityGtpProfileCap.setStatus('current')
apSecurityRekeyOnSNoverflowCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityRekeyOnSNoverflowCap = apSecurityRekeyOnSNoverflowCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityRekeyOnSNoverflowCap = apSecurityRekeyOnSNoverflowCap.setStatus('current')
apSecurityIkeInterfaceDpdStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceDpdStatsCap = apSecurityIkeInterfaceDpdStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceDpdStatsCap = apSecurityIkeInterfaceDpdStatsCap.setStatus('current')
apSecurityIkeInterfaceEapOnlyAuthStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapOnlyAuthStatsCap = apSecurityIkeInterfaceEapOnlyAuthStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapOnlyAuthStatsCap = apSecurityIkeInterfaceEapOnlyAuthStatsCap.setStatus('current')
apSecurityTscfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfCap = apSecurityTscfCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfCap = apSecurityTscfCap.setStatus('current')
apSecurityIkeInterfaceEapMethodsStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapMethodsStatsCap = apSecurityIkeInterfaceEapMethodsStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceEapMethodsStatsCap = apSecurityIkeInterfaceEapMethodsStatsCap.setStatus('current')
apSecurityIkeInterfaceIkeErrorStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceIkeErrorStatsCap = apSecurityIkeInterfaceIkeErrorStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceIkeErrorStatsCap = apSecurityIkeInterfaceIkeErrorStatsCap.setStatus('current')
apSecurityIkeInterfaceMobikeStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceMobikeStatsCap = apSecurityIkeInterfaceMobikeStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterfaceMobikeStatsCap = apSecurityIkeInterfaceMobikeStatsCap.setStatus('current')
apSecurityTscfTimeoutCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfTimeoutCap = apSecurityTscfTimeoutCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTscfTimeoutCap = apSecurityTscfTimeoutCap.setStatus('current')
apSecurityIkeInterface3GPPAuthErrorsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 24))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterface3GPPAuthErrorsCap = apSecurityIkeInterface3GPPAuthErrorsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityIkeInterface3GPPAuthErrorsCap = apSecurityIkeInterface3GPPAuthErrorsCap.setStatus('current')
apSecurityGtpCaviumStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 25))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpCaviumStatsCap = apSecurityGtpCaviumStatsCap.setProductRelease('Oracle Communications Acme Packet MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityGtpCaviumStatsCap = apSecurityGtpCaviumStatsCap.setStatus('current')
apSecurityTacacsDownLocalAuthCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 26))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsDownLocalAuthCap = apSecurityTacacsDownLocalAuthCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTacacsDownLocalAuthCap = apSecurityTacacsDownLocalAuthCap.setStatus('current')
apSecurityTlsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 27))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTlsCap = apSecurityTlsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecurityTlsCap = apSecurityTlsCap.setStatus('current')
apSecuritySrtpCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 28))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecuritySrtpCap = apSecuritySrtpCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSecuritySrtpCap = apSecuritySrtpCap.setStatus('current')
apH323StackCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 15, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackCap = apH323StackCap.setStatus('current')
apSLBEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBEndpointCapacityCap = apSLBEndpointCapacityCap.setStatus('current')
apSLBUntrustedEndpointCapacityCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSLBUntrustedEndpointCapacityCap = apSLBUntrustedEndpointCapacityCap.setStatus('current')
apDiamMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamMibCap = apDiamMibCap.setStatus('current')
apDiamNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamNotifCap = apDiamNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamNotifCap = apDiamNotifCap.setStatus('current')
apDiamClfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamClfCap = apDiamClfCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamClfCap = apDiamClfCap.setStatus('current')
apDiamIntfCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamIntfCap = apDiamIntfCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamIntfCap = apDiamIntfCap.setStatus('current')
apDiamAuthCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthCap = apDiamAuthCap.setProductRelease('Oracle Communications Acme MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthCap = apDiamAuthCap.setStatus('current')
apDiamAuthNotifyCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthNotifyCap = apDiamAuthNotifyCap.setProductRelease('Oracle Communications Acme MSG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDiamAuthNotifyCap = apDiamAuthNotifyCap.setStatus('current')
apDDStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroupCap = apDDStatsGroupCap.setStatus('current')
apDDNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDNotifGroupCap = apDDNotifGroupCap.setStatus('current')
apDDStatsGroup2Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup2Cap = apDDStatsGroup2Cap.setStatus('current')
apDDStatsGroup3Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup3Cap = apDDStatsGroup3Cap.setStatus('current')
apDDSCTPNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDSCTPNotifGroupCap = apDDSCTPNotifGroupCap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDSCTPNotifGroupCap = apDDSCTPNotifGroupCap.setStatus('current')
apDDStatsGroup4Cap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup4Cap = apDDStatsGroup4Cap.setProductRelease('Acme Packet Diameter Signaling Controller')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDDStatsGroup4Cap = apDDStatsGroup4Cap.setStatus('current')
apDNSALGStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setProductRelease('Acme Packet DNS ALG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGStatsGroupCap = apDNSALGStatsGroupCap.setStatus('current')
apDNSALGNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setProductRelease('Acme Packet PEC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGNotifGroupCap = apDNSALGNotifGroupCap.setStatus('current')
apDNSALGRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGRateGroupCap = apDNSALGRateGroupCap.setProductRelease('Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apDNSALGRateGroupCap = apDNSALGRateGroupCap.setStatus('current')
apAppsENUMStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMStatusGroupCap = apAppsENUMStatusGroupCap.setStatus('current')
apAppsDNSStatusGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSStatusGroupCap = apAppsDNSStatusGroupCap.setStatus('current')
apAppsENUMSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMSvrNotifGroupCap = apAppsENUMSvrNotifGroupCap.setStatus('current')
apAppsDNSSvrNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsDNSSvrNotifGroupCap = apAppsDNSSvrNotifGroupCap.setStatus('current')
apAppsENUMRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMRateGroupCap = apAppsENUMRateGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAppsENUMRateGroupCap = apAppsENUMRateGroupCap.setStatus('current')
apCommMonitorNotificationGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCommMonitorNotificationGroupCap = apCommMonitorNotificationGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCommMonitorNotificationGroupCap = apCommMonitorNotificationGroupCap.setStatus('current')
apSipSecInterfaceRegNotifGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegNotifGroupCap = apSipSecInterfaceRegNotifGroupCap.setStatus('current')
apSipSecInterfaceRegObjectsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSecInterfaceRegObjectsGroupCap = apSipSecInterfaceRegObjectsGroupCap.setStatus('current')
apSipSurvivabilityNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSurvivabilityNotificationsGroupCap = apSipSurvivabilityNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSurvivabilityNotificationsGroupCap = apSipSurvivabilityNotificationsGroupCap.setStatus('current')
apSipRateGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRateGroupCap = apSipRateGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRateGroupCap = apSipRateGroupCap.setStatus('current')
apSipCACStatsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsGroupCap = apSipCACStatsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsGroupCap = apSipCACStatsGroupCap.setStatus('current')
apSipCACNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACNotificationsGroupCap = apSipCACNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACNotificationsGroupCap = apSipCACNotificationsGroupCap.setStatus('current')
apSipCACStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsCap = apSipCACStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCACStatsCap = apSipCACStatsCap.setStatus('current')
apSipRecNotificationsGroupCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRecNotificationsGroupCap = apSipRecNotificationsGroupCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRecNotificationsGroupCap = apSipRecNotificationsGroupCap.setStatus('current')
apSipAudioVideoCallsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipAudioVideoCallsCap = apSipAudioVideoCallsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipAudioVideoCallsCap = apSipAudioVideoCallsCap.setStatus('current')
apSipVoLTECountersCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipVoLTECountersCap = apSipVoLTECountersCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipVoLTECountersCap = apSipVoLTECountersCap.setStatus('current')
apSipCallInformationCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCallInformationCap = apSipCallInformationCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipCallInformationCap = apSipCallInformationCap.setStatus('current')
apSmgmtSipMethodStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipMethodStatsCap = apSmgmtSipMethodStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSmgmtSipMethodStatsCap = apSmgmtSipMethodStatsCap.setStatus('current')
apSipSRVCCPreAlertingStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSRVCCPreAlertingStatsCap = apSipSRVCCPreAlertingStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipSRVCCPreAlertingStatsCap = apSipSRVCCPreAlertingStatsCap.setStatus('current')
apSipRegEvtSubscriptionCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRegEvtSubscriptionCap = apSipRegEvtSubscriptionCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipRegEvtSubscriptionCap = apSipRegEvtSubscriptionCap.setStatus('current')
apSipMSRPStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipMSRPStatsCap = apSipMSRPStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSipMSRPStatsCap = apSipMSRPStatsCap.setStatus('current')
apUsbcSysCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysCap = apUsbcSysCap.setStatus('current')
apUsbcSysDPDKCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysDPDKCap = apUsbcSysDPDKCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysDPDKCap = apUsbcSysDPDKCap.setStatus('current')
apUsbcSysScalingCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysScalingCap = apUsbcSysScalingCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysScalingCap = apUsbcSysScalingCap.setStatus('current')
apUsbcSysThreadCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 27, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap = apUsbcSysThreadCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap = apUsbcSysThreadCap.setStatus('current')
apUsbcSysFdCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysFdCap = apUsbcSysFdCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysFdCap = apUsbcSysFdCap.setStatus('current')
apUsbcSysThreadCap2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 28, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap2 = apUsbcSysThreadCap2.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap2 = apUsbcSysThreadCap2.setStatus('current')
apUsbcSysThreadCap3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 30, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap3 = apUsbcSysThreadCap3.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap3 = apUsbcSysThreadCap3.setStatus('current')
apUsbcSysThreadCap4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 27, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap4 = apUsbcSysThreadCap4.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysThreadCap4 = apUsbcSysThreadCap4.setStatus('current')
apUsbcSysSmCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 29, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysSmCap = apUsbcSysSmCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apUsbcSysSmCap = apUsbcSysSmCap.setStatus('current')
apRadiusMibCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusMibCap = apRadiusMibCap.setStatus('current')
apRadiusServerStatsCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apRadiusServerStatsCap = apRadiusServerStatsCap.setStatus('current')
apCoreLBMemberStatusNotifCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 24, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCoreLBMemberStatusNotifCap = apCoreLBMemberStatusNotifCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apCoreLBMemberStatusNotifCap = apCoreLBMemberStatusNotifCap.setStatus('current')
apAclDropCap = AgentCapabilities((1, 3, 6, 1, 4, 1, 9148, 2, 1, 31, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAclDropCap = apAclDropCap.setProductRelease('Oracle Communications Acme Packet SBC')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apAclDropCap = apAclDropCap.setStatus('current')
mibBuilder.exportSymbols("APAGENTCAP-MIB", apTCPMibCapabilities=apTCPMibCapabilities, apSipRateGroupCap=apSipRateGroupCap, apSecuritySrtpCap=apSecuritySrtpCap, apCodecRealmCodecCap3=apCodecRealmCodecCap3, apSmgmtXCodeG729UtilCap=apSmgmtXCodeG729UtilCap, apUsbcSysThreadCap=apUsbcSysThreadCap, apSnmpCap=apSnmpCap, apSecurityTacacsNotifCap=apSecurityTacacsNotifCap, apDDMibCapabilities=apDDMibCapabilities, apIfMibCap=apIfMibCap, apSmgmtAdminCap=apSmgmtAdminCap, apSmgmtShortSessionCap=apSmgmtShortSessionCap, apSecurityTscfTimeoutCap=apSecurityTscfTimeoutCap, apCodecTranscodingStatsCap=apCodecTranscodingStatsCap, apDDStatsGroup4Cap=apDDStatsGroup4Cap, apUsbcSysScalingCap=apUsbcSysScalingCap, apSecurityTlsCap=apSecurityTlsCap, apUsbcSysFdCap=apUsbcSysFdCap, apAclDropCap=apAclDropCap, apSLBUntrustedEndpointCapacityCap=apSLBUntrustedEndpointCapacityCap, apDiamAuthCap=apDiamAuthCap, apInterfacesCap=apInterfacesCap, apSmgmtTrapTableObjectCap=apSmgmtTrapTableObjectCap, apEnvMonPortChangeCap=apEnvMonPortChangeCap, apSecurityRekeyOnSNoverflowCap=apSecurityRekeyOnSNoverflowCap, apIfMibVHCCap=apIfMibVHCCap, apSmgmtRegistrationCap2=apSmgmtRegistrationCap2, apUsbcSysThreadMibCapabilities=apUsbcSysThreadMibCapabilities, apSmgmtCollectorPushSuccessNotifyCap=apSmgmtCollectorPushSuccessNotifyCap, apUsbcSysThreadMibCapabilities2=apUsbcSysThreadMibCapabilities2, apEnvMonCap2=apEnvMonCap2, apUdpCap2=apUdpCap2, apEntityCap=apEntityCap, apSipRecNotificationsGroupCap=apSipRecNotificationsGroupCap, apSipVoLTECountersCap=apSipVoLTECountersCap, apSysMgmtETCUtilCap=apSysMgmtETCUtilCap, apSecurityTscfCap=apSecurityTscfCap, apSecurityCertStatusCap=apSecurityCertStatusCap, apSecurityInetCap=apSecurityInetCap, apSmgmtMediaSuperCap=apSmgmtMediaSuperCap, apAppsDNSSvrNotifGroupCap=apAppsDNSSvrNotifGroupCap, apSecurityIkeInterfaceDpdStatsCap=apSecurityIkeInterfaceDpdStatsCap, apSecurityIkeIfcBlAuthIDErrorCap=apSecurityIkeIfcBlAuthIDErrorCap, apSyslogCap=apSyslogCap, apSecurityGtpStatusCap=apSecurityGtpStatusCap, apIcmpStatsCap=apIcmpStatsCap, apSmgmtRegNotifyCap=apSmgmtRegNotifyCap, apSipSecInterfaceRegObjectsGroupCap=apSipSecInterfaceRegObjectsGroupCap, apSmgmtXCodeEVRCNWUtilCap=apSmgmtXCodeEVRCNWUtilCap, apSmgmtRealmRegCacheSummaryCap=apSmgmtRealmRegCacheSummaryCap, apAppsDNSStatusGroupCap=apAppsDNSStatusGroupCap, apSipCACStatsGroupCap=apSipCACStatsGroupCap, apSmgmtXCodeEVSUtilCap=apSmgmtXCodeEVSUtilCap, apSLBEndpointCapacityCap=apSLBEndpointCapacityCap, apDiamIntfCap=apDiamIntfCap, apSmgmtRegistrationCap=apSmgmtRegistrationCap, apCodecRealmCodecCap6=apCodecRealmCodecCap6, apSmgmtCPULoadAvgCap=apSmgmtCPULoadAvgCap, apSmgmtLDAPCap=apSmgmtLDAPCap, apSmgmtCallRecordingCap=apSmgmtCallRecordingCap, apSipSRVCCPreAlertingStatsCap=apSipSRVCCPreAlertingStatsCap, apCoreLbMibCapabilities=apCoreLbMibCapabilities, apSipCallInformationCap=apSipCallInformationCap, apAgentCapModule=apAgentCapModule, apSmgmtStorageSpaceCap=apSmgmtStorageSpaceCap, apSmgmtRFactorCap=apSmgmtRFactorCap, apUsbcSysSmMibCapabilities=apUsbcSysSmMibCapabilities, apCodecRealmCodecCap7=apCodecRealmCodecCap7, apSipSurvivabilityNotificationsGroupCap=apSipSurvivabilityNotificationsGroupCap, apSmgmtMibCapabilities=apSmgmtMibCapabilities, apSmgmtDOSNotifyCap=apSmgmtDOSNotifyCap, apCodecRealmCodecCap5=apCodecRealmCodecCap5, apSmgmtRegistrationCapacityCap=apSmgmtRegistrationCapacityCap, apUsbcSysDPDKCap=apUsbcSysDPDKCap, apSmgmtENUMCap=apSmgmtENUMCap, apSmgmtCallsRejectedCap=apSmgmtCallsRejectedCap, apCodecMediaProcessingCap=apCodecMediaProcessingCap, apCodecRealmCodecCap4=apCodecRealmCodecCap4, apSmgmtCap5=apSmgmtCap5, apEnvMonitorMibCapabilities=apEnvMonitorMibCapabilities, apIPMibCapabilities=apIPMibCapabilities, apLicenseCap=apLicenseCap, apSmgmtLPCap=apSmgmtLPCap, apSmgmtExtSigRealmCap=apSmgmtExtSigRealmCap, apSlogMibCapabilities=apSlogMibCapabilities, apDNSALGMibCapabilities=apDNSALGMibCapabilities, apSecurityCap=apSecurityCap, apAppsENUMSvrNotifGroupCap=apAppsENUMSvrNotifGroupCap, apIfMibHCCap=apIfMibHCCap, apSmgmtH323AdditionsCap=apSmgmtH323AdditionsCap, apSmgmtCtrlStatsCap2=apSmgmtCtrlStatsCap2, apSwInventoryCap=apSwInventoryCap, apLicenseExpirationWarnCap=apLicenseExpirationWarnCap, apSecurityCertificateCap=apSecurityCertificateCap, apCoreLBMemberStatusNotifCap=apCoreLBMemberStatusNotifCap, apSmgmtExtSipCap=apSmgmtExtSipCap, apSipRegEvtSubscriptionCap=apSipRegEvtSubscriptionCap, PYSNMP_MODULE_ID=apAgentCapModule, apSmgmtCap6=apSmgmtCap6, apSmgmtNTPNotifyCap=apSmgmtNTPNotifyCap, apCodecRealmCodecCap=apCodecRealmCodecCap, apDDStatsGroupCap=apDDStatsGroupCap, apUsbcSysThreadCap4=apUsbcSysThreadCap4, apSmgmtXCodeSILKUtilCap=apSmgmtXCodeSILKUtilCap, apSmgmtSipInterfaceRegCacheLimCap=apSmgmtSipInterfaceRegCacheLimCap, apDDNotifGroupCap=apDDNotifGroupCap, apAppsMibCapabilities=apAppsMibCapabilities, apSecurityIPsecTunnelsCap=apSecurityIPsecTunnelsCap, apUsbcSysCap=apUsbcSysCap, apSmgmtNSEPCap=apSmgmtNSEPCap, apSmgmtXCodeEVRCUtilCap=apSmgmtXCodeEVRCUtilCap, apSecurityTacacsCap=apSecurityTacacsCap, apSecurityIkeInterfaceIkeErrorStatsCap=apSecurityIkeInterfaceIkeErrorStatsCap, apSecurityGtpProfileCap=apSecurityGtpProfileCap, apSmgmtEndPtDemotionCap=apSmgmtEndPtDemotionCap, apSecurityIkeInterfaceEapOnlyAuthStatsCap=apSecurityIkeInterfaceEapOnlyAuthStatsCap, apCodecMibCapabilities=apCodecMibCapabilities, apSLBMibCapabilities=apSLBMibCapabilities, apSystemManagementGatewaySynchronizedMonitorCap=apSystemManagementGatewaySynchronizedMonitorCap, apAppsENUMStatusGroupCap=apAppsENUMStatusGroupCap, apEnvMonCardCap=apEnvMonCardCap, apCommMonitorNotificationGroupCap=apCommMonitorNotificationGroupCap, apDiamClfCap=apDiamClfCap, apEntityCapabilities=apEntityCapabilities, apSecurityDhcpInterfaceCap=apSecurityDhcpInterfaceCap, apUsbcSysScalingMibCapabilities=apUsbcSysScalingMibCapabilities, apCsvConfigSaveCap=apCsvConfigSaveCap, apEnvMonCap=apEnvMonCap, apCsvConfigMibCapabilities=apCsvConfigMibCapabilities, apSmgmtCap2=apSmgmtCap2, apH323MibCapabilites=apH323MibCapabilites, apSmgmtRegCacheLimCap=apSmgmtRegCacheLimCap, apSecurityGtpCaviumStatsCap=apSecurityGtpCaviumStatsCap, apDiamMibCap=apDiamMibCap, apUsbcSysThreadCap3=apUsbcSysThreadCap3, apSmgmtCap4=apSmgmtCap4, apIfMibCapabilities=apIfMibCapabilities, apSecurityMibCapabilities=apSecurityMibCapabilities, apDiamMibCapabilities=apDiamMibCapabilities, apAppsENUMRateGroupCap=apAppsENUMRateGroupCap, apSmgmtRealmStatsQoSCap=apSmgmtRealmStatsQoSCap, apLicenseMibCapabilities=apLicenseMibCapabilities, apIpCap=apIpCap, apUDPMibCapabilities=apUDPMibCapabilities, apSecurityIkeDDoSInetCap=apSecurityIkeDDoSInetCap, apSecurityIkeInterfaceMobikeStatsCap=apSecurityIkeInterfaceMobikeStatsCap, apSecurityIkeInterface3GPPAuthErrorsCap=apSecurityIkeInterface3GPPAuthErrorsCap, apH323StackCap=apH323StackCap, apSecurityIkeInterfaceInfoCap=apSecurityIkeInterfaceInfoCap, apDDSCTPNotifGroupCap=apDDSCTPNotifGroupCap, apDNSALGStatsGroupCap=apDNSALGStatsGroupCap, apUsbcSysDPDKMibCapabilities=apUsbcSysDPDKMibCapabilities, apSmgmtDOSNotifyTrustedtoUntrustedCap=apSmgmtDOSNotifyTrustedtoUntrustedCap, apSmgmtHDRCap=apSmgmtHDRCap, apSecurityIkeInterfaceEapMethodsStatsCap=apSecurityIkeInterfaceEapMethodsStatsCap, apDNSALGNotifGroupCap=apDNSALGNotifGroupCap, apUsbcSysThreadCap2=apUsbcSysThreadCap2, apUsbcSysMibCapabilities=apUsbcSysMibCapabilities, apSnmpv3Cap=apSnmpv3Cap, apSecurityIkeDDoSCap=apSecurityIkeDDoSCap, apDDStatsGroup3Cap=apDDStatsGroup3Cap, apCodecRealmCodecCap2=apCodecRealmCodecCap2, apSecurityTacacsDownLocalAuthCap=apSecurityTacacsDownLocalAuthCap, apRadiusMibCap=apRadiusMibCap, apSmgmtRejectedMessagesCap=apSmgmtRejectedMessagesCap, apSmgmtXCodeOpusUtilCap=apSmgmtXCodeOpusUtilCap, apUdpCap=apUdpCap, apCodecRealmCodecCap8=apCodecRealmCodecCap8, apSmgmtCtrlStatsCap=apSmgmtCtrlStatsCap, apSmgmtH248Cap=apSmgmtH248Cap, apSmgmtH248PortMapUsageCap=apSmgmtH248PortMapUsageCap, apSmgmtCDRPushReceiverFailureCap=apSmgmtCDRPushReceiverFailureCap, apEnvMonCap4=apEnvMonCap4, apTcpCap2=apTcpCap2, apSmgmtClockNotifyCap=apSmgmtClockNotifyCap, apSmgmtSubscriptionSummaryCap=apSmgmtSubscriptionSummaryCap, apCodecRealmCodecCap9=apCodecRealmCodecCap9, apSipSecInterfaceRegNotifGroupCap=apSipSecInterfaceRegNotifGroupCap, apSipMSRPStatsCap=apSipMSRPStatsCap, apDiamAuthNotifyCap=apDiamAuthNotifyCap, apSipAudioVideoCallsCap=apSipAudioVideoCallsCap, apRadiusMibCapabilities=apRadiusMibCapabilities, apAclDropMibCapabilities=apAclDropMibCapabilities, apLicenseDBRegCap=apLicenseDBRegCap, apUsbcSysSmCap=apUsbcSysSmCap, apSnmpMibCapabilities=apSnmpMibCapabilities, apTcpCap=apTcpCap, apDiamNotifCap=apDiamNotifCap, apSmgmtRealmIcmpFailureCap=apSmgmtRealmIcmpFailureCap, apSecurityIkeInterfaceCap=apSecurityIkeInterfaceCap, apSmgmtSipMethodStatsCap=apSmgmtSipMethodStatsCap, apIpCap2=apIpCap2, apUsbcSysThreadMibCapabilities3=apUsbcSysThreadMibCapabilities3, apSwinventoryMibCapabilities=apSwinventoryMibCapabilities, apSipCACNotificationsGroupCap=apSipCACNotificationsGroupCap, apSipCACStatsCap=apSipCACStatsCap, apCodecRealmCodecCap10=apCodecRealmCodecCap10, apSmgmtRegistrationCap3=apSmgmtRegistrationCap3, apSipMibCapabilities=apSipMibCapabilities, apSmgmtCap3=apSmgmtCap3, apSmgmtSipRejectCap=apSmgmtSipRejectCap, apSmgmtApplicationCPUUsageCap=apSmgmtApplicationCPUUsageCap, apSmgmtDatabaseRegCap=apSmgmtDatabaseRegCap, apDNSALGRateGroupCap=apDNSALGRateGroupCap, apRadiusServerStatsCap=apRadiusServerStatsCap, apDDStatsGroup2Cap=apDDStatsGroup2Cap, apSmgmtInetAddrDOSNotifyCap=apSmgmtInetAddrDOSNotifyCap, apAmiCap=apAmiCap, apSmgmtCap=apSmgmtCap, apSmgmtPhyUtilCap=apSmgmtPhyUtilCap, apAmiMibCapabilities=apAmiMibCapabilities)
