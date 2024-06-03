#
# PySNMP MIB module BLUECOAT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-LICENSE-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 10:54:17 2024
# On host fv-az1986-135 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Gauge32, iso, TimeTicks, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ModuleIdentity, IpAddress, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "iso", "TimeTicks", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibIdentifier")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
appLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 16))
appLicenseMIB.setRevisions(('2015-01-13 03:00',))
if mibBuilder.loadTexts: appLicenseMIB.setLastUpdated('201501130300Z')
if mibBuilder.loadTexts: appLicenseMIB.setOrganization('Blue Coat Systems, Inc.')
appLicenseMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1))
appLicenseMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 2))
appLicenseMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3))
appLicenseMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 2, 0))
appLicenseMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 1))
appLicenseMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 2))
appLicenseMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 3))
appLicenseMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 1, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appLicenseMIBCompliance = appLicenseMIBCompliance.setStatus('current')
class LicenseState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("active", 1), ("expired", 2))

class LicenseExpireType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("perpetual", 1), ("subscription", 2), ("demo", 3))

appLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1))
appLicenseStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1), )
if mibBuilder.loadTexts: appLicenseStatusTable.setStatus('current')
appLicenseStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-LICENSE-MIB", "appLicenseStatusIndex"))
if mibBuilder.loadTexts: appLicenseStatusEntry.setStatus('current')
appLicenseStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: appLicenseStatusIndex.setStatus('current')
appLicenseStatusApplicationName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusApplicationName.setStatus('current')
appLicenseStatusFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusFeatureName.setStatus('current')
appLicenseStatusComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusComponentName.setStatus('current')
appLicenseStatusExpireType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 5), LicenseExpireType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusExpireType.setStatus('current')
appLicenseStatusExpireDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusExpireDate.setStatus('current')
appLicenseStatusLicenseState = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 7), LicenseState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusLicenseState.setStatus('current')
appLicenseStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 16, 2, 0, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
if mibBuilder.loadTexts: appLicenseStateTrap.setStatus('current')
appLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 2, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appLicenseMIBGroup = appLicenseMIBGroup.setStatus('current')
appLicenseMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 3, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStateTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appLicenseMIBNotifGroup = appLicenseMIBNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-LICENSE-MIB", appLicenseStatusApplicationName=appLicenseStatusApplicationName, appLicenseMIBNotifications=appLicenseMIBNotifications, appLicenseStatusFeatureName=appLicenseStatusFeatureName, appLicenseStatusEntry=appLicenseStatusEntry, appLicenseMIBNotifGroup=appLicenseMIBNotifGroup, appLicenseStatusExpireType=appLicenseStatusExpireType, appLicenseStatusExpireDate=appLicenseStatusExpireDate, PYSNMP_MODULE_ID=appLicenseMIB, appLicenseStatusTable=appLicenseStatusTable, LicenseState=LicenseState, appLicense=appLicense, appLicenseMIBGroup=appLicenseMIBGroup, appLicenseMIBCompliances=appLicenseMIBCompliances, appLicenseMIB=appLicenseMIB, appLicenseStatusComponentName=appLicenseStatusComponentName, appLicenseStatusIndex=appLicenseStatusIndex, appLicenseMIBObjects=appLicenseMIBObjects, appLicenseMIBConformance=appLicenseMIBConformance, appLicenseMIBNotifGroups=appLicenseMIBNotifGroups, LicenseExpireType=LicenseExpireType, appLicenseStateTrap=appLicenseStateTrap, appLicenseMIBGroups=appLicenseMIBGroups, appLicenseMIBCompliance=appLicenseMIBCompliance, appLicenseMIBNotificationsPrefix=appLicenseMIBNotificationsPrefix, appLicenseStatusLicenseState=appLicenseStatusLicenseState)
