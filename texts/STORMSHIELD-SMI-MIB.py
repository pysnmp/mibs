#
# PySNMP MIB module STORMSHIELD-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SMI-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 13:59:10 2021
# On host fv-az33-388 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, Gauge32, TimeTicks, ObjectIdentity, Integer32, Bits, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, Counter64, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Gauge32", "TimeTicks", "ObjectIdentity", "Integer32", "Bits", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "Counter64", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshield = MibIdentifier((1, 3, 6, 1, 4, 1, 11256))
stormshieldMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1))
snsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11256, 1, 6))
mibBuilder.exportSymbols("STORMSHIELD-SMI-MIB", stormshield=stormshield, stormshieldMIB=stormshieldMIB, snsNotifications=snsNotifications)
