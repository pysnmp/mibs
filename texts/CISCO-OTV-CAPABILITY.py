#
# PySNMP MIB module CISCO-OTV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-OTV-CAPABILITY
# Source digest sha256:550503b8aebcd4e3bebba2ee60da11f434b51693d4faded1ca5c7ac69a304f52
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoOtvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 622))
ciscoOtvCapability.setRevisions(('2013-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOtvCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOtvCapability.setLastUpdated('2013-07-29 00:00')
if mibBuilder.loadTexts: ciscoOtvCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOtvCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoOtvCapability.setDescription('The capabilities description of CISCO-OTV-MIB.')
ciscoOtvCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 622, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoOtvCapNxOSV06R0202PN7K.setDescription('CISCO-OTV-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-OTV-CAPABILITY", PYSNMP_MODULE_ID=ciscoOtvCapability, ciscoOtvCapNxOSV06R0202PN7K=ciscoOtvCapNxOSV06R0202PN7K, ciscoOtvCapability=ciscoOtvCapability)
