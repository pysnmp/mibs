#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed May 29 06:49:16 2024
# On host fv-az1019-850 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmSeverity, slAlarmIfIndex, slAlarmServiceAffect, slAlarmType, slAlarmActive = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmSeverity", "slAlarmIfIndex", "slAlarmServiceAffect", "slAlarmType", "slAlarmActive")
edfaStatus, edfaOperControlMode, edfaIfIndex = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaOperControlMode", "edfaIfIndex")
slEventIfIndex, slEventType, slGenEventIfIndex, slEventInventoryIfIndex, slGenEventUser, slEventUser, slEventInventoryAction, slEventInventoryType, slGenEventType, slEventInventorySerial, slGenEventVal, slEventVal, slEventInventoryPartnum = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventIfIndex", "slEventType", "slGenEventIfIndex", "slEventInventoryIfIndex", "slGenEventUser", "slEventUser", "slEventInventoryAction", "slEventInventoryType", "slGenEventType", "slEventInventorySerial", "slGenEventVal", "slEventVal", "slEventInventoryPartnum")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopIfIndex, slTestsTrapsLoopbackActive, slTestsIfLoopType = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopIfIndex", "slTestsTrapsLoopbackActive", "slTestsIfLoopType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Integer32, iso, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "Counter64")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, edfaStatusChangeV1=edfaStatusChangeV1, slEventTrapV1=slEventTrapV1, slEventInventoryTrapV1=slEventInventoryTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, slGenEventTrapV1=slGenEventTrapV1, slAlarmTrapV1=slAlarmTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1)
