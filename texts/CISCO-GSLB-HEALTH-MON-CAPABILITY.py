#
# PySNMP MIB module CISCO-GSLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-GSLB-HEALTH-MON-CAPABILITY
# Source digest sha256:1da05330b6cbc840d1b632ff9b19cc3c1108adcdc625e93f89ad42a4397a73c0
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGslbHealthMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 536))
ciscoGslbHealthMonCapability.setRevisions(('2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setLastUpdated('2007-02-23 00:00')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:  170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:  +1 800 553-NETS\n\n            E-mail:  cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapability.setDescription('The capabilities description\n        of CISCO-GSLB-HEALTH-MON-MIB.')
ciscoGslbHealthMonCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 536, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbHealthMonCapabilityV02R00 = ciscoGslbHealthMonCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbHealthMonCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB HEALTH MON MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-HEALTH-MON-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbHealthMonCapability, ciscoGslbHealthMonCapability=ciscoGslbHealthMonCapability, ciscoGslbHealthMonCapabilityV02R00=ciscoGslbHealthMonCapabilityV02R00)
