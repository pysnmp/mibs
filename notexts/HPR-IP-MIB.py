#
# PySNMP MIB module HPR-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source HPR-IP-MIB
# Source digest sha256:102b3e51351d7969b5fc5c0cdd91477ab7ecd7e4a239724ac47dbefdfacb2693
# Produced by pysmi-2.3.0
#
SnaControlPointName, = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hprCompliances, hprGroups, hprObjects = mibBuilder.importSymbols("HPR-MIB", "hprCompliances", "hprGroups", "hprObjects")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hprIp = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 6, 1, 5))
hprIp.setRevisions(('1998-09-24 00:00',))
if mibBuilder.loadTexts: hprIp.setLastUpdated('1998-09-24 00:00')
if mibBuilder.loadTexts: hprIp.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
class AppnTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("low", 1), ("medium", 2), ("high", 3), ("network", 4), ("llcAndFnRoutedNlp", 5))

class AppnTOSPrecedence(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

hprIpActiveLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpActiveLsTable.setStatus('current')
hprIpActiveLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "HPR-IP-MIB", "hprIpActiveLsLsName"), (0, "HPR-IP-MIB", "hprIpActiveLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpActiveLsEntry.setStatus('current')
hprIpActiveLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpActiveLsLsName.setStatus('current')
hprIpActiveLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 2), AppnTrafficType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpActiveLsAppnTrafficType.setStatus('current')
hprIpActiveLsUdpPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hprIpActiveLsUdpPackets.setStatus('current')
hprIpAppnPortTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpAppnPortTable.setStatus('current')
hprIpAppnPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "HPR-IP-MIB", "hprIpAppnPortName"), (0, "HPR-IP-MIB", "hprIpAppnPortAppnTrafficType"))
if mibBuilder.loadTexts: hprIpAppnPortEntry.setStatus('current')
hprIpAppnPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpAppnPortName.setStatus('current')
hprIpAppnPortAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 2), AppnTrafficType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpAppnPortAppnTrafficType.setStatus('current')
hprIpAppnPortTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 3), AppnTOSPrecedence()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hprIpAppnPortTOSPrecedence.setStatus('current')
hprIpLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpLsTable.setStatus('current')
hprIpLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "HPR-IP-MIB", "hprIpLsLsName"), (0, "HPR-IP-MIB", "hprIpLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpLsEntry.setStatus('current')
hprIpLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpLsLsName.setStatus('current')
hprIpLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 2), AppnTrafficType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpLsAppnTrafficType.setStatus('current')
hprIpLsTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsTOSPrecedence.setStatus('current')
hprIpLsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsRowStatus.setStatus('current')
hprIpCnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpCnTable.setStatus('current')
hprIpCnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "HPR-IP-MIB", "hprIpCnVrnName"), (0, "HPR-IP-MIB", "hprIpCnAppnTrafficType"))
if mibBuilder.loadTexts: hprIpCnEntry.setStatus('current')
hprIpCnVrnName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 1), SnaControlPointName()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpCnVrnName.setStatus('current')
hprIpCnAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 2), AppnTrafficType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: hprIpCnAppnTrafficType.setStatus('current')
hprIpCnTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnTOSPrecedence.setStatus('current')
hprIpCnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnRowStatus.setStatus('current')
hprIpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 6, 2, 1, 2)).setObjects(("HPR-IP-MIB", "hprIpMonitoringGroup"), ("HPR-IP-MIB", "hprIpConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpCompliance = hprIpCompliance.setStatus('current')
hprIpMonitoringGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 5)).setObjects(("HPR-IP-MIB", "hprIpActiveLsUdpPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpMonitoringGroup = hprIpMonitoringGroup.setStatus('current')
hprIpConfigurationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 6)).setObjects(("HPR-IP-MIB", "hprIpAppnPortTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsRowStatus"), ("HPR-IP-MIB", "hprIpCnTOSPrecedence"), ("HPR-IP-MIB", "hprIpCnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpConfigurationGroup = hprIpConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("HPR-IP-MIB", AppnTOSPrecedence=AppnTOSPrecedence, AppnTrafficType=AppnTrafficType, PYSNMP_MODULE_ID=hprIp, hprIp=hprIp, hprIpActiveLsAppnTrafficType=hprIpActiveLsAppnTrafficType, hprIpActiveLsEntry=hprIpActiveLsEntry, hprIpActiveLsLsName=hprIpActiveLsLsName, hprIpActiveLsTable=hprIpActiveLsTable, hprIpActiveLsUdpPackets=hprIpActiveLsUdpPackets, hprIpAppnPortAppnTrafficType=hprIpAppnPortAppnTrafficType, hprIpAppnPortEntry=hprIpAppnPortEntry, hprIpAppnPortName=hprIpAppnPortName, hprIpAppnPortTOSPrecedence=hprIpAppnPortTOSPrecedence, hprIpAppnPortTable=hprIpAppnPortTable, hprIpCnAppnTrafficType=hprIpCnAppnTrafficType, hprIpCnEntry=hprIpCnEntry, hprIpCnRowStatus=hprIpCnRowStatus, hprIpCnTOSPrecedence=hprIpCnTOSPrecedence, hprIpCnTable=hprIpCnTable, hprIpCnVrnName=hprIpCnVrnName, hprIpCompliance=hprIpCompliance, hprIpConfigurationGroup=hprIpConfigurationGroup, hprIpLsAppnTrafficType=hprIpLsAppnTrafficType, hprIpLsEntry=hprIpLsEntry, hprIpLsLsName=hprIpLsLsName, hprIpLsRowStatus=hprIpLsRowStatus, hprIpLsTOSPrecedence=hprIpLsTOSPrecedence, hprIpLsTable=hprIpLsTable, hprIpMonitoringGroup=hprIpMonitoringGroup)
