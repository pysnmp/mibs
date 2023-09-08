#
# PySNMP MIB module SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/SWPRIMGMT-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 11:11:55 2023
# On host fv-az590-991 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rcMgmt, = mibBuilder.importSymbols("RAPID-CITY", "rcMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cobra = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201))
privateMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1))
mibBuilder.exportSymbols("SWPRIMGMT-MIB", cobra=cobra, privateMgmt=privateMgmt)
