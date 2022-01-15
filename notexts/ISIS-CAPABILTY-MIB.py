#
# PySNMP MIB module ISIS-CAPABILTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ISIS-CAPABILTY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:09 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Bits, iso, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, Gauge32, Unsigned32, MibIdentifier, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
isisCapabiltyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
isisCapabiltyMIB.setRevisions(('2009-03-26 00:00',))
if mibBuilder.loadTexts: isisCapabiltyMIB.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: isisCapabiltyMIB.setOrganization('Cisco Systems, Inc.')
ciscoIsisCapabiltyV3R8Capability = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setProductRelease('Cisco IOX XR 3.8')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIsisCapabiltyV3R8Capability = ciscoIsisCapabiltyV3R8Capability.setStatus('current')
mibBuilder.exportSymbols("ISIS-CAPABILTY-MIB", PYSNMP_MODULE_ID=isisCapabiltyMIB, ciscoIsisCapabiltyV3R8Capability=ciscoIsisCapabiltyV3R8Capability, isisCapabiltyMIB=isisCapabiltyMIB)
