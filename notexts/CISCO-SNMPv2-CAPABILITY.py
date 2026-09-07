#
# PySNMP MIB module CISCO-SNMPv2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMPv2-CAPABILITY
# Source digest sha256:3f0439ac3834bd768864733fadc587fe2e5a68c5a55583b362f46eb60800b103
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 113))
ciscoSnmpV2Capability.setRevisions(('2007-11-12 00:00', '2006-05-30 00:00', '2006-04-24 00:00', '2004-03-18 00:00', '2002-02-07 00:00', '2002-01-31 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setLastUpdated('2007-11-12 00:00')
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpV2CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setStatus('current')
ciscoRpmsSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setProductRelease('Cisco Resource Policy Management Server (RPMS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setStatus('current')
ciscoMgxSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setStatus('current')
ciscoBpxSesSnmpV2CapabilityV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setProductRelease('Cisco BPX SES Release 1.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setStatus('current')
ciscoSnmpV2CapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setStatus('current')
ciscoSnmpV2CapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setStatus('current')
ciscoSnmpV2CapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setStatus('current')
ciscoSnmpV2Capc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMPv2-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpV2Capability, ciscoBpxSesSnmpV2CapabilityV10=ciscoBpxSesSnmpV2CapabilityV10, ciscoMgxSnmpV2CapabilityV20=ciscoMgxSnmpV2CapabilityV20, ciscoRpmsSnmpV2CapabilityV20=ciscoRpmsSnmpV2CapabilityV20, ciscoSnmpV2CapACSWV03R000=ciscoSnmpV2CapACSWV03R000, ciscoSnmpV2CapCatOSV08R0301=ciscoSnmpV2CapCatOSV08R0301, ciscoSnmpV2CapCatOSV08R0601=ciscoSnmpV2CapCatOSV08R0601, ciscoSnmpV2Capability=ciscoSnmpV2Capability, ciscoSnmpV2CapabilityV10R02=ciscoSnmpV2CapabilityV10R02, ciscoSnmpV2Capc4710aceVA1R700=ciscoSnmpV2Capc4710aceVA1R700)
