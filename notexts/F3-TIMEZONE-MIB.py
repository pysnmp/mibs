#
# PySNMP MIB module F3-TIMEZONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-TIMEZONE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 14:08:17 2024
# On host fv-az693-600 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "NotificationType", "Integer32", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
f3TimeZoneMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32))
f3TimeZoneMIB.setRevisions(('2014-06-05 00:00',))
if mibBuilder.loadTexts: f3TimeZoneMIB.setLastUpdated('201406050000Z')
if mibBuilder.loadTexts: f3TimeZoneMIB.setOrganization('ADVA Optical Networking')
f3TimeZoneConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1))
f3TimeZoneConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2))
class MonthOfYear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("january", 1), ("february", 2), ("march", 3), ("april", 4), ("may", 5), ("june", 6), ("july", 7), ("august", 8), ("september", 9), ("october", 10), ("november", 11), ("december", 12))

f3TimeZoneUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneUtcOffset.setStatus('current')
f3TimeZoneDstControlEnabled = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstControlEnabled.setStatus('current')
f3TimeZoneDstUtcOffset = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstUtcOffset.setStatus('current')
f3TimeZoneDstStartMonth = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 4), MonthOfYear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartMonth.setStatus('current')
f3TimeZoneDstStartDay = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartDay.setStatus('current')
f3TimeZoneDstStartTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstStartTime.setStatus('current')
f3TimeZoneDstEndMonth = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 7), MonthOfYear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndMonth.setStatus('current')
f3TimeZoneDstEndDay = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndDay.setStatus('current')
f3TimeZoneDstEndTime = MibScalar((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3TimeZoneDstEndTime.setStatus('current')
f3TimeZoneCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1))
f3TimeZoneGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2))
f3TimeZoneCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 1, 1)).setObjects(("F3-TIMEZONE-MIB", "f3TimeZoneConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TimeZoneCompliance = f3TimeZoneCompliance.setStatus('current')
f3TimeZoneConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 32, 2, 2, 1)).setObjects(("F3-TIMEZONE-MIB", "f3TimeZoneUtcOffset"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstControlEnabled"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstUtcOffset"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartMonth"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartDay"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstStartTime"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndMonth"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndDay"), ("F3-TIMEZONE-MIB", "f3TimeZoneDstEndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3TimeZoneConfigGroup = f3TimeZoneConfigGroup.setStatus('current')
mibBuilder.exportSymbols("F3-TIMEZONE-MIB", f3TimeZoneDstEndDay=f3TimeZoneDstEndDay, f3TimeZoneConfigObjects=f3TimeZoneConfigObjects, f3TimeZoneDstControlEnabled=f3TimeZoneDstControlEnabled, PYSNMP_MODULE_ID=f3TimeZoneMIB, MonthOfYear=MonthOfYear, f3TimeZoneGroups=f3TimeZoneGroups, f3TimeZoneDstStartTime=f3TimeZoneDstStartTime, f3TimeZoneDstEndTime=f3TimeZoneDstEndTime, f3TimeZoneDstStartMonth=f3TimeZoneDstStartMonth, f3TimeZoneConformance=f3TimeZoneConformance, f3TimeZoneCompliances=f3TimeZoneCompliances, f3TimeZoneCompliance=f3TimeZoneCompliance, f3TimeZoneDstUtcOffset=f3TimeZoneDstUtcOffset, f3TimeZoneDstEndMonth=f3TimeZoneDstEndMonth, f3TimeZoneConfigGroup=f3TimeZoneConfigGroup, f3TimeZoneDstStartDay=f3TimeZoneDstStartDay, f3TimeZoneMIB=f3TimeZoneMIB, f3TimeZoneUtcOffset=f3TimeZoneUtcOffset)
