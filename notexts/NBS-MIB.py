#
# PySNMP MIB module NBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 08:06:56 2023
# On host fv-az256-323 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, Gauge32, Bits, Unsigned32, Counter32, IpAddress, MibIdentifier, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Gauge32", "Bits", "Unsigned32", "Counter32", "IpAddress", "MibIdentifier", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 250))
if mibBuilder.loadTexts: nbsMib.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: nbsMib.setOrganization('NBS')
nbs = ObjectIdentity((1, 3, 6, 1, 4, 1, 629))
if mibBuilder.loadTexts: nbs.setStatus('current')
class Unsigned16TC(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Unsigned64TC(TextualConvention, Counter64):
    status = 'current'

class WritableU64(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NbsTcTemperature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 1000)

class NbsTcMilliVolt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMilliAmp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMicroAmp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class NbsTcMilliDb(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 100000)

class NbsTcMilliWatts(TextualConvention, Integer32):
    status = 'current'

class NbsTcMHz(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NbsTcStatusSimple(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("bad", 2), ("good", 3), ("notInstalled", 4))

class NbsTcStatusLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSupported", 1), ("statusLowError", 2), ("statusLowWarning", 3), ("statusGood", 4), ("statusHighWarning", 5), ("statusHighError", 6))

class NbsTcPartIndex(TextualConvention, Unsigned32):
    status = 'current'

class NbsTcStagingCommit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2), ("revertToCommitted", 3), ("apply", 4))

mibBuilder.exportSymbols("NBS-MIB", NbsTcStatusLevel=NbsTcStatusLevel, NbsTcPartIndex=NbsTcPartIndex, NbsTcStagingCommit=NbsTcStagingCommit, PYSNMP_MODULE_ID=nbsMib, NbsTcTemperature=NbsTcTemperature, Unsigned16TC=Unsigned16TC, NbsTcMilliVolt=NbsTcMilliVolt, NbsTcStatusSimple=NbsTcStatusSimple, NbsTcMicroAmp=NbsTcMicroAmp, NbsTcMilliDb=NbsTcMilliDb, nbs=nbs, nbsMib=nbsMib, WritableU64=WritableU64, NbsTcMilliAmp=NbsTcMilliAmp, NbsTcMHz=NbsTcMHz, Unsigned64TC=Unsigned64TC, NbsTcMilliWatts=NbsTcMilliWatts)
