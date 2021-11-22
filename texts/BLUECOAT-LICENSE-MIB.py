#
# PySNMP MIB module BLUECOAT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-LICENSE-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:30:08 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, ObjectIdentity, Bits, MibIdentifier, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, TimeTicks, Integer32, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Bits", "MibIdentifier", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "TimeTicks", "Integer32", "Counter32", "Unsigned32", "Counter64")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
appLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 16))
appLicenseMIB.setRevisions(('2015-01-13 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: appLicenseMIB.setRevisionsDescriptions(('Initial revision of this MIB.',))
if mibBuilder.loadTexts: appLicenseMIB.setLastUpdated('201501130300Z')
if mibBuilder.loadTexts: appLicenseMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: appLicenseMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: appLicenseMIB.setDescription('The appliance license status MIB is used to monitor\n                         the state of appliance Licenses')
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
if mibBuilder.loadTexts: appLicenseMIBCompliance.setDescription('The compliance statement for health check module. ')
class LicenseState(TextualConvention, Integer32):
    description = 'State of the License'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("active", 1), ("expired", 2))

class LicenseExpireType(TextualConvention, Integer32):
    description = 'Type of license expiration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("perpetual", 1), ("subscription", 2), ("demo", 3))

appLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1))
appLicenseStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1), )
if mibBuilder.loadTexts: appLicenseStatusTable.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusTable.setDescription('Table of appliance licenses.')
appLicenseStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-LICENSE-MIB", "appLicenseStatusIndex"))
if mibBuilder.loadTexts: appLicenseStatusEntry.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusEntry.setDescription('An appLicenseStatusTable entry describes the\n                         license status for each license of the appliance.')
appLicenseStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: appLicenseStatusIndex.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusIndex.setDescription('An arbitrary value which uniquely identifies the license.')
appLicenseStatusApplicationName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusApplicationName.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusApplicationName.setDescription('This variable indicates the application name of the license entry.')
appLicenseStatusFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusFeatureName.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusFeatureName.setDescription('This variable indicates the feature name of the license entry.')
appLicenseStatusComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusComponentName.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusComponentName.setDescription('This variable indicates the component name of the license entry.')
appLicenseStatusExpireType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 5), LicenseExpireType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusExpireType.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusExpireType.setDescription('This variable indicates the type of license expiration.')
appLicenseStatusExpireDate = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusExpireDate.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusExpireDate.setDescription('This variable indicates the license entry expiration date\n                         if applicable.')
appLicenseStatusLicenseState = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 16, 1, 1, 1, 1, 7), LicenseState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appLicenseStatusLicenseState.setStatus('current')
if mibBuilder.loadTexts: appLicenseStatusLicenseState.setDescription('This variable indicates the state of the license entry.')
appLicenseStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 16, 2, 0, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
if mibBuilder.loadTexts: appLicenseStateTrap.setStatus('current')
if mibBuilder.loadTexts: appLicenseStateTrap.setDescription('The appliance license state has changed.')
appLicenseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 2, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStatusApplicationName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusFeatureName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusComponentName"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireType"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusExpireDate"), ("BLUECOAT-LICENSE-MIB", "appLicenseStatusLicenseState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appLicenseMIBGroup = appLicenseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: appLicenseMIBGroup.setDescription('Group of Appliance License related objects.')
appLicenseMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 16, 3, 3, 1)).setObjects(("BLUECOAT-LICENSE-MIB", "appLicenseStateTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appLicenseMIBNotifGroup = appLicenseMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: appLicenseMIBNotifGroup.setDescription('Group of Appliance License notifications.')
mibBuilder.exportSymbols("BLUECOAT-LICENSE-MIB", appLicenseStatusExpireDate=appLicenseStatusExpireDate, appLicenseMIBGroups=appLicenseMIBGroups, appLicenseMIBNotifications=appLicenseMIBNotifications, appLicense=appLicense, PYSNMP_MODULE_ID=appLicenseMIB, appLicenseMIB=appLicenseMIB, appLicenseMIBCompliances=appLicenseMIBCompliances, appLicenseMIBCompliance=appLicenseMIBCompliance, appLicenseStatusLicenseState=appLicenseStatusLicenseState, LicenseState=LicenseState, appLicenseStatusExpireType=appLicenseStatusExpireType, appLicenseMIBNotifGroup=appLicenseMIBNotifGroup, appLicenseMIBObjects=appLicenseMIBObjects, appLicenseStatusComponentName=appLicenseStatusComponentName, appLicenseStatusEntry=appLicenseStatusEntry, appLicenseMIBConformance=appLicenseMIBConformance, appLicenseMIBGroup=appLicenseMIBGroup, appLicenseStatusIndex=appLicenseStatusIndex, appLicenseMIBNotificationsPrefix=appLicenseMIBNotificationsPrefix, appLicenseMIBNotifGroups=appLicenseMIBNotifGroups, appLicenseStateTrap=appLicenseStateTrap, LicenseExpireType=LicenseExpireType, appLicenseStatusApplicationName=appLicenseStatusApplicationName, appLicenseStatusFeatureName=appLicenseStatusFeatureName, appLicenseStatusTable=appLicenseStatusTable)
