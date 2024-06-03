#
# PySNMP MIB module NBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:46:19 2024
# On host fv-az1530-906 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, ModuleIdentity, MibIdentifier, Counter64, IpAddress, Counter32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ObjectIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "ModuleIdentity", "MibIdentifier", "Counter64", "IpAddress", "Counter32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ObjectIdentity", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("NBS-MIB", Unsigned64TC=Unsigned64TC, NbsTcStatusLevel=NbsTcStatusLevel, NbsTcTemperature=NbsTcTemperature, NbsTcMilliDb=NbsTcMilliDb, nbsMib=nbsMib, NbsTcMHz=NbsTcMHz, WritableU64=WritableU64, NbsTcMilliVolt=NbsTcMilliVolt, Unsigned16TC=Unsigned16TC, NbsTcMilliAmp=NbsTcMilliAmp, NbsTcMicroAmp=NbsTcMicroAmp, NbsTcMilliWatts=NbsTcMilliWatts, NbsTcStatusSimple=NbsTcStatusSimple, NbsTcPartIndex=NbsTcPartIndex, PYSNMP_MODULE_ID=nbsMib, NbsTcStagingCommit=NbsTcStagingCommit, nbs=nbs)
