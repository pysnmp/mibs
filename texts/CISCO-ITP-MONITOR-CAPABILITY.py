#
# PySNMP MIB module CISCO-ITP-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ITP-MONITOR-CAPABILITY
# Source digest sha256:1a4119c5b9402a56acb616fc16285abb7e4dc43e33a813816a964ed2bec6d201
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 422))
ciscoItpMonCapability.setRevisions(('2004-11-23 00:00', '2004-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMonCapability.setRevisionsDescriptions(('Add the new ciscoItpmNotificationsGroupRev1 group\n                to support ciscoItpMonitorState notification.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMonCapability.setLastUpdated('2004-11-23 00:00')
if mibBuilder.loadTexts: ciscoItpMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMonCapability.setContactInfo('       Cisco Systems\n                       Customer Service\n               \n               Postal: 170 West Tasman Drive\n                       San Jose, CA  95134\n                       USA\n               \n                  Tel: +1 800 553-NETS\n               \n               E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpMonCapability.setDescription('Agent capabilities for the CISCO-ITP-MONITOR-MIB.')
ciscoItpMonCapabilityV12R0221SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setProductRelease('Cisco IOS 12.2(21)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0221SW.setDescription('IOS 12.2(21)SW Cisco CISCO-ITP-MONITOR-MIB.my \n                     User Agent MIB capabilities.')
ciscoItpMonCapabilityV12R0251SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0251SW.setDescription('IOS 12.2(25)SW Cisco CISCO-ITP-MONITOR-MIB.my \n                     User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MONITOR-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpMonCapability, ciscoItpMonCapability=ciscoItpMonCapability, ciscoItpMonCapabilityV12R0221SW=ciscoItpMonCapabilityV12R0221SW, ciscoItpMonCapabilityV12R0251SW=ciscoItpMonCapabilityV12R0251SW)
