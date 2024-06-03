#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Jun  3 11:52:17 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Bits, Integer32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Bits", "Integer32", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
