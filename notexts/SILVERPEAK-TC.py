#
# PySNMP MIB module SILVERPEAK-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-TC
# Produced by pysmi-1.1.12 at Tue Sep 17 12:07:51 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
silverpeakModules, = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Counter32, Bits, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Counter32", "Bits", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibIdentifier")
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

mibBuilder.exportSymbols("SILVERPEAK-TC", SilverpeakDescription=SilverpeakDescription, SilverpeakAlarmSeverity=SilverpeakAlarmSeverity, SilverpeakSeqNum=SilverpeakSeqNum, SilverpeakYesNo=SilverpeakYesNo, PYSNMP_MODULE_ID=silverpeakTextualConventions, silverpeakTextualConventions=silverpeakTextualConventions)
