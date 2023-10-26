#
# PySNMP MIB module SYSLOG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/SYSLOG
# Produced by pysmi-1.1.8 at Thu Oct 26 09:02:55 2023
# On host fv-az1032-268 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
SyslogEnableT, SyslogFilterSelectT = mibBuilder.importSymbols("ExaltComm", "SyslogEnableT", "SyslogFilterSelectT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Unsigned32, iso, Gauge32, Counter32, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, MibIdentifier, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Unsigned32", "iso", "Gauge32", "Counter32", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "MibIdentifier", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
advSystemConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5))
if mibBuilder.loadTexts: advSystemConfig.setStatus('current')
if mibBuilder.loadTexts: advSystemConfig.setDescription('This is the device specific advanced configuration section.')
syslogCfg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6))
if mibBuilder.loadTexts: syslogCfg.setStatus('current')
if mibBuilder.loadTexts: syslogCfg.setDescription('Syslog remote logging configuration.')
syslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1), SyslogEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogEnable.setStatus('current')
if mibBuilder.loadTexts: syslogEnable.setDescription('this mib to enable/disable the Syslog remote logging in the radio.\n\t                     0 - disbale Syslog remote logging. \n\t\t\t     1 - enable Syslog remote logging.')
syslogRemoteIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRemoteIpAddr.setStatus('current')
if mibBuilder.loadTexts: syslogRemoteIpAddr.setDescription('IP address of the remote host the Syslog event messages being sent to.\n\t                     IP address is in xxx.xxx.xxx.xxx format')
syslogFilterSelect = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 3), SyslogFilterSelectT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogFilterSelect.setStatus('current')
if mibBuilder.loadTexts: syslogFilterSelect.setDescription('logging filter selection.\n\t                   \n\t\t\t    0 - All - send all event messages to remote                    \n\t\t\t    1 - Minor - Minor only                 \n\t\t\t    2 - Minor, Major and critical                  \n\t\t\t    3 - Major only          \n\t\t\t    4 - Major and Critical                \n\t\t\t    5 - Critical only.')
commitSyslogSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 6, 1000), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitSyslogSettings.setStatus('current')
if mibBuilder.loadTexts: commitSyslogSettings.setDescription('This command allows saving or clear the Syslog configuration.\n                            Option strings to be written are: save, clear, correspondingly saving changes to\n                            configuration to the persistent storage or clearing unsaved changes.')
mibBuilder.exportSymbols("SYSLOG", advSystemConfig=advSystemConfig, syslogRemoteIpAddr=syslogRemoteIpAddr, syslogFilterSelect=syslogFilterSelect, syslogEnable=syslogEnable, syslogCfg=syslogCfg, commitSyslogSettings=commitSyslogSettings)
