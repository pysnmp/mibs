#
# PySNMP MIB module EKINOPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ekinops/EKINOPS-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 12:02:58 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, enterprises, Integer32, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, ObjectIdentity, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "enterprises", "Integer32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter64", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ekinops = ModuleIdentity((1, 3, 6, 1, 4, 1, 20044))
ekinops.setRevisions(('2004-08-18 00:00', '2005-04-04 00:00', '2005-06-08 00:00', '2006-01-19 00:00', '2006-10-26 00:00', '2007-05-24 00:00', '2009-03-16 00:00',))
if mibBuilder.loadTexts: ekinops.setLastUpdated('200903160000Z')
if mibBuilder.loadTexts: ekinops.setOrganization('Ekinops')
class EkiState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class EkiOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

class EkiProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("protGBE", 1), ("prot1GFC", 2), ("prot2GFC", 3), ("protOC48", 4), ("protclearchannel", 6), ("prot10GBE", 8), ("protOC192", 9), ("protStm1", 10), ("protStm4", 11), ("prot2GBE", 12), ("prot4GFC", 13), ("protEscon", 14), ("protFastEth", 15))

class EkiMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("manual", 2))

class EkiSynchroMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("internal", 1), ("external", 2))

class EkiApiState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(128, 129, 130, 132, 133))
    namedValues = NamedValues(("moduleNotResponding", 128), ("messageFormatError", 129), ("cmdExecutionError", 130), ("unknownArticleError", 132), ("unknownMessageError", 133))

class EkiMeasureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 15)

class EkiLoadGWSW(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("gW", 1), ("sW", 2))

class EkiLoadState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("downloading", 2))

class EkiLoadPermutMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("manual", 0), ("autoImmediate", 1), ("autoScheduled", 2))

class EkiLoadPermutMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("coldReset", 0), ("warmReset", 1))

mibBuilder.exportSymbols("EKINOPS-MIB", PYSNMP_MODULE_ID=ekinops, EkiOnOff=EkiOnOff, EkiMode=EkiMode, EkiLoadPermutMethod=EkiLoadPermutMethod, EkiMeasureType=EkiMeasureType, EkiProtocol=EkiProtocol, ekinops=ekinops, EkiSynchroMode=EkiSynchroMode, EkiLoadState=EkiLoadState, EkiLoadPermutMode=EkiLoadPermutMode, EkiState=EkiState, EkiLoadGWSW=EkiLoadGWSW, EkiApiState=EkiApiState)
