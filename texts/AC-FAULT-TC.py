#
# PySNMP MIB module AC-FAULT-TC (http://snmplabs.com/pysmi)
# ASN.1 source AC-FAULT-TC
# Source digest sha256:7f900253aef9e59d988758afe10278eb37359a476bc80781c222973e0ba6b4f8
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
class AcAlarmSeverity(TextualConvention, Integer32):
    description = 'ISO/IEC 10164-4, ITU X.733 alarm severities'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("cleared", 0), ("indeterminate", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5))

class AcAlarmEventType(TextualConvention, Integer32):
    description = 'ISO/IEC 10164-4, ITU X.733 event types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("communicationsAlarm", 1), ("qualityOfServiceAlarm", 2), ("processingErrorAlarm", 3), ("equipmentAlarm", 4), ("environmentalAlarm", 5))

class AcAlarmProbableCause(TextualConvention, Integer32):
    description = 'ISO/IEC 10164-4, ITU X.733 probable causes'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74))
    namedValues = NamedValues(("other", 0), ("adapterError", 1), ("applicationSubsystemFailure", 2), ("bandwidthReduced", 3), ("callEstablishmentError", 4), ("communicationsProtocolError", 5), ("communicationsSubsystemFailure", 6), ("configurationOrCustomizationError", 7), ("congestion", 8), ("corruptData", 9), ("cpuCyclesLimitExceeded", 10), ("dataSetOrModemError", 11), ("degradedSignal", 12), ("dteDceInterfaceError", 13), ("enclosureDoorOpen", 14), ("equipmentMalfunction", 15), ("excessiveVibration", 16), ("fileError", 17), ("fireDetected", 18), ("floodDetected", 19), ("framingError", 20), ("heatingVentCoolingSystemProblem", 21), ("humidityUnacceptable", 22), ("inputOutputDeviceError", 23), ("inputDeviceError", 24), ("lanError", 25), ("leakDetected", 26), ("localNodeTransmissionError", 27), ("lossOfFrame", 28), ("lossOfSignal", 29), ("materialSupplyExhausted", 30), ("multiplexerProblem", 31), ("outOfMemory", 32), ("ouputDeviceError", 33), ("performanceDegraded", 34), ("powerProblem", 35), ("pressureUnacceptable", 36), ("processorProblem", 37), ("pumpFailure", 38), ("queueSizeExceeded", 39), ("receiveFailure", 40), ("receiverFailure", 41), ("remoteNodeTransmissionError", 42), ("resourceAtOrNearingCapacity", 43), ("responseTimeExecessive", 44), ("retransmissionRateExcessive", 45), ("softwareError", 46), ("softwareProgramAbnormallyTerminated", 47), ("softwareProgramError", 48), ("storageCapacityProblem", 49), ("temperatureUnacceptable", 50), ("thresholdCrossed", 51), ("timingProblem", 52), ("toxicLeakDetected", 53), ("transmitFailure", 54), ("transmitterFailure", 55), ("underlyingResourceUnavailable", 56), ("versionMismatch", 57), ("authenticationFailure", 58), ("breachOfConfidentiality", 59), ("cableTamper", 60), ("delayedInformation", 61), ("denialOfService", 62), ("duplicateInformation", 63), ("informationMissing", 64), ("informationModificationDetected", 65), ("informationOutOfSequence", 66), ("intrusionDetection", 67), ("keyExpired", 68), ("nonRepudiationFailure", 69), ("outOfHoursActivity", 70), ("outOfService", 71), ("proceduralError", 72), ("unauthorizedAccessAttempt", 73), ("unexpectedInformation", 74))

mibBuilder.exportSymbols("AC-FAULT-TC", AcAlarmEventType=AcAlarmEventType, AcAlarmProbableCause=AcAlarmProbableCause, AcAlarmSeverity=AcAlarmSeverity)
