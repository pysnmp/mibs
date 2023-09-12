#
# PySNMP MIB module S5-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-TCS-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:30:06 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
s5Tcs, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Tcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, Gauge32, Integer32, ModuleIdentity, iso, Counter64, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "Gauge32", "Integer32", "ModuleIdentity", "iso", "Counter64", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5TcsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 17, 0))
s5TcsMib.setRevisions(('2013-10-10 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: s5TcsMib.setLastUpdated('201310100000Z')
if mibBuilder.loadTexts: s5TcsMib.setOrganization('Nortel Networks')
class IpxAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class TimeIntervalHrd(TextualConvention, Integer32):
    status = 'current'

class TimeIntervalSec(TextualConvention, Integer32):
    status = 'current'

class SrcIndx(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 999999)

class MediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("eth", 2), ("tok", 3), ("fddi", 4))

class FddiBkNetMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("thruLow", 2), ("thruHigh", 3), ("thruLowThruHigh", 4))

class BkNetId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class BkChan(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LocChan(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class AttId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-255, 255)

mibBuilder.exportSymbols("S5-TCS-MIB", AttId=AttId, PYSNMP_MODULE_ID=s5TcsMib, FddiBkNetMode=FddiBkNetMode, s5TcsMib=s5TcsMib, TimeIntervalSec=TimeIntervalSec, MediaType=MediaType, TimeIntervalHrd=TimeIntervalHrd, SrcIndx=SrcIndx, LocChan=LocChan, IpxAddress=IpxAddress, BkNetId=BkNetId, BkChan=BkChan)
