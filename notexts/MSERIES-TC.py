#
# PySNMP MIB module MSERIES-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-TC
# Produced by pysmi-1.1.12 at Thu May 30 02:21:31 2024
# On host fv-az775-912 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, iso, Bits, NotificationType, ModuleIdentity, Gauge32, Unsigned32, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "Bits", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
smartTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 5))
smartTcMIB.setRevisions(('2014-02-12 13:27', '2013-10-15 13:41', '2011-12-05 00:00',))
if mibBuilder.loadTexts: smartTcMIB.setLastUpdated('201402121327Z')
if mibBuilder.loadTexts: smartTcMIB.setOrganization('SmartOptics')
class AlarmPerceivedSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class AlarmNotificationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmental", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViloation", 10), ("timeDomainViolation", 11))

class AlarmProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57))
    namedValues = NamedValues(("undefined", 0), ("adapterError", 1), ("applicationSubsystemFailure", 2), ("bandwidthReduced", 3), ("callEstablishmentError", 4), ("communicationsProtocolError", 5), ("communicationsSubsystemFailure", 6), ("configurationOrCustomizationError", 7), ("congestion", 8), ("corruptData", 9), ("cpuCyclesLimitExceeded", 10), ("dTEdCEInterfaceError", 11), ("datasetOrModemError", 12), ("degradedSignal", 13), ("enclosureDoorOpen", 14), ("equipmentMalfunction", 15), ("excessiveVibration", 16), ("fileError", 17), ("fireDetected", 18), ("floodDetected", 19), ("framingError", 20), ("heatingOrVentilationOrCoolingSystemProblem", 21), ("humidityUnacceptable", 22), ("inputDeviceError", 23), ("inputOutputDeviceError", 24), ("lANError", 25), ("leakDetected", 26), ("localNodeTransmissionError", 27), ("lossOfFrame", 28), ("lossOfSignal", 29), ("materialSupplyExhausted", 30), ("multiplexerProblem", 31), ("outOfMemory", 32), ("outputDeviceError", 33), ("performanceDegraded", 34), ("powerProblem", 35), ("pressureUnacceptable", 36), ("processorProblem", 37), ("pumpFailure", 38), ("queueSizeExceeded", 39), ("receiveFailure", 40), ("receiverFailure", 41), ("remoteNodeTransmissionError", 42), ("resourceAtOrNearingCapacity", 43), ("responseTimeExcessive", 44), ("retransmissionRateExcessive", 45), ("softwareProgramError", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("storageCapacityProblem", 49), ("temperatureUnacceptable", 50), ("thresholdCrossed", 51), ("timingProblem", 52), ("toxicLeakDetected", 53), ("transmitFailure", 54), ("transmitterFailure", 55), ("underlyingResourceUnavailable", 56), ("versionMismatch", 57))

class UnitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nmb", 1), ("psu1", 2), ("psu2", 3), ("fan", 4), ("system", 5), ("slaveNmb", 6), ("slavePsu1", 7), ("slavePsu2", 8), ("slaveFan", 9))

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("biDi", 3))

class PortStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("idle", 1), ("down", 2), ("up", 3), ("high", 4), ("low", 5), ("eyeSafety", 6), ("cd", 7), ("ncd", 8))

class PortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("service", 2))

mibBuilder.exportSymbols("MSERIES-TC", PYSNMP_MODULE_ID=smartTcMIB, AlarmPerceivedSeverity=AlarmPerceivedSeverity, PortType=PortType, UnitType=UnitType, PortMode=PortMode, smartTcMIB=smartTcMIB, AlarmNotificationType=AlarmNotificationType, PortStatus=PortStatus, AlarmProbableCause=AlarmProbableCause)
