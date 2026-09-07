#
# PySNMP MIB module CISCO-SNMP-MPD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-MPD-CAPABILITY
# Source digest sha256:c439aad1a61c28f473729012be466248310a359518235147bd5d20a883f47555
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpMpdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 317))
ciscoSnmpMpdCapability.setRevisions(('2008-02-11 00:00', '2006-05-27 00:00', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setRevisionsDescriptions(('Added capability statement\n        cSnmpMpdCapabilityc4710aceVA1R700 for ACE \n        4710 Application Control Engine Appliance.', 'Added capability statement\n        cSnmpMpdCapabilityACSWV03R000 for \n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setLastUpdated('2008-02-11 00:00')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setDescription('The capabilities description of SNMP-MPD-MIB.')
cSnmpMpdCapabilityCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityCatOSV05R0401.setDescription('SNMP-MPD-MIB capabilities.')
cSnmpMpdCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityACSWV03R000.setDescription('SNMP-MPD-MIB capabilities.')
cSnmpMpdCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityc4710aceVA1R700.setDescription('SNMP-MPD-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-MPD-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpMpdCapability, cSnmpMpdCapabilityACSWV03R000=cSnmpMpdCapabilityACSWV03R000, cSnmpMpdCapabilityCatOSV05R0401=cSnmpMpdCapabilityCatOSV05R0401, cSnmpMpdCapabilityc4710aceVA1R700=cSnmpMpdCapabilityc4710aceVA1R700, ciscoSnmpMpdCapability=ciscoSnmpMpdCapability)
