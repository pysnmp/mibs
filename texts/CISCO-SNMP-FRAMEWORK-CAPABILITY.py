#
# PySNMP MIB module CISCO-SNMP-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-FRAMEWORK-CAPABILITY
# Source digest sha256:31489bf4589205ef74014787b048f202443db505b1aa61ccd2d48471fd003978
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 315))
ciscoSnmpFrameworkCapability.setRevisions(('2007-11-12 00:00', '2006-05-27 00:00', '2003-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setRevisionsDescriptions(('Added capability statement\n        cSnmpFrameworkCapc4710aceVA1R700 for \n        ACE 4710 Application Control Engine \n        Appliance.', 'Added capability statement\n        cSnmpFrameworkCapACSWV03R000 for \n        Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setLastUpdated('2007-11-12 00:00')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setDescription('The capabilities description of\n        SNMP-FRAMEWORK-MIB.')
cSnmpFrameworkCapCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapCatOSV05R0401.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
cSnmpFrameworkCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapACSWV03R000.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
cSnmpFrameworkCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapc4710aceVA1R700.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-FRAMEWORK-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpFrameworkCapability, cSnmpFrameworkCapACSWV03R000=cSnmpFrameworkCapACSWV03R000, cSnmpFrameworkCapCatOSV05R0401=cSnmpFrameworkCapCatOSV05R0401, cSnmpFrameworkCapc4710aceVA1R700=cSnmpFrameworkCapc4710aceVA1R700, ciscoSnmpFrameworkCapability=ciscoSnmpFrameworkCapability)
