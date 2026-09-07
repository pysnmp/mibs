#
# PySNMP MIB module CISCO-MAU-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MAU-EXT-CAPABILITY
# Source digest sha256:8cc64519c7462cf78ec34b431fc230bc38206b6bc910c7645410eed7bf9bd318
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMauExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 404))
ciscoMauExtCapability.setRevisions(('2008-10-28 00:00', '2004-12-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMauExtCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoMauExtCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMauExtCapability.setLastUpdated('2008-10-28 00:00')
if mibBuilder.loadTexts: ciscoMauExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMauExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMauExtCapability.setDescription('The capabilities description of CISCO-MAU-EXT-MIB.')
ciscoMauExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapCatOSV08R0401 = ciscoMauExtCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoMauExtCapCatOSV08R0401.setDescription('CISCO-MAU-EXT-MIB capabilities.')
ciscoMauExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 404, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauExtCapV12R0233SXIPCat6K = ciscoMauExtCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauExtCapV12R0233SXIPCat6K.setDescription('CISCO-MAU-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAU-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoMauExtCapability, ciscoMauExtCapCatOSV08R0401=ciscoMauExtCapCatOSV08R0401, ciscoMauExtCapV12R0233SXIPCat6K=ciscoMauExtCapV12R0233SXIPCat6K, ciscoMauExtCapability=ciscoMauExtCapability)
