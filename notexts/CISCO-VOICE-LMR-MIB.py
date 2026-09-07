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
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setLastUpdated('2004-10-14 00:00')
if mibBuilder.loadTexts: ciscoVoiceLmrMIB.setOrganization('Cisco Systems, Inc.')
cvlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1))
cvlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2))
cvlToneObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1))
class VoiceFrequency(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4000)

class VoiceAmplitude(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-30, 3)

class LmrToneDuration(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 500)

cvlClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlClassTable.setStatus('current')
cvlClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlClassIndex"))
if mibBuilder.loadTexts: cvlClassEntry.setStatus('current')
cvlClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlClassIndex.setStatus('current')
cvlClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlClassName.setStatus('current')
cvlDigitalFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("digitalFilterNone", 0), ("digitalFilter1950HZ", 1), ("digitalFilter2175HZ", 2))).clone('digitalFilterNone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlDigitalFilter.setStatus('current')
cvlGuardToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 4), VoiceFrequency().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneFreq.setStatus('current')
cvlGuardToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 5), VoiceAmplitude().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlGuardToneAmp.setStatus('current')
cvlIdleToneFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlIdleToneFlag.setStatus('current')
cvlSignalToneTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneTable.setStatus('current')
cvlSignalToneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneGroupIndex"), (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneIndex"))
if mibBuilder.loadTexts: cvlSignalToneEntry.setStatus('current')
cvlSignalToneGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneGroupIndex.setStatus('current')
cvlSignalToneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvlSignalToneIndex.setStatus('current')
cvlSignalToneName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneName.setStatus('current')
cvlSignalToneFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 4), VoiceFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneFreq.setStatus('current')
cvlSignalToneAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 5), VoiceAmplitude()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneAmp.setStatus('current')
cvlSignalToneDur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 6), LmrToneDuration()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvlSignalToneDur.setStatus('current')
cvlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1))
cvlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2))
cvlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlToneClassGroup"), ("CISCO-VOICE-LMR-MIB", "cvlToneSignalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlMIBCompliance = cvlMIBCompliance.setStatus('current')
cvlToneClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlClassName"), ("CISCO-VOICE-LMR-MIB", "cvlDigitalFilter"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlGuardToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlIdleToneFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneClassGroup = cvlToneClassGroup.setStatus('current')
cvlToneSignalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)).setObjects(("CISCO-VOICE-LMR-MIB", "cvlSignalToneName"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneFreq"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneAmp"), ("CISCO-VOICE-LMR-MIB", "cvlSignalToneDur"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvlToneSignalGroup = cvlToneSignalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-LMR-MIB", LmrToneDuration=LmrToneDuration, PYSNMP_MODULE_ID=ciscoVoiceLmrMIB, VoiceAmplitude=VoiceAmplitude, VoiceFrequency=VoiceFrequency, ciscoVoiceLmrMIB=ciscoVoiceLmrMIB, cvlClassEntry=cvlClassEntry, cvlClassIndex=cvlClassIndex, cvlClassName=cvlClassName, cvlClassTable=cvlClassTable, cvlDigitalFilter=cvlDigitalFilter, cvlGuardToneAmp=cvlGuardToneAmp, cvlGuardToneFreq=cvlGuardToneFreq, cvlIdleToneFlag=cvlIdleToneFlag, cvlMIBCompliance=cvlMIBCompliance, cvlMIBCompliances=cvlMIBCompliances, cvlMIBConformance=cvlMIBConformance, cvlMIBGroups=cvlMIBGroups, cvlMIBObjects=cvlMIBObjects, cvlSignalToneAmp=cvlSignalToneAmp, cvlSignalToneDur=cvlSignalToneDur, cvlSignalToneEntry=cvlSignalToneEntry, cvlSignalToneFreq=cvlSignalToneFreq, cvlSignalToneGroupIndex=cvlSignalToneGroupIndex, cvlSignalToneIndex=cvlSignalToneIndex, cvlSignalToneName=cvlSignalToneName, cvlSignalToneTable=cvlSignalToneTable, cvlToneClassGroup=cvlToneClassGroup, cvlToneObjects=cvlToneObjects, cvlToneSignalGroup=cvlToneSignalGroup)
