#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.8 at Mon Sep 19 08:29:20 2022
# On host fv-az152-47 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogFilterSelectT, SyslogEnableT = mibBuilder.importSymbols("ExaltComm", "SyslogFilterSelectT", "SyslogEnableT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32, Integer32, Bits, IpAddress, MibIdentifier, ObjectIdentity, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32", "Integer32", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "ModuleIdentity")
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
mibBuilder.exportSymbols("SYSLOG", advSystemConfig=advSystemConfig, syslogFilterSelect=syslogFilterSelect, syslogEnable=syslogEnable, syslogRemoteIpAddr=syslogRemoteIpAddr, syslogCfg=syslogCfg, commitSyslogSettings=commitSyslogSettings)
