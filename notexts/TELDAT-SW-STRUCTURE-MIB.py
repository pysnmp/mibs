#
# PySNMP MIB module TELDAT-SW-STRUCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:26:25 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, MibIdentifier, ModuleIdentity, ObjectIdentity, Bits, Counter64, Gauge32, IpAddress, iso, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter64", "Gauge32", "IpAddress", "iso", "Unsigned32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TELDAT-SW-STRUCTURE-MIB", telProdNpMonProtocols=telProdNpMonProtocols, telProdNpMonInterface=telProdNpMonInterface, telProdNpMonInterfNodo=telProdNpMonInterfNodo, telProductsNpConfig=telProductsNpConfig, telProdNpConfProtocol=telProdNpConfProtocol, telProdNpMonFeatures=telProdNpMonFeatures, telProductsNucleox=telProductsNucleox, telProductsNpMonit=telProductsNpMonit, telProdNpMonitSistema=telProdNpMonitSistema, telProdNpMonProtIP=telProdNpMonProtIP, telProdNpMonInterfRouter=telProdNpMonInterfRouter, telProdNpConfInterface=telProdNpConfInterface)
