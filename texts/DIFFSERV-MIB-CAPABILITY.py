#
# PySNMP MIB module DIFFSERV-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DIFFSERV-MIB-CAPABILITY
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
IndexInteger, IfDirection = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger", "IfDirection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Counter64, Unsigned32, ModuleIdentity, TimeTicks, Counter32, NotificationType, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
