#
# PySNMP MIB module BLUECOAT-SG-ICAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ICAP-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 20:03:51 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, IpAddress, ObjectIdentity, iso, Bits, Counter64, MibIdentifier, NotificationType, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "IpAddress", "ObjectIdentity", "iso", "Bits", "Counter64", "MibIdentifier", "NotificationType", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGICAPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 14))
bluecoatSGICAPMIB.setRevisions(('2013-02-08 14:00',))
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setLastUpdated('201302081400Z')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setOrganization('Blue Coat Systems, Inc.')
bluecoatSgICAPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1))
bluecoatSgICAPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2))
sgICAPMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0))
bluecoatSgICAPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3))
class ICAPServiceEntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("service", 1), ("servivceGroup", 2))

class ICAPServiceNotificationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("queuedRequestsAboveThreshold", 1), ("queuedRequestsBelowThreshold", 2), ("deferredRequestsAboveThreshold", 3), ("deferredRequestsBelowThreshold", 4))

bluecoatSgICAPValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1))
icapService = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1))
icapServiceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1), )
if mibBuilder.loadTexts: icapServiceStatsTable.setStatus('current')
icapServiceStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-ICAP-MIB", "icapServiceStatsIndex"))
if mibBuilder.loadTexts: icapServiceStatsTableEntry.setStatus('current')
icapServiceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: icapServiceStatsIndex.setStatus('current')
icapServiceStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsName.setStatus('current')
icapServiceStatsEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 3), ICAPServiceEntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsEntityType.setStatus('current')
icapServiceStatsPlainConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainConns.setStatus('current')
icapServiceStatsSecuredConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecuredConns.setStatus('current')
icapServiceStatsPlainActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainActvReqs.setStatus('current')
icapServiceStatsSecureActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecureActvReqs.setStatus('current')
icapServiceStatsQueuedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsQueuedReqs.setStatus('current')
icapServiceStatsDeferredReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsDeferredReqs.setStatus('current')
icapServiceStatsRcvdBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsRcvdBytes.setStatus('current')
icapServiceStatsSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSentBytes.setStatus('current')
icapServiceStatsFailedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsFailedReqs.setStatus('current')
icapServiceStatsSuccessfullReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSuccessfullReqs.setStatus('current')
sgICAPNotification = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 2), ICAPServiceNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgICAPNotification.setStatus('current')
sgICAPTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"))
if mibBuilder.loadTexts: sgICAPTrap.setStatus('current')
bluecoatSgICAPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1))
bluecoatSgICAPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2))
bluecoatSgICAPMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3))
bluecoatSgICAPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "bluecoatSgICAPMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBCompliance = bluecoatSgICAPMIBCompliance.setStatus('current')
bluecoatSgICAPMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsEntityType"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecuredConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecureActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsRcvdBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSentBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsFailedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSuccessfullReqs"), ("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBGroup = bluecoatSgICAPMIBGroup.setStatus('current')
bluecoatSgICAPMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBNotifGroup = bluecoatSgICAPMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-ICAP-MIB", bluecoatSgICAPMIBNotifications=bluecoatSgICAPMIBNotifications, icapServiceStatsEntityType=icapServiceStatsEntityType, icapServiceStatsRcvdBytes=icapServiceStatsRcvdBytes, ICAPServiceNotificationType=ICAPServiceNotificationType, ICAPServiceEntityType=ICAPServiceEntityType, sgICAPTrap=sgICAPTrap, bluecoatSgICAPMIBGroups=bluecoatSgICAPMIBGroups, bluecoatSgICAPMIBGroup=bluecoatSgICAPMIBGroup, sgICAPMIBNotificationsPrefix=sgICAPMIBNotificationsPrefix, icapServiceStatsTableEntry=icapServiceStatsTableEntry, bluecoatSgICAPValues=bluecoatSgICAPValues, sgICAPNotification=sgICAPNotification, bluecoatSGICAPMIB=bluecoatSGICAPMIB, bluecoatSgICAPMIBNotifGroup=bluecoatSgICAPMIBNotifGroup, icapServiceStatsPlainActvReqs=icapServiceStatsPlainActvReqs, icapServiceStatsSentBytes=icapServiceStatsSentBytes, icapServiceStatsSecuredConns=icapServiceStatsSecuredConns, icapServiceStatsFailedReqs=icapServiceStatsFailedReqs, icapServiceStatsName=icapServiceStatsName, bluecoatSgICAPMIBCompliances=bluecoatSgICAPMIBCompliances, icapServiceStatsPlainConns=icapServiceStatsPlainConns, PYSNMP_MODULE_ID=bluecoatSGICAPMIB, bluecoatSgICAPMIBConformance=bluecoatSgICAPMIBConformance, bluecoatSgICAPMIBCompliance=bluecoatSgICAPMIBCompliance, icapService=icapService, icapServiceStatsIndex=icapServiceStatsIndex, bluecoatSgICAPMIBObjects=bluecoatSgICAPMIBObjects, icapServiceStatsSuccessfullReqs=icapServiceStatsSuccessfullReqs, icapServiceStatsTable=icapServiceStatsTable, bluecoatSgICAPMIBNotifGroups=bluecoatSgICAPMIBNotifGroups, icapServiceStatsDeferredReqs=icapServiceStatsDeferredReqs, icapServiceStatsQueuedReqs=icapServiceStatsQueuedReqs, icapServiceStatsSecureActvReqs=icapServiceStatsSecureActvReqs)
