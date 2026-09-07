#
# PySNMP MIB module CISCO-IEEE8021-PAE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IEEE8021-PAE-CAPABILITY
# Source digest sha256:35b35ba848e6f6e637fb37edf4ec7ae3a6ac292c2322e7ebd00f43c3e9a23990
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoIeee8021PaeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 314))
ciscoIeee8021PaeCapability.setRevisions(('2012-09-05 00:00', '2011-03-25 16:00', '2010-11-01 00:00', '2010-03-22 00:00', '2009-08-26 00:00', '2008-06-02 00:00', '2007-07-09 00:00', '2004-01-13 00:00', '2003-09-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021PaeCapability.setRevisionsDescriptions(('Added capability statement\n        cIeee8021PaeCapV15R0101SYCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0233SXJPCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0250SYPCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0233SXI4PCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0252SGPCat4K.\n\n        Added VARIATIONs for dot1xPaePortEntry and\n        dot1xAuthConfigEntry in\n        cIeee8021PaeCapV12R0233SXIPCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0233SXIPCat6K.', 'Added capability statement\n        cIeee8021PaeCapV12R0233SXHPCat6K.', 'Added capability statement\n        ciscoIeee8021PaeCapCatOSV08R0301.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021PaeCapability.setLastUpdated('2012-09-05 00:00')
if mibBuilder.loadTexts: ciscoIeee8021PaeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021PaeCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ibns@cisco.com,\n                    cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021PaeCapability.setDescription('The capabilities description of IEEE8021-PAE-MIB.')
cIeee8021PaeCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0111bEXCat6K = cIeee8021PaeCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0111bEXCat6K = cIeee8021PaeCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0111bEXCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
ciscoIeee8021PaeCapCatOSV07R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021PaeCapCatOSV07R0101 = ciscoIeee8021PaeCapCatOSV07R0101.setProductRelease('Cisco CatOS 7.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021PaeCapCatOSV07R0101 = ciscoIeee8021PaeCapCatOSV07R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021PaeCapCatOSV07R0101.setDescription('IEEE8021-PAE-MIB capabilities.')
ciscoIeee8021PaeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021PaeCapCatOSV08R0301 = ciscoIeee8021PaeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021PaeCapCatOSV08R0301 = ciscoIeee8021PaeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021PaeCapCatOSV08R0301.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXHPCat6K = cIeee8021PaeCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXHPCat6K = cIeee8021PaeCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0233SXHPCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXIPCat6K = cIeee8021PaeCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXIPCat6K = cIeee8021PaeCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0233SXIPCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0252SGPCat4K = cIeee8021PaeCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0252SGPCat4K = cIeee8021PaeCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0252SGPCat4K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXI4PCat6K = cIeee8021PaeCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXI4PCat6K = cIeee8021PaeCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0233SXI4PCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0250SYPCat6K = cIeee8021PaeCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0250SYPCat6K = cIeee8021PaeCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0250SYPCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXJPCat6K = cIeee8021PaeCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV12R0233SXJPCat6K = cIeee8021PaeCapV12R0233SXJPCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV12R0233SXJPCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
cIeee8021PaeCapV15R0101SYCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 314, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV15R0101SYCat6K = cIeee8021PaeCapV15R0101SYCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8021PaeCapV15R0101SYCat6K = cIeee8021PaeCapV15R0101SYCat6K.setStatus('current')
if mibBuilder.loadTexts: cIeee8021PaeCapV15R0101SYCat6K.setDescription('IEEE8021-PAE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8021-PAE-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021PaeCapability, cIeee8021PaeCapV12R0111bEXCat6K=cIeee8021PaeCapV12R0111bEXCat6K, cIeee8021PaeCapV12R0233SXHPCat6K=cIeee8021PaeCapV12R0233SXHPCat6K, cIeee8021PaeCapV12R0233SXI4PCat6K=cIeee8021PaeCapV12R0233SXI4PCat6K, cIeee8021PaeCapV12R0233SXIPCat6K=cIeee8021PaeCapV12R0233SXIPCat6K, cIeee8021PaeCapV12R0233SXJPCat6K=cIeee8021PaeCapV12R0233SXJPCat6K, cIeee8021PaeCapV12R0250SYPCat6K=cIeee8021PaeCapV12R0250SYPCat6K, cIeee8021PaeCapV12R0252SGPCat4K=cIeee8021PaeCapV12R0252SGPCat4K, cIeee8021PaeCapV15R0101SYCat6K=cIeee8021PaeCapV15R0101SYCat6K, ciscoIeee8021PaeCapCatOSV07R0101=ciscoIeee8021PaeCapCatOSV07R0101, ciscoIeee8021PaeCapCatOSV08R0301=ciscoIeee8021PaeCapCatOSV08R0301, ciscoIeee8021PaeCapability=ciscoIeee8021PaeCapability)
