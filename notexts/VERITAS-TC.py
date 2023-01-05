#
# PySNMP MIB module VERITAS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-TC.mib
# Produced by pysmi-1.1.8 at Thu Jan  5 09:16:26 2023
# On host fv-az351-145 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Opaque, Bits, Counter32, ModuleIdentity, Integer32, Counter64, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, MibIdentifier, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Opaque", "Bits", "Counter32", "ModuleIdentity", "Integer32", "Counter64", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "MibIdentifier", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veritasModules, = mibBuilder.importSymbols("VERITAS-REG", "veritasModules")
veritastc = ModuleIdentity((1, 3, 6, 1, 4, 1, 1302, 5, 2))
if mibBuilder.loadTexts: veritastc.setLastUpdated('0401082030Z')
if mibBuilder.loadTexts: veritastc.setOrganization('VERITAS Software Corp.')
class Float(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class Utf8StringLong(TextualConvention, OctetString):
    status = 'current'
    displayHint = '65535t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

class Utf8StringShort(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uint64ReadOnly(TextualConvention, Counter64):
    status = 'current'

class Int64ReadWrite(TextualConvention, OctetString):
    status = 'current'
    displayHint = '21a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 21)

mibBuilder.exportSymbols("VERITAS-TC", veritastc=veritastc, Uint64ReadOnly=Uint64ReadOnly, Utf8StringLong=Utf8StringLong, Float=Float, Int64ReadWrite=Int64ReadWrite, Utf8StringShort=Utf8StringShort, PYSNMP_MODULE_ID=veritastc)
