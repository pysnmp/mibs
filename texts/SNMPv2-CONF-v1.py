#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Fri Jan  7 16:50:07 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ModuleIdentity, ObjectIdentity, MibIdentifier, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "IpAddress", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
