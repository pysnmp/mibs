#
# PySNMP MIB module CISCO-SLB-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SLB-EXT-CAPABILITY
# Source digest sha256:47b5378684ee3ac578f0db4716135d659da2f937fdbcd6847015d46e12f9d48d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 496))
ciscoSlbExtCapability.setRevisions(('2008-07-02 00:00', '2008-02-07 00:00', '2006-12-08 00:00', '2006-02-21 00:00',))
if mibBuilder.loadTexts: ciscoSlbExtCapability.setLastUpdated('2008-07-02 00:00')
if mibBuilder.loadTexts: ciscoSlbExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSlbExtCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV03R000 = ciscoSlbExtCapabilityACSWV03R000.setStatus('current')
ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setProductRelease('ACSW (Application Control Software)\n                version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setStatus('current')
ciscoSlbExtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA1R700 = ciscoSlbExtCapc4710aceVA1R700.setStatus('current')
ciscoSlbExtCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 496, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapc4710aceVA3R100 = ciscoSlbExtCapc4710aceVA3R100.setStatus('current')
mibBuilder.exportSymbols("CISCO-SLB-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoSlbExtCapability, ciscoSlbExtCapability=ciscoSlbExtCapability, ciscoSlbExtCapabilityACSWV03R000=ciscoSlbExtCapabilityACSWV03R000, ciscoSlbExtCapabilityACSWV300RA12=ciscoSlbExtCapabilityACSWV300RA12, ciscoSlbExtCapc4710aceVA1R700=ciscoSlbExtCapc4710aceVA1R700, ciscoSlbExtCapc4710aceVA3R100=ciscoSlbExtCapc4710aceVA3R100)
