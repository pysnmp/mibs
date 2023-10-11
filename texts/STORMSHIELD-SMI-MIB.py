#
# PySNMP MIB module STORMSHIELD-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SMI-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 11:38:49 2023
# On host fv-az456-991 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, IpAddress, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, enterprises, NotificationType, iso, ObjectIdentity, Gauge32, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "enterprises", "NotificationType", "iso", "ObjectIdentity", "Gauge32", "Counter32", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshield = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
stormshieldMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
snsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("STORMSHIELD-SMI-MIB", stormshield=stormshield, snsNotifications=snsNotifications, stormshieldMIB=stormshieldMIB)
