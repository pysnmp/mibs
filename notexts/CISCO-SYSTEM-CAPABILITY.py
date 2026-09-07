#
# PySNMP MIB module CISCO-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYSTEM-CAPABILITY
# Source digest sha256:9463d803a077ad73dd6e58079acf9e6e5cd8f14380fb249e8a880c567dc420af
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 276))
ciscoSystemCapability.setRevisions(('2008-07-02 00:00', '2007-07-31 00:00', '2003-09-15 00:00', '2002-03-06 00:00',))
if mibBuilder.loadTexts: ciscoSystemCapability.setLastUpdated('2008-07-02 00:00')
if mibBuilder.loadTexts: ciscoSystemCapability.setOrganization('Cisco Systems, Inc.')
ciscoSystemCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                         BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setStatus('current')
ciscoSystemCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setStatus('current')
ciscoSystemCapabilityMGXV5R0500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setProductRelease('MGX8850 5.5 Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setStatus('current')
ciscoSystemCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setProductRelease('ACSW (Application Control Software)\n                    version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setStatus('current')
ciscoSystemCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoSystemCapability, ciscoSystemCapACSWV03R000=ciscoSystemCapACSWV03R000, ciscoSystemCapCatOSV08R0101=ciscoSystemCapCatOSV08R0101, ciscoSystemCapability=ciscoSystemCapability, ciscoSystemCapabilityMGXV5R0500=ciscoSystemCapabilityMGXV5R0500, ciscoSystemCapabilityV2R00=ciscoSystemCapabilityV2R00, ciscoSystemCapc4710aceVA1R700=ciscoSystemCapc4710aceVA1R700)
