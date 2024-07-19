#
# PySNMP MIB module SL-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-TRAP-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:05:53 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
tftpStatus, = mibBuilder.importSymbols("RAD-MIB", "tftpStatus")
slAlarmActive, slAlarmSeverity, slAlarmIfIndex, slAlarmServiceAffect, slAlarmType = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmActive", "slAlarmSeverity", "slAlarmIfIndex", "slAlarmServiceAffect", "slAlarmType")
edfaStatus, edfaOperControlMode, edfaIfIndex = mibBuilder.importSymbols("SL-EDFA-MIB", "edfaStatus", "edfaOperControlMode", "edfaIfIndex")
slEventInventoryAction, slGenEventType, slEventIfIndex, slEventInventoryType, slGenEventVal, slEventInventorySerial, slEventInventoryPartnum, slEventUser, slGenEventIfIndex, slEventInventoryIfIndex, slEventVal, slGenEventUser, slEventType = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventInventoryAction", "slGenEventType", "slEventIfIndex", "slEventInventoryType", "slGenEventVal", "slEventInventorySerial", "slEventInventoryPartnum", "slEventUser", "slGenEventIfIndex", "slEventInventoryIfIndex", "slEventVal", "slGenEventUser", "slEventType")
packetlight, = mibBuilder.importSymbols("SL-NE-MIB", "packetlight")
optApsConfigUserWorkingIndex, optApsConfigActiveConnectionRx = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex", "optApsConfigActiveConnectionRx")
slTestsIfLoopIfIndex, slTestsIfLoopType, slTestsTrapsLoopbackActive = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsIfLoopIfIndex", "slTestsIfLoopType", "slTestsTrapsLoopbackActive")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, NotificationType, IpAddress, ObjectIdentity, Counter64, Gauge32, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "NotificationType", "IpAddress", "ObjectIdentity", "Counter64", "Gauge32", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
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
mibBuilder.exportSymbols("SL-TRAP-MIB", slEventTrapV1=slEventTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, edfaControlModeChangeV1=edfaControlModeChangeV1, slEventInventoryTrapV1=slEventInventoryTrapV1, edfaStatusChangeV1=edfaStatusChangeV1, slGenEventTrapV1=slGenEventTrapV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slAlarmTrapV1=slAlarmTrapV1, tftpStatusChangeTrapV1=tftpStatusChangeTrapV1)
