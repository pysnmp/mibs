#
# PySNMP MIB module ISIS-CAPABILTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ISIS-CAPABILTY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 14:59:53 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, MibIdentifier, Bits, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Counter32, TimeTicks, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Bits", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
isisCapabiltyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
isisCapabiltyMIB.setRevisions(('2009-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: isisCapabiltyMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: isisCapabiltyMIB.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: isisCapabiltyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: isisCapabiltyMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: isisCapabiltyMIB.setDescription('Agent capabilities for the ISIS MIB')
ciscoIsisCapabiltyV3R8Capability = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setProductRelease('Cisco IOX XR 3.8')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setStatus('current')
if mibBuilder.loadTexts: ciscoIsisCapabiltyV3R8Capability.setDescription('ISIS-MIB capabilities for IOS-XR release 3.8.')
mibBuilder.exportSymbols("ISIS-CAPABILTY-MIB", isisCapabiltyMIB=isisCapabiltyMIB, PYSNMP_MODULE_ID=isisCapabiltyMIB, ciscoIsisCapabiltyV3R8Capability=ciscoIsisCapabiltyV3R8Capability)
