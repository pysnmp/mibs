#
# PySNMP MIB module CISCO-VOICE-FR-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-FR-DIAL-CONTROL-MIB
# Source digest sha256:bc61a56d5b0395db85b8240a2f8fe91d0a8d1dffb00bde7350c2ee7d55aa2c57
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
ciscoVoiceFrDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 36))
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setLastUpdated('1998-04-14 00:00')
if mibBuilder.loadTexts: ciscoVoiceFrDialControlMIB.setOrganization('Cisco Systems, Inc.')
cvfrdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1))
cvFrCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1))
cvFrCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvFrCallHistoryTable.setStatus('current')
cvFrCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvFrCallHistoryEntry.setStatus('current')
cvFrCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryConnectionId.setStatus('current')
cvFrCallHistoryDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryDlci.setStatus('current')
cvFrCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistoryLowerIfName.setStatus('current')
cvFrCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 36, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvFrCallHistorySessionTarget.setStatus('current')
cvfrdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3))
cvfrdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1))
cvfrdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2))
cvfrdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 1, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvfrdcMIBCompliance = cvfrdcMIBCompliance.setStatus('current')
cvFrCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 36, 3, 2, 1)).setObjects(("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryConnectionId"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryDlci"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistoryLowerIfName"), ("CISCO-VOICE-FR-DIAL-CONTROL-MIB", "cvFrCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvFrCallHistoryGroup = cvFrCallHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-FR-DIAL-CONTROL-MIB", PYSNMP_MODULE_ID=ciscoVoiceFrDialControlMIB, ciscoVoiceFrDialControlMIB=ciscoVoiceFrDialControlMIB, cvFrCallHistory=cvFrCallHistory, cvFrCallHistoryConnectionId=cvFrCallHistoryConnectionId, cvFrCallHistoryDlci=cvFrCallHistoryDlci, cvFrCallHistoryEntry=cvFrCallHistoryEntry, cvFrCallHistoryGroup=cvFrCallHistoryGroup, cvFrCallHistoryLowerIfName=cvFrCallHistoryLowerIfName, cvFrCallHistorySessionTarget=cvFrCallHistorySessionTarget, cvFrCallHistoryTable=cvFrCallHistoryTable, cvfrdcMIBCompliance=cvfrdcMIBCompliance, cvfrdcMIBCompliances=cvfrdcMIBCompliances, cvfrdcMIBConformance=cvfrdcMIBConformance, cvfrdcMIBGroups=cvfrdcMIBGroups, cvfrdcMIBObjects=cvfrdcMIBObjects)
