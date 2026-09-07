#
# PySNMP MIB module PRODUCTS-MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source PRODUCTS-MIB-4RF
# Source digest sha256:973b3645a2f008e63231f7e86742c92827ba444354c97de94a734eafc97e6ff9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fourRFExperimental, fourRFModules, fourRFProducts = mibBuilder.importSymbols("MIB-4RF", "fourRFExperimental", "fourRFModules", "fourRFProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fourRFProductsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 2))
fourRFProductsModule.setRevisions(('2007-04-30 00:00', '2004-02-13 00:00',))
if mibBuilder.loadTexts: fourRFProductsModule.setLastUpdated('2007-04-30 00:00')
if mibBuilder.loadTexts: fourRFProductsModule.setOrganization('www.4rf.com')
fourRFCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 1))
if mibBuilder.loadTexts: fourRFCommon.setStatus('current')
fourRFAprisa = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 2))
if mibBuilder.loadTexts: fourRFAprisa.setStatus('current')
fourRFAprisaXE = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 3))
if mibBuilder.loadTexts: fourRFAprisaXE.setStatus('current')
mibBuilder.exportSymbols("PRODUCTS-MIB-4RF", PYSNMP_MODULE_ID=fourRFProductsModule, fourRFAprisa=fourRFAprisa, fourRFAprisaXE=fourRFAprisaXE, fourRFCommon=fourRFCommon, fourRFProductsModule=fourRFProductsModule)
