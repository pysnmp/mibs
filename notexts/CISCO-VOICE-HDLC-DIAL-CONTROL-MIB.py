#
# PySNMP MIB module CISCO-VOICE-HDLC-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Source digest sha256:104e8ba919947b2c2c7f0c02666e690ab51b5d8ebce3f71d4988cf52b758c94e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-DIAL-CONTROL-MIB", "CvcGUid")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceHdlcDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 37))
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setLastUpdated('1998-04-14 00:00')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvhdlcdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1))
cvHdlcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1))
cvHdlcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvHdlcCallHistoryTable.setStatus('current')
cvHdlcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvHdlcCallHistoryEntry.setStatus('current')
cvHdlcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryConnectionId.setStatus('current')
cvHdlcCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryLowerIfName.setStatus('current')
cvHdlcCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistorySessionTarget.setStatus('current')
cvhdlcdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3))
cvhdlcdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1))
cvhdlcdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2))
cvhdlcdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvhdlcdcMIBCompliance = cvhdlcdcMIBCompliance.setStatus('current')
cvHdlcCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryConnectionId"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryLowerIfName"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvHdlcCallHistoryGroup = cvHdlcCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", PYSNMP_MODULE_ID=ciscoVoiceHdlcDialControlMIB, ciscoVoiceHdlcDialControlMIB=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistory=cvHdlcCallHistory, cvHdlcCallHistoryConnectionId=cvHdlcCallHistoryConnectionId, cvHdlcCallHistoryEntry=cvHdlcCallHistoryEntry, cvHdlcCallHistoryGroup=cvHdlcCallHistoryGroup, cvHdlcCallHistoryLowerIfName=cvHdlcCallHistoryLowerIfName, cvHdlcCallHistorySessionTarget=cvHdlcCallHistorySessionTarget, cvHdlcCallHistoryTable=cvHdlcCallHistoryTable, cvhdlcdcMIBCompliance=cvhdlcdcMIBCompliance, cvhdlcdcMIBCompliances=cvhdlcdcMIBCompliances, cvhdlcdcMIBConformance=cvhdlcdcMIBConformance, cvhdlcdcMIBGroups=cvhdlcdcMIBGroups, cvhdlcdcMIBObjects=cvhdlcdcMIBObjects)
