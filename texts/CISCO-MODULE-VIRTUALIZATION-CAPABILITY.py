#
# PySNMP MIB module CISCO-MODULE-VIRTUALIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MODULE-VIRTUALIZATION-CAPABILITY
# Source digest sha256:f918e1d90649d8e39fb5a81b524e7b56079dd1f74acfe2d1cd8c16505a3b3d1f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoModuleVirtualizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 497))
ciscoModuleVirtualizationCapability.setRevisions(('2008-06-14 00:00', '2006-05-31 00:00', '2006-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoModVirtCapc4710aceVA1R700 for \n        ACE 4710 Application Control Engine \n        Appliance.', 'Corrected the contact E-mail id:\n        cs-l4l7security@cisco.com', 'Added capability statement\n        ciscoModuleVirtualizationCapabilityACSWV03R000 \n        for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setLastUpdated('2008-06-14 00:00')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l4l7security@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setDescription('The capabilities description of\n        CISCO-MODULE-VIRTUALIZATION-MIB.')
ciscoModuleVirtualizationCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapabilityACSWV03R000.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
ciscoModVirtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoModVirtCapc4710aceVA1R700.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-VIRTUALIZATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoModuleVirtualizationCapability, ciscoModVirtCapc4710aceVA1R700=ciscoModVirtCapc4710aceVA1R700, ciscoModuleVirtualizationCapability=ciscoModuleVirtualizationCapability, ciscoModuleVirtualizationCapabilityACSWV03R000=ciscoModuleVirtualizationCapabilityACSWV03R000)
