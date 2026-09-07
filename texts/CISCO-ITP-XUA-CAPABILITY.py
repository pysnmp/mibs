#
# PySNMP MIB module CISCO-ITP-XUA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-XUA-CAPABILITY
# Source digest sha256:0671b544ae9082247a91fa920cc2305425e6882aa0de2bca8b53d7ca14b02b0d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpXuaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 268))
ciscoItpXuaCapability.setRevisions(('2008-06-25 00:00', '2007-09-26 00:00', '2006-10-05 00:00', '2004-11-03 00:00', '2003-10-15 00:00', '2003-08-15 00:00', '2002-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpXuaCapability.setRevisionsDescriptions(('Added ciscoItpXuaCapabilityV12R0415SW,\n               ciscoItpXuaCapabilityV12R0218IXE,\n               ciscoItpXuaCapabilityV12R0233IRA capability statements.', 'Added ciscoItpXuaCapabilityV12R0411SW capability statement.\n         Corrected several problems with various capability statements\n         as follows.\n\n         Modified ciscoItpXuaCapabilityV12R0225SW\n\n         Modified ciscoItpXuaCapabilityV12R0219SW as follows.\n             removed cItpXuaInstOffload\n             removed cItpXuaInstOffloadSlot\n             added cItpXuaSgmRemoteIpType\n             added cItpXuaSgmRemoteIpAddr\n             added cItpXuaSgmRemoteIpRowStatus\n\n         Update ciscoItpXuaCapabilityV12R0218IXA based on changes to\n         prior capability statements.\n         ', 'Added ciscoItpXuaCapabilityV12R0218IXA capability statement.', 'Added ciscoItpXuaCapabilityV12R0225SW agent\n         capability statement to support the following\n         changes.\n\n         Added the following tables.\n            cItpXuaASRouteTable\n            cItpXuaASRouteAsTable\n\n         Added the following objects.\n            cItpXuaAspAsWeight to cItpXuaAspAsTable\n            cItpXuaAsNetworkAppear to cItpXuaAsTable\n            cItpXuaAsCongLevel to cItpXuaAsTable\n        ', 'Added ciscoItpXuaCapabilityV12R0223SW01 agent\n         capability statement to support the following\n         changes.\n\n         Deprecated the following object.\n           cItpXuaAspAssocId\n\n         Added the following objects.\n           cItpXuaAsNetworkName\n           cItpXuaAspAssocIdU32', 'Added ciscoItpXuaCapabilityV12R0219SW agent\n         capability statement to support the following\n         changes.\n\n         Added following objects and tables.\n           cItpXuaSgmRemoteIpTable\n           cItpXuaSgmCongLevel\n           cItpXuaAspCongLevel\n\n         Added following notifications.\n           ciscoItpXuaAspCongChange\n           ciscoItpXuaSgmCongChange', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpXuaCapability.setLastUpdated('2008-06-25 00:00')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpXuaCapability.setDescription('Agent capabilities for the CISCO-ITP-XUA-MIB.')
ciscoItpXuaCapabilityV12R0204MB5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setProductRelease('Cisco IOS 12.2(4)MB5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0204MB5 = ciscoItpXuaCapabilityV12R0204MB5.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0204MB5.setDescription('IOS 12.2(4)MB5 Cisco CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0219SW = ciscoItpXuaCapabilityV12R0219SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0219SW.setDescription('IOS 12.2(19)SW Cisco CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0223SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setProductRelease('Cisco IOS 12.2(23)SW01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0223SW01 = ciscoItpXuaCapabilityV12R0223SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0223SW01.setDescription('IOS 12.2(23)SW01 Cisco CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0225SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0225SW = ciscoItpXuaCapabilityV12R0225SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0225SW.setDescription('IOS 12.2(25)SW Cisco CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXA = ciscoItpXuaCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0411SW = ciscoItpXuaCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0415SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setProductRelease('Cisco IOS 12.4(15)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0415SW = ciscoItpXuaCapabilityV12R0415SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0415SW.setDescription('Cisco IOS 12.4(15)SW CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0218IXE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setProductRelease('Cisco IOS 12.2(18)IXE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0218IXE = ciscoItpXuaCapabilityV12R0218IXE.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0218IXE.setDescription('Cisco IOS 12.2(18)IXE CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
ciscoItpXuaCapabilityV12R0233IRA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 268, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setProductRelease('Cisco IOS 12.2(33)IRA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpXuaCapabilityV12R0233IRA = ciscoItpXuaCapabilityV12R0233IRA.setStatus('current')
if mibBuilder.loadTexts: ciscoItpXuaCapabilityV12R0233IRA.setDescription('Cisco IOS 12.2(33)IRA CISCO-ITP-XUA-MIB.my\n        User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-XUA-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpXuaCapability, ciscoItpXuaCapability=ciscoItpXuaCapability, ciscoItpXuaCapabilityV12R0204MB5=ciscoItpXuaCapabilityV12R0204MB5, ciscoItpXuaCapabilityV12R0218IXA=ciscoItpXuaCapabilityV12R0218IXA, ciscoItpXuaCapabilityV12R0218IXE=ciscoItpXuaCapabilityV12R0218IXE, ciscoItpXuaCapabilityV12R0219SW=ciscoItpXuaCapabilityV12R0219SW, ciscoItpXuaCapabilityV12R0223SW01=ciscoItpXuaCapabilityV12R0223SW01, ciscoItpXuaCapabilityV12R0225SW=ciscoItpXuaCapabilityV12R0225SW, ciscoItpXuaCapabilityV12R0233IRA=ciscoItpXuaCapabilityV12R0233IRA, ciscoItpXuaCapabilityV12R0411SW=ciscoItpXuaCapabilityV12R0411SW, ciscoItpXuaCapabilityV12R0415SW=ciscoItpXuaCapabilityV12R0415SW)
