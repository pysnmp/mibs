#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Mon Sep 16 14:50:50 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, Integer32, MibIdentifier, ModuleIdentity, IpAddress, Counter64, Counter32, NotificationType, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
