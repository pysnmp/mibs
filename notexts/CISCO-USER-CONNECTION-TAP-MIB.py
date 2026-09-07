#
# PySNMP MIB module CISCO-USER-CONNECTION-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-USER-CONNECTION-TAP-MIB
# Source digest sha256:89e0a6cb5fc110213d2f8a5098f9b1c2d6477542b5bbee8e550cddf3f4f6a7a3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoUserConnectionTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 400))
ciscoUserConnectionTapMIB.setRevisions(('2007-08-09 00:00', '2004-03-11 00:00',))
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setLastUpdated('2007-08-09 00:00')
if mibBuilder.loadTexts: ciscoUserConnectionTapMIB.setOrganization('Cisco Systems, Inc.')
cUserConnectionTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1))
cUserConnectionTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2))
cuctTapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1))
cuctTapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("acctSessionId", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuctTapStreamCapabilities.setStatus('current')
cuctTapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cuctTapStreamTable.setStatus('current')
cuctTapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cuctTapStreamEntry.setStatus('current')
cuctTapStreamAcctSessID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamAcctSessID.setStatus('current')
cuctTapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 400, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cuctTapStreamStatus.setStatus('current')
cUserConnectionTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1))
cUserConnectionTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2))
cUserConnectionTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 1, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamComplianceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cUserConnectionTapMIBCompliance = cUserConnectionTapMIBCompliance.setStatus('current')
cuctTapStreamComplianceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 400, 2, 2, 1)).setObjects(("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamCapabilities"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamAcctSessID"), ("CISCO-USER-CONNECTION-TAP-MIB", "cuctTapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cuctTapStreamComplianceGroup = cuctTapStreamComplianceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-USER-CONNECTION-TAP-MIB", PYSNMP_MODULE_ID=ciscoUserConnectionTapMIB, cUserConnectionTapMIBCompliance=cUserConnectionTapMIBCompliance, cUserConnectionTapMIBCompliances=cUserConnectionTapMIBCompliances, cUserConnectionTapMIBConform=cUserConnectionTapMIBConform, cUserConnectionTapMIBGroups=cUserConnectionTapMIBGroups, cUserConnectionTapMIBObjects=cUserConnectionTapMIBObjects, ciscoUserConnectionTapMIB=ciscoUserConnectionTapMIB, cuctTapStreamAcctSessID=cuctTapStreamAcctSessID, cuctTapStreamCapabilities=cuctTapStreamCapabilities, cuctTapStreamComplianceGroup=cuctTapStreamComplianceGroup, cuctTapStreamEncodePacket=cuctTapStreamEncodePacket, cuctTapStreamEntry=cuctTapStreamEntry, cuctTapStreamStatus=cuctTapStreamStatus, cuctTapStreamTable=cuctTapStreamTable)
