#
# PySNMP MIB module CISCO-SLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SLB-HEALTH-MON-CAPABILITY
# Source digest sha256:7c3aab51f5c85df7dceb44f1c411dbe67d4f3b535955f90c2a74e775e0107f0d
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbHealthMonCapapbility = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 508))
ciscoSlbHealthMonCapapbility.setRevisions(('2008-07-03 00:00', '2008-02-08 00:00', '2006-06-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setRevisionsDescriptions(('Added ciscoSlbHealthMonCapc4710aceVA3R100\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Added ciscoSlbHealthMonCapc4710aceVA1R700\n        agent capabilities for ACE 4710 Application \n        Control Engine Appliance.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setLastUpdated('2008-07-03 00:00')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setDescription('The capabilities description of\n        CISCO-SLB-HEALTH-MON-MIB.')
ciscoSlbHealthMonCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapabilityACSWV03R000.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA1R700.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
ciscoSlbHealthMonCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapc4710aceVA3R100.setDescription('CISCO-SLB-HEALTH-MON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SLB-HEALTH-MON-CAPABILITY", PYSNMP_MODULE_ID=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapabilityACSWV03R000=ciscoSlbHealthMonCapabilityACSWV03R000, ciscoSlbHealthMonCapapbility=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapc4710aceVA1R700=ciscoSlbHealthMonCapc4710aceVA1R700, ciscoSlbHealthMonCapc4710aceVA3R100=ciscoSlbHealthMonCapc4710aceVA3R100)
