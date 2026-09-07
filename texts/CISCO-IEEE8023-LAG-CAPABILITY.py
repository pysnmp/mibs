#
# PySNMP MIB module CISCO-IEEE8023-LAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IEEE8023-LAG-CAPABILITY
# Source digest sha256:aa315361f99265053243bbcde059da61453ee8bbceca6cc7347330492cd19c93
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8023LagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 337))
ciscoIeee8023LagCapability.setRevisions(('2006-04-19 00:00', '2004-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setRevisionsDescriptions(('Added cIeee8023LagCapCatOSV08R0601.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setLastUpdated('2006-04-19 00:00')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setDescription('The capabilities description of IEEE8023-LAG-MIB.')
cIeee8023LagCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapV12R0111bEXCat6K.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapV12R0214SXCat6K.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapCatOSV08R0101.setDescription('IEEE8023-LAG-MIB capabilities.')
cIeee8023LagCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: cIeee8023LagCapCatOSV08R0601.setDescription('IEEE8023-LAG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8023-LAG-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8023LagCapability, cIeee8023LagCapCatOSV08R0101=cIeee8023LagCapCatOSV08R0101, cIeee8023LagCapCatOSV08R0601=cIeee8023LagCapCatOSV08R0601, cIeee8023LagCapV12R0111bEXCat6K=cIeee8023LagCapV12R0111bEXCat6K, cIeee8023LagCapV12R0214SXCat6K=cIeee8023LagCapV12R0214SXCat6K, ciscoIeee8023LagCapability=ciscoIeee8023LagCapability)
