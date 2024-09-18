#
# PySNMP MIB module SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/SWPRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Sep 18 06:49:17 2024
# On host fv-az1780-151 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rcMgmt, = mibBuilder.importSymbols("RAPID-CITY", "rcMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cobra = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201))
privateMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1))
mibBuilder.exportSymbols("SWPRIMGMT-MIB", privateMgmt=privateMgmt, cobra=cobra)
