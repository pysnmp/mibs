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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fourRFProductsModule.setRevisionsDescriptions(('Second draft', 'First draft',))
if mibBuilder.loadTexts: fourRFProductsModule.setLastUpdated('2007-04-30 00:00')
if mibBuilder.loadTexts: fourRFProductsModule.setOrganization('www.4rf.com')
if mibBuilder.loadTexts: fourRFProductsModule.setContactInfo('postal:   4RF Communications Ltd\n                    26 Glover Street\n                    Ngauranga\n                    PO Box 13-506\n                    Wellington 6032\n                    New Zealand\n                    \n          phone:    +64 4 499 6000\n          email:    support@4rf.com')
if mibBuilder.loadTexts: fourRFProductsModule.setDescription('4RF product registrations, all 4RF SNMP managed products have\n         a root identifier specified here.')
fourRFCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 1))
if mibBuilder.loadTexts: fourRFCommon.setStatus('current')
if mibBuilder.loadTexts: fourRFCommon.setDescription('Sub-tree for common elements.')
fourRFAprisa = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 2))
if mibBuilder.loadTexts: fourRFAprisa.setStatus('current')
if mibBuilder.loadTexts: fourRFAprisa.setDescription('Sub-tree for Aprisa/AprisaView.')
fourRFAprisaXE = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 3))
if mibBuilder.loadTexts: fourRFAprisaXE.setStatus('current')
if mibBuilder.loadTexts: fourRFAprisaXE.setDescription('Sub-tree for AprisaXE.')
mibBuilder.exportSymbols("PRODUCTS-MIB-4RF", PYSNMP_MODULE_ID=fourRFProductsModule, fourRFAprisa=fourRFAprisa, fourRFAprisaXE=fourRFAprisaXE, fourRFCommon=fourRFCommon, fourRFProductsModule=fourRFProductsModule)
