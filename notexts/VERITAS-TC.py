#
# PySNMP MIB module VERITAS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-TC.mib
# Produced by pysmi-1.1.8 at Thu Dec 15 08:35:46 2022
# On host fv-az193-683 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, Gauge32, Integer32, Bits, NotificationType, ModuleIdentity, Opaque, Counter64, Unsigned32, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Gauge32", "Integer32", "Bits", "NotificationType", "ModuleIdentity", "Opaque", "Counter64", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
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

mibBuilder.exportSymbols("VERITAS-TC", veritastc=veritastc, Utf8StringLong=Utf8StringLong, PYSNMP_MODULE_ID=veritastc, Int64ReadWrite=Int64ReadWrite, Utf8StringShort=Utf8StringShort, Float=Float, Uint64ReadOnly=Uint64ReadOnly)
