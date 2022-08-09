#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Tue Aug  9 15:36:12 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, TimeTicks, iso, NotificationType, ObjectIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Integer32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "TimeTicks", "iso", "NotificationType", "ObjectIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
