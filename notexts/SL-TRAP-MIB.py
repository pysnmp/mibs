#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:16:17 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmSeverity, slAlarmType, slAlarmIfIndex, slAlarmActive, slAlarmServiceAffect = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmSeverity", "slAlarmType", "slAlarmIfIndex", "slAlarmActive", "slAlarmServiceAffect")
edfaOperControlMode, edfaIfIndex, edfaStatus = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaOperControlMode", "edfaIfIndex", "edfaStatus")
slGenEventUser, slEventInventoryIfIndex, slGenEventType, slEventUser, slGenEventIfIndex, slEventInventoryType, slEventType, slEventIfIndex, slEventInventorySerial, slEventInventoryPartnum, slEventVal, slEventInventoryAction, slGenEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventUser", "slEventInventoryIfIndex", "slGenEventType", "slEventUser", "slGenEventIfIndex", "slEventInventoryType", "slEventType", "slEventIfIndex", "slEventInventorySerial", "slEventInventoryPartnum", "slEventVal", "slEventInventoryAction", "slGenEventVal")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigActiveConnectionRx, optApsConfigUserWorkingIndex = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx", "optApsConfigUserWorkingIndex")
slTestsIfLoopType, slTestsIfLoopIfIndex, slTestsTrapsLoopbackActive = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsIfLoopIfIndex", "slTestsTrapsLoopbackActive")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Counter32, Counter64, iso, NotificationType, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Counter32", "Counter64", "iso", "NotificationType", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
slAlarmTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,101)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"))
slTestsTrapsLoopbackTableChangedV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,122)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
edfaStatusChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,128)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaStatus"))
edfaControlModeChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,129)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaOperControlMode"))
optApsTrapSwitchoverV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,130)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
slEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,131)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
tftpStatusChangeTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,132)).setObjects(("RAD-MIB", "tftpStatus"))
slEventInventoryTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,133)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
slGenEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,134)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
mibBuilder.exportSymbols("SL-TRAP-MIB", slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slEventTrapV1=slEventTrapV1, slAlarmTrapV1=slAlarmTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, slEventInventoryTrapV1=slEventInventoryTrapV1, slGenEventTrapV1=slGenEventTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, edfaStatusChangeV1=edfaStatusChangeV1)
