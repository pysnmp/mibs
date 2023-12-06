#
# PySNMP MIB module VERITAS-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veritas/VERITAS-REG.mib
# Produced by pysmi-1.1.11 at Wed Dec  6 03:07:16 2023
# On host fv-az520-882 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Unsigned32, Counter64, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Gauge32, Counter32, Integer32, TimeTicks, iso, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Unsigned32", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Gauge32", "Counter32", "Integer32", "TimeTicks", "iso", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VERITAS-REG", veritas=veritas, products=products, PYSNMP_MODULE_ID=veritasGlobalRegModule, veritasGlobalRegModule=veritasGlobalRegModule, veritasModules=veritasModules)
