#
# PySNMP MIB module CISCO-VOICE-LMR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-LMR-MIB
# Source digest sha256:044ed041d4c66141636453ceee29b38f5a5d552cd2869fe20242fcc3f56dd8c3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoVoiceLmrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 510))
ciscoVoiceLmrMIB.setRevisions(('2004-10-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setRevisionsDescriptions(('the initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setLastUpdated('2004-10-14 00:00')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setDescription('This MIB module  provides management of voice tone\n                 signal as static injected tone for Land Mobile Radio\n                 The tone signal includes tone, pause, guard/idle tone.\n                 User can configure a sequence of tone and pause to\n                 be played out before any voice sample is played out.\n                 These tones are used to wake up the radio and \n                 select the radio channel. During the voice playout,\n                 a configured guard tone will be mixed with the voice\n                 to keep the radio active. For some radio systems, \n                 there is no need for the guard tone, but a configured\n                 idle tone is needed  to inform the radio that the\n                 channel is idle. It is possible that the radio system\n                 will generate guard/idle tone.  In that case,\n                 the IOS can instruct the DSP to filter out the radio\n                 generated guard/idle tone by enabling digital filter. \n                 Digital filter is able to filter out either 1950HZ or\n                 2175HZ tone.\n                ')
cvlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1))
cvlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2))
cvlToneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1))
class VoiceFrequency(TextualConvention, Unsigned32):
    description = 'This textual convention is used to represent the\n               audible voice frequency between 1HZ to 4000HZ.\n               Value 0 indicates this textual convention is not\n               configured.\n              '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4000)

class VoiceAmplitude(TextualConvention, Integer32):
    description = 'This textual convention is used to\n               represent the amplitude of voice between -30 \n               to 3 dbm.\n               dbm is the absolute output and input optical\n               power levels in mW.\n              '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-30, 3)

class LmrToneDuration(TextualConvention, Unsigned32):
    description = 'This textual convention is used to represent\n               the duration of tone played. It is measured in\n               milliseconds.\n              '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 500)

cvlClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlClassTable.setStatus('current')
if mibBuilder.loadTexts: cvlClassTable.setDescription('The table contains the LMR guard/idle tone frequency\n            and amplitude. It also specifies what frequency will be\n            filtered out from radio voice input by dsp digital filter.\n           ')
cvlClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlClassIndex"))
if mibBuilder.loadTexts: cvlClassEntry.setStatus('current')
if mibBuilder.loadTexts: cvlClassEntry.setDescription('A concept row in cvlClassTable. It has class name,\n             tone frequency, tone amplitude, guard/idle tone\n             indicator and digital filter information.\n            ')
cvlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlClassIndex.setStatus('current')
if mibBuilder.loadTexts: cvlClassIndex.setDescription('An arbitrary integer which increases monotonically to\n             index the cvlClassTable.\n            ')
cvlClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlClassName.setStatus('current')
if mibBuilder.loadTexts: cvlClassName.setDescription('The object reflects the voice class name.')
cvlDigitalFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("digitalFilterNone", 0), ("digitalFilter1950HZ", 1), ("digitalFilter2175HZ", 2))).clone('digitalFilterNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlDigitalFilter.setStatus('current')
if mibBuilder.loadTexts: cvlDigitalFilter.setDescription('This object reflects which tone frequency should \n             be filtered out from radio input.\n             ')
cvlGuardToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 4), VoiceFrequency().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneFreq.setStatus('current')
if mibBuilder.loadTexts: cvlGuardToneFreq.setDescription('This object reflects the guard/idle tone frequency between\n             1-4000 HZ. If there is no guard/idle tone configured for\n             this voice class, cvlGuardToneFreq has value 0.\n            ')
cvlGuardToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 5), VoiceAmplitude().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneAmp.setStatus('current')
if mibBuilder.loadTexts: cvlGuardToneAmp.setDescription('This object reflects the guard/idle tone amplitude in dbm.\n            ')
cvlIdleToneFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlIdleToneFlag.setStatus('current')
if mibBuilder.loadTexts: cvlIdleToneFlag.setDescription('This object reflects this voice class has guard/idle\n             tone configured. true means guard tone and false means\n             idle tone. \n            ')
cvlSignalToneTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneTable.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneTable.setDescription('The table contains the LMR injected tone information\n            and playout sequence for voice class tone signal.\n            The tones with same cvlSignalToneGroupIndex\n            will be played out in ascending order of the \n            cvlSignalToneIndex.            \n           ')
cvlSignalToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneGroupIndex"), (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneIndex"))
if mibBuilder.loadTexts: cvlSignalToneEntry.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneEntry.setDescription('An entry in the table, containing information\n             about a single tone.')
cvlSignalToneGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setDescription('This object reflects a group of tones. \n             The tones with same cvlSignalToneGroupIndex\n             will be played out in ascending order of the \n             cvlSignalToneIndex.\n            ')
cvlSignalToneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneIndex.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneIndex.setDescription('This object reflects the tone playout sequence in\n             ascending order of the index for the tones with same\n             cvlSignalToneGroupIndex value.\n            ')
cvlSignalToneName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneName.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneName.setDescription('The object reflects the tone signal class name.')
cvlSignalToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneFreq.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneFreq.setDescription('This object reflects the tone frequency in HZ.\n             If the value is 0 then no tone will be played out\n             and can be used to provide pause during a sequence\n             of tones.\n            ')
cvlSignalToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneAmp.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneAmp.setDescription('This object reflects the signal tone amplitude in dbm.')
cvlSignalToneDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 6), LmrToneDuration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneDur.setStatus('current')
if mibBuilder.loadTexts: cvlSignalToneDur.setDescription('This object reflects the signal tone duration.')
cvlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1))
cvlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2))
cvlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlToneClassGroup"), ("CISCO-VOICE-LMR-MIB", "cvlToneSignalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlMIBCompliance = cvlMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvlMIBCompliance.setDescription('The compliance statements for the Cisco Land Mobile\n             Radio (LMR) MIB.\n            ')
cvlToneClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlClassName"), ("CISCO-VOICE-LMR-MIB", "cvlDigitalFilter"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlIdleToneFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneClassGroup = cvlToneClassGroup.setStatus('current')
if mibBuilder.loadTexts: cvlToneClassGroup.setDescription('A collection of objects that provide info \n                 applicable to digital notch filter or guard/idle\n                 tone.\n                ')
cvlToneSignalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlSignalToneName"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneDur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneSignalGroup = cvlToneSignalGroup.setStatus('current')
if mibBuilder.loadTexts: cvlToneSignalGroup.setDescription('A collection of objects that provide info \n                 applicable to either wake-up tone, function\n                 selection or pause between tones. It also \n                 provides the info about the playout sequence\n                 of the tones.\n                ')
mibBuilder.exportSymbols("CISCO-VOICE-LMR-MIB", LmrToneDuration=LmrToneDuration, PYSNMP_MODULE_ID=ciscoVoiceLmrMIB, VoiceAmplitude=VoiceAmplitude, VoiceFrequency=VoiceFrequency, ciscoVoiceLmrMIB=ciscoVoiceLmrMIB, cvlClassEntry=cvlClassEntry, cvlClassIndex=cvlClassIndex, cvlClassName=cvlClassName, cvlClassTable=cvlClassTable, cvlDigitalFilter=cvlDigitalFilter, cvlGuardToneAmp=cvlGuardToneAmp, cvlGuardToneFreq=cvlGuardToneFreq, cvlIdleToneFlag=cvlIdleToneFlag, cvlMIBCompliance=cvlMIBCompliance, cvlMIBCompliances=cvlMIBCompliances, cvlMIBConformance=cvlMIBConformance, cvlMIBGroups=cvlMIBGroups, cvlMIBObjects=cvlMIBObjects, cvlSignalToneAmp=cvlSignalToneAmp, cvlSignalToneDur=cvlSignalToneDur, cvlSignalToneEntry=cvlSignalToneEntry, cvlSignalToneFreq=cvlSignalToneFreq, cvlSignalToneGroupIndex=cvlSignalToneGroupIndex, cvlSignalToneIndex=cvlSignalToneIndex, cvlSignalToneName=cvlSignalToneName, cvlSignalToneTable=cvlSignalToneTable, cvlToneClassGroup=cvlToneClassGroup, cvlToneObjects=cvlToneObjects, cvlToneSignalGroup=cvlToneSignalGroup)
