#
# PySNMP MIB module RBN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-TC
# Produced by pysmi-1.1.12 at Mon Jun  3 11:55:47 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rbnModules, = mibBuilder.importSymbols("RBN-SMI", "rbnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, Unsigned32, iso, ObjectIdentity, ModuleIdentity, Bits, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Unsigned32", "iso", "ObjectIdentity", "ModuleIdentity", "Bits", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 5, 2))
rbnTC.setRevisions(('2011-01-19 18:00', '2009-10-20 17:00', '2004-06-19 17:00', '2003-03-17 17:00', '2002-11-11 00:00', '2002-06-26 00:00', '2000-07-14 00:00',))
if mibBuilder.loadTexts: rbnTC.setLastUpdated('201101191800Z')
if mibBuilder.loadTexts: rbnTC.setOrganization('Ericsson AB.')
class RbnCircuitHandle(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d:2x-2x-2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class RbnKBytes(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class RbnPercentage(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd%'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class RbnSlot(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnPort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class RbnVidOrUntagged(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class RbnPortMediumType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("dsl", 11), ("cable", 12), ("wireless", 13), ("satellite", 14))

class RbnUnsigned64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("RBN-TC", PYSNMP_MODULE_ID=rbnTC, RbnCircuitHandle=RbnCircuitHandle, RbnKBytes=RbnKBytes, RbnPort=RbnPort, RbnPortMediumType=RbnPortMediumType, RbnVidOrUntagged=RbnVidOrUntagged, RbnSlot=RbnSlot, RbnUnsigned64=RbnUnsigned64, rbnTC=rbnTC, RbnPercentage=RbnPercentage)
