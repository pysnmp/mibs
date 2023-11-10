#
# PySNMP MIB module TELDAT-SW-STRUCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-SW-STRUCTURE-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 13:28:41 2023
# On host fv-az1435-737 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, ModuleIdentity, ObjectIdentity, Counter32, IpAddress, Gauge32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "ModuleIdentity", "ObjectIdentity", "Counter32", "IpAddress", "Gauge32", "TimeTicks", "Bits")
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
mibBuilder.exportSymbols("TELDAT-SW-STRUCTURE-MIB", telProdNpMonInterface=telProdNpMonInterface, telProductsNpMonit=telProductsNpMonit, telProdNpConfInterface=telProdNpConfInterface, telProductsNucleox=telProductsNucleox, telProdNpMonitSistema=telProdNpMonitSistema, telProdNpMonInterfRouter=telProdNpMonInterfRouter, telProdNpMonProtocols=telProdNpMonProtocols, telProdNpMonFeatures=telProdNpMonFeatures, telProdNpMonProtIP=telProdNpMonProtIP, telProdNpConfProtocol=telProdNpConfProtocol, telProductsNpConfig=telProductsNpConfig, telProdNpMonInterfNodo=telProdNpMonInterfNodo)
