#
# PySNMP MIB module EKINOPS-MGNT2-NMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ekinops/EKINOPS-MGNT2-NMS-MIB
# Produced by pysmi-1.1.3 at Thu Dec  9 14:29:43 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
EkiOnOff, ekinops = mibBuilder.importSymbols("EKINOPS-MIB", "EkiOnOff", "ekinops")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ObjectIdentity, IpAddress, iso, MibIdentifier, Counter32, NotificationType, ModuleIdentity, TimeTicks, Counter64, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter64", "Unsigned32", "Integer32")
DateAndTime, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "DisplayString", "TextualConvention")
SnmpUDPAddress, = mibBuilder.importSymbols("SNMPv2-TM", "SnmpUDPAddress")
mgnt2NMS = ModuleIdentity((1, 3, 6, 1, 4, 1, 20044, 1000))
mgnt2NMS.setRevisions(('2009-07-26 15:00', '2015-04-13 00:00', '2015-11-12 00:00', '2016-06-06 00:00',))
if mibBuilder.loadTexts: mgnt2NMS.setLastUpdated('201511120000Z')
if mibBuilder.loadTexts: mgnt2NMS.setOrganization('Ekinops')
mgnt2NMSMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 1))
mgnt2SupportMCConf = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 2))
mgnt2SupportMCCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1))
mgnt2SupportMCGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 2))
class Mgnt2NotificationId(TextualConvention, Counter32):
    status = 'current'

class Mgnt2AlmProbableCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 1000))
    namedValues = NamedValues(("other", 1), ("adapterError", 2), ("applicationSubsystemFailure", 3), ("bandwidthReduced", 4), ("callEstablishmentError", 5), ("communicationsProtocolError", 6), ("communicationsSubsystemFailure", 7), ("configurationOrCustomizationError", 8), ("congestion", 9), ("corruptData", 10), ("cpuCyclesLimitExceeded", 11), ("dataSetOrModemError", 12), ("degradedSignal", 13), ("dteDceInterfaceError", 14), ("enclosureDoorOpen", 15), ("equipmentMalfunction", 16), ("excessiveVibration", 17), ("fileError", 18), ("fireDetected", 19), ("floodDetected", 20), ("framingError", 21), ("heatingVentCoolingSystemProblem", 22), ("humidityUnacceptable", 23), ("inputOutputDeviceError", 24), ("inputDeviceError", 25), ("lanError", 26), ("leakDetected", 27), ("localNodeTransmissionError", 28), ("lossOfFrame", 29), ("lossOfSignal", 30), ("materialSupplyExhausted", 31), ("multiplexerProblem", 32), ("outOfMemory", 33), ("ouputDeviceError", 34), ("performanceDegraded", 35), ("powerProblem", 36), ("pressureUnacceptable", 37), ("processorProblem", 38), ("pumpFailure", 39), ("queueSizeExceeded", 40), ("receiveFailure", 41), ("receiverFailure", 42), ("remoteNodeTransmissionError", 43), ("resourceAtOrNearingCapacity", 44), ("responseTimeExecessive", 45), ("retransmissionRateExcessive", 46), ("softwareError", 47), ("softwareProgramAbnormallyTerminated", 48), ("softwareProgramError", 49), ("storageCapacityProblem", 50), ("temperatureUnacceptable", 51), ("thresholdCrossed", 52), ("timingProblem", 53), ("toxicLeakDetected", 54), ("transmitFailure", 55), ("transmitterFailure", 56), ("underlyingResourceUnavailable", 57), ("versionMismatch", 58), ("authenticationFailure", 59), ("breachOfConfidentiality", 60), ("cableTamper", 61), ("delayedInformation", 62), ("denialOfService", 63), ("duplicateInformation", 64), ("informationMissing", 65), ("informationModificationDetected", 66), ("informationOutOfSequence", 67), ("intrusionDetection", 68), ("keyExpired", 69), ("nonRepudiationFailure", 70), ("outOfHoursActivity", 71), ("outOfService", 72), ("proceduralError", 73), ("unauthorizedAccessAttempt", 74), ("unexpectedInformation", 75), ("informationalStatus", 1000))

class Mgnt2ObjectClassId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("mgnt", 13))

class Mgnt2AlmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("indeterminate", 5), ("cleared", 6))

class Mgnt2AlmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("communicationsAlarm", 2), ("qualityOfServiceAlarm", 3), ("processingErrorAlarm", 4), ("equipmentAlarm", 5), ("environmentalAlarm", 6), ("integrityViolation", 7), ("operationalViolation", 8), ("physicalViolation", 9), ("securityServiceOrMechanismViolation", 10), ("timeDomainViolation", 11), ("synthesisAlarm", 12))

class Mgnt2EventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("objectCreation", 1), ("objectDeletion", 2), ("attributeValueChange", 3), ("stateChange", 4), ("activityLog", 5))

class Mgnt2EventSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("event", 1), ("control", 2), ("config", 3))

class Mgnt2LacState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("accessDenied", 0), ("accessRequested", 1), ("accessGrantedCraft", 2), ("accessGrantedCli", 3), ("accessGrantedSnmp", 4))

class Mgnt2ServerAddress(TextualConvention, OctetString):
    status = 'current'

class Mgnt2UploadDownloadFileEncoding(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("ascii", 2), ("xml", 3), ("bin", 4), ("data", 5))

class Mgnt2UploadDownloadFileCompression(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCompression", 1), ("bzip", 2), ("gzip", 3))

class Mgnt2UploadDownloadActionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("success", 0), ("start", 1), ("inProgress", 2), ("failed", 3), ("automatic", 4), ("abort", 5))

class Mgnt2UploadDownloadErrorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("noError", 0), ("missingLogin", 1), ("missingPassword", 2), ("missingFile", 3), ("serverUnreachable", 4), ("badPassword", 5), ("noSpaceLeft", 6), ("corruptedFile", 7), ("canceled", 8), ("noWriteAccess", 9), ("undefinedError", 10), ("accessViolation", 11), ("fileExist", 12), ("wrongDirection", 13), ("wrongName", 14), ("wrongCompression", 15))

class Mgnt2SoftwareDownloadActionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noError", 0), ("missingLogin", 1), ("missingPassword", 2), ("missingFile", 3), ("serverUnreachable", 4), ("badPassword", 5), ("noSpaceLeft", 6), ("corruptedFile", 7), ("canceled", 8), ("noWriteAccess", 9))

class Mgnt2DownloadFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("pmPackage", 0), ("mgntPackage", 1), ("configurationFile", 2), ("logFile", 3), ("perfFile", 4), ("wavePlan", 5), ("adminPackage", 6))

mgnt2ActiveAlmTable = MibTable((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1), )
if mibBuilder.loadTexts: mgnt2ActiveAlmTable.setStatus('current')
mgnt2ActiveAlmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1), ).setIndexNames((0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmNotificationId"))
if mibBuilder.loadTexts: mgnt2ActiveAlmEntry.setStatus('current')
mgnt2ActiveAlmNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 1), Mgnt2NotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmNotificationId.setStatus('current')
mgnt2ActiveAlmProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 2), Mgnt2AlmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmProbableCause.setStatus('current')
mgnt2ActiveAlmObjectClassIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 3), Mgnt2ObjectClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmObjectClassIdentifier.setStatus('current')
mgnt2ActiveAlmSourcePm = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmSourcePm.setStatus('current')
mgnt2ActiveAlmBoardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmBoardNumber.setStatus('current')
mgnt2ActiveAlmSourcePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmSourcePortType.setStatus('current')
mgnt2ActiveAlmSourcePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmSourcePortNumber.setStatus('current')
mgnt2ActiveAlmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 8), Mgnt2AlmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmSeverity.setStatus('current')
mgnt2ActiveAlmSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmSpecificProblem.setStatus('current')
mgnt2ActiveAlmAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmAdditionalText.setStatus('current')
mgnt2ActiveAlmType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 11), Mgnt2AlmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmType.setStatus('current')
mgnt2ActiveAlmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmTime.setStatus('current')
mgnt2ActiveAlmNodeControllerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmNodeControllerIpAddress.setStatus('current')
mgnt2ActiveAlmChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ActiveAlmChassisId.setStatus('current')
mgnt2AlmLogTable = MibTable((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2), )
if mibBuilder.loadTexts: mgnt2AlmLogTable.setStatus('current')
mgnt2AlmLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1), ).setIndexNames((0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNotificationId"))
if mibBuilder.loadTexts: mgnt2AlmLogEntry.setStatus('current')
mgnt2AlmLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 1), Mgnt2NotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogNotificationId.setStatus('current')
mgnt2AlmLogProbableCause = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 2), Mgnt2AlmProbableCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogProbableCause.setStatus('current')
mgnt2AlmLogObjectClassIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 3), Mgnt2ObjectClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogObjectClassIdentifier.setStatus('current')
mgnt2AlmLogSourcePm = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogSourcePm.setStatus('current')
mgnt2AlmLogBoardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogBoardNumber.setStatus('current')
mgnt2AlmLogSourcePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogSourcePortType.setStatus('current')
mgnt2AlmLogSourcePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogSourcePortNumber.setStatus('current')
mgnt2AlmLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 8), Mgnt2AlmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogSeverity.setStatus('current')
mgnt2AlmLogSpecificProblem = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogSpecificProblem.setStatus('current')
mgnt2AlmLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogAdditionalText.setStatus('current')
mgnt2AlmLogAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 11), Mgnt2AlmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogAlarmType.setStatus('current')
mgnt2AlmLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogTime.setStatus('current')
mgnt2AlmLogNodeControllerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogNodeControllerIpAddress.setStatus('current')
mgnt2AlmLogChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2AlmLogChassisId.setStatus('current')
mgnt2EventLogTable = MibTable((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3), )
if mibBuilder.loadTexts: mgnt2EventLogTable.setStatus('current')
mgnt2EventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1), ).setIndexNames((0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNotificationId"))
if mibBuilder.loadTexts: mgnt2EventLogEntry.setStatus('current')
mgnt2EventLogNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 1), Mgnt2NotificationId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogNotificationId.setStatus('current')
mgnt2EventLogObjectClassIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 2), Mgnt2ObjectClassId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogObjectClassIdentifier.setStatus('current')
mgnt2EventLogSourcePm = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogSourcePm.setStatus('current')
mgnt2EventLogBoardNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogBoardNumber.setStatus('current')
mgnt2EventLogSourcePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogSourcePortType.setStatus('current')
mgnt2EventLogSourcePortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogSourcePortNumber.setStatus('current')
mgnt2EventLogEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 8), Mgnt2EventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogEventType.setStatus('current')
mgnt2EventLogSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 9), Mgnt2EventSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogSourceType.setStatus('current')
mgnt2EventLogReason = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogReason.setStatus('current')
mgnt2EventLogAdditionalText = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogAdditionalText.setStatus('current')
mgnt2EventLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 12), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogTime.setStatus('current')
mgnt2EventLogNodeControllerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogNodeControllerIpAddress.setStatus('current')
mgnt2EventLogChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 3, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2EventLogChassisId.setStatus('current')
mgnt2UploadDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5))
mgnt2UploadDownloadFilename = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadFilename.setStatus('current')
mgnt2UploadDownloadAddress = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 2), Mgnt2ServerAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadAddress.setStatus('current')
mgnt2UploadDownloadLogin = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadLogin.setStatus('current')
mgnt2UploadDownloadPasswd = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadPasswd.setStatus('current')
mgnt2UploadDownloadTxRetries = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadTxRetries.setStatus('current')
mgnt2UploadDownloadActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 6), Mgnt2UploadDownloadActionStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadActionStatus.setStatus('current')
mgnt2UploadDownloadErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 7), Mgnt2UploadDownloadErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2UploadDownloadErrorCode.setStatus('current')
mgnt2UploadDownloadDirection = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadDirection.setStatus('current')
mgnt2UploadDownloadProgress = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadProgress.setStatus('current')
mgnt2UploadDownloadReceivedFiles = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadReceivedFiles.setStatus('current')
mgnt2UploadDownloadRemainingFiles = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadRemainingFiles.setStatus('current')
mgnt2UploadDownloadFileType = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 12), Mgnt2DownloadFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadFileType.setStatus('current')
mgnt2UploadDownloadFileCompression = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 13), Mgnt2UploadDownloadFileCompression()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadFileCompression.setStatus('current')
mgnt2UploadDownloadDeleteLastFile = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 5, 14), EkiOnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2UploadDownloadDeleteLastFile.setStatus('current')
mgnt2Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6))
mgnt2ConfigurationChecksum = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 1), DisplayString())
if mibBuilder.loadTexts: mgnt2ConfigurationChecksum.setStatus('deprecated')
mgnt2ConfigurationActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2ConfigurationActionStatus.setStatus('current')
mgnt2ConfigurationActivationErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ConfigurationActivationErrorCode.setStatus('current')
mgnt2ConfigurationActivationErrorString = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 6, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2ConfigurationActivationErrorString.setStatus('current')
mgnt2SoftwareDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7))
mgnt2SoftwareDownloadActionStatus = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActionStatus.setStatus('current')
mgnt2SoftwareDownloadActivationErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationErrorCode.setStatus('current')
mgnt2SoftwareDownloadActivationErrorString = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationErrorString.setStatus('current')
mgnt2SoftwareDownloadActivationSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationSlotNumber.setStatus('current')
mgnt2SoftwareDownloadActivationClearFile = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationClearFile.setStatus('current')
mgnt2SoftwareDownloadActivationFilename = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationFilename.setStatus('current')
mgnt2SoftwareDownloadActivationAutoRestart = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationAutoRestart.setStatus('current')
mgnt2SoftwareDownloadActivationFileType = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 7, 9), Mgnt2DownloadFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2SoftwareDownloadActivationFileType.setStatus('current')
mgnt2LacTable = MibTable((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8), )
if mibBuilder.loadTexts: mgnt2LacTable.setStatus('current')
mgnt2LacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1), ).setIndexNames((0, "EKINOPS-MGNT2-NMS-MIB", "mgnt2LacIndex"))
if mibBuilder.loadTexts: mgnt2LacEntry.setStatus('current')
mgnt2LacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2LacIndex.setStatus('current')
mgnt2LacState = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 2), Mgnt2LacState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2LacState.setStatus('current')
mgnt2LacNoResponseTimeOutPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgnt2LacNoResponseTimeOutPeriod.setStatus('current')
mgnt2PolledInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10))
mgnt2PolledInfoLastAlarmNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2PolledInfoLastAlarmNotificationId.setStatus('current')
mgnt2PolledInfoLastEventNotificationId = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2PolledInfoLastEventNotificationId.setStatus('current')
mgnt2PolledInfoConfigurationChecksum = MibScalar((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgnt2PolledInfoConfigurationChecksum.setStatus('current')
mgnt2TrapNMSAlarm = NotificationType((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 11)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNotificationId"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogObjectClassIdentifier"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePm"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogBoardNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogProbableCause"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSeverity"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSpecificProblem"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAdditionalText"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAlarmType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogTime"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogNodeControllerIpAddress"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogChassisId"))
if mibBuilder.loadTexts: mgnt2TrapNMSAlarm.setStatus('current')
mgnt2TrapNMSEvent = NotificationType((1, 3, 6, 1, 4, 1, 20044, 1000, 1, 12)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNotificationId"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogObjectClassIdentifier"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePm"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogBoardNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogEventType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourceType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogReason"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogAdditionalText"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogTime"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogNodeControllerIpAddress"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogChassisId"))
if mibBuilder.loadTexts: mgnt2TrapNMSEvent.setStatus('current')
mgnt2SupportMc = ModuleCompliance((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 1)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmGroup"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogGroup"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgnt2SupportMc = mgnt2SupportMc.setStatus('current')
mgnt2ActiveAlmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 2)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmProbableCause"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmObjectClassIdentifier"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePm"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmBoardNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePortType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSourcePortNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmSeverity"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2ActiveAlmTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgnt2ActiveAlmGroup = mgnt2ActiveAlmGroup.setStatus('current')
mgnt2AlmLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 3)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogProbableCause"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogObjectClassIdentifier"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePm"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogBoardNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSourcePortNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogSeverity"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogAlarmType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2AlmLogTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgnt2AlmLogGroup = mgnt2AlmLogGroup.setStatus('current')
mgnt2EventLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20044, 1000, 2, 1, 4)).setObjects(("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogObjectClassIdentifier"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePm"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogBoardNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourcePortNumber"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogEventType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogSourceType"), ("EKINOPS-MGNT2-NMS-MIB", "mgnt2EventLogTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgnt2EventLogGroup = mgnt2EventLogGroup.setStatus('current')
mibBuilder.exportSymbols("EKINOPS-MGNT2-NMS-MIB", Mgnt2AlmSeverity=Mgnt2AlmSeverity, mgnt2AlmLogAdditionalText=mgnt2AlmLogAdditionalText, mgnt2UploadDownloadReceivedFiles=mgnt2UploadDownloadReceivedFiles, mgnt2UploadDownload=mgnt2UploadDownload, mgnt2ActiveAlmAdditionalText=mgnt2ActiveAlmAdditionalText, mgnt2EventLogAdditionalText=mgnt2EventLogAdditionalText, mgnt2SoftwareDownload=mgnt2SoftwareDownload, mgnt2SoftwareDownloadActivationErrorCode=mgnt2SoftwareDownloadActivationErrorCode, mgnt2AlmLogBoardNumber=mgnt2AlmLogBoardNumber, mgnt2UploadDownloadFilename=mgnt2UploadDownloadFilename, Mgnt2LacState=Mgnt2LacState, mgnt2AlmLogTable=mgnt2AlmLogTable, mgnt2AlmLogGroup=mgnt2AlmLogGroup, mgnt2AlmLogObjectClassIdentifier=mgnt2AlmLogObjectClassIdentifier, mgnt2AlmLogSourcePortNumber=mgnt2AlmLogSourcePortNumber, mgnt2LacState=mgnt2LacState, mgnt2AlmLogSourcePm=mgnt2AlmLogSourcePm, mgnt2AlmLogTime=mgnt2AlmLogTime, mgnt2UploadDownloadPasswd=mgnt2UploadDownloadPasswd, mgnt2ActiveAlmSourcePm=mgnt2ActiveAlmSourcePm, mgnt2UploadDownloadFileCompression=mgnt2UploadDownloadFileCompression, mgnt2EventLogGroup=mgnt2EventLogGroup, mgnt2AlmLogChassisId=mgnt2AlmLogChassisId, mgnt2AlmLogNotificationId=mgnt2AlmLogNotificationId, mgnt2ActiveAlmSpecificProblem=mgnt2ActiveAlmSpecificProblem, mgnt2EventLogChassisId=mgnt2EventLogChassisId, mgnt2SupportMc=mgnt2SupportMc, Mgnt2EventType=Mgnt2EventType, mgnt2EventLogSourceType=mgnt2EventLogSourceType, mgnt2ActiveAlmEntry=mgnt2ActiveAlmEntry, mgnt2AlmLogEntry=mgnt2AlmLogEntry, mgnt2SoftwareDownloadActivationErrorString=mgnt2SoftwareDownloadActivationErrorString, Mgnt2ObjectClassId=Mgnt2ObjectClassId, mgnt2EventLogTime=mgnt2EventLogTime, mgnt2AlmLogNodeControllerIpAddress=mgnt2AlmLogNodeControllerIpAddress, mgnt2SupportMCGroup=mgnt2SupportMCGroup, mgnt2EventLogNodeControllerIpAddress=mgnt2EventLogNodeControllerIpAddress, mgnt2PolledInfo=mgnt2PolledInfo, Mgnt2AlmType=Mgnt2AlmType, mgnt2LacTable=mgnt2LacTable, Mgnt2UploadDownloadActionStatus=Mgnt2UploadDownloadActionStatus, mgnt2PolledInfoConfigurationChecksum=mgnt2PolledInfoConfigurationChecksum, mgnt2ActiveAlmTable=mgnt2ActiveAlmTable, Mgnt2UploadDownloadFileCompression=Mgnt2UploadDownloadFileCompression, mgnt2UploadDownloadDirection=mgnt2UploadDownloadDirection, PYSNMP_MODULE_ID=mgnt2NMS, mgnt2PolledInfoLastEventNotificationId=mgnt2PolledInfoLastEventNotificationId, mgnt2ActiveAlmSourcePortNumber=mgnt2ActiveAlmSourcePortNumber, mgnt2AlmLogProbableCause=mgnt2AlmLogProbableCause, Mgnt2NotificationId=Mgnt2NotificationId, mgnt2AlmLogSourcePortType=mgnt2AlmLogSourcePortType, mgnt2PolledInfoLastAlarmNotificationId=mgnt2PolledInfoLastAlarmNotificationId, mgnt2UploadDownloadAddress=mgnt2UploadDownloadAddress, mgnt2ConfigurationActivationErrorCode=mgnt2ConfigurationActivationErrorCode, mgnt2UploadDownloadFileType=mgnt2UploadDownloadFileType, mgnt2SoftwareDownloadActivationAutoRestart=mgnt2SoftwareDownloadActivationAutoRestart, mgnt2SoftwareDownloadActivationFileType=mgnt2SoftwareDownloadActivationFileType, mgnt2ActiveAlmGroup=mgnt2ActiveAlmGroup, mgnt2NMS=mgnt2NMS, mgnt2NMSMibObject=mgnt2NMSMibObject, Mgnt2AlmProbableCause=Mgnt2AlmProbableCause, mgnt2TrapNMSAlarm=mgnt2TrapNMSAlarm, mgnt2Configuration=mgnt2Configuration, mgnt2ActiveAlmProbableCause=mgnt2ActiveAlmProbableCause, mgnt2EventLogTable=mgnt2EventLogTable, mgnt2EventLogNotificationId=mgnt2EventLogNotificationId, mgnt2SoftwareDownloadActivationClearFile=mgnt2SoftwareDownloadActivationClearFile, Mgnt2UploadDownloadFileEncoding=Mgnt2UploadDownloadFileEncoding, mgnt2AlmLogAlarmType=mgnt2AlmLogAlarmType, Mgnt2ServerAddress=Mgnt2ServerAddress, mgnt2UploadDownloadErrorCode=mgnt2UploadDownloadErrorCode, mgnt2SupportMCCompl=mgnt2SupportMCCompl, mgnt2AlmLogSeverity=mgnt2AlmLogSeverity, mgnt2EventLogEventType=mgnt2EventLogEventType, mgnt2ActiveAlmSeverity=mgnt2ActiveAlmSeverity, mgnt2UploadDownloadTxRetries=mgnt2UploadDownloadTxRetries, mgnt2EventLogEntry=mgnt2EventLogEntry, mgnt2EventLogSourcePortType=mgnt2EventLogSourcePortType, mgnt2ConfigurationActivationErrorString=mgnt2ConfigurationActivationErrorString, Mgnt2SoftwareDownloadActionStatus=Mgnt2SoftwareDownloadActionStatus, mgnt2EventLogObjectClassIdentifier=mgnt2EventLogObjectClassIdentifier, mgnt2LacNoResponseTimeOutPeriod=mgnt2LacNoResponseTimeOutPeriod, mgnt2LacEntry=mgnt2LacEntry, mgnt2UploadDownloadRemainingFiles=mgnt2UploadDownloadRemainingFiles, mgnt2ActiveAlmSourcePortType=mgnt2ActiveAlmSourcePortType, mgnt2EventLogReason=mgnt2EventLogReason, mgnt2EventLogSourcePm=mgnt2EventLogSourcePm, mgnt2ConfigurationActionStatus=mgnt2ConfigurationActionStatus, mgnt2UploadDownloadActionStatus=mgnt2UploadDownloadActionStatus, mgnt2UploadDownloadDeleteLastFile=mgnt2UploadDownloadDeleteLastFile, mgnt2ActiveAlmNotificationId=mgnt2ActiveAlmNotificationId, mgnt2ConfigurationChecksum=mgnt2ConfigurationChecksum, mgnt2SoftwareDownloadActionStatus=mgnt2SoftwareDownloadActionStatus, mgnt2UploadDownloadProgress=mgnt2UploadDownloadProgress, mgnt2ActiveAlmObjectClassIdentifier=mgnt2ActiveAlmObjectClassIdentifier, mgnt2SupportMCConf=mgnt2SupportMCConf, Mgnt2UploadDownloadErrorCode=Mgnt2UploadDownloadErrorCode, mgnt2ActiveAlmBoardNumber=mgnt2ActiveAlmBoardNumber, mgnt2EventLogBoardNumber=mgnt2EventLogBoardNumber, mgnt2TrapNMSEvent=mgnt2TrapNMSEvent, Mgnt2EventSourceType=Mgnt2EventSourceType, mgnt2ActiveAlmNodeControllerIpAddress=mgnt2ActiveAlmNodeControllerIpAddress, mgnt2ActiveAlmTime=mgnt2ActiveAlmTime, Mgnt2DownloadFileType=Mgnt2DownloadFileType, mgnt2UploadDownloadLogin=mgnt2UploadDownloadLogin, mgnt2SoftwareDownloadActivationFilename=mgnt2SoftwareDownloadActivationFilename, mgnt2LacIndex=mgnt2LacIndex, mgnt2AlmLogSpecificProblem=mgnt2AlmLogSpecificProblem, mgnt2EventLogSourcePortNumber=mgnt2EventLogSourcePortNumber, mgnt2ActiveAlmType=mgnt2ActiveAlmType, mgnt2SoftwareDownloadActivationSlotNumber=mgnt2SoftwareDownloadActivationSlotNumber, mgnt2ActiveAlmChassisId=mgnt2ActiveAlmChassisId)
