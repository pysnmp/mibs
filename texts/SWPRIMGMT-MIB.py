#
# PySNMP MIB module SWPRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/SWPRIMGMT-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:39:23 2022
# On host fv-az128-12 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
rcMgmt, = mibBuilder.importSymbols("RAPID-CITY", "rcMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Integer32, ObjectIdentity, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cobra = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201))
privateMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 1, 201, 1))
mibBuilder.exportSymbols("SWPRIMGMT-MIB", privateMgmt=privateMgmt, cobra=cobra)
