#
# PySNMP MIB module SNMPv2-TC-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Jun  3 12:19:19 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Counter32, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Gauge32, Counter64, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Counter32", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Gauge32", "Counter64", "MibIdentifier", "Bits", "TimeTicks")
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

mibBuilder.exportSymbols("SNMPv2-TC-v1", PhysAddress=PhysAddress, TestAndIncr=TestAndIncr, RowStatus=RowStatus, TimeInterval=TimeInterval, InstancePointer=InstancePointer, MacAddress=MacAddress, DisplayString=DisplayString, RowPointer=RowPointer, TruthValue=TruthValue, TimeStamp=TimeStamp, DateAndTime=DateAndTime, AutonomousType=AutonomousType)
