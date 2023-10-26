#
# PySNMP MIB module SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/SWPRIMGMT-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:34:53 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rcMgmt, = mibBuilder.importSymbols("RAPID-CITY", "rcMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, ModuleIdentity, Counter64, IpAddress, ObjectIdentity, iso, Integer32, MibIdentifier, Counter32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "ModuleIdentity", "Counter64", "IpAddress", "ObjectIdentity", "iso", "Integer32", "MibIdentifier", "Counter32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cobra = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201))
privateMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1))
mibBuilder.exportSymbols("SWPRIMGMT-MIB", cobra=cobra, privateMgmt=privateMgmt)
