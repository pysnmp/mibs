#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Jul  1 09:09:23 2024
# On host fv-az532-988 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, TimeTicks, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, IpAddress, Counter32, Counter64, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "TimeTicks", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter32", "Counter64", "Gauge32", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
