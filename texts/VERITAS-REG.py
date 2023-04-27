#
# PySNMP MIB module VERITAS-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-REG.mib
# Produced by pysmi-1.1.8 at Thu Apr 27 10:45:07 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, NotificationType, ObjectIdentity, Counter64, enterprises, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity", "Counter64", "enterprises", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Gauge32", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
veritasGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1302, 5, 1))
veritasGlobalRegModule.setRevisions(('1901-09-05 04:45', '1901-10-22 22:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: veritasGlobalRegModule.setRevisionsDescriptions(('The initial revision of this module.', 'Corrected comments.',))
if mibBuilder.loadTexts: veritasGlobalRegModule.setLastUpdated('0109050445Z')
if mibBuilder.loadTexts: veritasGlobalRegModule.setOrganization('VERITAS Software Corporation')
if mibBuilder.loadTexts: veritasGlobalRegModule.setContactInfo('VERITAS Software Corporation\n\t\t\t\t\t\t mailstop\n\t\t\t\t\t\t 350 Ellis Street\n\t\t\t\t\t\t P.O. Box 7011\n\t\t\t\t\t \t Mountain View CA 94043-2237\n\t\t\t\t\t \t Tel: +1 650 318 4464\n\t\t\t\t\t \t Email: support@veritas.com')
if mibBuilder.loadTexts: veritasGlobalRegModule.setDescription('The global registration of the basic hierarchy of the \n\t\t\t\t\t\t VERITAS Software enterprise MIB tree.')
veritas = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302))
if mibBuilder.loadTexts: veritas.setStatus('current')
if mibBuilder.loadTexts: veritas.setDescription('The root of the OID sub-tree assigned to VERITAS Software\n\t\t\t\t by the Internet Assigned Numbers Authority (IANA)')
products = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302, 3))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('Sub-tree for product object and event definitions')
veritasModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 1302, 5))
if mibBuilder.loadTexts: veritasModules.setStatus('current')
if mibBuilder.loadTexts: veritasModules.setDescription('Sub-tree for module registrations')
mibBuilder.exportSymbols("VERITAS-REG", veritasGlobalRegModule=veritasGlobalRegModule, veritasModules=veritasModules, products=products, veritas=veritas, PYSNMP_MODULE_ID=veritasGlobalRegModule)
