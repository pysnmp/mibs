#
# PySNMP MIB module CISCO-PRIVATE-VLAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-PRIVATE-VLAN-CAPABILITY
# Source digest sha256:49611618c76469737ea6206fe548fb0b087ba46a9545c6a8ce83593053e96c8e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrivateVlanCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 402))
ciscoPrivateVlanCapability.setRevisions(('2004-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setLastUpdated('2004-03-31 00:00')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setDescription('The capabilities description of\n                CISCO-PRIVATE-VLAN-MIB.')
cPrivateVlanCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapV12R0111ECat6K.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
cPrivateVlanCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapCatOSV08R0101.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-CAPABILITY", PYSNMP_MODULE_ID=ciscoPrivateVlanCapability, cPrivateVlanCapCatOSV08R0101=cPrivateVlanCapCatOSV08R0101, cPrivateVlanCapV12R0111ECat6K=cPrivateVlanCapV12R0111ECat6K, ciscoPrivateVlanCapability=ciscoPrivateVlanCapability)
