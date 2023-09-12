#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Tue Sep 12 07:20:08 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, NotificationType, ModuleIdentity, IpAddress, iso, ObjectIdentity, MibIdentifier, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "NotificationType", "ModuleIdentity", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
