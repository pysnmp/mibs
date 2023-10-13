#
# PySNMP MIB module SNMPv2-TC-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Fri Oct 13 13:55:01 2023
# On host fv-az877-675 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, IpAddress, Bits, Counter64, Integer32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, MibIdentifier, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "MibIdentifier", "Unsigned32", "Counter32")
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

mibBuilder.exportSymbols("SNMPv2-TC-v1", InstancePointer=InstancePointer, RowStatus=RowStatus, RowPointer=RowPointer, PhysAddress=PhysAddress, DisplayString=DisplayString, TimeStamp=TimeStamp, TestAndIncr=TestAndIncr, TruthValue=TruthValue, MacAddress=MacAddress, AutonomousType=AutonomousType, TimeInterval=TimeInterval, DateAndTime=DateAndTime)
