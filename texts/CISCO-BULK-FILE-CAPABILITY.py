#
# PySNMP MIB module CISCO-BULK-FILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BULK-FILE-CAPABILITY
# Source digest sha256:c77f654e1ed48b648ad0c7d67bda09de4865315c6ad54391e6fdfc019e57fe78
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBulkFileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 188))
ciscoBulkFileCapability.setRevisions(('2006-02-06 00:00', '2003-11-13 00:00', '2002-02-17 00:00', '2000-12-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBulkFileCapability.setRevisionsDescriptions(('Added ciscoBulkFileCapCRS1V2R0\n                         Agent Capabilities for IOS XR 2.0', 'Added VXSM 5.0.0 PRODUCT-RELEASE of \n                         ciscoBulkFileCapabilityV3R00', 'Added following capabilities for\n                         MGX8850/SES Products:\n\n                         - ciscoBulkFileCapabilityV2R00\n                         - ciscoBulkFileCapabilityV3R00.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBulkFileCapability.setLastUpdated('2006-02-06 00:00')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n\n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n\n                           Tel: +1 800 553-NETS\n\n                        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoBulkFileCapability.setDescription('Agent capabilities for CISCO-BULK-FILE-MIB')
ciscoBulkFileCapabilityV1R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setProductRelease('Cisco IOS mc 1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV1R0 = ciscoBulkFileCapabilityV1R0.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV1R0.setDescription('Cisco Bulk File MIB capabilities')
ciscoBulkFileCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                          BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV2R00 = ciscoBulkFileCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV2R00.setDescription('CISCO-BULK-FILE-MIB Capabilities.')
ciscoBulkFileCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,\n                          BPX SES Release 3.00,\n                          VXSM  Release 5.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapabilityV3R00 = ciscoBulkFileCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapabilityV3R00.setDescription('CISCO-BULK-FILE-MIB Capabilities.')
ciscoBulkFileCapCRS1V2R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 188, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBulkFileCapCRS1V2R0 = ciscoBulkFileCapCRS1V2R0.setStatus('current')
if mibBuilder.loadTexts: ciscoBulkFileCapCRS1V2R0.setDescription('CISCO-BULK-FILE-MIB Capabilities\n                         for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-BULK-FILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoBulkFileCapability, ciscoBulkFileCapCRS1V2R0=ciscoBulkFileCapCRS1V2R0, ciscoBulkFileCapability=ciscoBulkFileCapability, ciscoBulkFileCapabilityV1R0=ciscoBulkFileCapabilityV1R0, ciscoBulkFileCapabilityV2R00=ciscoBulkFileCapabilityV2R00, ciscoBulkFileCapabilityV3R00=ciscoBulkFileCapabilityV3R00)
