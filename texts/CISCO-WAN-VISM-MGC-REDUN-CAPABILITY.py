#
# PySNMP MIB module CISCO-WAN-VISM-MGC-REDUN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-MGC-REDUN-CAPABILITY
# Source digest sha256:3f6ab1f2eed7fe27eb642ca7c73266591fcc84867dae9f6a89d41a4417b89896
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgcRedunCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 338))
ciscoWanVismMgcRedunCapability.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setLastUpdated('2001-08-22 00:00')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setDescription('The Agent Capabilities for CISCO-WAN-MGC-REDUN-MIB\n                ')
ciscoWanVismMgcRedunCapV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapV2R00.setDescription('CISCO-WAN-VISM-MGC-REDUN-MIB capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MGC-REDUN-CAPABILITY", PYSNMP_MODULE_ID=ciscoWanVismMgcRedunCapability, ciscoWanVismMgcRedunCapV2R00=ciscoWanVismMgcRedunCapV2R00, ciscoWanVismMgcRedunCapability=ciscoWanVismMgcRedunCapability)
