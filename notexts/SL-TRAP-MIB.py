#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 07:34:06 2022
# On host fv-az215-626 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmSeverity, slAlarmServiceAffect, slAlarmActive, slAlarmType, slAlarmIfIndex = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmSeverity", "slAlarmServiceAffect", "slAlarmActive", "slAlarmType", "slAlarmIfIndex")
edfaIfIndex, edfaStatus, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaIfIndex", "edfaStatus", "edfaOperControlMode")
slEventType, slGenEventIfIndex, slEventVal, slEventInventoryAction, slEventInventorySerial, slGenEventVal, slEventInventoryIfIndex, slEventInventoryPartnum, slEventUser, slGenEventUser, slEventIfIndex, slEventInventoryType, slGenEventType = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventType", "slGenEventIfIndex", "slEventVal", "slEventInventoryAction", "slEventInventorySerial", "slGenEventVal", "slEventInventoryIfIndex", "slEventInventoryPartnum", "slEventUser", "slGenEventUser", "slEventIfIndex", "slEventInventoryType", "slGenEventType")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigActiveConnectionRx, optApsConfigUserWorkingIndex = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx", "optApsConfigUserWorkingIndex")
slTestsIfLoopType, slTestsIfLoopIfIndex, slTestsTrapsLoopbackActive = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsIfLoopIfIndex", "slTestsTrapsLoopbackActive")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32, Gauge32, IpAddress, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32", "Gauge32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
slAlarmTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,101)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"))
slTestsTrapsLoopbackTableChangedV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,122)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
edfaStatusChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,128)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaStatus"))
edfaControlModeChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,129)).setObjects(("SL-EDFA-MIB", "edfaIfIndex"), ("SL-EDFA-MIB", "edfaOperControlMode"))
optApsTrapSwitchoverV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,130)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
slEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,131)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
tftpStatusChangeTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,132)).setObjects(("RAD-MIB", "tftpStatus"))
slEventInventoryTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,133)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
slGenEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,134)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
mibBuilder.exportSymbols("SL-TRAP-MIB", slAlarmTrapV1=slAlarmTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slGenEventTrapV1=slGenEventTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slEventTrapV1=slEventTrapV1, slEventInventoryTrapV1=slEventInventoryTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, edfaStatusChangeV1=edfaStatusChangeV1)
