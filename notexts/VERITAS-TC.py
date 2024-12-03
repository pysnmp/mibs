#
# PySNMP MIB module VERITAS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-TC.mib
# Produced by pysmi-1.1.12 at Tue Dec  3 11:45:52 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, enterprises, Unsigned32, MibIdentifier, Opaque, Integer32, NotificationType, Gauge32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "enterprises", "Unsigned32", "MibIdentifier", "Opaque", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks")
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

mibBuilder.exportSymbols("VERITAS-TC", Int64ReadWrite=Int64ReadWrite, Utf8StringShort=Utf8StringShort, Utf8StringLong=Utf8StringLong, Uint64ReadOnly=Uint64ReadOnly, Float=Float, veritastc=veritastc, PYSNMP_MODULE_ID=veritastc)
