#
# PySNMP MIB module TELESTE-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-ROOT-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 15:00:37 2021
# On host fv-az126-713 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, enterprises, Unsigned32, TimeTicks, Counter64, ObjectIdentity, iso, Integer32, NotificationType, ModuleIdentity, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "Unsigned32", "TimeTicks", "Counter64", "ObjectIdentity", "iso", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TELESTE-ROOT-MIB", atmux=atmux, Uint8=Uint8, bxx=bxx, ntpcontrol=ntpcontrol, easi=easi, spectrumAnalyser=spectrumAnalyser, functional=functional, DateAndTime=DateAndTime, ems=ems, etth=etth, hdo=hdo, cfo=cfo, ftth=ftth, inf=inf, Int8=Int8, pilotGenerator=pilotGenerator, Uint32=Uint32, headEnd=headEnd, Int16=Int16, TDisplayString=TDisplayString, bk=bk, hfcOptics=hfcOptics, acx=acx, ValueStatus=ValueStatus, TPhysAddress=TPhysAddress, dvo=dvo, Uint16=Uint16, gendata=gendata, dvx=dvx, emt=emt, teleste=teleste, common=common, hmsModem=hmsModem, luminato=luminato, experimental=experimental)
