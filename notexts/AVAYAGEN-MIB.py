#
# PySNMP MIB module AVAYAGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AVAYAGEN-MIB.mib
# Produced by pysmi-1.1.12 at Tue Sep 17 13:28:48 2024
# On host fv-az975-559 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, TimeTicks, ObjectIdentity, iso, Unsigned32, Counter64, IpAddress, MibIdentifier, Integer32, Bits, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "TimeTicks", "ObjectIdentity", "iso", "Unsigned32", "Counter64", "IpAddress", "MibIdentifier", "Integer32", "Bits", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avaya = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889))
avaya.setRevisions(('1904-01-27 09:00', '1902-08-15 09:00', '1902-07-28 09:00', '1901-08-09 17:00', '1901-06-21 11:55', '1900-10-15 10:45', '1900-10-15 13:05',))
if mibBuilder.loadTexts: avaya.setLastUpdated('0401270900Z')
if mibBuilder.loadTexts: avaya.setOrganization('Avaya Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2))
avGatewayProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 6))
avGatewayMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6))
lsg = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1))
avayaEISTopology = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 10))
avayaSystemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 11))
mibBuilder.exportSymbols("AVAYAGEN-MIB", avayaEISTopology=avayaEISTopology, avGatewayProducts=avGatewayProducts, lsg=lsg, mibs=mibs, avaya=avaya, avGatewayMibs=avGatewayMibs, avayaSystemStats=avayaSystemStats, products=products, PYSNMP_MODULE_ID=avaya)
