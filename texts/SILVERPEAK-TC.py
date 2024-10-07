#
# PySNMP MIB module SILVERPEAK-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-TC
# Produced by pysmi-1.1.12 at Mon Oct  7 02:58:27 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
silverpeakModules, = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ObjectIdentity, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, iso, Bits, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "iso", "Bits", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
silverpeakTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867, 2, 1))
if mibBuilder.loadTexts: silverpeakTextualConventions.setLastUpdated('201101240000Z')
if mibBuilder.loadTexts: silverpeakTextualConventions.setOrganization('Silver Peak Systems, Inc.')
if mibBuilder.loadTexts: silverpeakTextualConventions.setContactInfo('  URL: http://www.silver-peak.com/contact\n            E-mail: support@silver-peak.com ')
if mibBuilder.loadTexts: silverpeakTextualConventions.setDescription('This module defines the textual conventions used throughout\n        Silverpeak Systems enterprise mibs.')
class SilverpeakDescription(DisplayString):
    description = 'Represents a string description used for any MIB object.\n         '
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class SilverpeakYesNo(TextualConvention, Integer32):
    description = 'Textual convention for yes/no enum.\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class SilverpeakSeqNum(TextualConvention, Integer32):
    description = 'Represents the unique sequence number associated with each\n         generated trap.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SilverpeakAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    description = 'Represents the perceived alarm condition associated with a\n        service affecting condition and/or event.\n\n            indeterminate(8) -\n                Indicates that the severity level cannot be\n                determined. \n\n            unacknowledged(7) -\n                Indicates that the severity level cannot be\n                determined. \n\n            acknowledged(6) -\n                Indicates that the severity level cannot be\n                determined. \n\n            cleared(5) -\n                Indicates a previous alarm condition has been\n                cleared.  It is not required (unless specifically\n                stated elsewhere on a case by case basis) that an\n                alarm condition that has been cleared will produce\n                a notification or other event containing an\n                alarm severity with this value.\n\n            critical(4) -\n                Indicates that a service or safety affecting\n                condition has occurred and an immediate\n                corrective action is required.\n\n            major(3) -\n                Indicates that a service affecting condition has\n                occurred and an urgent corrective action is\n                required.\n\n            minor(2) -\n                Indicates the existence of a non-service affecting\n                condition and that corrective action should be\n                taken in order to prevent a more serious (for\n                example, service or safety affecting) condition.\n\n            warning(1) -\n                Indicates the detection of a potential or impending\n                service or safety affecting condition, before any\n                significant effects have been felt.\n\n            info(0) -\n                Indicates an alarm condition that does not\n                meet any other severity definition.  This can\n                include important, but non-urgent, notices or\n                informational events.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("info", 0), ("warning", 1), ("minor", 2), ("major", 3), ("critical", 4), ("cleared", 5), ("acknowledged", 6), ("unacknowledged", 7), ("indeterminate", 8))

mibBuilder.exportSymbols("SILVERPEAK-TC", silverpeakTextualConventions=silverpeakTextualConventions, SilverpeakYesNo=SilverpeakYesNo, SilverpeakSeqNum=SilverpeakSeqNum, SilverpeakAlarmSeverity=SilverpeakAlarmSeverity, SilverpeakDescription=SilverpeakDescription, PYSNMP_MODULE_ID=silverpeakTextualConventions)
