#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:30:56 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmServiceAffect, slAlarmIfIndex, slAlarmSeverity, slAlarmActive, slAlarmType = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmServiceAffect", "slAlarmIfIndex", "slAlarmSeverity", "slAlarmActive", "slAlarmType")
edfaStatus, edfaIfIndex, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaIfIndex", "edfaOperControlMode")
slGenEventUser, slGenEventIfIndex, slEventType, slEventInventoryIfIndex, slEventInventoryType, slEventIfIndex, slEventInventorySerial, slEventInventoryPartnum, slEventUser, slGenEventType, slEventVal, slEventInventoryAction, slGenEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventUser", "slGenEventIfIndex", "slEventType", "slEventInventoryIfIndex", "slEventInventoryType", "slEventIfIndex", "slEventInventorySerial", "slEventInventoryPartnum", "slEventUser", "slGenEventType", "slEventVal", "slEventInventoryAction", "slGenEventVal")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopIfIndex, slTestsTrapsLoopbackActive, slTestsIfLoopType = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopIfIndex", "slTestsTrapsLoopbackActive", "slTestsIfLoopType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, NotificationType, Counter32, ModuleIdentity, MibIdentifier, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "NotificationType", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slEventTrapV1=slEventTrapV1, slEventInventoryTrapV1=slEventInventoryTrapV1, slAlarmTrapV1=slAlarmTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slGenEventTrapV1=slGenEventTrapV1, edfaStatusChangeV1=edfaStatusChangeV1, edfaControlModeChangeV1=edfaControlModeChangeV1)
