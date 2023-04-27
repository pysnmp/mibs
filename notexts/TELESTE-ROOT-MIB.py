#
# PySNMP MIB module TELESTE-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-ROOT-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 11:44:13 2023
# On host fv-az561-589 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Bits, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, Unsigned32, IpAddress, Counter32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Bits", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "iso", "Counter64")
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
mibBuilder.exportSymbols("TELESTE-ROOT-MIB", pilotGenerator=pilotGenerator, hfcOptics=hfcOptics, atmux=atmux, dvx=dvx, TDisplayString=TDisplayString, hmsModem=hmsModem, Uint16=Uint16, gendata=gendata, functional=functional, Int8=Int8, common=common, ems=ems, Uint8=Uint8, experimental=experimental, teleste=teleste, ftth=ftth, TPhysAddress=TPhysAddress, acx=acx, ntpcontrol=ntpcontrol, hdo=hdo, luminato=luminato, ValueStatus=ValueStatus, etth=etth, bk=bk, headEnd=headEnd, dvo=dvo, bxx=bxx, DateAndTime=DateAndTime, easi=easi, cfo=cfo, emt=emt, inf=inf, Uint32=Uint32, spectrumAnalyser=spectrumAnalyser, Int16=Int16)
