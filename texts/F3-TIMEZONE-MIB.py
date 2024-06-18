#
# PySNMP MIB module F3-TIMEZONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-TIMEZONE-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 02:31:29 2024
# On host fv-az849-858 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, ObjectIdentity, Integer32, Bits, TimeTicks, Gauge32, Counter32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "Integer32", "Bits", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
f3TimeZoneMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32))
f3TimeZoneMIB.setRevisions(('2014-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3TimeZoneMIB.setRevisionsDescriptions(('\n         Notes from release 201406050000Z,\n         (1) MIB version ready for release FSP150CC 6.5.CC.',))
if mibBuilder.loadTexts: f3TimeZoneMIB.setLastUpdated('201406050000Z')
if mibBuilder.loadTexts: f3TimeZoneMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3TimeZoneMIB.setContactInfo('        Michal Pawlowski\n                     ADVA Optical Networking, Inc.\n                Tel: +48 58 7716 416\n             E-mail: mpawlowski@advaoptical.com\n             Postal: ul. Slaska 35/37\n                     81-310 Gdynia, Poland')
if mibBuilder.loadTexts: f3TimeZoneMIB.setDescription('This module defines the Time Zone MIB definitions \n             used by the F3 (FSP150CM/CC) product lines.\n             Copyright (C) ADVA Optical Networking.')
f3TimeZoneConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1))
f3TimeZoneConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2))
class MonthOfYear(TextualConvention, Integer32):
    description = 'Month of year.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("january", 1), ("february", 2), ("march", 3), ("april", 4), ("may", 5), ("june", 6), ("july", 7), ("august", 8), ("september", 9), ("october", 10), ("november", 11), ("december", 12))

f3TimeZoneUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneUtcOffset.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneUtcOffset.setDescription('This object provides the ability to set UTC offset.')
f3TimeZoneDstControlEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstControlEnabled.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstControlEnabled.setDescription('This object provides the ability to toggle DST functionality.')
f3TimeZoneDstUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstUtcOffset.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstUtcOffset.setDescription('This object provides the ability to set DST Offset which is\n          the Daylight Savings Time offset from Local Time.')
f3TimeZoneDstStartMonth = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 4), MonthOfYear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartMonth.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstStartMonth.setDescription('This object provides the ability to set DST start month.')
f3TimeZoneDstStartDay = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartDay.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstStartDay.setDescription('This object provides the ability to set DST start day.')
f3TimeZoneDstStartTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartTime.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstStartTime.setDescription('This object provides the ability to set DST start time.')
f3TimeZoneDstEndMonth = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 7), MonthOfYear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndMonth.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstEndMonth.setDescription('This object provides the ability to set DST end month.')
f3TimeZoneDstEndDay = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndDay.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstEndDay.setDescription('This object provides the ability to set DST end day.')
f3TimeZoneDstEndTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndTime.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneDstEndTime.setDescription('This object provides the ability to set DST end time.')
f3TimeZoneCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1))
f3TimeZoneGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2))
f3TimeZoneCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1, 1)).setObjects(("F3-TIMEZONE-MIB", "f3TimeZoneConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TimeZoneCompliance = f3TimeZoneCompliance.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneCompliance.setDescription('Describes the requirements for conformance to the F3-TIMEZONE-MIB compliance.')
f3TimeZoneConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2, 1)).setObjects(("F3-TIMEZONE-MIB", "f3TimeZoneUtcOffset"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstControlEnabled"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstUtcOffset"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartMonth"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartDay"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartTime"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndMonth"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndDay"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TimeZoneConfigGroup = f3TimeZoneConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3TimeZoneConfigGroup.setDescription('A collection of objects used to manage the Time Zone.')
mibBuilder.exportSymbols("F3-TIMEZONE-MIB", f3TimeZoneDstUtcOffset=f3TimeZoneDstUtcOffset, f3TimeZoneCompliances=f3TimeZoneCompliances, f3TimeZoneDstEndDay=f3TimeZoneDstEndDay, f3TimeZoneDstEndTime=f3TimeZoneDstEndTime, f3TimeZoneDstEndMonth=f3TimeZoneDstEndMonth, f3TimeZoneConfigGroup=f3TimeZoneConfigGroup, MonthOfYear=MonthOfYear, f3TimeZoneDstStartMonth=f3TimeZoneDstStartMonth, f3TimeZoneDstStartTime=f3TimeZoneDstStartTime, f3TimeZoneUtcOffset=f3TimeZoneUtcOffset, f3TimeZoneCompliance=f3TimeZoneCompliance, f3TimeZoneDstStartDay=f3TimeZoneDstStartDay, f3TimeZoneGroups=f3TimeZoneGroups, f3TimeZoneMIB=f3TimeZoneMIB, f3TimeZoneConformance=f3TimeZoneConformance, f3TimeZoneDstControlEnabled=f3TimeZoneDstControlEnabled, f3TimeZoneConfigObjects=f3TimeZoneConfigObjects, PYSNMP_MODULE_ID=f3TimeZoneMIB)
