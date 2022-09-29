#
# PySNMP MIB module SILVERPEAK-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-TC
# Produced by pysmi-1.1.8 at Thu Sep 29 13:15:12 2022
# On host fv-az340-469 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
silverpeakModules, = mibBuilder.importSymbols("SILVERPEAK-SMI", "silverpeakModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, Counter64, Gauge32, NotificationType, TimeTicks, ModuleIdentity, IpAddress, Integer32, MibIdentifier, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Counter64", "Gauge32", "NotificationType", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32", "MibIdentifier", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
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

mibBuilder.exportSymbols("SILVERPEAK-TC", silverpeakTextualConventions=silverpeakTextualConventions, SilverpeakSeqNum=SilverpeakSeqNum, SilverpeakDescription=SilverpeakDescription, SilverpeakAlarmSeverity=SilverpeakAlarmSeverity, SilverpeakYesNo=SilverpeakYesNo, PYSNMP_MODULE_ID=silverpeakTextualConventions)
