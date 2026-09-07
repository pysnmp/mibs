#
# PySNMP MIB module CISCO-ENHANCED-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENHANCED-SLB-CAPABILITY
# Source digest sha256:b1ec1afd25f8b279a3e18404e853795118a0a9404de7a3e2348cd3457aff8659
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEnhancedSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 507))
ciscoEnhancedSlbCapability.setRevisions(('2008-07-07 00:00', '2008-02-08 00:00', '2006-05-22 00:00',))
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setLastUpdated('2008-07-07 00:00')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setOrganization('Cisco Systems, Inc.')
ciscoEnhancedSlbCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setStatus('current')
ciscoEnhancedSlbCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setStatus('current')
ciscoEnhancedSlbCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENHANCED-SLB-CAPABILITY", PYSNMP_MODULE_ID=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapACSWV03R000=ciscoEnhancedSlbCapACSWV03R000, ciscoEnhancedSlbCapability=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapc4710aceVA1R70=ciscoEnhancedSlbCapc4710aceVA1R70, ciscoEnhancedSlbCapc4710aceVA3R10=ciscoEnhancedSlbCapc4710aceVA3R10)
