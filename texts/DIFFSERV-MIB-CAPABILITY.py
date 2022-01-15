#
# PySNMP MIB module DIFFSERV-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DIFFSERV-MIB-CAPABILITY
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:21 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
IndexInteger, IfDirection = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "IfDirection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, MibIdentifier, TimeTicks, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
diffServMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 377))
diffServMibCapability.setRevisions(('2003-10-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: diffServMibCapability.setRevisionsDescriptions(('The capabilities description of \n                                 DIFFSERV-MIB (RFC 3289) for\n                                 MDS 1.3(1).',))
if mibBuilder.loadTexts: diffServMibCapability.setLastUpdated('200310130000Z')
if mibBuilder.loadTexts: diffServMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: diffServMibCapability.setContactInfo('       Cisco Systems\n                                        Customer Service\n\n                                Postal: 170 West Tasman Drive\n                                        San Jose, CA  95134\n                                        USA\n\n                                Tel: +1 800 553-NETS\n\n                                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: diffServMibCapability.setDescription('Agent capabilities for \n                                 DIFFSERV-MIB')
diffServMibCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 377, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    diffServMibCapabilityMDS13R1 = diffServMibCapabilityMDS13R1.setStatus('current')
if mibBuilder.loadTexts: diffServMibCapabilityMDS13R1.setDescription('DIFFSERV MIB capabilities')
mibBuilder.exportSymbols("DIFFSERV-MIB-CAPABILITY", diffServMibCapability=diffServMibCapability, diffServMibCapabilityMDS13R1=diffServMibCapabilityMDS13R1, PYSNMP_MODULE_ID=diffServMibCapability)
