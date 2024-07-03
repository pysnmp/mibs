#
# PySNMP MIB module ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ETHERNET-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:03:05 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
locEthAlarms, interface, remEthAlarms = mibBuilder.importSymbols("ExaltComProducts", "locEthAlarms", "interface", "remEthAlarms")
EthernetMgmtTypeT, EnableStatusT, AlarmLevelT = mibBuilder.importSymbols("ExaltComm", "EthernetMgmtTypeT", "EnableStatusT", "AlarmLevelT")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter32, MibIdentifier, ObjectIdentity, IpAddress, TimeTicks, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Bits, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "MibIdentifier", "ObjectIdentity", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Bits", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class EthernetFunctionT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("traffic", 0), ("mgmt", 1), ("trafficmgmt", 2))

class EthernetModeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("full1000", 0), ("half1000", 1), ("full100", 2), ("half100", 3), ("full10", 4), ("half10", 5), ("auto", 6))

class EthRateLimitTypeT(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("kbps", 0), ("mbps", 1))

class EthRateLimitValueT(TextualConvention, Integer32):
    status = 'current'

ethernet = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1))
if mibBuilder.loadTexts: ethernet.setStatus('current')
ethernetNumChannels = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 3), Gauge32()).setUnits('channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetNumChannels.setStatus('current')
ethernetInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4), )
if mibBuilder.loadTexts: ethernetInterfaces.setStatus('current')
ethernetInterface = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1), ).setIndexNames((0, "ETHERNET-MIB", "function"), (0, "ETHERNET-MIB", "mode"), (0, "ETHERNET-MIB", "alarm"), (0, "ETHERNET-MIB", "mute"), (0, "ETHERNET-MIB", "dhcp"), (0, "ETHERNET-MIB", "rateConfig"), (0, "ETHERNET-MIB", "rateType"), (0, "ETHERNET-MIB", "rateLimit"))
if mibBuilder.loadTexts: ethernetInterface.setStatus('current')
function = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 1), EthernetFunctionT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: function.setStatus('current')
mode = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 2), EthernetModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mode.setStatus('current')
alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 3), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm.setStatus('current')
mute = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 4), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mute.setStatus('current')
rateConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 5), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateConfig.setStatus('current')
rateType = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 6), EthRateLimitTypeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateType.setStatus('current')
rateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 7), EthRateLimitValueT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rateLimit.setStatus('current')
dhcp = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 8), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcp.setStatus('current')
ethernetLearning = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 5), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetLearning.setStatus('current')
ethernetMgmt = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 6), EthernetMgmtTypeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetMgmt.setStatus('current')
ethernetFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 7), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetFlowControl.setStatus('current')
commitEthernetSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitEthernetSettings.setStatus('current')
locETHAlarms = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1), )
if mibBuilder.loadTexts: locETHAlarms.setStatus('current')
locEthAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1), ).setIndexNames((0, "ETHERNET-MIB", "locEthAlarm"))
if mibBuilder.loadTexts: locEthAlarmsEntry.setStatus('current')
locEthAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1, 1), AlarmLevelT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: locEthAlarm.setStatus('current')
remETHAlarms = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1), )
if mibBuilder.loadTexts: remETHAlarms.setStatus('current')
remEthAlarmsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1), ).setIndexNames((0, "ETHERNET-MIB", "remEthAlarm"))
if mibBuilder.loadTexts: remEthAlarmsEntry.setStatus('current')
remEthAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1, 1), AlarmLevelT()).setMaxAccess("readonly")
if mibBuilder.loadTexts: remEthAlarm.setStatus('current')
mibBuilder.exportSymbols("ETHERNET-MIB", rateLimit=rateLimit, alarm=alarm, remEthAlarm=remEthAlarm, remEthAlarmsEntry=remEthAlarmsEntry, function=function, remETHAlarms=remETHAlarms, EthernetFunctionT=EthernetFunctionT, ethernetFlowControl=ethernetFlowControl, ethernetInterface=ethernetInterface, ethernetLearning=ethernetLearning, EthernetModeT=EthernetModeT, mode=mode, ethernetNumChannels=ethernetNumChannels, locEthAlarmsEntry=locEthAlarmsEntry, rateType=rateType, locETHAlarms=locETHAlarms, commitEthernetSettings=commitEthernetSettings, EthRateLimitValueT=EthRateLimitValueT, locEthAlarm=locEthAlarm, ethernetInterfaces=ethernetInterfaces, ethernet=ethernet, ethernetMgmt=ethernetMgmt, rateConfig=rateConfig, dhcp=dhcp, EthRateLimitTypeT=EthRateLimitTypeT, mute=mute)
