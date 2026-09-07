#
# PySNMP MIB module CISCO-PNNI-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PNNI-CAPABILITY
# Source digest sha256:376762f372dbc0370b869db2e4f8fb61ae33dba8bd8806398c41edc2d4e13acc
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPnniCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoPnniCapability.setRevisions(('2002-05-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPnniCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPnniCapability.setLastUpdated('2002-05-02 00:00')
if mibBuilder.loadTexts: ciscoPnniCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPnniCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoPnniCapability.setDescription('The Agent Capabilities for PNNI-MIB.')
ciscoPnniCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPnniCapabilityV2R00 = ciscoPnniCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoPnniCapabilityV2R00.setDescription('PNNI MIB Capabilities.')
mibBuilder.exportSymbols("CISCO-PNNI-CAPABILITY", PYSNMP_MODULE_ID=ciscoPnniCapability, ciscoPnniCapability=ciscoPnniCapability, ciscoPnniCapabilityV2R00=ciscoPnniCapabilityV2R00)
