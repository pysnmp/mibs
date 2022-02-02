#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.8 at Wed Feb  2 18:23:21 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogFilterSelectT, SyslogEnableT = mibBuilder.importSymbols("ExaltComm", "SyslogFilterSelectT", "SyslogEnableT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, ModuleIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity, TimeTicks, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "NotificationType", "Integer32")
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
mibBuilder.exportSymbols("SYSLOG", syslogRemoteIpAddr=syslogRemoteIpAddr, syslogCfg=syslogCfg, syslogEnable=syslogEnable, advSystemConfig=advSystemConfig, syslogFilterSelect=syslogFilterSelect, commitSyslogSettings=commitSyslogSettings)
