#
# PySNMP MIB module Job-Monitoring-MIB (http://snmplabs.com/pysmi)
# ASN.1 source Job-Monitoring-MIB
# Source digest sha256:5f6454644bcace35cb476c23ac145d7ba0b14d6adaaa1ce1816673983ee93290
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jobmonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2699, 1, 1))
jobmonMIB.setRevisions(('1999-02-19 00:00',))
if mibBuilder.loadTexts: jobmonMIB.setLastUpdated('1999-02-19 00:00')
if mibBuilder.loadTexts: jobmonMIB.setOrganization('Printer Working Group (PWG)')
class JmUTF8StringTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 63)

class JmJobStringTC(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 63)

class JmNaturalLanguageTagTC(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 63)

class JmTimeStampTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JmJobSourcePlatformTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("sptUNIX", 3), ("sptOS2", 4), ("sptPCDOS", 5), ("sptNT", 6), ("sptMVS", 7), ("sptVM", 8), ("sptOS400", 9), ("sptVMS", 10), ("sptWindows", 11), ("sptNetWare", 12))

class JmFinishingTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("staple", 4), ("punch", 5), ("cover", 6), ("bind", 7))

class JmPrintQualityTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("draft", 3), ("normal", 4), ("high", 5))

class JmPrinterResolutionTC(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(9, 9)
    fixedLength = 9

class JmTonerEconomyTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("off", 3), ("on", 4))

class JmBooleanTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("unknown", 2), ("false", 3), ("true", 4))

class JmMediumTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("stationery", 3), ("transparency", 4), ("envelope", 5), ("envelopePlain", 6), ("envelopeWindow", 7), ("continuousLong", 8), ("continuousShort", 9), ("tabStock", 10), ("multiPartForm", 11), ("labels", 12), ("multiLayer", 13))

class JmJobCollationTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("uncollatedSheets", 3), ("collatedDocuments", 4), ("uncollatedDocuments", 5))

class JmJobSubmissionIDTypeTC(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class JmJobStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 2), ("pending", 3), ("pendingHeld", 4), ("processing", 5), ("processingStopped", 6), ("canceled", 7), ("aborted", 8), ("completed", 9))

class JmAttributeTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 50, 51, 52, 53, 54, 55, 56, 70, 71, 72, 73, 74, 75, 76, 77, 90, 91, 92, 93, 94, 95, 96, 97, 110, 111, 112, 113, 114, 115, 130, 131, 132, 150, 151, 152, 170, 171, 172, 173, 174, 175, 190, 191, 192, 193, 194, 195))
    namedValues = NamedValues(("other", 1), ("jobStateReasons2", 3), ("jobStateReasons3", 4), ("jobStateReasons4", 5), ("processingMessage", 6), ("processingMessageNaturalLangTag", 7), ("jobCodedCharSet", 8), ("jobNaturalLanguageTag", 9), ("jobURI", 20), ("jobAccountName", 21), ("serverAssignedJobName", 22), ("jobName", 23), ("jobServiceTypes", 24), ("jobSourceChannelIndex", 25), ("jobSourcePlatformType", 26), ("submittingServerName", 27), ("submittingApplicationName", 28), ("jobOriginatingHost", 29), ("deviceNameRequested", 30), ("queueNameRequested", 31), ("physicalDevice", 32), ("numberOfDocuments", 33), ("fileName", 34), ("documentName", 35), ("jobComment", 36), ("documentFormatIndex", 37), ("documentFormat", 38), ("jobPriority", 50), ("jobProcessAfterDateAndTime", 51), ("jobHold", 52), ("jobHoldUntil", 53), ("outputBin", 54), ("sides", 55), ("finishing", 56), ("printQualityRequested", 70), ("printQualityUsed", 71), ("printerResolutionRequested", 72), ("printerResolutionUsed", 73), ("tonerEcomonyRequested", 74), ("tonerEcomonyUsed", 75), ("tonerDensityRequested", 76), ("tonerDensityUsed", 77), ("jobCopiesRequested", 90), ("jobCopiesCompleted", 91), ("documentCopiesRequested", 92), ("documentCopiesCompleted", 93), ("jobKOctetsTransferred", 94), ("sheetCompletedCopyNumber", 95), ("sheetCompletedDocumentNumber", 96), ("jobCollationType", 97), ("impressionsSpooled", 110), ("impressionsSentToDevice", 111), ("impressionsInterpreted", 112), ("impressionsCompletedCurrentCopy", 113), ("fullColorImpressionsCompleted", 114), ("highlightColorImpressionsCompleted", 115), ("pagesRequested", 130), ("pagesCompleted", 131), ("pagesCompletedCurrentCopy", 132), ("sheetsRequested", 150), ("sheetsCompleted", 151), ("sheetsCompletedCurrentCopy", 152), ("mediumRequested", 170), ("mediumConsumed", 171), ("colorantRequested", 172), ("colorantConsumed", 173), ("mediumTypeConsumed", 174), ("mediumSizeConsumed", 175), ("jobSubmissionToServerTime", 190), ("jobSubmissionTime", 191), ("jobStartedBeingHeldTime", 192), ("jobStartedProcessingTime", 193), ("jobCompletionTime", 194), ("jobProcessingCPUTime", 195))

class JmJobServiceTypesTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JmJobStateReasons1TC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JmJobStateReasons2TC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JmJobStateReasons3TC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JmJobStateReasons4TC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

jobmonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1))
jmGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1))
jmGeneralTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmGeneralTable.setStatus('current')
jmGeneralEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"))
if mibBuilder.loadTexts: jmGeneralEntry.setStatus('current')
jmGeneralJobSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmGeneralJobSetIndex.setStatus('current')
jmGeneralNumberOfActiveJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralNumberOfActiveJobs.setStatus('current')
jmGeneralOldestActiveJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralOldestActiveJobIndex.setStatus('current')
jmGeneralNewestActiveJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralNewestActiveJobIndex.setStatus('current')
jmGeneralJobPersistence = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 2147483647)).clone(60)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralJobPersistence.setStatus('current')
jmGeneralAttributePersistence = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 2147483647)).clone(60)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralAttributePersistence.setStatus('current')
jmGeneralJobSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 1, 1, 1, 7), JmUTF8StringTC().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmGeneralJobSetName.setStatus('current')
jmJobID = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2))
jmJobIDTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmJobIDTable.setStatus('current')
jmJobIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "Job-Monitoring-MIB", "jmJobSubmissionID"))
if mibBuilder.loadTexts: jmJobIDEntry.setStatus('current')
jmJobSubmissionID = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(48, 48)).setFixedLength(48)).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmJobSubmissionID.setStatus('current')
jmJobIDJobSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobIDJobSetIndex.setStatus('current')
jmJobIDJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobIDJobIndex.setStatus('current')
jmJob = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3))
jmJobTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmJobTable.setStatus('current')
jmJobEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"), (0, "Job-Monitoring-MIB", "jmJobIndex"))
if mibBuilder.loadTexts: jmJobEntry.setStatus('current')
jmJobIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmJobIndex.setStatus('current')
jmJobState = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 2), JmJobStateTC().clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobState.setStatus('current')
jmJobStateReasons1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 3), JmJobStateReasons1TC().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobStateReasons1.setStatus('current')
jmNumberOfInterveningJobs = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmNumberOfInterveningJobs.setStatus('current')
jmJobKOctetsPerCopyRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobKOctetsPerCopyRequested.setStatus('current')
jmJobKOctetsProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobKOctetsProcessed.setStatus('current')
jmJobImpressionsPerCopyRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobImpressionsPerCopyRequested.setStatus('current')
jmJobImpressionsCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobImpressionsCompleted.setStatus('current')
jmJobOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 3, 1, 1, 9), JmJobStringTC().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmJobOwner.setStatus('current')
jmAttribute = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4))
jmAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmAttributeTable.setStatus('current')
jmAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "Job-Monitoring-MIB", "jmGeneralJobSetIndex"), (0, "Job-Monitoring-MIB", "jmJobIndex"), (0, "Job-Monitoring-MIB", "jmAttributeTypeIndex"), (0, "Job-Monitoring-MIB", "jmAttributeInstanceIndex"))
if mibBuilder.loadTexts: jmAttributeEntry.setStatus('current')
jmAttributeTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 1), JmAttributeTypeTC()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmAttributeTypeIndex.setStatus('current')
jmAttributeInstanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: jmAttributeInstanceIndex.setStatus('current')
jmAttributeValueAsInteger = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2, 2147483647)).clone(-2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmAttributeValueAsInteger.setStatus('current')
jmAttributeValueAsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2699, 1, 1, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: jmAttributeValueAsOctets.setStatus('current')
jobmonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 2))
jmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3))
jmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 1)).setObjects(("Job-Monitoring-MIB", "jmGeneralGroup"), ("Job-Monitoring-MIB", "jmJobIDGroup"), ("Job-Monitoring-MIB", "jmJobGroup"), ("Job-Monitoring-MIB", "jmAttributeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jmMIBCompliance = jmMIBCompliance.setStatus('current')
jmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2))
jmGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 1)).setObjects(("Job-Monitoring-MIB", "jmGeneralNumberOfActiveJobs"), ("Job-Monitoring-MIB", "jmGeneralOldestActiveJobIndex"), ("Job-Monitoring-MIB", "jmGeneralNewestActiveJobIndex"), ("Job-Monitoring-MIB", "jmGeneralJobPersistence"), ("Job-Monitoring-MIB", "jmGeneralAttributePersistence"), ("Job-Monitoring-MIB", "jmGeneralJobSetName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jmGeneralGroup = jmGeneralGroup.setStatus('current')
jmJobIDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 2)).setObjects(("Job-Monitoring-MIB", "jmJobIDJobSetIndex"), ("Job-Monitoring-MIB", "jmJobIDJobIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jmJobIDGroup = jmJobIDGroup.setStatus('current')
jmJobGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 3)).setObjects(("Job-Monitoring-MIB", "jmJobState"), ("Job-Monitoring-MIB", "jmJobStateReasons1"), ("Job-Monitoring-MIB", "jmNumberOfInterveningJobs"), ("Job-Monitoring-MIB", "jmJobKOctetsPerCopyRequested"), ("Job-Monitoring-MIB", "jmJobKOctetsProcessed"), ("Job-Monitoring-MIB", "jmJobImpressionsPerCopyRequested"), ("Job-Monitoring-MIB", "jmJobImpressionsCompleted"), ("Job-Monitoring-MIB", "jmJobOwner"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jmJobGroup = jmJobGroup.setStatus('current')
jmAttributeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2699, 1, 1, 3, 2, 4)).setObjects(("Job-Monitoring-MIB", "jmAttributeValueAsInteger"), ("Job-Monitoring-MIB", "jmAttributeValueAsOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jmAttributeGroup = jmAttributeGroup.setStatus('current')
mibBuilder.exportSymbols("Job-Monitoring-MIB", JmAttributeTypeTC=JmAttributeTypeTC, JmBooleanTC=JmBooleanTC, JmFinishingTC=JmFinishingTC, JmJobCollationTypeTC=JmJobCollationTypeTC, JmJobServiceTypesTC=JmJobServiceTypesTC, JmJobSourcePlatformTypeTC=JmJobSourcePlatformTypeTC, JmJobStateReasons1TC=JmJobStateReasons1TC, JmJobStateReasons2TC=JmJobStateReasons2TC, JmJobStateReasons3TC=JmJobStateReasons3TC, JmJobStateReasons4TC=JmJobStateReasons4TC, JmJobStateTC=JmJobStateTC, JmJobStringTC=JmJobStringTC, JmJobSubmissionIDTypeTC=JmJobSubmissionIDTypeTC, JmMediumTypeTC=JmMediumTypeTC, JmNaturalLanguageTagTC=JmNaturalLanguageTagTC, JmPrintQualityTC=JmPrintQualityTC, JmPrinterResolutionTC=JmPrinterResolutionTC, JmTimeStampTC=JmTimeStampTC, JmTonerEconomyTC=JmTonerEconomyTC, JmUTF8StringTC=JmUTF8StringTC, PYSNMP_MODULE_ID=jobmonMIB, jmAttribute=jmAttribute, jmAttributeEntry=jmAttributeEntry, jmAttributeGroup=jmAttributeGroup, jmAttributeInstanceIndex=jmAttributeInstanceIndex, jmAttributeTable=jmAttributeTable, jmAttributeTypeIndex=jmAttributeTypeIndex, jmAttributeValueAsInteger=jmAttributeValueAsInteger, jmAttributeValueAsOctets=jmAttributeValueAsOctets, jmGeneral=jmGeneral, jmGeneralAttributePersistence=jmGeneralAttributePersistence, jmGeneralEntry=jmGeneralEntry, jmGeneralGroup=jmGeneralGroup, jmGeneralJobPersistence=jmGeneralJobPersistence, jmGeneralJobSetIndex=jmGeneralJobSetIndex, jmGeneralJobSetName=jmGeneralJobSetName, jmGeneralNewestActiveJobIndex=jmGeneralNewestActiveJobIndex, jmGeneralNumberOfActiveJobs=jmGeneralNumberOfActiveJobs, jmGeneralOldestActiveJobIndex=jmGeneralOldestActiveJobIndex, jmGeneralTable=jmGeneralTable, jmJob=jmJob, jmJobEntry=jmJobEntry, jmJobGroup=jmJobGroup, jmJobID=jmJobID, jmJobIDEntry=jmJobIDEntry, jmJobIDGroup=jmJobIDGroup, jmJobIDJobIndex=jmJobIDJobIndex, jmJobIDJobSetIndex=jmJobIDJobSetIndex, jmJobIDTable=jmJobIDTable, jmJobImpressionsCompleted=jmJobImpressionsCompleted, jmJobImpressionsPerCopyRequested=jmJobImpressionsPerCopyRequested, jmJobIndex=jmJobIndex, jmJobKOctetsPerCopyRequested=jmJobKOctetsPerCopyRequested, jmJobKOctetsProcessed=jmJobKOctetsProcessed, jmJobOwner=jmJobOwner, jmJobState=jmJobState, jmJobStateReasons1=jmJobStateReasons1, jmJobSubmissionID=jmJobSubmissionID, jmJobTable=jmJobTable, jmMIBCompliance=jmMIBCompliance, jmMIBConformance=jmMIBConformance, jmMIBGroups=jmMIBGroups, jmNumberOfInterveningJobs=jmNumberOfInterveningJobs, jobmonMIB=jobmonMIB, jobmonMIBNotifications=jobmonMIBNotifications, jobmonMIBObjects=jobmonMIBObjects)
