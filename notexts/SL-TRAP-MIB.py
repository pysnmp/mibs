#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:59:34 2024
# On host fv-az1200-312 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmIfIndex, slAlarmType, slAlarmSeverity, slAlarmServiceAffect, slAlarmActive = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmIfIndex", "slAlarmType", "slAlarmSeverity", "slAlarmServiceAffect", "slAlarmActive")
edfaIfIndex, edfaOperControlMode, edfaStatus = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaIfIndex", "edfaOperControlMode", "edfaStatus")
slGenEventType, slEventInventoryPartnum, slEventType, slEventInventoryType, slGenEventVal, slEventInventoryIfIndex, slEventUser, slEventVal, slGenEventIfIndex, slEventIfIndex, slGenEventUser, slEventInventoryAction, slEventInventorySerial = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventType", "slEventInventoryPartnum", "slEventType", "slEventInventoryType", "slGenEventVal", "slEventInventoryIfIndex", "slEventUser", "slEventVal", "slGenEventIfIndex", "slEventIfIndex", "slGenEventUser", "slEventInventoryAction", "slEventInventorySerial")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigActiveConnectionRx, optApsConfigUserWorkingIndex = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx", "optApsConfigUserWorkingIndex")
slTestsTrapsLoopbackActive, slTestsIfLoopType, slTestsIfLoopIfIndex = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsTrapsLoopbackActive", "slTestsIfLoopType", "slTestsIfLoopIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ObjectIdentity, Unsigned32, IpAddress, Counter32, MibIdentifier, Gauge32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "Counter64")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", slGenEventTrapV1=slGenEventTrapV1, edfaStatusChangeV1=edfaStatusChangeV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, edfaControlModeChangeV1=edfaControlModeChangeV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slEventInventoryTrapV1=slEventInventoryTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slEventTrapV1=slEventTrapV1, slAlarmTrapV1=slAlarmTrapV1)
