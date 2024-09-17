#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.12 at Tue Sep 17 12:22:09 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogFilterSelectT, SyslogEnableT = mibBuilder.importSymbols("ExaltComm", "SyslogFilterSelectT", "SyslogEnableT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, Integer32, Bits, Counter32, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Gauge32, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Integer32", "Bits", "Counter32", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Gauge32", "TimeTicks", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
advSystemConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5))
if mibBuilder.loadTexts: advSystemConfig.setStatus('current')
syslogCfg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6))
if mibBuilder.loadTexts: syslogCfg.setStatus('current')
syslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1), SyslogEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogEnable.setStatus('current')
syslogRemoteIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRemoteIpAddr.setStatus('current')
syslogFilterSelect = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 3), SyslogFilterSelectT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogFilterSelect.setStatus('current')
commitSyslogSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1000), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitSyslogSettings.setStatus('current')
mibBuilder.exportSymbols("SYSLOG", syslogEnable=syslogEnable, syslogCfg=syslogCfg, syslogRemoteIpAddr=syslogRemoteIpAddr, commitSyslogSettings=commitSyslogSettings, advSystemConfig=advSystemConfig, syslogFilterSelect=syslogFilterSelect)
