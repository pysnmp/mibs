#
# PySNMP MIB module CISCO-IP-PROTOCOL-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IP-PROTOCOL-FILTER-CAPABILITY
# Source digest sha256:6352550c49ce276cfe79ac6b4bad0753c5099f8f7ee691ef1b4ee02faa2e3adc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpProtFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 500))
ciscoIpProtFilterCapability.setRevisions(('2008-06-09 00:00', '2006-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setRevisionsDescriptions(('Added capability statement\n        cIpProtFilterCapc4710aceVA1R700 for ACE 4710 \n        Application Control Engine Appliance.', 'Added capability statement\n        cIpProtFilterCapACSWV03R000 \n        for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setLastUpdated('2008-06-09 00:00')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setDescription('The capabilities description for\n        CISCO-IP-PROTOCOL-FILTER-MIB.')
cIpProtFilterCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapACSWV03R000.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
cIpProtFilterCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                  for ACE 4710 Application Control Engine \n                  Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapc4710aceVA1R700.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-PROTOCOL-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpProtFilterCapability, cIpProtFilterCapACSWV03R000=cIpProtFilterCapACSWV03R000, cIpProtFilterCapc4710aceVA1R700=cIpProtFilterCapc4710aceVA1R700, ciscoIpProtFilterCapability=ciscoIpProtFilterCapability)
