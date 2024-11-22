#
# PySNMP MIB module VERITAS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-TC.mib
# Produced by pysmi-1.1.12 at Fri Nov 22 16:03:40 2024
# On host fv-az1205-935 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, IpAddress, Counter64, Opaque, NotificationType, enterprises, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, TimeTicks, Bits, Unsigned32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "Counter64", "Opaque", "NotificationType", "enterprises", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "TimeTicks", "Bits", "Unsigned32", "ModuleIdentity", "MibIdentifier")
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

mibBuilder.exportSymbols("VERITAS-TC", veritastc=veritastc, Float=Float, Uint64ReadOnly=Uint64ReadOnly, Utf8StringShort=Utf8StringShort, Utf8StringLong=Utf8StringLong, Int64ReadWrite=Int64ReadWrite, PYSNMP_MODULE_ID=veritastc)
