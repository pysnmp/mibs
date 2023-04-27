#
# PySNMP MIB module AVAYAGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AVAYAGEN-MIB.mib
# Produced by pysmi-1.1.8 at Thu Apr 27 12:06:09 2023
# On host fv-az741-387 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, Bits, Counter64, iso, Integer32, ObjectIdentity, MibIdentifier, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "Bits", "Counter64", "iso", "Integer32", "ObjectIdentity", "MibIdentifier", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AVAYAGEN-MIB", mibs=mibs, avGatewayProducts=avGatewayProducts, avayaSystemStats=avayaSystemStats, avayaEISTopology=avayaEISTopology, products=products, avaya=avaya, PYSNMP_MODULE_ID=avaya, avGatewayMibs=avGatewayMibs, lsg=lsg)
