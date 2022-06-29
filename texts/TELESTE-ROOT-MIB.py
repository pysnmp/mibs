#
# PySNMP MIB module TELESTE-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teleste/TELESTE-ROOT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:16:10 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Integer32, Bits, Gauge32, Counter32, Unsigned32, enterprises, TimeTicks, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Integer32", "Bits", "Gauge32", "Counter32", "Unsigned32", "enterprises", "TimeTicks", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity")
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
mibBuilder.exportSymbols("TELESTE-ROOT-MIB", Uint16=Uint16, experimental=experimental, easi=easi, ntpcontrol=ntpcontrol, spectrumAnalyser=spectrumAnalyser, hfcOptics=hfcOptics, teleste=teleste, emt=emt, cfo=cfo, functional=functional, dvo=dvo, inf=inf, ems=ems, bxx=bxx, Int16=Int16, DateAndTime=DateAndTime, TPhysAddress=TPhysAddress, etth=etth, headEnd=headEnd, pilotGenerator=pilotGenerator, Uint8=Uint8, ftth=ftth, atmux=atmux, dvx=dvx, Int8=Int8, gendata=gendata, ValueStatus=ValueStatus, acx=acx, Uint32=Uint32, common=common, bk=bk, luminato=luminato, TDisplayString=TDisplayString, hdo=hdo, hmsModem=hmsModem)
