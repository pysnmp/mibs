#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:48:02 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, TimeTicks, ObjectIdentity, NotificationType, Integer32, Gauge32, ModuleIdentity, Counter32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "TimeTicks", "ObjectIdentity", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
taitCommonRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1, 1))
taitCommonRegModule.setRevisions(('2012-02-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: taitCommonRegModule.setRevisionsDescriptions(('Update with new identity.',))
if mibBuilder.loadTexts: taitCommonRegModule.setLastUpdated('201202201200Z')
if mibBuilder.loadTexts: taitCommonRegModule.setOrganization('www.taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setContactInfo('postal: Tait International Limited\n                   558 Wairakei Road\n                   PO Box 1645\n                   Christchurch\n                   New Zealand\n\n           phone:  +64 3358 3399\n           email:  support@taitradio.com')
if mibBuilder.loadTexts: taitCommonRegModule.setDescription('The Tait Communication registration module.')
tait = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570))
if mibBuilder.loadTexts: tait.setStatus('current')
if mibBuilder.loadTexts: tait.setDescription('The root of the sub-tree for Tait Communications.')
taitRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1))
if mibBuilder.loadTexts: taitRegistrations.setStatus('current')
if mibBuilder.loadTexts: taitRegistrations.setDescription('Sub-tree for registrations, which includes modules.')
taitModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 1, 1))
if mibBuilder.loadTexts: taitModules.setStatus('current')
if mibBuilder.loadTexts: taitModules.setDescription('Sub-tree for module registrations. It contains the textual context files.')
taitGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 2))
if mibBuilder.loadTexts: taitGeneric.setStatus('current')
if mibBuilder.loadTexts: taitGeneric.setDescription('Sub-tree for common objects and events for products.')
taitProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3570, 3))
if mibBuilder.loadTexts: taitProducts.setStatus('current')
if mibBuilder.loadTexts: taitProducts.setDescription('Sub-tree for product-specific objects and events.')
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitGeneric=taitGeneric, taitModules=taitModules, taitCommonRegModule=taitCommonRegModule, taitRegistrations=taitRegistrations, PYSNMP_MODULE_ID=taitCommonRegModule, taitProducts=taitProducts, tait=tait)
