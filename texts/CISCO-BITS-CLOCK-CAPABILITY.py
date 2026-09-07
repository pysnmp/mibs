#
# PySNMP MIB module CISCO-BITS-CLOCK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BITS-CLOCK-CAPABILITY
# Source digest sha256:362d5ee4e00d4f7052f7daaf7154622c8aa6d9b52744b5258e52defc839d5663
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBitsClockCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 433))
ciscoBitsClockCapability.setRevisions(('2005-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBitsClockCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBitsClockCapability.setLastUpdated('2005-03-08 00:00')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setDescription('Agent capabilities for the CISCO-BITS-CLOCK-MIB.')
ciscoBitsClockV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 433, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoBitsClockV12R025000SW1.setDescription('IOS 12.2(25)SW1 Cisco CISCO-BITS-CLOCK-MIB.my \n                   User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-BITS-CLOCK-CAPABILITY", PYSNMP_MODULE_ID=ciscoBitsClockCapability, ciscoBitsClockCapability=ciscoBitsClockCapability, ciscoBitsClockV12R025000SW1=ciscoBitsClockV12R025000SW1)
