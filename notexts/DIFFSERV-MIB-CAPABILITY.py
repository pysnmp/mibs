#
# PySNMP MIB module DIFFSERV-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DIFFSERV-MIB-CAPABILITY
# Produced by pysmi-1.1.8 at Sat Jan 15 19:25:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
IndexInteger, IfDirection = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "IfDirection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, TimeTicks, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
diffServMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 377))
diffServMibCapability.setRevisions(('2003-10-13 00:00',))
if mibBuilder.loadTexts: diffServMibCapability.setLastUpdated('200310130000Z')
if mibBuilder.loadTexts: diffServMibCapability.setOrganization('Cisco Systems, Inc.')
diffServMibCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 377, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setStatus('current')
mibBuilder.exportSymbols("DIFFSERV-MIB-CAPABILITY", PYSNMP_MODULE_ID=diffServMibCapability, diffServMibCapabilityMDS13R1=diffServMibCapabilityMDS13R1, diffServMibCapability=diffServMibCapability)
