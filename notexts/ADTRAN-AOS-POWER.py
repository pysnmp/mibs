#
# PySNMP MIB module ADTRAN-AOS-POWER (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-POWER
# Produced by pysmi-1.1.12 at Wed Jul  3 09:52:33 2024
# On host fv-az530-296 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSPower = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSPower")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Counter32, ObjectIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Gauge32, IpAddress, iso, TimeTicks, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Gauge32", "IpAddress", "iso", "TimeTicks", "Integer32", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
adGenAOSPowerMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1))
adGenAOSPowerMonitor.setRevisions(('2010-09-10 00:00', '2013-02-10 00:00',))
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setLastUpdated('201009100000Z')
if mibBuilder.loadTexts: adGenAOSPowerMonitor.setOrganization('ADTRAN, Inc.')
adGenAOSPowerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0))
adGenAOSPowerRollOverCtl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1))
adGenAOSPowerEpsRps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2))
class AdEpsPowerDeliveryStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("delivering", 1), ("notDelivering", 2), ("failed", 3), ("unknown", 4))

class AdRpsPowerDeliveryStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("failed", 1), ("busy", 2), ("delivering", 3), ("available", 4), ("unknown", 5))

class AdPowerConnectionStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("connected", 1), ("notConnected", 2), ("notApplicable", 3), ("unknown", 4))

adGenAOSPowerRolloverOnAC = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRolloverOnAC.setStatus('current')
adGenAOSPwrRollOvrEvntSecSinceEpoch = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSPwrRollOvrEvntSecSinceEpoch.setStatus('current')
adGenAOSPowerEpsRpsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1), )
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsTable.setStatus('current')
adGenAOSPowerEpsRpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"))
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsEntry.setStatus('current')
adGenAOSPowerEpsRpsInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsRpsInstanceId.setStatus('current')
adGenAOSPowerEpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 2), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsConnectionState.setStatus('current')
adGenAOSPowerEpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 3), AdEpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerEpsDeliveryState.setStatus('current')
adGenAOSPowerRpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 4), AdPowerConnectionStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsConnectionState.setStatus('current')
adGenAOSPowerRpsDeliveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 5), AdRpsPowerDeliveryStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSPowerRpsDeliveryState.setStatus('current')
adGenAOSPowerRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"), ("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"))
if mibBuilder.loadTexts: adGenAOSPowerRollover.setStatus('current')
adGenAOSEpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSEpsConnectionChange.setStatus('current')
adGenAOSEpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSEpsDeliveryChange.setStatus('current')
adGenAOSRpsConnectionChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"))
if mibBuilder.loadTexts: adGenAOSRpsConnectionChange.setStatus('current')
adGenAOSRpsDeliveryChange = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"))
if mibBuilder.loadTexts: adGenAOSRpsDeliveryChange.setStatus('current')
adGenAOSPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11))
adGenAOSPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1))
adGenAOSPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2))
adGenAOSPowerFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollOverCtlGroup"), ("ADTRAN-AOS-POWER", "adGenAOSPowerNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsRpsConfigurationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSEpsNotificationGroup"), ("ADTRAN-AOS-POWER", "adGenAOSRpsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerFullCompliance = adGenAOSPowerFullCompliance.setStatus('current')
adGenAOSPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 1)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerNotificationGroup = adGenAOSPowerNotificationGroup.setStatus('current')
adGenAOSPowerRollOverCtlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 2)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSPowerRollOverCtlGroup = adGenAOSPowerRollOverCtlGroup.setStatus('current')
adGenAOSEpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 3)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSEpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSEpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsNotificationGroup = adGenAOSEpsNotificationGroup.setStatus('current')
adGenAOSRpsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 4)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSRpsConnectionChange"), ("ADTRAN-AOS-POWER", "adGenAOSRpsDeliveryChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSRpsNotificationGroup = adGenAOSRpsNotificationGroup.setStatus('current')
adGenAOSEpsRpsConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 5)).setObjects(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"), ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSEpsRpsConfigurationGroup = adGenAOSEpsRpsConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-POWER", adGenAOSPowerRollover=adGenAOSPowerRollover, adGenAOSEpsDeliveryChange=adGenAOSEpsDeliveryChange, adGenAOSPowerEpsRpsTable=adGenAOSPowerEpsRpsTable, AdPowerConnectionStateTC=AdPowerConnectionStateTC, adGenAOSEpsConnectionChange=adGenAOSEpsConnectionChange, adGenAOSPowerGroups=adGenAOSPowerGroups, adGenAOSPowerEpsDeliveryState=adGenAOSPowerEpsDeliveryState, adGenAOSEpsNotificationGroup=adGenAOSEpsNotificationGroup, adGenAOSPowerMonitor=adGenAOSPowerMonitor, adGenAOSPowerRpsConnectionState=adGenAOSPowerRpsConnectionState, adGenAOSPowerEpsRpsInstanceId=adGenAOSPowerEpsRpsInstanceId, adGenAOSPowerRollOverCtl=adGenAOSPowerRollOverCtl, adGenAOSRpsConnectionChange=adGenAOSRpsConnectionChange, adGenAOSRpsNotificationGroup=adGenAOSRpsNotificationGroup, adGenAOSPowerNotificationGroup=adGenAOSPowerNotificationGroup, AdRpsPowerDeliveryStateTC=AdRpsPowerDeliveryStateTC, adGenAOSPwrRollOvrEvntSecSinceEpoch=adGenAOSPwrRollOvrEvntSecSinceEpoch, adGenAOSPowerRollOverCtlGroup=adGenAOSPowerRollOverCtlGroup, AdEpsPowerDeliveryStateTC=AdEpsPowerDeliveryStateTC, adGenAOSPowerEpsConnectionState=adGenAOSPowerEpsConnectionState, adGenAOSPowerEpsRpsEntry=adGenAOSPowerEpsRpsEntry, adGenAOSPowerEpsRps=adGenAOSPowerEpsRps, adGenAOSPowerRpsDeliveryState=adGenAOSPowerRpsDeliveryState, adGenAOSPowerFullCompliance=adGenAOSPowerFullCompliance, PYSNMP_MODULE_ID=adGenAOSPowerMonitor, adGenAOSPowerConformance=adGenAOSPowerConformance, adGenAOSRpsDeliveryChange=adGenAOSRpsDeliveryChange, adGenAOSPowerRolloverOnAC=adGenAOSPowerRolloverOnAC, adGenAOSPowerTraps=adGenAOSPowerTraps, adGenAOSEpsRpsConfigurationGroup=adGenAOSEpsRpsConfigurationGroup, adGenAOSPowerCompliances=adGenAOSPowerCompliances)
