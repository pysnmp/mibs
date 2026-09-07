#
# PySNMP MIB module CISCO-CCM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CCM-CAPABILITY
# Source digest sha256:e97124c077ed6ab624c43fdaf61c230a607f5ed62d3562497184541856f570aa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCCMCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 211))
ciscoCCMCapability.setRevisions(('2011-06-14 00:00', '2009-12-15 00:00', '2008-08-21 00:00', '2008-02-20 00:00', '2005-11-21 00:00', '2003-10-03 00:00', '2002-03-21 00:00', '2001-07-02 00:00', '2001-06-19 00:00',))
if mibBuilder.loadTexts: ciscoCCMCapability.setLastUpdated('2011-06-14 00:00')
if mibBuilder.loadTexts: ciscoCCMCapability.setOrganization('Cisco Systems, Inc.')
ciscoCCMCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setProductRelease('Cisco Call Manager 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R00 = ciscoCCMCapabilityV3R00.setStatus('current')
ciscoCCMCapabilityV3R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setProductRelease('Cisco Call Manager 3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R01 = ciscoCCMCapabilityV3R01.setStatus('current')
ciscoCCMCapabilityV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03 = ciscoCCMCapabilityV3R03.setStatus('obsolete')
ciscoCCMCapabilityV3R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setProductRelease('Cisco Call Manager 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV3R03Rev1 = ciscoCCMCapabilityV3R03Rev1.setStatus('current')
ciscoCCMCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setProductRelease('Cisco Call Manager 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV4R00 = ciscoCCMCapabilityV4R00.setStatus('current')
ciscoCCMCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setProductRelease('Cisco Call Manager 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV5R00 = ciscoCCMCapabilityV5R00.setStatus('current')
ciscoCCMCapabilityV7R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setProductRelease('Cisco Unified Communications Manager 7.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R00 = ciscoCCMCapabilityV7R00.setStatus('current')
ciscoCCMCapabilityV7R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setProductRelease('Cisco Unified Communications Manager 7.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV7R01 = ciscoCCMCapabilityV7R01.setStatus('current')
ciscoCCMCapabilityV8R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setProductRelease('Cisco Unified Communications Manager 8.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R00 = ciscoCCMCapabilityV8R00.setStatus('current')
ciscoCCMCapabilityV8R05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 211, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setProductRelease('Cisco Unified Communications Manager 8.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCCMCapabilityV8R05 = ciscoCCMCapabilityV8R05.setStatus('current')
mibBuilder.exportSymbols("CISCO-CCM-CAPABILITY", PYSNMP_MODULE_ID=ciscoCCMCapability, ciscoCCMCapability=ciscoCCMCapability, ciscoCCMCapabilityV3R00=ciscoCCMCapabilityV3R00, ciscoCCMCapabilityV3R01=ciscoCCMCapabilityV3R01, ciscoCCMCapabilityV3R03=ciscoCCMCapabilityV3R03, ciscoCCMCapabilityV3R03Rev1=ciscoCCMCapabilityV3R03Rev1, ciscoCCMCapabilityV4R00=ciscoCCMCapabilityV4R00, ciscoCCMCapabilityV5R00=ciscoCCMCapabilityV5R00, ciscoCCMCapabilityV7R00=ciscoCCMCapabilityV7R00, ciscoCCMCapabilityV7R01=ciscoCCMCapabilityV7R01, ciscoCCMCapabilityV8R00=ciscoCCMCapabilityV8R00, ciscoCCMCapabilityV8R05=ciscoCCMCapabilityV8R05)
