#
# PySNMP MIB module TELDAT-SW-STRUCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 12:00:46 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, MibIdentifier, NotificationType, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Counter64, IpAddress, Integer32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "Bits", "Unsigned32")
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
mibBuilder.exportSymbols("TELDAT-SW-STRUCTURE-MIB", telProdNpMonInterfNodo=telProdNpMonInterfNodo, telProductsNpConfig=telProductsNpConfig, telProdNpConfProtocol=telProdNpConfProtocol, telProdNpConfInterface=telProdNpConfInterface, telProdNpMonInterfRouter=telProdNpMonInterfRouter, telProdNpMonFeatures=telProdNpMonFeatures, telProductsNucleox=telProductsNucleox, telProdNpMonitSistema=telProdNpMonitSistema, telProdNpMonInterface=telProdNpMonInterface, telProdNpMonProtocols=telProdNpMonProtocols, telProdNpMonProtIP=telProdNpMonProtIP, telProductsNpMonit=telProductsNpMonit)
