#
# PySNMP MIB module QOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/QOS
# Produced by pysmi-1.1.12 at Tue Jun  4 07:49:06 2024
# On host fv-az837-21 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
radioConfig, = mibBuilder.importSymbols("ExaltComProducts", "radioConfig")
QosTagT, VlanIdT, EnableStatusT = mibBuilder.importSymbols("ExaltComm", "QosTagT", "VlanIdT", "EnableStatusT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Counter64, TimeTicks, Unsigned32, iso, Bits, Gauge32, IpAddress, NotificationType, ModuleIdentity, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "Unsigned32", "iso", "Bits", "Gauge32", "IpAddress", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class QosPriorityT(TextualConvention, Integer32):
    description = 'This MIB variable sets Qos priority, the higher number \n                             the higher priority'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3))

class QosModeT(TextualConvention, Integer32):
    description = 'This MIB variable sets Qos Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4, 5, 6))
    namedValues = NamedValues(("disable", 0), ("qos-mode-802-1p", 4), ("qos-mode-diffserv", 5), ("qos-mode-port", 6))

class QosScheduleModeT(TextualConvention, Integer32):
    description = 'This MIB variable defines available QoS Scheduler modes'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("weighted-round-robin", 0), ("hybrid1-mode-3sp-2wrr-1wrr-0wrr", 1), ("hybrid2-mode-3sp-2sp-1wrr-0wrr", 2), ("strict-priority", 3))

class QosCos3WeightT(TextualConvention, Integer32):
    description = 'This MIB variable defines available weights for Queue 3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(8, 16, 32))
    namedValues = NamedValues(("w-8", 8), ("w-16", 16), ("w-32", 32))

class QosCos2WeightT(TextualConvention, Integer32):
    description = 'This MIB variable defines available weights for Queue 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(4, 8, 16))
    namedValues = NamedValues(("w-4", 4), ("w-8", 8), ("w-16", 16))

class QosCos1WeightT(TextualConvention, Integer32):
    description = 'This MIB variable defines available weights for Queue 1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 4, 8))
    namedValues = NamedValues(("w-2", 2), ("w-4", 4), ("w-8", 8))

class QosCos0WeightT(TextualConvention, Integer32):
    description = 'This MIB variable defines available weights for Queue 0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("w-1", 1), ("w-2", 2), ("w-4", 4))

advSystemConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5))
if mibBuilder.loadTexts: advSystemConfig.setStatus('current')
if mibBuilder.loadTexts: advSystemConfig.setDescription('This is the device specific advanced configuration section.')
extAirG2QoS = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8))
if mibBuilder.loadTexts: extAirG2QoS.setStatus('current')
if mibBuilder.loadTexts: extAirG2QoS.setDescription('QOS configuration.')
qosDefaultQueue = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosDefaultQueue.setStatus('current')
if mibBuilder.loadTexts: qosDefaultQueue.setDescription("The default queue to catch all traffic that don't belong to any queue.")
qosEth1Mode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 2), QosModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEth1Mode.setStatus('current')
if mibBuilder.loadTexts: qosEth1Mode.setDescription('This setting set the qos mode or disable QoS on ETH1.')
qosEth2Mode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 3), QosModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEth2Mode.setStatus('current')
if mibBuilder.loadTexts: qosEth2Mode.setDescription('This setting set the qos mode or disable QoS on ETH2.')
qosDiffServList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4), )
if mibBuilder.loadTexts: qosDiffServList.setStatus('current')
if mibBuilder.loadTexts: qosDiffServList.setDescription('This is a table of Qos DiffServ value and proiority.')
qosScheduler = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7))
if mibBuilder.loadTexts: qosScheduler.setStatus('current')
if mibBuilder.loadTexts: qosScheduler.setDescription('QOS Scheduler configuration.')
qosDiffServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1), ).setIndexNames((0, "QOS", "diffServValue"), (0, "QOS", "diffServPriority"), (0, "QOS", "diffServEnable"))
if mibBuilder.loadTexts: qosDiffServEntry.setStatus('current')
if mibBuilder.loadTexts: qosDiffServEntry.setDescription('This is DiffServ table entry.')
diffServValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServValue.setStatus('current')
if mibBuilder.loadTexts: diffServValue.setDescription('This is the value for the corresponding DiffServ table entry.')
diffServPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 2), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServPriority.setStatus('current')
if mibBuilder.loadTexts: diffServPriority.setDescription('This is the priority for the corresponding DiffServ table entry.')
diffServEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 4, 1, 3), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diffServEnable.setStatus('current')
if mibBuilder.loadTexts: diffServEnable.setDescription('This is the status for the corresponding  DiffServ table entry.')
qosPortETH1Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5))
qosEth1m802dot1pList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1), )
if mibBuilder.loadTexts: qosEth1m802dot1pList.setStatus('current')
if mibBuilder.loadTexts: qosEth1m802dot1pList.setDescription('This is a table of Qos 802.1p tag and proiority.')
qosEth1m802dot1pEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1), ).setIndexNames((0, "QOS", "tagEth1Priority"), (0, "QOS", "tagEth1Status"))
if mibBuilder.loadTexts: qosEth1m802dot1pEntry.setStatus('current')
if mibBuilder.loadTexts: qosEth1m802dot1pEntry.setDescription('This is a 802.1p table entry.')
tagEth1Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth1Priority.setStatus('current')
if mibBuilder.loadTexts: tagEth1Priority.setDescription('This is the priority for the corresponding ETH1 802.1p tag entry.')
tagEth1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 1, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth1Status.setStatus('current')
if mibBuilder.loadTexts: tagEth1Status.setDescription('This is the status for the corresponding ETH1 802.1p tag entry.')
qosEth1PortList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2), )
if mibBuilder.loadTexts: qosEth1PortList.setStatus('current')
if mibBuilder.loadTexts: qosEth1PortList.setDescription('This is a table of Qos Port mode.')
qosEth1PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1), ).setIndexNames((0, "QOS", "portEth1Priority"), (0, "QOS", "portEth1Status"))
if mibBuilder.loadTexts: qosEth1PortEntry.setStatus('current')
if mibBuilder.loadTexts: qosEth1PortEntry.setDescription('This is a Port mode table entry.')
portEth1Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth1Priority.setStatus('current')
if mibBuilder.loadTexts: portEth1Priority.setDescription('This is the priority for the corresponding ETH1 Port mode entry.')
portEth1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 5, 2, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth1Status.setStatus('current')
if mibBuilder.loadTexts: portEth1Status.setDescription('This is the status for the corresponding ETH1 Port mode entry.')
qosPortETH2Conf = MibIdentifier((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6))
qosEth2m802dot1pList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1), )
if mibBuilder.loadTexts: qosEth2m802dot1pList.setStatus('current')
if mibBuilder.loadTexts: qosEth2m802dot1pList.setDescription('This is a table of Qos 802.1p tag and proiority.')
qosEth2m802dot1pEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1), ).setIndexNames((0, "QOS", "tagEth2Priority"), (0, "QOS", "tagEth2Status"))
if mibBuilder.loadTexts: qosEth2m802dot1pEntry.setStatus('current')
if mibBuilder.loadTexts: qosEth2m802dot1pEntry.setDescription('This is a 802.1p table entry.')
tagEth2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth2Priority.setStatus('current')
if mibBuilder.loadTexts: tagEth2Priority.setDescription('This is the priority for the corresponding ETH2 802.1p tag entry.')
tagEth2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 1, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tagEth2Status.setStatus('current')
if mibBuilder.loadTexts: tagEth2Status.setDescription('This is the status for the corresponding ETH2 802.1p tag entry.')
qosEth2PortList = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2), )
if mibBuilder.loadTexts: qosEth2PortList.setStatus('current')
if mibBuilder.loadTexts: qosEth2PortList.setDescription('This is a table of Qos Port mode.')
qosEth2PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1), ).setIndexNames((0, "QOS", "portEth2Priority"), (0, "QOS", "portEth2Status"))
if mibBuilder.loadTexts: qosEth2PortEntry.setStatus('current')
if mibBuilder.loadTexts: qosEth2PortEntry.setDescription('This is a ETH2 Port mode table entry.')
portEth2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1, 1), QosPriorityT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth2Priority.setStatus('current')
if mibBuilder.loadTexts: portEth2Priority.setDescription('This is the priority for the corresponding ETH2 Port mode entry.')
portEth2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 6, 2, 1, 2), EnableStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portEth2Status.setStatus('current')
if mibBuilder.loadTexts: portEth2Status.setDescription('This is the status for the corresponding ETH2 Port mode entry.')
qosScheduleMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 1), QosScheduleModeT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosScheduleMode.setStatus('current')
if mibBuilder.loadTexts: qosScheduleMode.setDescription('The QoS queues scheduler mode')
qosCos3Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 2), QosCos3WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos3Weight.setStatus('current')
if mibBuilder.loadTexts: qosCos3Weight.setDescription('QoS queue 3 weight.')
qosCos2Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 3), QosCos2WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos2Weight.setStatus('current')
if mibBuilder.loadTexts: qosCos2Weight.setDescription('QoS queue 2 weight.')
qosCos1Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 4), QosCos1WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos1Weight.setStatus('current')
if mibBuilder.loadTexts: qosCos1Weight.setDescription('QoS queue 1 weight.')
qosCos0Weight = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 7, 5), QosCos0WeightT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCos0Weight.setStatus('current')
if mibBuilder.loadTexts: qosCos0Weight.setDescription('QoS queue 0 weight.')
commitQosSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 5, 8, 1000), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitQosSettings.setStatus('current')
if mibBuilder.loadTexts: commitQosSettings.setDescription('This command allows saving or clear configuration.\n                            Options are: save, clear, correspondingly saving changes to\n                            configuration to the persistent storage or clearing unsaved changes.')
mibBuilder.exportSymbols("QOS", qosEth2PortEntry=qosEth2PortEntry, qosEth2Mode=qosEth2Mode, portEth2Priority=portEth2Priority, QosModeT=QosModeT, extAirG2QoS=extAirG2QoS, QosPriorityT=QosPriorityT, qosEth1PortList=qosEth1PortList, commitQosSettings=commitQosSettings, QosScheduleModeT=QosScheduleModeT, qosEth1PortEntry=qosEth1PortEntry, QosCos1WeightT=QosCos1WeightT, QosCos0WeightT=QosCos0WeightT, qosEth1Mode=qosEth1Mode, diffServEnable=diffServEnable, tagEth2Priority=tagEth2Priority, tagEth2Status=tagEth2Status, portEth1Priority=portEth1Priority, portEth1Status=portEth1Status, advSystemConfig=advSystemConfig, qosDiffServList=qosDiffServList, qosEth1m802dot1pEntry=qosEth1m802dot1pEntry, qosEth2PortList=qosEth2PortList, qosCos0Weight=qosCos0Weight, qosCos2Weight=qosCos2Weight, qosEth2m802dot1pList=qosEth2m802dot1pList, qosCos3Weight=qosCos3Weight, tagEth1Status=tagEth1Status, diffServPriority=diffServPriority, tagEth1Priority=tagEth1Priority, qosScheduler=qosScheduler, diffServValue=diffServValue, QosCos2WeightT=QosCos2WeightT, QosCos3WeightT=QosCos3WeightT, qosEth2m802dot1pEntry=qosEth2m802dot1pEntry, qosDefaultQueue=qosDefaultQueue, qosEth1m802dot1pList=qosEth1m802dot1pList, qosCos1Weight=qosCos1Weight, qosDiffServEntry=qosDiffServEntry, qosPortETH2Conf=qosPortETH2Conf, qosScheduleMode=qosScheduleMode, qosPortETH1Conf=qosPortETH1Conf, portEth2Status=portEth2Status)
