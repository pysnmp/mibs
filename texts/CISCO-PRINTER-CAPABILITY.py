#
# PySNMP MIB module CISCO-PRINTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PRINTER-CAPABILITY
# Source digest sha256:207efe2bb27c14eb56a7aa91e5b51fbfb566a9e39811a5c851a74482e267a0b9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrinterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 548))
ciscoPrinterCapability.setRevisions(('2007-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrinterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrinterCapability.setLastUpdated('2007-06-07 00:00')
if mibBuilder.loadTexts: ciscoPrinterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrinterCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPrinterCapability.setDescription('Agent capabilities for Printer-MIB')
ciscoPrinterCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 548, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoPrinterCapabilityV12R04.setDescription('Printer MIB capabilities')
mibBuilder.exportSymbols("CISCO-PRINTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoPrinterCapability, ciscoPrinterCapability=ciscoPrinterCapability, ciscoPrinterCapabilityV12R04=ciscoPrinterCapabilityV12R04)
