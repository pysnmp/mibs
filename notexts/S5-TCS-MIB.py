#
# PySNMP MIB module S5-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/S5-TCS-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:45:54 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
s5Tcs, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Tcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, TimeTicks, Gauge32, Bits, iso, ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Bits", "iso", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("S5-TCS-MIB", BkChan=BkChan, LocChan=LocChan, MediaType=MediaType, IpxAddress=IpxAddress, BkNetId=BkNetId, TimeIntervalHrd=TimeIntervalHrd, s5TcsMib=s5TcsMib, SrcIndx=SrcIndx, AttId=AttId, TimeIntervalSec=TimeIntervalSec, FddiBkNetMode=FddiBkNetMode, PYSNMP_MODULE_ID=s5TcsMib)
