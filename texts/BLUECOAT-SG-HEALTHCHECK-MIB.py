#
# PySNMP MIB module BLUECOAT-SG-HEALTHCHECK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-HEALTHCHECK-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:21:44 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Integer32, IpAddress, MibIdentifier, ObjectIdentity, Counter64, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
deviceHealthCheckMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 7))
deviceHealthCheckMIB.setRevisions(('2013-05-22 03:00', '2013-05-21 03:00', '2007-11-05 03:00', '2002-08-28 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceHealthCheckMIB.setRevisionsDescriptions(('Added OID for time of last health check.', 'Added OIDs for device health check table.', 'Minor corrections and reformatting. Changed the\n                         trap OID for compatibility with SNMPv1.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceHealthCheckMIB.setLastUpdated('201305220300Z')
if mibBuilder.loadTexts: deviceHealthCheckMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceHealthCheckMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceHealthCheckMIB.setDescription('The health check MIB is used to monitor\n                         changes in the health of upstream systems.')
deviceHealthCheckMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1))
deviceHealthCheckMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2))
deviceHealthCheckMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3))
deviceHealthCheckMIBNotifsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0))
class HealthCheckMessageString(TextualConvention, OctetString):
    description = 'The message describing a change in the health\n                          of an upstream system.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

deviceHealthCheckStringValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1))
deviceHealthCheckValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2))
deviceHealthCheckMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1, 1), HealthCheckMessageString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckMessage.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckMessage.setDescription('The custom message generated for this change in health.')
deviceHealthCheckValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1), )
if mibBuilder.loadTexts: deviceHealthCheckValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckValueTable.setDescription('Table of Heath Check services.')
deviceHealthCheckValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"))
if mibBuilder.loadTexts: deviceHealthCheckValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckValueEntry.setDescription('A deviceHealthCheckValueTable entry describes the status\n                         of a health check service.')
class HealthCheckStatus(TextualConvention, Integer32):
    description = 'Indicates the current value of the health check.\n                (1) - unknown\n                (2) - ok\n                (3) - ok with errors\n                (4) - ok for some IPs                \n                (5) - ok but failing\n                (6) - check failed\n                (7) - dns failed\n                (8) - ok on alt server'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("okWithErrors", 3), ("okForSomeIPs", 4), ("okButFailing", 5), ("checkFailed", 6), ("dnsFailed", 7), ("okOnAltServer", 8))

deviceHealthCheckName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckName.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckName.setDescription('The name of health check service.')
deviceHealthCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 2), HealthCheckStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckState.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckState.setDescription('This variable indicates health check state.')
deviceHealthCheckTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHealthCheckTime.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckTime.setDescription('This variable indicates time (duration) in milliseconds the last health check took.')
deviceHealthCheckTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage"))
if mibBuilder.loadTexts: deviceHealthCheckTrap.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckTrap.setDescription('A notification is generated when the health\n                         of a monitored system changes.')
deviceHealthCheckMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1))
deviceHealthCheckMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2))
deviceHealthCheckMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3))
deviceHealthCheckMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBCompliance = deviceHealthCheckMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckMIBCompliance.setDescription('The compliance statement for health check module. ')
deviceHealthCheckMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckState"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTime"), ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBGroup = deviceHealthCheckMIBGroup.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckMIBGroup.setDescription('Group of Health Check-related objects implemented in ProxySG appliances.')
deviceHealthCheckMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3, 1)).setObjects(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    deviceHealthCheckMIBNotifGroup = deviceHealthCheckMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: deviceHealthCheckMIBNotifGroup.setDescription('Group of Health Check notifications implemented in ProxySG appliances.')
mibBuilder.exportSymbols("BLUECOAT-SG-HEALTHCHECK-MIB", deviceHealthCheckStringValues=deviceHealthCheckStringValues, deviceHealthCheckMIBCompliance=deviceHealthCheckMIBCompliance, deviceHealthCheckTrap=deviceHealthCheckTrap, deviceHealthCheckMIBObjects=deviceHealthCheckMIBObjects, HealthCheckStatus=HealthCheckStatus, deviceHealthCheckMIBGroup=deviceHealthCheckMIBGroup, deviceHealthCheckMIBConformance=deviceHealthCheckMIBConformance, PYSNMP_MODULE_ID=deviceHealthCheckMIB, deviceHealthCheckMIBGroups=deviceHealthCheckMIBGroups, deviceHealthCheckMIBNotifsPrefix=deviceHealthCheckMIBNotifsPrefix, deviceHealthCheckName=deviceHealthCheckName, deviceHealthCheckValues=deviceHealthCheckValues, deviceHealthCheckMIBNotifGroup=deviceHealthCheckMIBNotifGroup, HealthCheckMessageString=HealthCheckMessageString, deviceHealthCheckState=deviceHealthCheckState, deviceHealthCheckValueEntry=deviceHealthCheckValueEntry, deviceHealthCheckMIBNotifGroups=deviceHealthCheckMIBNotifGroups, deviceHealthCheckMIB=deviceHealthCheckMIB, deviceHealthCheckMIBCompliances=deviceHealthCheckMIBCompliances, deviceHealthCheckTime=deviceHealthCheckTime, deviceHealthCheckMessage=deviceHealthCheckMessage, deviceHealthCheckMIBNotifs=deviceHealthCheckMIBNotifs, deviceHealthCheckValueTable=deviceHealthCheckValueTable)
