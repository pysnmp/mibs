#
# PySNMP MIB module CISCO-SYSLOG-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SYSLOG-EXT-CAPABILITY
# Source digest sha256:cdcbf01425c093e3104c7eaab548eca8cc278d71b64d1d699750f1b72c0e9e4f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 454))
ciscoSyslogExtCapability.setRevisions(('2008-06-30 00:00', '2006-04-18 00:00', '2005-09-01 00:00',))
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setLastUpdated('2008-06-30 00:00')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSyslogExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setStatus('current')
ciscoSyslogExtCapabilityACSWV03R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setProductRelease('ACSW (Application Control Software) 3.0\n                for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setStatus('obsolete')
ciscoSyslogExtCapACSWV03R0000Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setStatus('current')
ciscoSyslogExtCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoSyslogExtCapability, ciscoSyslogExtCapACSWV03R0000Rev1=ciscoSyslogExtCapACSWV03R0000Rev1, ciscoSyslogExtCapability=ciscoSyslogExtCapability, ciscoSyslogExtCapabilityACSWV03R0000=ciscoSyslogExtCapabilityACSWV03R0000, ciscoSyslogExtCapabilityMDS3R0=ciscoSyslogExtCapabilityMDS3R0, ciscoSyslogExtCapabilityc4710aceVA1R700=ciscoSyslogExtCapabilityc4710aceVA1R700)
