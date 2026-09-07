#
# PySNMP MIB module PCUBE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source PCUBE-SMI
# Source digest sha256:adf0a211d923546e84777a0e9f78e1103dddc608c6baac05812cbd3198ac032c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pcube = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655))
pcube.setRevisions(('2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcube.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcube.setLastUpdated('2002-01-14 20:00')
if mibBuilder.loadTexts: pcube.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcube.setContactInfo('Cisco Systems\n                 Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcube.setDescription('The Structure of Management Information for the\n        Pcube enterprise.')
pcubeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 1))
if mibBuilder.loadTexts: pcubeProducts.setStatus('current')
if mibBuilder.loadTexts: pcubeProducts.setDescription('pcubeProducts is the root OBJECT IDENTIFIER from\n        which sysObjectID values are assigned.  Actual\n        values are defined in PCUBE-PRODUCTS-MIB.')
pcubeModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 2))
if mibBuilder.loadTexts: pcubeModules.setStatus('current')
if mibBuilder.loadTexts: pcubeModules.setDescription('pcubeModules provides a root object identifier\n        from which MODULE-IDENTITY values may be assigned.')
pcubeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 3))
if mibBuilder.loadTexts: pcubeMgmt.setStatus('current')
if mibBuilder.loadTexts: pcubeMgmt.setDescription('pcubeMgmt is the main subtree for new MIB development.')
pcubeWorkgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5655, 4))
if mibBuilder.loadTexts: pcubeWorkgroup.setStatus('current')
if mibBuilder.loadTexts: pcubeWorkgroup.setDescription("pcubeWorkgroup is the main subtree for objects and events of\n        P-Cube's products.")
mibBuilder.exportSymbols("PCUBE-SMI", PYSNMP_MODULE_ID=pcube, pcube=pcube, pcubeMgmt=pcubeMgmt, pcubeModules=pcubeModules, pcubeProducts=pcubeProducts, pcubeWorkgroup=pcubeWorkgroup)
