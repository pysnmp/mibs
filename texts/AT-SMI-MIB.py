#
# PySNMP MIB module AT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SMI-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:49:47 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Gauge32, Counter64, Bits, iso, TimeTicks, Integer32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "Bits", "iso", "TimeTicks", "Integer32", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alliedTelesis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207))
alliedTelesis.setRevisions(('2014-09-30 00:00', '2010-06-15 00:15', '2008-02-28 00:00', '2006-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alliedTelesis.setRevisionsDescriptions(('Merged object IDs from ATKK-WLAN-SMI-MIB for Wireless Products.', 'MIB revision history dates in descriptions updated.', 'Standardized the file head.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: alliedTelesis.setLastUpdated('201409300000Z')
if mibBuilder.loadTexts: alliedTelesis.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: alliedTelesis.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: alliedTelesis.setDescription('The Structure of Management Information for Allied Telesis enterprise.')
class DisplayStringUnsized(TextualConvention, OctetString):
    reference = 'DisplayString'
    description = 'Represents textual information taken from the NVT ASCII\n                character set. It is a variation of DisplayString which\n                is defined in RFC 2579.'
    status = 'current'
    displayHint = '255a'

products = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1))
if mibBuilder.loadTexts: products.setStatus('current')
if mibBuilder.loadTexts: products.setDescription('products is the root OBJECT IDENTIFIER. Beneath it there are subtree\n                bridgeRouter and routerSwitch, which are is defined in AT-PRODUCTS-MIB.')
wirelesslan = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 13))
if mibBuilder.loadTexts: wirelesslan.setStatus('current')
if mibBuilder.loadTexts: wirelesslan.setDescription('subtree beneath which wireless lan product MIB object ids are assigned.')
mibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8))
if mibBuilder.loadTexts: mibObject.setStatus('current')
if mibBuilder.loadTexts: mibObject.setDescription('mibObject is the root OBJECT IDENTIFIER from which brouterMib and\n                wirelessLanmMIB are built.')
brouterMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4))
if mibBuilder.loadTexts: brouterMib.setStatus('current')
if mibBuilder.loadTexts: brouterMib.setDescription('subtree beneath which atRouter object ids are assigned.')
wirelessLanmMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42))
if mibBuilder.loadTexts: wirelessLanmMIB.setStatus('current')
if mibBuilder.loadTexts: wirelessLanmMIB.setDescription('subtree beneath which object ids for wlanAccess and uwc are assigned.')
atUWC = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 8))
if mibBuilder.loadTexts: atUWC.setStatus('current')
if mibBuilder.loadTexts: atUWC.setDescription('subtree beneath which wlanSwitch object ids are assigned.')
atRouter = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4))
if mibBuilder.loadTexts: atRouter.setStatus('current')
if mibBuilder.loadTexts: atRouter.setDescription('subtree beneath which various groups of object id are assigned.')
objects = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1))
if mibBuilder.loadTexts: objects.setStatus('current')
if mibBuilder.loadTexts: objects.setDescription('subtree beneath which object ids for boards and chips are assigned.')
traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2))
if mibBuilder.loadTexts: traps.setStatus('current')
if mibBuilder.loadTexts: traps.setDescription('subtree beneath which un-sorted trap ids are assigned.')
sysinfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3))
if mibBuilder.loadTexts: sysinfo.setStatus('current')
if mibBuilder.loadTexts: sysinfo.setDescription('subtree beneath which system inforamtion ids are assigned.')
modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4))
if mibBuilder.loadTexts: modules.setStatus('current')
if mibBuilder.loadTexts: modules.setDescription('subtree beneath which software module ids are assigned.')
arInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5))
if mibBuilder.loadTexts: arInterfaces.setStatus('current')
if mibBuilder.loadTexts: arInterfaces.setDescription('subtree beneath which interface ids are assigned.')
protocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6))
if mibBuilder.loadTexts: protocols.setStatus('current')
if mibBuilder.loadTexts: protocols.setDescription('subtree beneath which protocol ids are assigned.')
atAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7))
if mibBuilder.loadTexts: atAgents.setStatus('current')
if mibBuilder.loadTexts: atAgents.setDescription('subtree beneath which variation from standards defined.')
mibBuilder.exportSymbols("AT-SMI-MIB", mibObject=mibObject, sysinfo=sysinfo, modules=modules, objects=objects, PYSNMP_MODULE_ID=alliedTelesis, atRouter=atRouter, traps=traps, wirelessLanmMIB=wirelessLanmMIB, protocols=protocols, atAgents=atAgents, wirelesslan=wirelesslan, brouterMib=brouterMib, alliedTelesis=alliedTelesis, products=products, DisplayStringUnsized=DisplayStringUnsized, atUWC=atUWC, arInterfaces=arInterfaces)
