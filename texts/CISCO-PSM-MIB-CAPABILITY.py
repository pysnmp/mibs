#
# PySNMP MIB module CISCO-PSM-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PSM-MIB-CAPABILITY
# Source digest sha256:717a8376eee9a8583572fd168488b78c17bec724620a2755c161b5b3d797d659
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPsmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoPsmMibCapability.setRevisions(('2003-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPsmMibCapability.setRevisionsDescriptions(('The capabilities description of \n                                 Cisco Port Security MIB for\n                                 MDS 1.2(1).',))
if mibBuilder.loadTexts: ciscoPsmMibCapability.setLastUpdated('2003-08-05 00:00')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setContactInfo('       Cisco Systems\n                                        Customer Service\n\n                                Postal: 170 West Tasman Drive\n                                        San Jose, CA  95134\n                                        USA\n\n                                Tel: +1 800 553-NETS\n\n                                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoPsmMibCapability.setDescription('Agent capabilities for \n                                 CISCO-PSM-MIB')
ciscoPsmMibCapabilityMDS12R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setProductRelease('Cisco MDS 1.2(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPsmMibCapabilityMDS12R0 = ciscoPsmMibCapabilityMDS12R0.setStatus('current')
if mibBuilder.loadTexts: ciscoPsmMibCapabilityMDS12R0.setDescription('Cisco Port Security MIB capabilities')
mibBuilder.exportSymbols("CISCO-PSM-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoPsmMibCapability, ciscoPsmMibCapability=ciscoPsmMibCapability, ciscoPsmMibCapabilityMDS12R0=ciscoPsmMibCapabilityMDS12R0)
