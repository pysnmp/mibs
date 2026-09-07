#
# PySNMP MIB module CISCO-P-BRIDGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-P-BRIDGE-CAPABILITY
# Source digest sha256:eb2340db95230c4c43e6ad43f8fadee9d06378f679aa0391bcc7276090b0dce2
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeInterval")
ciscoPBridgeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 385))
ciscoPBridgeCapability.setRevisions(('2004-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPBridgeCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPBridgeCapability.setLastUpdated('2004-01-14 00:00')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPBridgeCapability.setDescription('The agent capabilities description of\n                 P-BRIDGE-MIB.')
ciscoPBridgeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 385, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPBridgeCapCatOSV08R0301 = ciscoPBridgeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoPBridgeCapCatOSV08R0301.setDescription('P-BRIDGE-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-P-BRIDGE-CAPABILITY", PYSNMP_MODULE_ID=ciscoPBridgeCapability, ciscoPBridgeCapCatOSV08R0301=ciscoPBridgeCapCatOSV08R0301, ciscoPBridgeCapability=ciscoPBridgeCapability)
