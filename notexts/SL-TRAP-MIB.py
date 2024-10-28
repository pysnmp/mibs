#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Mon Oct 28 02:13:28 2024
# On host fv-az1014-591 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmActive, slAlarmServiceAffect, slAlarmType, slAlarmIfIndex, slAlarmSeverity = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmActive", "slAlarmServiceAffect", "slAlarmType", "slAlarmIfIndex", "slAlarmSeverity")
edfaIfIndex, edfaStatus, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaIfIndex", "edfaStatus", "edfaOperControlMode")
slGenEventIfIndex, slGenEventType, slEventInventorySerial, slGenEventUser, slEventInventoryType, slEventInventoryIfIndex, slEventInventoryPartnum, slGenEventVal, slEventUser, slEventInventoryAction, slEventVal, slEventIfIndex, slEventType = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventIfIndex", "slGenEventType", "slEventInventorySerial", "slGenEventUser", "slEventInventoryType", "slEventInventoryIfIndex", "slEventInventoryPartnum", "slGenEventVal", "slEventUser", "slEventInventoryAction", "slEventVal", "slEventIfIndex", "slEventType")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsTrapsLoopbackActive, slTestsIfLoopIfIndex, slTestsIfLoopType = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsTrapsLoopbackActive", "slTestsIfLoopIfIndex", "slTestsIfLoopType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, ModuleIdentity, Integer32, NotificationType, iso, TimeTicks, ObjectIdentity, Counter32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "ModuleIdentity", "Integer32", "NotificationType", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", slEventInventoryTrapV1=slEventInventoryTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, edfaStatusChangeV1=edfaStatusChangeV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slAlarmTrapV1=slAlarmTrapV1, slGenEventTrapV1=slGenEventTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, slEventTrapV1=slEventTrapV1)
