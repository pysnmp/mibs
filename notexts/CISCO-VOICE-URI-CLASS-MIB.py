#
# PySNMP MIB module CISCO-VOICE-URI-CLASS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-URI-CLASS-MIB
# Source digest sha256:68ad6505c1843e690d22e547f8b19fdbf14a9da2b0e6bce9c0c05761f511d859
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVoiceUriClassMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 99999999))
ciscoVoiceUriClassMIB.setRevisions(('2002-10-10 00:00',))
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setLastUpdated('2002-10-10 00:00')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setOrganization('Cisco Systems, Inc.')
class CvUriClassTagIndex(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CvUriClassTag(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPattern(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPreference(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

cvUriClassMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0))
cvUriClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1))
cvUriClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1))
cvUriClassSIPGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2))
cvUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvUriClassCfgTable.setStatus('current')
cvUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvUriClassCfgEntry.setStatus('current')
cvUriClassCfgTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1), CvUriClassTagIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvUriClassCfgTag.setStatus('current')
cvUriClassCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sip", 1), ("tel", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgType.setStatus('current')
cvUriClassCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgStatus.setStatus('current')
cvSIPUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setStatus('current')
cvSIPUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setStatus('current')
cvSIPUriClassCfgUserIDPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setStatus('current')
cvSIPUriClassCfgHostPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setStatus('current')
cvSIPUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setStatus('current')
cvTELUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setStatus('current')
cvTELUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setStatus('current')
cvTELUriClassCfgPhoneNumPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setStatus('current')
cvTELUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setStatus('current')
cvCommonUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setStatus('current')
cvCommonUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setStatus('current')
cvCommonUriClassCfgURIPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setStatus('current')
cvUriClassSIPHostPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1), CvUriClassPreference().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setStatus('current')
cvUriClassSIPUserIDPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2), CvUriClassPreference().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setStatus('current')
cvUriClassMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2))
cvUriClassMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1))
cvUriClassMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2))
cvUriClassMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassMIBCompliance = cvUriClassMIBCompliance.setStatus('current')
cvUriClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassGroup = cvUriClassGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-URI-CLASS-MIB", CvUriClassPattern=CvUriClassPattern, CvUriClassPreference=CvUriClassPreference, CvUriClassTag=CvUriClassTag, CvUriClassTagIndex=CvUriClassTagIndex, PYSNMP_MODULE_ID=ciscoVoiceUriClassMIB, ciscoVoiceUriClassMIB=ciscoVoiceUriClassMIB, cvCommonUriClassCfgEntry=cvCommonUriClassCfgEntry, cvCommonUriClassCfgTable=cvCommonUriClassCfgTable, cvCommonUriClassCfgURIPattern=cvCommonUriClassCfgURIPattern, cvSIPUriClassCfgEntry=cvSIPUriClassCfgEntry, cvSIPUriClassCfgHostPattern=cvSIPUriClassCfgHostPattern, cvSIPUriClassCfgPhoneCtxtPattern=cvSIPUriClassCfgPhoneCtxtPattern, cvSIPUriClassCfgTable=cvSIPUriClassCfgTable, cvSIPUriClassCfgUserIDPattern=cvSIPUriClassCfgUserIDPattern, cvTELUriClassCfgEntry=cvTELUriClassCfgEntry, cvTELUriClassCfgPhoneCtxtPattern=cvTELUriClassCfgPhoneCtxtPattern, cvTELUriClassCfgPhoneNumPattern=cvTELUriClassCfgPhoneNumPattern, cvTELUriClassCfgTable=cvTELUriClassCfgTable, cvUriClass=cvUriClass, cvUriClassCfgEntry=cvUriClassCfgEntry, cvUriClassCfgStatus=cvUriClassCfgStatus, cvUriClassCfgTable=cvUriClassCfgTable, cvUriClassCfgTag=cvUriClassCfgTag, cvUriClassCfgType=cvUriClassCfgType, cvUriClassGroup=cvUriClassGroup, cvUriClassMIBCompliance=cvUriClassMIBCompliance, cvUriClassMIBCompliances=cvUriClassMIBCompliances, cvUriClassMIBConformance=cvUriClassMIBConformance, cvUriClassMIBGroups=cvUriClassMIBGroups, cvUriClassMIBNotifications=cvUriClassMIBNotifications, cvUriClassMIBObjects=cvUriClassMIBObjects, cvUriClassSIPGeneralConfig=cvUriClassSIPGeneralConfig, cvUriClassSIPHostPreference=cvUriClassSIPHostPreference, cvUriClassSIPUserIDPreference=cvUriClassSIPUserIDPreference)
