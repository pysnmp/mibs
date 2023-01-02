#
# PySNMP MIB module SILVERPEAK-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-TC
# Produced by pysmi-1.1.8 at Mon Jan  2 15:35:48 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
silverpeakModules, = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ObjectIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Counter64, Gauge32, ModuleIdentity, Bits, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Counter64", "Gauge32", "ModuleIdentity", "Bits", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
silverpeakTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867, 2, 1))
if mibBuilder.loadTexts: silverpeakTextualConventions.setLastUpdated('201101240000Z')
if mibBuilder.loadTexts: silverpeakTextualConventions.setOrganization('Silver Peak Systems, Inc.')
class SilverpeakDescription(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 255)

class SilverpeakYesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class SilverpeakSeqNum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class SilverpeakAlarmSeverity(TextualConvention, Integer32):
    reference = 'ITU-X.733'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("info", 0), ("warning", 1), ("minor", 2), ("major", 3), ("critical", 4), ("cleared", 5), ("acknowledged", 6), ("unacknowledged", 7), ("indeterminate", 8))

mibBuilder.exportSymbols("SILVERPEAK-TC", SilverpeakDescription=SilverpeakDescription, PYSNMP_MODULE_ID=silverpeakTextualConventions, SilverpeakAlarmSeverity=SilverpeakAlarmSeverity, SilverpeakYesNo=SilverpeakYesNo, SilverpeakSeqNum=SilverpeakSeqNum, silverpeakTextualConventions=silverpeakTextualConventions)
