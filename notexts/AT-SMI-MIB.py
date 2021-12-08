#
# PySNMP MIB module AT-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-SMI-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:26:45 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, ModuleIdentity, Counter32, iso, Gauge32, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Counter64, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "Counter32", "iso", "Gauge32", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Counter64", "enterprises", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("AT-SMI-MIB", traps=traps, objects=objects, DisplayStringUnsized=DisplayStringUnsized, arInterfaces=arInterfaces, modules=modules, atRouter=atRouter, PYSNMP_MODULE_ID=alliedTelesis, alliedTelesis=alliedTelesis, products=products, brouterMib=brouterMib, atAgents=atAgents, mibObject=mibObject, wirelessLanmMIB=wirelessLanmMIB, wirelesslan=wirelesslan, protocols=protocols, sysinfo=sysinfo, atUWC=atUWC)
