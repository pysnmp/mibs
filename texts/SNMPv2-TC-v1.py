#
# PySNMP MIB module SNMPv2-TC-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Thu Jan  5 08:57:25 2023
# On host fv-az351-145 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, iso, NotificationType, Bits, MibIdentifier, Gauge32, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "NotificationType", "Bits", "MibIdentifier", "Gauge32", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PhysAddress(OctetString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AutonomousType(ObjectIdentifier):
    pass

class InstancePointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class RowPointer(ObjectIdentifier):
    pass

mibBuilder.exportSymbols("SNMPv2-TC-v1", MacAddress=MacAddress, AutonomousType=AutonomousType, TimeStamp=TimeStamp, InstancePointer=InstancePointer, TimeInterval=TimeInterval, DisplayString=DisplayString, TestAndIncr=TestAndIncr, RowPointer=RowPointer, PhysAddress=PhysAddress, TruthValue=TruthValue, DateAndTime=DateAndTime, RowStatus=RowStatus)
