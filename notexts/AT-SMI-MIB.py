#
# PySNMP MIB module AT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-SMI-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:47:35 2023
# On host fv-az555-184 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Bits, ModuleIdentity, Integer32, TimeTicks, Counter64, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Bits", "ModuleIdentity", "Integer32", "TimeTicks", "Counter64", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "enterprises", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alliedTelesis = ModuleIdentity((1, 3, 6, 1, 4, 1, 207))
alliedTelesis.setRevisions(('2014-09-30 00:00', '2010-06-15 00:15', '2008-02-28 00:00', '2006-06-14 00:00',))
if mibBuilder.loadTexts: alliedTelesis.setLastUpdated('201409300000Z')
if mibBuilder.loadTexts: alliedTelesis.setOrganization('Allied Telesis, Inc.')
class DisplayStringUnsized(TextualConvention, OctetString):
    reference = 'DisplayString'
    status = 'current'
    displayHint = '255a'

products = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1))
if mibBuilder.loadTexts: products.setStatus('current')
wirelesslan = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 1, 13))
if mibBuilder.loadTexts: wirelesslan.setStatus('current')
mibObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8))
if mibBuilder.loadTexts: mibObject.setStatus('current')
brouterMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4))
if mibBuilder.loadTexts: brouterMib.setStatus('current')
wirelessLanmMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42))
if mibBuilder.loadTexts: wirelessLanmMIB.setStatus('current')
atUWC = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 8))
if mibBuilder.loadTexts: atUWC.setStatus('current')
atRouter = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4))
if mibBuilder.loadTexts: atRouter.setStatus('current')
objects = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1))
if mibBuilder.loadTexts: objects.setStatus('current')
traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2))
if mibBuilder.loadTexts: traps.setStatus('current')
sysinfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3))
if mibBuilder.loadTexts: sysinfo.setStatus('current')
modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4))
if mibBuilder.loadTexts: modules.setStatus('current')
arInterfaces = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5))
if mibBuilder.loadTexts: arInterfaces.setStatus('current')
protocols = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6))
if mibBuilder.loadTexts: protocols.setStatus('current')
atAgents = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7))
if mibBuilder.loadTexts: atAgents.setStatus('current')
mibBuilder.exportSymbols("AT-SMI-MIB", arInterfaces=arInterfaces, DisplayStringUnsized=DisplayStringUnsized, mibObject=mibObject, wirelesslan=wirelesslan, objects=objects, products=products, atUWC=atUWC, alliedTelesis=alliedTelesis, atAgents=atAgents, brouterMib=brouterMib, atRouter=atRouter, protocols=protocols, wirelessLanmMIB=wirelessLanmMIB, sysinfo=sysinfo, modules=modules, PYSNMP_MODULE_ID=alliedTelesis, traps=traps)
