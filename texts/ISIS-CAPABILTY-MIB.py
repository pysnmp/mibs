#
# PySNMP MIB module ISIS-CAPABILTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ISIS-CAPABILTY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:05:13 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, Counter32, Integer32, Unsigned32, ObjectIdentity, Gauge32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, TimeTicks, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "TimeTicks", "iso", "IpAddress")
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
mibBuilder.exportSymbols("ISIS-CAPABILTY-MIB", ciscoIsisCapabiltyV3R8Capability=ciscoIsisCapabiltyV3R8Capability, isisCapabiltyMIB=isisCapabiltyMIB, PYSNMP_MODULE_ID=isisCapabiltyMIB)
