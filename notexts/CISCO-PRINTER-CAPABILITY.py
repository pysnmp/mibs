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
if mibBuilder.loadTexts: ciscoPrinterCapability.setLastUpdated('2007-06-07 00:00')
if mibBuilder.loadTexts: ciscoPrinterCapability.setOrganization('Cisco Systems, Inc.')
ciscoPrinterCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 548, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRINTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoPrinterCapability, ciscoPrinterCapability=ciscoPrinterCapability, ciscoPrinterCapabilityV12R04=ciscoPrinterCapabilityV12R04)
