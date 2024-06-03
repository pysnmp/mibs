#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Jun  3 13:04:22 2024
# On host fv-az1121-719 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, ModuleIdentity, IpAddress, Unsigned32, Integer32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "ModuleIdentity", "IpAddress", "Unsigned32", "Integer32", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
