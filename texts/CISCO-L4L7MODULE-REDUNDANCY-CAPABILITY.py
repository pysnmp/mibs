#
# PySNMP MIB module CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY
# Source digest sha256:af0823707b468adb268a0dba943548fa6690ee1c054d9aa516b24276d831d57e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL4l7moduleRedundancyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 566))
ciscoL4l7moduleRedundancyCapability.setRevisions(('2008-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setRevisionsDescriptions(('Added capability statement cl4l7ModRedCapc4701aceVA3R100',))
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setLastUpdated('2008-07-23 00:00')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l4l7security@cisco.com')
if mibBuilder.loadTexts: ciscoL4l7moduleRedundancyCapability.setDescription('The capabilities description for\n        CISCO-L4L7MODULE-REDUNDANCY-MIB.')
cl4l7ModRedCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 566, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cl4l7ModRedCapc4710aceVA3R100 = cl4l7ModRedCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: cl4l7ModRedCapc4710aceVA3R100.setDescription('CISCO-L4L7-MODULE-REDUNDANCY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-REDUNDANCY-CAPABILITY", PYSNMP_MODULE_ID=ciscoL4l7moduleRedundancyCapability, ciscoL4l7moduleRedundancyCapability=ciscoL4l7moduleRedundancyCapability, cl4l7ModRedCapc4710aceVA3R100=cl4l7ModRedCapc4710aceVA3R100)
