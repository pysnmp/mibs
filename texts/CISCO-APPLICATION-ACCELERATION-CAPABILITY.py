#
# PySNMP MIB module CISCO-APPLICATION-ACCELERATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-APPLICATION-ACCELERATION-CAPABILITY
# Source digest sha256:d567b71ebaa64e7cfd4086bed92f93f64629762268a215bc6cfcc8419da91daa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppAccCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 567))
ciscoAppAccCapability.setRevisions(('2008-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAppAccCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoAppAccCapc4710aceVA1R700 for ACE 4710 Application \n        Control Engine Appliance.',))
if mibBuilder.loadTexts: ciscoAppAccCapability.setLastUpdated('2008-07-29 00:00')
if mibBuilder.loadTexts: ciscoAppAccCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAppAccCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-avs@cisco.com')
if mibBuilder.loadTexts: ciscoAppAccCapability.setDescription('The capabilities description of\n        CISCO-APPLICATION-ACCELERATION-MIB.')
ciscoAppAccCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 567, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for ACE \n                4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoAppAccCapc4710aceVA1R700.setDescription('CISCO-APPLICATION-ACCELERATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-APPLICATION-ACCELERATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppAccCapability, ciscoAppAccCapability=ciscoAppAccCapability, ciscoAppAccCapc4710aceVA1R700=ciscoAppAccCapc4710aceVA1R700)
