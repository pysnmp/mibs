#
# PySNMP MIB module TELESTE-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-ROOT-MIB
# Produced by pysmi-1.1.11 at Tue Dec  5 08:40:13 2023
# On host fv-az1433-65 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, ModuleIdentity, enterprises, ObjectIdentity, Bits, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, Integer32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ModuleIdentity", "enterprises", "ObjectIdentity", "Bits", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class TDisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TPhysAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class Int8(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class Int16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32768)

class Uint8(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class Uint16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65536)

class Uint32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DateAndTime(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(16, 28)

class ValueStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("valueNormal", 1), ("valueHIHI", 2), ("valueHi", 3), ("valueLo", 4), ("valueLOLO", 5))

teleste = MibIdentifier((1, 3, 6, 1, 4, 1, 3715))
ems = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 1))
gendata = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 2))
bk = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 3))
bxx = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 4))
dvo = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 5))
dvx = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 6))
inf = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 7))
atmux = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 8))
easi = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 9))
emt = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 10))
acx = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 11))
etth = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 12))
hdo = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 14))
cfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 15))
ftth = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 16))
luminato = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 17))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 99))
functional = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100))
hmsModem = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 1))
spectrumAnalyser = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 2))
pilotGenerator = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 3))
ntpcontrol = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 4))
hfcOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 10))
headEnd = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 100, 20))
experimental = MibIdentifier((1, 3, 6, 1, 4, 1, 3715, 999))
mibBuilder.exportSymbols("TELESTE-ROOT-MIB", TPhysAddress=TPhysAddress, spectrumAnalyser=spectrumAnalyser, hmsModem=hmsModem, Uint32=Uint32, Uint8=Uint8, hfcOptics=hfcOptics, acx=acx, luminato=luminato, Uint16=Uint16, teleste=teleste, pilotGenerator=pilotGenerator, hdo=hdo, Int8=Int8, dvo=dvo, inf=inf, etth=etth, Int16=Int16, bk=bk, gendata=gendata, bxx=bxx, easi=easi, emt=emt, ems=ems, DateAndTime=DateAndTime, dvx=dvx, headEnd=headEnd, atmux=atmux, cfo=cfo, TDisplayString=TDisplayString, ntpcontrol=ntpcontrol, common=common, experimental=experimental, ValueStatus=ValueStatus, functional=functional, ftth=ftth)
