#
# PySNMP MIB module CISCO-AAA-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AAA-SERVER-CAPABILITY
# Source digest sha256:073775e695def93dc07936396c16b42fbcc10a6acff114726690319f043dd736
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAAAServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 129))
ciscoAAAServerCapability.setRevisions(('2008-07-21 00:00', '2006-02-21 00:00', '2003-11-14 00:00', '2000-01-20 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerCapability.setLastUpdated('2008-07-21 00:00')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setOrganization('Cisco Systems, Inc.')
ciscoAAAServerCapabilityV10R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setProductRelease('Cisco IOS 12.0(4)XJ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setStatus('current')
ciscoAAAServerCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setStatus('current')
ciscoAAAServerCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setStatus('current')
ciscoAAAServerCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-CAPABILITY", PYSNMP_MODULE_ID=ciscoAAAServerCapability, ciscoAAAServerCapability=ciscoAAAServerCapability, ciscoAAAServerCapabilityACSWV03R000=ciscoAAAServerCapabilityACSWV03R000, ciscoAAAServerCapabilityMDS13R1=ciscoAAAServerCapabilityMDS13R1, ciscoAAAServerCapabilityV10R00=ciscoAAAServerCapabilityV10R00, ciscoAAAServerCapc4710aceVA1R70=ciscoAAAServerCapc4710aceVA1R70)
