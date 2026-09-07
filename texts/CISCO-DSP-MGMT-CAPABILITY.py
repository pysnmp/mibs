#
# PySNMP MIB module CISCO-DSP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DSP-MGMT-CAPABILITY
# Source digest sha256:8d11030f455e18a7af171c251eef79d3203fd08eaeba8da3114f02cf9330c60d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDspMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 121))
ciscoDspMgmtCapability.setRevisions(('2011-04-18 00:00', '2006-08-09 00:00', '2005-10-16 00:00', '2005-06-29 00:00', '2005-04-21 00:00', '2004-08-07 00:00', '2003-09-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDspMgmtCapability.setRevisionsDescriptions(('Added ciscoDspMgmtCapabilityV15R02.', 'Added ciscoDspMgmtCapabilityV5R400.', 'Added ciscoDspMgmtCapabilityV5R300.', 'Added ciscoDspMgmtCapabilityV12R03 for IOS.', 'Added ciscoDspMgmtCapabilityV5R100.', 'Added ciscoDspMgmtCapabilityV5R015', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setLastUpdated('2011-04-18 00:00')
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setDescription('The agent capabilities for CISCO-DSP-MGMT-MIB.')
ciscoDspMgmtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV5R00.setDescription('Agent capabilities for Voice Switch Service\n        Module(VXSM) in Release 5.0.0.')
ciscoDspMgmtCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV5R015.setDescription('Agent capabilities for Voice Switch Service\n        Module(VXSM) in Release 5.0.15')
ciscoDspMgmtCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setProductRelease('MGX8880 Release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV5R100.setDescription('Agent capabilities for Voice Switch Service\n        Module(VXSM) in Release 5.1.00')
ciscoDspMgmtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV12R03.setDescription('Cisco DSP Management MIB capabilities')
ciscoDspMgmtCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setProductRelease('MGX8880 Release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV5R300.setDescription('Agent capabilities for Voice Switch Service\n        Module(VXSM) in Release 5.3.00')
ciscoDspMgmtCapabilityV5R400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setProductRelease('MGX8880 Release 5.4.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV5R400.setDescription('Agent capabilities for Voice Switch Service\n        Module(VXSM) in Release 5.4.00')
ciscoDspMgmtCapabilityV15R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setStatus('current')
if mibBuilder.loadTexts: ciscoDspMgmtCapabilityV15R02.setDescription('Cisco DSP Management MIB capabilities for IOS.')
mibBuilder.exportSymbols("CISCO-DSP-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDspMgmtCapability, ciscoDspMgmtCapability=ciscoDspMgmtCapability, ciscoDspMgmtCapabilityV12R03=ciscoDspMgmtCapabilityV12R03, ciscoDspMgmtCapabilityV15R02=ciscoDspMgmtCapabilityV15R02, ciscoDspMgmtCapabilityV5R00=ciscoDspMgmtCapabilityV5R00, ciscoDspMgmtCapabilityV5R015=ciscoDspMgmtCapabilityV5R015, ciscoDspMgmtCapabilityV5R100=ciscoDspMgmtCapabilityV5R100, ciscoDspMgmtCapabilityV5R300=ciscoDspMgmtCapabilityV5R300, ciscoDspMgmtCapabilityV5R400=ciscoDspMgmtCapabilityV5R400)
