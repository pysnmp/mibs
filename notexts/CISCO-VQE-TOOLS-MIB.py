#
# PySNMP MIB module CISCO-VQE-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VQE-TOOLS-MIB
# Source digest sha256:f2be2f56b73809a20af0132bf1b04124b4b6e19479e594cbe720e399f5359151
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVqeToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 969))
ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setLastUpdated('2009-12-18 13:41')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setOrganization('Cisco Systems, Inc.')
ciscoVqeToolsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 0))
ciscoVqeToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1))
ciscoVqeToolsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2))
cvqtVcdsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1))
cvqtNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1), Gauge32()).setUnits('RTSP connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtNumberOfSessions.setStatus('current')
cvqtTotalReceivedRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2), Counter64()).setUnits('RTSP requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setStatus('current')
cvqtTotalSentResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3), Counter64()).setUnits('RTSP responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalSentResponses.setStatus('current')
cvqtRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4), Gauge32()).setUnits('requests per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtRequestRate.setStatus('current')
cvqtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1))
cvqtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2))
cvqtMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvqtMIBReadOnlyCompliance = cvqtMIBReadOnlyCompliance.setStatus('current')
ciscoVqeToolsVcdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"), ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVqeToolsVcdsGroup = ciscoVqeToolsVcdsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VQE-TOOLS-MIB", PYSNMP_MODULE_ID=ciscoVqeToolsMIB, ciscoVqeToolsMIB=ciscoVqeToolsMIB, ciscoVqeToolsMIBConform=ciscoVqeToolsMIBConform, ciscoVqeToolsMIBNotifs=ciscoVqeToolsMIBNotifs, ciscoVqeToolsMIBObjects=ciscoVqeToolsMIBObjects, ciscoVqeToolsVcdsGroup=ciscoVqeToolsVcdsGroup, cvqtMIBCompliances=cvqtMIBCompliances, cvqtMIBGroups=cvqtMIBGroups, cvqtMIBReadOnlyCompliance=cvqtMIBReadOnlyCompliance, cvqtNumberOfSessions=cvqtNumberOfSessions, cvqtRequestRate=cvqtRequestRate, cvqtTotalReceivedRequests=cvqtTotalReceivedRequests, cvqtTotalSentResponses=cvqtTotalSentResponses, cvqtVcdsInfo=cvqtVcdsInfo)
