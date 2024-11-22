#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:46:59 2024
# On host fv-az1437-189 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmServiceAffect, slAlarmIfIndex, slAlarmType, slAlarmActive, slAlarmSeverity = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmServiceAffect", "slAlarmIfIndex", "slAlarmType", "slAlarmActive", "slAlarmSeverity")
edfaStatus, edfaIfIndex, edfaOperControlMode = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaIfIndex", "edfaOperControlMode")
slEventInventorySerial, slEventInventoryType, slGenEventUser, slEventVal, slEventIfIndex, slEventInventoryPartnum, slEventInventoryIfIndex, slEventInventoryAction, slGenEventType, slEventUser, slGenEventIfIndex, slEventType, slGenEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventInventorySerial", "slEventInventoryType", "slGenEventUser", "slEventVal", "slEventIfIndex", "slEventInventoryPartnum", "slEventInventoryIfIndex", "slEventInventoryAction", "slGenEventType", "slEventUser", "slGenEventIfIndex", "slEventType", "slGenEventVal")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopType, slTestsTrapsLoopbackActive, slTestsIfLoopIfIndex = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsTrapsLoopbackActive", "slTestsIfLoopIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, Counter64, Gauge32, Unsigned32, iso, Counter32, IpAddress, ObjectIdentity, NotificationType, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "iso", "Counter32", "IpAddress", "ObjectIdentity", "NotificationType", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slEventTrapV1=slEventTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, edfaControlModeChangeV1=edfaControlModeChangeV1, edfaStatusChangeV1=edfaStatusChangeV1, slEventInventoryTrapV1=slEventInventoryTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slGenEventTrapV1=slGenEventTrapV1, slAlarmTrapV1=slAlarmTrapV1)
