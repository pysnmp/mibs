#
# PySNMP MIB module STORMSHIELD-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SMI-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 01:07:15 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, Gauge32, ModuleIdentity, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, ObjectIdentity, NotificationType, enterprises, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "ObjectIdentity", "NotificationType", "enterprises", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshield = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
stormshieldMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
snsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("STORMSHIELD-SMI-MIB", snsNotifications=snsNotifications, stormshield=stormshield, stormshieldMIB=stormshieldMIB)
