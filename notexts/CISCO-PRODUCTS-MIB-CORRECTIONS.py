#
# PySNMP MIB module CISCO-PRODUCTS-MIB-CORRECTIONS (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PRODUCTS-MIB-CORRECTIONS
# Source digest sha256:de8881f71ce62327ef55184aa34c2de00fd378273f783c913c5be4fed090cfe3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoModules, ciscoProducts = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules", "ciscoProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoProductsMIBCorrections = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 65535))
ciscoProductsMIBCorrections.setRevisions(('2014-11-27 00:00',))
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setLastUpdated('2014-11-27 00:00')
if mibBuilder.loadTexts: ciscoProductsMIBCorrections.setOrganization('The Netdisco project')
catalyst365024TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1823))
catalyst365048TS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1824))
catalyst365024PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1825))
catalyst365048PS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1826))
catalyst365024TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1827))
catalyst365048TD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1828))
catalyst365024PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1829))
catalyst365048PD = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 1, 1830))
mibBuilder.exportSymbols("CISCO-PRODUCTS-MIB-CORRECTIONS", PYSNMP_MODULE_ID=ciscoProductsMIBCorrections, catalyst365024PD=catalyst365024PD, catalyst365024PS=catalyst365024PS, catalyst365024TD=catalyst365024TD, catalyst365024TS=catalyst365024TS, catalyst365048PD=catalyst365048PD, catalyst365048PS=catalyst365048PS, catalyst365048TD=catalyst365048TD, catalyst365048TS=catalyst365048TS, ciscoProductsMIBCorrections=ciscoProductsMIBCorrections)
