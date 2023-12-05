#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.11 at Tue Dec  5 02:33:35 2023
# On host fv-az1535-909 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmIfIndex, slAlarmServiceAffect, slAlarmType, slAlarmSeverity, slAlarmActive = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmIfIndex", "slAlarmServiceAffect", "slAlarmType", "slAlarmSeverity", "slAlarmActive")
edfaStatus, edfaIfIndex, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaIfIndex", "edfaOperControlMode")
slGenEventIfIndex, slEventInventoryAction, slEventUser, slGenEventVal, slGenEventType, slEventVal, slGenEventUser, slEventIfIndex, slEventInventoryIfIndex, slEventInventoryType, slEventInventorySerial, slEventType, slEventInventoryPartnum = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventIfIndex", "slEventInventoryAction", "slEventUser", "slGenEventVal", "slGenEventType", "slEventVal", "slGenEventUser", "slEventIfIndex", "slEventInventoryIfIndex", "slEventInventoryType", "slEventInventorySerial", "slEventType", "slEventInventoryPartnum")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopType, slTestsTrapsLoopbackActive, slTestsIfLoopIfIndex = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsTrapsLoopbackActive", "slTestsIfLoopIfIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Gauge32, iso, MibIdentifier, ObjectIdentity, Bits, TimeTicks, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Gauge32", "iso", "MibIdentifier", "ObjectIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", edfaStatusChangeV1=edfaStatusChangeV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slAlarmTrapV1=slAlarmTrapV1, slEventTrapV1=slEventTrapV1, slEventInventoryTrapV1=slEventInventoryTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slGenEventTrapV1=slGenEventTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, edfaControlModeChangeV1=edfaControlModeChangeV1)
