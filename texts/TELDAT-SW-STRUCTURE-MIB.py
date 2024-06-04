#
# PySNMP MIB module TELDAT-SW-STRUCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 07:54:50 2024
# On host fv-az837-21 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter64, IpAddress, ModuleIdentity, Gauge32, MibIdentifier, NotificationType, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
telproducts, = mibBuilder.importSymbols("TELDAT-MIB", "telproducts")
telProductsNucleox = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1))
telProductsNpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 1))
telProductsNpMonit = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2))
telProdNpConfInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 1, 4))
telProdNpConfProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 1, 5))
telProdNpMonitSistema = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1))
telProdNpMonInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2))
telProdNpMonProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 3))
telProdNpMonFeatures = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 4))
telProdNpMonInterfRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2))
telProdNpMonInterfNodo = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 3))
telProdNpMonProtIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 3, 1))
mibBuilder.exportSymbols("TELDAT-SW-STRUCTURE-MIB", telProdNpMonitSistema=telProdNpMonitSistema, telProdNpConfInterface=telProdNpConfInterface, telProdNpConfProtocol=telProdNpConfProtocol, telProductsNpMonit=telProductsNpMonit, telProdNpMonInterface=telProdNpMonInterface, telProdNpMonInterfRouter=telProdNpMonInterfRouter, telProdNpMonInterfNodo=telProdNpMonInterfNodo, telProductsNpConfig=telProductsNpConfig, telProdNpMonFeatures=telProdNpMonFeatures, telProdNpMonProtocols=telProdNpMonProtocols, telProductsNucleox=telProductsNucleox, telProdNpMonProtIP=telProdNpMonProtIP)
