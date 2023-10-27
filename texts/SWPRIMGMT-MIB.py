#
# PySNMP MIB module SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/SWPRIMGMT-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:44:55 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rcMgmt, = mibBuilder.importSymbols("RAPID-CITY", "rcMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Counter32, Gauge32, ModuleIdentity, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, ObjectIdentity, Unsigned32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cobra = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201))
privateMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1))
mibBuilder.exportSymbols("SWPRIMGMT-MIB", privateMgmt=privateMgmt, cobra=cobra)
