#
# PySNMP MIB module RADLAN-SNMPv2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMPv2
# Produced by pysmi-1.1.8 at Fri Sep  8 08:07:01 2023
# On host fv-az887-856 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter64, IpAddress, NotificationType, MibIdentifier, TimeTicks, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class RowPointer(TextualConvention, ObjectIdentifier):
    status = 'current'

mibBuilder.exportSymbols("RADLAN-SNMPv2", RowPointer=RowPointer, TruthValue=TruthValue, RowStatus=RowStatus)
