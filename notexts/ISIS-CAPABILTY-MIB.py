#
# PySNMP MIB module ISIS-CAPABILTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ISIS-CAPABILTY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:42 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, Counter32, IpAddress, Bits, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
isisCapabiltyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
isisCapabiltyMIB.setRevisions(('2009-03-26 00:00',))
if mibBuilder.loadTexts: isisCapabiltyMIB.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: isisCapabiltyMIB.setOrganization('Cisco Systems, Inc.')
ciscoIsisCapabiltyV3R8Capability = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setProductRelease('Cisco IOX XR 3.8')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setStatus('current')
mibBuilder.exportSymbols("ISIS-CAPABILTY-MIB", ciscoIsisCapabiltyV3R8Capability=ciscoIsisCapabiltyV3R8Capability, PYSNMP_MODULE_ID=isisCapabiltyMIB, isisCapabiltyMIB=isisCapabiltyMIB)
