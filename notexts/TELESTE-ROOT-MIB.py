#
# PySNMP MIB module TELESTE-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:38:01 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter64, Unsigned32, IpAddress, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, MibIdentifier, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter64", "Unsigned32", "IpAddress", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "iso", "Bits")
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
mibBuilder.exportSymbols("TELESTE-ROOT-MIB", bxx=bxx, cfo=cfo, pilotGenerator=pilotGenerator, Int8=Int8, DateAndTime=DateAndTime, hfcOptics=hfcOptics, Uint16=Uint16, emt=emt, common=common, inf=inf, gendata=gendata, luminato=luminato, spectrumAnalyser=spectrumAnalyser, dvx=dvx, ftth=ftth, TDisplayString=TDisplayString, acx=acx, ntpcontrol=ntpcontrol, bk=bk, dvo=dvo, atmux=atmux, experimental=experimental, TPhysAddress=TPhysAddress, hmsModem=hmsModem, easi=easi, headEnd=headEnd, hdo=hdo, functional=functional, etth=etth, teleste=teleste, Uint8=Uint8, ValueStatus=ValueStatus, ems=ems, Uint32=Uint32, Int16=Int16)
