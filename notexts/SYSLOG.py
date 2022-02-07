#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.8 at Mon Feb  7 15:49:37 2022
# On host fv-az77-513 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogEnableT, SyslogFilterSelectT = mibBuilder.importSymbols("ExaltComm", "SyslogEnableT", "SyslogFilterSelectT")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, ObjectIdentity, Gauge32, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32, ModuleIdentity, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32", "ModuleIdentity", "iso", "MibIdentifier")
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
mibBuilder.exportSymbols("SYSLOG", syslogRemoteIpAddr=syslogRemoteIpAddr, syslogCfg=syslogCfg, syslogFilterSelect=syslogFilterSelect, syslogEnable=syslogEnable, commitSyslogSettings=commitSyslogSettings, advSystemConfig=advSystemConfig)
