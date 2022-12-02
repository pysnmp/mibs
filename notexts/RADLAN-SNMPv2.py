#
# PySNMP MIB module RADLAN-SNMPv2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMPv2
# Produced by pysmi-1.1.8 at Fri Dec  2 17:11:53 2022
# On host fv-az444-693 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Unsigned32, Counter32, ObjectIdentity, TimeTicks, Counter64, MibIdentifier, Bits, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "Counter32", "ObjectIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Bits", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Gauge32")
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

mibBuilder.exportSymbols("RADLAN-SNMPv2", RowPointer=RowPointer, RowStatus=RowStatus, TruthValue=TruthValue)
