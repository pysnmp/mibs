#
# PySNMP MIB module CISCO-IEEE8021-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IEEE8021-CFM-CAPABILITY
# Source digest sha256:7d58b39b36d06cc7efbd4aea44d3e216c9692923efd077a62eb5dbe41a11bf4a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 578))
ciscoIeee8021CfmCapability.setRevisions(('2010-02-23 00:00', '2009-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoIeee8021CfmCapV12R0254SE.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setLastUpdated('2010-02-23 00:00')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA 95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapability.setDescription('The capabilities description of IEEE8021-CFM-MIB.')
ciscoIeee8021CfmCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapCatOSV08R0702 = ciscoIeee8021CfmCapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapCatOSV08R0702.setDescription('IEEE8021-CFM-MIB capabilities.')
ciscoIeee8021CfmCapV12R0254SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 578, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setProductRelease('Cisco IOS 12.2(54)SE')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmCapV12R0254SE = ciscoIeee8021CfmCapV12R0254SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmCapV12R0254SE.setDescription('IEEE8021-CFM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8021CfmCapability, ciscoIeee8021CfmCapCatOSV08R0702=ciscoIeee8021CfmCapCatOSV08R0702, ciscoIeee8021CfmCapV12R0254SE=ciscoIeee8021CfmCapV12R0254SE, ciscoIeee8021CfmCapability=ciscoIeee8021CfmCapability)
