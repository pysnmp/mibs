#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Jul  1 09:09:21 2024
# On host fv-az532-988 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, ObjectIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity, Gauge32, Bits, Counter32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "Counter32", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
