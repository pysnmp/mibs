#
# PySNMP MIB module NBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-MIB
# Produced by pysmi-1.1.12 at Wed Dec  4 17:57:32 2024
# On host fv-az2036-124 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, ModuleIdentity, NotificationType, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, ObjectIdentity, Counter64, IpAddress, Unsigned32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "NotificationType", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "ObjectIdentity", "Counter64", "IpAddress", "Unsigned32", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 250))
if mibBuilder.loadTexts: nbsMib.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: nbsMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsMib.setDescription("Textual conventions for NBS mibs.\n\n       Some informal NBS conventions used include the following:\n\n         A DESCRIPTION specifying 'Persistent' indicates a user-\n         configured attribute that can be stored in the Agent's\n         non-volatile file system as a configuration file such as\n         'startup-config'.\n\n         A DESCRIPTION specifying 'Impulse' indicates a user setting\n         that the Agent will immediately attempt but will not store\n         persistently.\n\n         An object name containing 'Admin' indicates a setting\n         requested by the user which may be overridden by the system.\n         Admin objects should be updated in the Agent immediately, so\n         a GET request immediately after the SET is accepted will\n         be answered with a GET-RESPONSE indicating the new value.\n\n         An object name containing 'Oper' indicates an attribute's\n         actual state.\n\n         An object name containing 'Caps' is a bitmask which refers to\n         the capabilities of an entity to support corresponding entries\n         in a specified feature table.")
nbs = ObjectIdentity((1, 3, 6, 1, 4, 1, 629))
if mibBuilder.loadTexts: nbs.setStatus('current')
if mibBuilder.loadTexts: nbs.setDescription('Root OID of NBS mibs')
class Unsigned16TC(TextualConvention, Unsigned32):
    description = 'Used to represent an unsigned two-octet integer'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Unsigned64TC(TextualConvention, Counter64):
    description = 'Used to represent an unsigned eight-octet integer'
    status = 'current'

class WritableU64(TextualConvention, OctetString):
    description = 'Used to represent an unsigned eight-octet integer which can\n         be SET in SNMPv1'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NbsTcTemperature(TextualConvention, Integer32):
    description = 'Temperature in degrees Celsius.  When writable, persistent.\n        Not supported value: 0x80000000\n        (decimal -2147483648)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 1000)

class NbsTcMilliVolt(TextualConvention, Integer32):
    description = 'Voltage in units of milliVolts.  When writable, persistent.\n        Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMilliAmp(TextualConvention, Integer32):
    description = 'Amperage in units of milliAmps.  When writable, persistent.\n        Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 1000000)

class NbsTcMicroAmp(TextualConvention, Integer32):
    description = 'Electrical current in units of micro amperes. When writable, persistent.\n        Not supported value: -1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1, 2147483647)

class NbsTcMilliDb(TextualConvention, Integer32):
    description = 'Decibels in thousandths.  When writable, persistent.\n\n        The reserved value -1,000,000 indicates that the signal is\n        blocked from passing through.\n\n        Blocked value:       -1000000\n        Not supported value: 0x80000000\n        (decimal -2147483648)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 100000)

class NbsTcMilliWatts(TextualConvention, Integer32):
    description = 'Electrical Power, in milliwatts.\n\n        Not supported value: -1'
    status = 'current'

class NbsTcMHz(TextualConvention, Unsigned32):
    description = 'Frequency in units of MHz.  When writable, persistent.\n        Not supported value: 0'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NbsTcStatusSimple(TextualConvention, Integer32):
    description = 'Basic operating status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("bad", 2), ("good", 3), ("notInstalled", 4))

class NbsTcStatusLevel(TextualConvention, Integer32):
    description = 'Severity level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notSupported", 1), ("statusLowError", 2), ("statusLowWarning", 3), ("statusGood", 4), ("statusHighWarning", 5), ("statusHighError", 6))

class NbsTcPartIndex(TextualConvention, Unsigned32):
    description = 'Unique ID within scope of an ifIndex'
    status = 'current'

class NbsTcStagingCommit(TextualConvention, Integer32):
    description = 'Staging commit command'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notSupported", 1), ("supported", 2), ("revertToCommitted", 3), ("apply", 4))

mibBuilder.exportSymbols("NBS-MIB", NbsTcStatusSimple=NbsTcStatusSimple, nbsMib=nbsMib, PYSNMP_MODULE_ID=nbsMib, NbsTcPartIndex=NbsTcPartIndex, Unsigned16TC=Unsigned16TC, Unsigned64TC=Unsigned64TC, nbs=nbs, NbsTcMHz=NbsTcMHz, NbsTcMilliWatts=NbsTcMilliWatts, NbsTcTemperature=NbsTcTemperature, NbsTcStatusLevel=NbsTcStatusLevel, NbsTcStagingCommit=NbsTcStagingCommit, NbsTcMilliDb=NbsTcMilliDb, NbsTcMicroAmp=NbsTcMicroAmp, NbsTcMilliAmp=NbsTcMilliAmp, NbsTcMilliVolt=NbsTcMilliVolt, WritableU64=WritableU64)
