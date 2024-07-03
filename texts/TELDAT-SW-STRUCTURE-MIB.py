#
# PySNMP MIB module TELDAT-SW-STRUCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 13:34:42 2024
# On host fv-az693-695 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, iso, NotificationType, Unsigned32, Integer32, Bits, Counter32, IpAddress, Counter64, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "iso", "NotificationType", "Unsigned32", "Integer32", "Bits", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
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
mibBuilder.exportSymbols("TELDAT-SW-STRUCTURE-MIB", telProdNpMonProtIP=telProdNpMonProtIP, telProdNpMonProtocols=telProdNpMonProtocols, telProductsNpMonit=telProductsNpMonit, telProdNpMonFeatures=telProdNpMonFeatures, telProdNpMonInterface=telProdNpMonInterface, telProdNpConfInterface=telProdNpConfInterface, telProdNpMonitSistema=telProdNpMonitSistema, telProductsNucleox=telProductsNucleox, telProdNpConfProtocol=telProdNpConfProtocol, telProdNpMonInterfRouter=telProdNpMonInterfRouter, telProductsNpConfig=telProductsNpConfig, telProdNpMonInterfNodo=telProdNpMonInterfNodo)
