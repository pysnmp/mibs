#
# PySNMP MIB module CISCO-STP-EXTENSIONS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-STP-EXTENSIONS-CAPABILITY
# Source digest sha256:71796380d01634005cb9729a35a7398626b811a53ec17dafe1b268c188596395
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoStpExtensionsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 360))
ciscoStpExtensionsCapability.setRevisions(('2014-03-27 00:00', '2013-09-30 00:00', '2011-09-30 00:00', '2007-02-23 00:00', '2005-09-15 00:00', '2005-06-15 00:00', '2004-11-20 00:00', '2004-06-02 00:00', '2004-04-02 00:00', '2004-01-21 00:00', '2003-09-10 00:00',))
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setLastUpdated('2014-03-27 00:00')
if mibBuilder.loadTexts: ciscoStpExtensionsCapability.setOrganization('Cisco Systems, Inc.')
cstpxCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0101 = cstpxCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0101 = cstpxCapCatOSV08R0101.setStatus('current')
cstpxCapV12R0113E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0113E = cstpxCapV12R0113E.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0113E = cstpxCapV12R0113E.setStatus('current')
cstpxCapV12R0214SX = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0214SX = cstpxCapV12R0214SX.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0214SX = cstpxCapV12R0214SX.setStatus('current')
cstpxCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0301 = cstpxCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0301 = cstpxCapCatOSV08R0301.setStatus('current')
cstpxCapV12R0217bSXACat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0217bSXACat6k = cstpxCapV12R0217bSXACat6k.setProductRelease('Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0217bSXACat6k = cstpxCapV12R0217bSXACat6k.setStatus('current')
cstpxCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0401 = cstpxCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0401 = cstpxCapCatOSV08R0401.setStatus('current')
cstpxCapV12R0218SXEPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXEPCat6k = cstpxCapV12R0218SXEPCat6k.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXEPCat6k = cstpxCapV12R0218SXEPCat6k.setStatus('current')
cstpxCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0501 = cstpxCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapCatOSV08R0501 = cstpxCapCatOSV08R0501.setStatus('current')
cstpxCapV12R0218SXFPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXFPCat6k = cstpxCapV12R0218SXFPCat6k.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV12R0218SXFPCat6k = cstpxCapV12R0218SXFPCat6k.setStatus('current')
cstpxCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0001SYPCat6kSup2T = cstpxCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0001SYPCat6kSup2T = cstpxCapV15R0001SYPCat6kSup2T.setStatus('current')
cstpxCapV15R0102SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6k = cstpxCapV15R0102SYPCat6k.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6k = cstpxCapV15R0102SYPCat6k.setStatus('current')
cstpxCapV15R0102SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6kSup2T = cstpxCapV15R0102SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapV15R0102SYPCat6kSup2T = cstpxCapV15R0102SYPCat6kSup2T.setStatus('current')
cstpxCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 360, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapNxOSV05R0201PN7k = cstpxCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cstpxCapNxOSV05R0201PN7k = cstpxCapNxOSV05R0201PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-STP-EXTENSIONS-CAPABILITY", PYSNMP_MODULE_ID=ciscoStpExtensionsCapability, ciscoStpExtensionsCapability=ciscoStpExtensionsCapability, cstpxCapCatOSV08R0101=cstpxCapCatOSV08R0101, cstpxCapCatOSV08R0301=cstpxCapCatOSV08R0301, cstpxCapCatOSV08R0401=cstpxCapCatOSV08R0401, cstpxCapCatOSV08R0501=cstpxCapCatOSV08R0501, cstpxCapNxOSV05R0201PN7k=cstpxCapNxOSV05R0201PN7k, cstpxCapV12R0113E=cstpxCapV12R0113E, cstpxCapV12R0214SX=cstpxCapV12R0214SX, cstpxCapV12R0217bSXACat6k=cstpxCapV12R0217bSXACat6k, cstpxCapV12R0218SXEPCat6k=cstpxCapV12R0218SXEPCat6k, cstpxCapV12R0218SXFPCat6k=cstpxCapV12R0218SXFPCat6k, cstpxCapV15R0001SYPCat6kSup2T=cstpxCapV15R0001SYPCat6kSup2T, cstpxCapV15R0102SYPCat6k=cstpxCapV15R0102SYPCat6k, cstpxCapV15R0102SYPCat6kSup2T=cstpxCapV15R0102SYPCat6kSup2T)
