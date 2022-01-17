#
# PySNMP MIB module BLUECOAT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-LICENSE-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 19:19:33 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, iso, ObjectIdentity, IpAddress, MibIdentifier, Counter64, Bits, Gauge32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter64", "Bits", "Gauge32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType")
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
mibBuilder.exportSymbols("BLUECOAT-LICENSE-MIB", appLicenseStateTrap=appLicenseStateTrap, appLicenseStatusExpireType=appLicenseStatusExpireType, appLicenseStatusComponentName=appLicenseStatusComponentName, appLicenseMIBNotifGroup=appLicenseMIBNotifGroup, appLicenseStatusExpireDate=appLicenseStatusExpireDate, appLicenseMIBNotifications=appLicenseMIBNotifications, appLicenseMIBGroup=appLicenseMIBGroup, appLicenseMIBCompliances=appLicenseMIBCompliances, appLicenseMIBNotifGroups=appLicenseMIBNotifGroups, LicenseState=LicenseState, appLicenseMIBObjects=appLicenseMIBObjects, appLicenseStatusFeatureName=appLicenseStatusFeatureName, appLicenseMIBCompliance=appLicenseMIBCompliance, appLicenseStatusEntry=appLicenseStatusEntry, PYSNMP_MODULE_ID=appLicenseMIB, appLicenseMIBNotificationsPrefix=appLicenseMIBNotificationsPrefix, appLicenseStatusLicenseState=appLicenseStatusLicenseState, appLicenseStatusTable=appLicenseStatusTable, appLicense=appLicense, appLicenseMIBConformance=appLicenseMIBConformance, appLicenseMIB=appLicenseMIB, appLicenseStatusIndex=appLicenseStatusIndex, appLicenseStatusApplicationName=appLicenseStatusApplicationName, appLicenseMIBGroups=appLicenseMIBGroups, LicenseExpireType=LicenseExpireType)
