#
# PySNMP MIB module SNMPv2-CONF-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-TC-v1
# Produced by pysmi-1.1.8 at Fri Jan 27 13:59:36 2023
# On host fv-az417-962 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, TimeTicks, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, ModuleIdentity, MibIdentifier, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
