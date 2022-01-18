#
# PySNMP MIB module STORMSHIELD-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SMI-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:13:32 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, Counter64, Bits, Gauge32, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, iso, NotificationType, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Counter64", "Bits", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "iso", "NotificationType", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stormshield = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
stormshieldMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
snsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("STORMSHIELD-SMI-MIB", stormshieldMIB=stormshieldMIB, stormshield=stormshield, snsNotifications=snsNotifications)
