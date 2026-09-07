#
# PySNMP MIB module CISCO-CABLE-DIAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CABLE-DIAG-CAPABILITY
# Source digest sha256:5c553955b2201c98095ad92f13b6cb01450d3b0bc9933de4687478787f9ec941
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCableDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 394))
ciscoCableDiagCapability.setRevisions(('2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCableDiagCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCableDiagCapability.setLastUpdated('2004-02-03 00:00')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCableDiagCapability.setDescription('The agent capabilities description of \n                CISCO-CABLE-DIAG-MIB.')
ciscoCableDiagCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 394, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableDiagCapCatOSV08R0301 = ciscoCableDiagCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCableDiagCapCatOSV08R0301 = ciscoCableDiagCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoCableDiagCapCatOSV08R0301.setDescription('CISCO-CABLE-DIAG-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-CABLE-DIAG-CAPABILITY", PYSNMP_MODULE_ID=ciscoCableDiagCapability, ciscoCableDiagCapCatOSV08R0301=ciscoCableDiagCapCatOSV08R0301, ciscoCableDiagCapability=ciscoCableDiagCapability)
