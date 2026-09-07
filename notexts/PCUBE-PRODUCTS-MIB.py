#
# PySNMP MIB module PCUBE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source PCUBE-PRODUCTS-MIB
# Source digest sha256:4aa9a21dea4b07f1ff9173dc5ea2593859f2bb5180dc4a9e478fadc689030416
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
pcubeModules, pcubeProducts = mibBuilder.importSymbols("PCUBE-SMI", "pcubeModules", "pcubeProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcubeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 2))
pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))
if mibBuilder.loadTexts: pcubeProductsMIB.setLastUpdated('2002-01-14 20:00')
if mibBuilder.loadTexts: pcubeProductsMIB.setOrganization('Cisco Systems, Inc.')
sce100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 1))
sce1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 2))
sce2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 3))
mibBuilder.exportSymbols("PCUBE-PRODUCTS-MIB", PYSNMP_MODULE_ID=pcubeProductsMIB, pcubeProductsMIB=pcubeProductsMIB, sce1000=sce1000, sce100=sce100, sce2000=sce2000)
