#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Sat Jul  6 01:12:24 2024
# On host fv-az1532-138 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmServiceAffect, slAlarmActive, slAlarmType, slAlarmSeverity, slAlarmIfIndex = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmServiceAffect", "slAlarmActive", "slAlarmType", "slAlarmSeverity", "slAlarmIfIndex")
edfaOperControlMode, edfaStatus, edfaIfIndex = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaOperControlMode", "edfaStatus", "edfaIfIndex")
slGenEventUser, slEventIfIndex, slEventInventoryIfIndex, slEventType, slEventInventoryPartnum, slEventInventoryType, slEventInventorySerial, slGenEventVal, slGenEventIfIndex, slEventInventoryAction, slGenEventType, slEventUser, slEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slGenEventUser", "slEventIfIndex", "slEventInventoryIfIndex", "slEventType", "slEventInventoryPartnum", "slEventInventoryType", "slEventInventorySerial", "slGenEventVal", "slGenEventIfIndex", "slEventInventoryAction", "slGenEventType", "slEventUser", "slEventVal")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopType, slTestsIfLoopIfIndex, slTestsTrapsLoopbackActive = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopType", "slTestsIfLoopIfIndex", "slTestsTrapsLoopbackActive")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, Counter64, ModuleIdentity, Gauge32, Counter32, ObjectIdentity, MibIdentifier, Bits, Integer32, Unsigned32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "Integer32", "Unsigned32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", edfaControlModeChangeV1=edfaControlModeChangeV1, slEventTrapV1=slEventTrapV1, slAlarmTrapV1=slAlarmTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slGenEventTrapV1=slGenEventTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1, edfaStatusChangeV1=edfaStatusChangeV1, slEventInventoryTrapV1=slEventInventoryTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1)
