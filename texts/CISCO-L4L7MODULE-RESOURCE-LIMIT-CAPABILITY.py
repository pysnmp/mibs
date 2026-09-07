#
# PySNMP MIB module CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY
# Source digest sha256:e88d9be20e53749ed93faa044e2bc324d406dce39968474f56bd84f59e5219da
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL4L7ModRsrcLimCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 499))
ciscoL4L7ModRsrcLimCap.setRevisions(('2008-07-22 00:00', '2008-07-21 00:00', '2006-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setRevisionsDescriptions(('Added capability statement cL4L7ModRsrcLimCapc4710aceVA3R10\n        for ACE 4710 Application Control Engine Appliance A3(1.0).', 'Added VARIATION for crlRateLimitResourceMin object to\n        cL4L7ModRsrcLimCapACSWV03R000 agent capability.\n\n        Added capability statement cL4L7ModRsrcLimCapc4710aceVA1R700\n        for ACE 4710 Application Control Engine Appliance.', 'Added capability statement\n        cL4L7ModRsrcLimCapACSWV03R000 \n        for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setLastUpdated('2008-07-22 00:00')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l47security@cisco.com')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setDescription('The capabilities description for\n        CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB.')
cL4L7ModRsrcLimCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapACSWV03R000.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities.')
cL4L7ModRsrcLimCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapc4710aceVA1R700.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities.')
cL4L7ModRsrcLimCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setStatus('current')
if mibBuilder.loadTexts: cL4L7ModRsrcLimCapc4710aceVA3R10.setDescription('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB capabilities for\n        ACE 4710 Application Control Engine Appliance A3(1.0).')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY", PYSNMP_MODULE_ID=ciscoL4L7ModRsrcLimCap, cL4L7ModRsrcLimCapACSWV03R000=cL4L7ModRsrcLimCapACSWV03R000, cL4L7ModRsrcLimCapc4710aceVA1R700=cL4L7ModRsrcLimCapc4710aceVA1R700, cL4L7ModRsrcLimCapc4710aceVA3R10=cL4L7ModRsrcLimCapc4710aceVA3R10, ciscoL4L7ModRsrcLimCap=ciscoL4L7ModRsrcLimCap)
