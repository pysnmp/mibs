#
# PySNMP MIB module STORMSHIELD-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SMI-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:58:39 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, ModuleIdentity, TimeTicks, NotificationType, Integer32, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "ModuleIdentity", "TimeTicks", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stormshield = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
stormshieldMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
snsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("STORMSHIELD-SMI-MIB", snsNotifications=snsNotifications, stormshieldMIB=stormshieldMIB, stormshield=stormshield)
