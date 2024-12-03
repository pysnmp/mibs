#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.12 at Tue Dec  3 11:36:29 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, TimeTicks, Gauge32, MibIdentifier, Integer32, Bits, Counter64, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Bits", "Counter64", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
