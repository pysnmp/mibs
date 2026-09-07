#
# PySNMP MIB module CISCO-ATM-TRUNK-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-TRUNK-STAT-CAPABILITY
# Source digest sha256:58cb2963423f7911ba0605834dc054957a3b6210f27d922959e1eaf3e02497af
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmTrunkStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 420))
ciscoAtmTrunkStatCapability.setRevisions(('2005-09-19 00:00', '2004-11-17 00:00', '2004-06-15 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setLastUpdated('2005-09-19 00:00')
if mibBuilder.loadTexts: ciscoAtmTrunkStatCapability.setOrganization('Cisco Systems, Inc.')
cAtmTrunkStatCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setProductRelease('Cisco VISM Release 3.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM33 = cAtmTrunkStatCapVISM33.setStatus('current')
cAtmTrunkStatCapVISM3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 420, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setProductRelease('Cisco VISM Release 3.3.25.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cAtmTrunkStatCapVISM3325 = cAtmTrunkStatCapVISM3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRUNK-STAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoAtmTrunkStatCapability, cAtmTrunkStatCapVISM3325=cAtmTrunkStatCapVISM3325, cAtmTrunkStatCapVISM33=cAtmTrunkStatCapVISM33, ciscoAtmTrunkStatCapability=ciscoAtmTrunkStatCapability)
