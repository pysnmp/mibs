#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:11:14 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmType, slAlarmServiceAffect, slAlarmSeverity, slAlarmActive, slAlarmIfIndex = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmType", "slAlarmServiceAffect", "slAlarmSeverity", "slAlarmActive", "slAlarmIfIndex")
edfaIfIndex, edfaOperControlMode, edfaStatus = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaIfIndex", "edfaOperControlMode", "edfaStatus")
slGenEventUser, slGenEventIfIndex, slEventType, slEventVal, slEventInventoryType, slEventIfIndex, slEventUser, slEventInventoryIfIndex, slEventInventoryAction, slEventInventorySerial, slEventInventoryPartnum, slGenEventType, slGenEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventUser", "slGenEventIfIndex", "slEventType", "slEventVal", "slEventInventoryType", "slEventIfIndex", "slEventUser", "slEventInventoryIfIndex", "slEventInventoryAction", "slEventInventorySerial", "slEventInventoryPartnum", "slGenEventType", "slGenEventVal")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsTrapsLoopbackActive, slTestsIfLoopType, slTestsIfLoopIfIndex = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsTrapsLoopbackActive", "slTestsIfLoopType", "slTestsIfLoopIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Unsigned32, Counter64, ModuleIdentity, ObjectIdentity, iso, IpAddress, Gauge32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "Counter64", "ModuleIdentity", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", slEventInventoryTrapV1=slEventInventoryTrapV1, slAlarmTrapV1=slAlarmTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slEventTrapV1=slEventTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slGenEventTrapV1=slGenEventTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, edfaStatusChangeV1=edfaStatusChangeV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1)
