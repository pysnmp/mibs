#
# PySNMP MIB module CISCO-WAN-VISM-T38-FAX-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-VISM-T38-FAX-CAPABILITY
# Source digest sha256:8578b50dcb70152c51edbfec7c307eac40011dca28137c19a5b707c262f70b03
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismT38FaxCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 335))
cwVismT38FaxCapability.setRevisions(('2001-08-05 00:00', '2002-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismT38FaxCapability.setRevisionsDescriptions(('Initial version of this MIB module', '\n                t38FaxInfoFieldSize variation was modified.\n                t38HsDataPacketSize variation was added.\n                t38LsDataRedundancy variation was modified.\n                t38HsDataRedundancy variation was modified.\n                t38ErrCorrection variation was added.\n                t38NSFCountryCode variation was modified.\n                t38NSFVendorCode variation was added.\n                t38Redundancy variation was added.\n                ',))
if mibBuilder.loadTexts: cwVismT38FaxCapability.setLastUpdated('2002-06-01 00:00')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setDescription('The Agent Capabilities for CISCO-WAN-T38-FAXRELAY-MIB.')
cwVismT38FaxCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setProductRelease('VISM Release3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismT38FaxCapabilityV2R00.setDescription('CISCO-WAN-T38-FAXRELAY-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-T38-FAX-CAPABILITY", PYSNMP_MODULE_ID=cwVismT38FaxCapability, cwVismT38FaxCapability=cwVismT38FaxCapability, cwVismT38FaxCapabilityV2R00=cwVismT38FaxCapabilityV2R00)
