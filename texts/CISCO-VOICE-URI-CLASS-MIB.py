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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setLastUpdated('2002-10-10 00:00')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceUriClassMIB.setDescription("This MIB provides information about Voice URI classes\n                 that are used to select Dial Peers based on URI's. A\n                 Voice URI class contains a set of configurations that\n                 is used to match a Voice URI.\n                 \n                 URI        - Uniform Resource Indicator\n                 URL        - Uniform Resource Locator\n                 regex      - regular expression\n                 RFC 2543   - SIP: Session Initiation Protocol\n                 RFC 2806   - URLs for Telephone Calls")
class CvUriClassTagIndex(TextualConvention, OctetString):
    description = 'A Voice URI class tag. This is a value used to uniquely\n         identify each Voice URI class in the system.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CvUriClassTag(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n         CvUriClassTagIndex convention. This extension allows\n         zero-length strings to be used for tags. Examples of usage\n         of zero-length strings as tags might include situations\n         where none of the Voice URI classes need to be referenced.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPattern(TextualConvention, OctetString):
    description = 'A regular expression pattern that is configured in the voice \n         URI classes. The default value is a zero-length string. Any\n         pattern set to this default value is not used for matching\n         with the URI'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvUriClassPreference(TextualConvention, Integer32):
    description = 'Preference for a field in the URI. Lower number indicates\n         higher preference. The preference is used to break ties when\n         more than one class matches a given URI. The class, which has\n         the longest match for a field with the highest preference is\n         given higher priority.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 10)

cvUriClassMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0))
cvUriClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1))
cvUriClass = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1))
cvUriClassSIPGeneralConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2))
cvUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgTable.setDescription('The table contains generic Voice URI class information.')
cvUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgEntry.setDescription("A single Voice URI class. The creation of this entry\n         will result in the automatic creation of a corresponding\n         'cvUriClassCfgType' URI class entry and a\n         cvCommonUriClassCfgEntry.")
cvUriClassCfgTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1), CvUriClassTagIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvUriClassCfgTag.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgTag.setDescription('A name that uniquely identifies a Voice URI class in the\n         system.')
cvUriClassCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sip", 1), ("tel", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgType.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgType.setDescription("Specifies the type of Voice URI class. The type is the schema\n         of the URI's, which this class is configured to match.\n\n         sip   - Voice URI class to match sip: URI's (RFC 2543)\n         tel   - Voice URI class to match tel: URI's (RFC 2806)\n\n         Once created this object cannot be modified.")
cvUriClassCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvUriClassCfgStatus.setStatus('current')
if mibBuilder.loadTexts: cvUriClassCfgStatus.setDescription('This object is used to create, modify or delete a row in this\n         table. A row can be deleted or modified regardless of its\n         current state. When the row is created with createAndWait, it\n         is placed in notInService state, until such time when either\n         the state is changed to active, or the row is deleted.')
cvSIPUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgTable.setDescription('The table contains information related to sip: schema-specific\n         Voice URI classes.')
cvSIPUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class.\n         This entry is created automatically when a cvUriClassCfgEntry\n         of cvUriClassCfgType(1) is created. The manager cannot create\n         this entry.')
cvSIPUriClassCfgUserIDPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgUserIDPattern.setDescription('A regular expression to match the user-id in a sip: URI. If\n         this object is set to a zero-length string it is not used for\n         matching with the URI.\n         This object cannot be set if cvCommonUriClassCfgURIPattern\n         is also set.')
cvSIPUriClassCfgHostPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgHostPattern.setDescription('A regular expression to match the host portion in a\n         sip: URI. If this object is set to a zero-length string it is\n         not used for matching with the URI.\n         This object cannot be set if cvCommonUriClassCfgURIPattern\n         is also set.')
cvSIPUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setStatus('current')
if mibBuilder.loadTexts: cvSIPUriClassCfgPhoneCtxtPattern.setDescription('A regular expression to match the phone-context attribute\n         in a sip: URI. If this object is set to a zero-length string\n         it is not used for matching with the URI.\n         This object cannot be set if cvCommonUriClassCfgURIPattern\n         is also set.')
cvTELUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgTable.setDescription('The table contains information related to tel: schema-specific\n         Voice URI classes.')
cvTELUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class.\n         This entry is created automatically when a cvUriClassCfgEntry\n         of cvUriClassCfgType(2) is created. The manager cannot create\n         this entry.')
cvTELUriClassCfgPhoneNumPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneNumPattern.setDescription('A regular expression to match the phone number portion in a\n         tel: URI. If this object is set to a zero-length string it is\n         not used for matching with the URI.\n         This object cannot be set if cvCommonUriClassCfgURIPattern\n         is also set.')
cvTELUriClassCfgPhoneCtxtPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2), CvUriClassPattern().clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setStatus('current')
if mibBuilder.loadTexts: cvTELUriClassCfgPhoneCtxtPattern.setDescription('A regular expression to match the phone-context attribute in a\n         tel: URI. If this object is set to a zero-length string it is\n         not used for matching with the URI.\n         This object cannot be set if cvCommonUriClassCfgURIPattern\n         is also set.')
cvCommonUriClassCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgTable.setDescription('The table contains common configuration information specific to\n         the Voice URI classes.')
cvCommonUriClassCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"))
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgEntry.setDescription('A single sip: schema-specific Voice URI class.\n         This entry is created automatically when a cvUriClassCfgEntry\n         is created. The manager cannot create this entry.')
cvCommonUriClassCfgURIPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setStatus('current')
if mibBuilder.loadTexts: cvCommonUriClassCfgURIPattern.setDescription('A regular expression to match an entire URI. If this object is\n         set to a zero-length string it is not used for matching with\n         the URI.\n         This object is mutually exclusive with patterns that match\n         specific fields from the URI e.g.,\n         cvSIPUriClassCfgUserIDPattern, or cvSIPUriClassCfgPhonePattern.\n         If more than one class matches a URI, the classes that matched\n         with the URI based on this pattern, are given the least\n         priority amongst matching classes.')
cvUriClassSIPHostPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1), CvUriClassPreference().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setStatus('current')
if mibBuilder.loadTexts: cvUriClassSIPHostPreference.setDescription('Preference assigned to the match length resulting from a match\n         of cvSIPUriClassCfgHostPattern against the host portion of a\n         sip: URI.')
cvUriClassSIPUserIDPreference = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2), CvUriClassPreference().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setStatus('current')
if mibBuilder.loadTexts: cvUriClassSIPUserIDPreference.setDescription('Preference assigned to the match length resulting from a match\n         of cvSIPUriClassCfgUserIDPattern against the user-id portion of\n         a sip: URI.')
cvUriClassMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2))
cvUriClassMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1))
cvUriClassMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2))
cvUriClassMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassMIBCompliance = cvUriClassMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvUriClassMIBCompliance.setDescription('The compliance statement for entities which implement the\n         CISCO VOICE URI CLASS MIB.')
cvUriClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)).setObjects(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"), ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvUriClassGroup = cvUriClassGroup.setStatus('current')
if mibBuilder.loadTexts: cvUriClassGroup.setDescription('A collection of objects providing the general Voice URI Class\n         configuration capability.')
mibBuilder.exportSymbols("CISCO-VOICE-URI-CLASS-MIB", CvUriClassPattern=CvUriClassPattern, CvUriClassPreference=CvUriClassPreference, CvUriClassTag=CvUriClassTag, CvUriClassTagIndex=CvUriClassTagIndex, PYSNMP_MODULE_ID=ciscoVoiceUriClassMIB, ciscoVoiceUriClassMIB=ciscoVoiceUriClassMIB, cvCommonUriClassCfgEntry=cvCommonUriClassCfgEntry, cvCommonUriClassCfgTable=cvCommonUriClassCfgTable, cvCommonUriClassCfgURIPattern=cvCommonUriClassCfgURIPattern, cvSIPUriClassCfgEntry=cvSIPUriClassCfgEntry, cvSIPUriClassCfgHostPattern=cvSIPUriClassCfgHostPattern, cvSIPUriClassCfgPhoneCtxtPattern=cvSIPUriClassCfgPhoneCtxtPattern, cvSIPUriClassCfgTable=cvSIPUriClassCfgTable, cvSIPUriClassCfgUserIDPattern=cvSIPUriClassCfgUserIDPattern, cvTELUriClassCfgEntry=cvTELUriClassCfgEntry, cvTELUriClassCfgPhoneCtxtPattern=cvTELUriClassCfgPhoneCtxtPattern, cvTELUriClassCfgPhoneNumPattern=cvTELUriClassCfgPhoneNumPattern, cvTELUriClassCfgTable=cvTELUriClassCfgTable, cvUriClass=cvUriClass, cvUriClassCfgEntry=cvUriClassCfgEntry, cvUriClassCfgStatus=cvUriClassCfgStatus, cvUriClassCfgTable=cvUriClassCfgTable, cvUriClassCfgTag=cvUriClassCfgTag, cvUriClassCfgType=cvUriClassCfgType, cvUriClassGroup=cvUriClassGroup, cvUriClassMIBCompliance=cvUriClassMIBCompliance, cvUriClassMIBCompliances=cvUriClassMIBCompliances, cvUriClassMIBConformance=cvUriClassMIBConformance, cvUriClassMIBGroups=cvUriClassMIBGroups, cvUriClassMIBNotifications=cvUriClassMIBNotifications, cvUriClassMIBObjects=cvUriClassMIBObjects, cvUriClassSIPGeneralConfig=cvUriClassSIPGeneralConfig, cvUriClassSIPHostPreference=cvUriClassSIPHostPreference, cvUriClassSIPUserIDPreference=cvUriClassSIPUserIDPreference)
