#
# PySNMP MIB module CISCO-VOICE-DNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-DNIS-MIB
# Source digest sha256:f7e2b6a9996b1bf879663285f5a7cc74d557f10147f364ae7519a5de19151b7a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoVoiceDnisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 219))
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setLastUpdated('2002-05-01 00:00')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setOrganization('Cisco Systems, Inc.')
class DnisMapname(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

cvDnisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1))
cvDnisMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1))
cvDnisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisMappingTable.setStatus('current')
cvDnisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"))
if mibBuilder.loadTexts: cvDnisMappingEntry.setStatus('current')
cvDnisMappingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1), DnisMapname().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisMappingName.setStatus('current')
cvDnisMappingUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingUrl.setStatus('current')
cvDnisMappingRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("refresh", 2))).clone('idle')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingRefresh.setStatus('current')
cvDnisMappingUrlAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setStatus('current')
cvDnisMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingStatus.setStatus('current')
cvDnisNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisNodeTable.setStatus('current')
cvDnisNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"), (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"))
if mibBuilder.loadTexts: cvDnisNodeEntry.setStatus('current')
cvDnisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1), CvE164String()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvDnisNumber.setStatus('current')
cvDnisNodeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2), DisplayString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeUrl.setStatus('current')
cvDnisNodeModifiable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisNodeModifiable.setStatus('current')
cvDnisNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeStatus.setStatus('current')
cvDnisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2))
cvDnisMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0))
cvDnisMappingUrlInaccessible = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setStatus('current')
cvDnisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3))
cvDnisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1))
cvDnisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2))
cvDnisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisGroup"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisMIBCompliance = cvDnisMIBCompliance.setStatus('current')
cvDnisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisGroup = cvDnisGroup.setStatus('current')
cvDnisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisNotificationGroup = cvDnisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-DNIS-MIB", CvE164String=CvE164String, DnisMapname=DnisMapname, PYSNMP_MODULE_ID=ciscoVoiceDnisMIB, ciscoVoiceDnisMIB=ciscoVoiceDnisMIB, cvDnisGroup=cvDnisGroup, cvDnisMIBCompliance=cvDnisMIBCompliance, cvDnisMIBCompliances=cvDnisMIBCompliances, cvDnisMIBConformance=cvDnisMIBConformance, cvDnisMIBGroups=cvDnisMIBGroups, cvDnisMIBNotificationPrefix=cvDnisMIBNotificationPrefix, cvDnisMIBNotifications=cvDnisMIBNotifications, cvDnisMIBObjects=cvDnisMIBObjects, cvDnisMap=cvDnisMap, cvDnisMappingEntry=cvDnisMappingEntry, cvDnisMappingName=cvDnisMappingName, cvDnisMappingRefresh=cvDnisMappingRefresh, cvDnisMappingStatus=cvDnisMappingStatus, cvDnisMappingTable=cvDnisMappingTable, cvDnisMappingUrl=cvDnisMappingUrl, cvDnisMappingUrlAccessError=cvDnisMappingUrlAccessError, cvDnisMappingUrlInaccessible=cvDnisMappingUrlInaccessible, cvDnisNodeEntry=cvDnisNodeEntry, cvDnisNodeModifiable=cvDnisNodeModifiable, cvDnisNodeStatus=cvDnisNodeStatus, cvDnisNodeTable=cvDnisNodeTable, cvDnisNodeUrl=cvDnisNodeUrl, cvDnisNotificationGroup=cvDnisNotificationGroup, cvDnisNumber=cvDnisNumber)
