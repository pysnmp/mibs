#
# PySNMP MIB module TAIT-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/tait/TAIT-COMMON-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 12:23:56 2023
# On host fv-az615-431 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, Integer32, MibIdentifier, Gauge32, Unsigned32, enterprises, ModuleIdentity, Counter64, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Integer32", "MibIdentifier", "Gauge32", "Unsigned32", "enterprises", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TAIT-COMMON-MIB", taitCommonRegModule=taitCommonRegModule, taitRegistrations=taitRegistrations, PYSNMP_MODULE_ID=taitCommonRegModule, taitGeneric=taitGeneric, taitProducts=taitProducts, tait=tait, taitModules=taitModules)
