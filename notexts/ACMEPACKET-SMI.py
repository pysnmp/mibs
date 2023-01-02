#
# PySNMP MIB module ACMEPACKET-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-SMI
# Produced by pysmi-1.1.8 at Mon Jan  2 15:33:43 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, enterprises, Bits, Unsigned32, MibIdentifier, ObjectIdentity, iso, Counter32, Gauge32, IpAddress, NotificationType, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "enterprises", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "iso", "Counter32", "Gauge32", "IpAddress", "NotificationType", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acmepacket = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148))
acmepacket.setRevisions(('2012-02-02 18:00', '2004-02-26 18:00', '2001-09-05 00:00', '2014-06-26 00:00',))
if mibBuilder.loadTexts: acmepacket.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: acmepacket.setOrganization('Oracle Communications')
acmepacketAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 2))
if mibBuilder.loadTexts: acmepacketAgentCapability.setStatus('current')
acmepacketMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 3))
if mibBuilder.loadTexts: acmepacketMgmt.setStatus('current')
acmepacketConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 4))
if mibBuilder.loadTexts: acmepacketConfig.setStatus('current')
acmepacketExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 5))
if mibBuilder.loadTexts: acmepacketExperiment.setStatus('current')
acmepacketModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 6))
if mibBuilder.loadTexts: acmepacketModules.setStatus('current')
mibBuilder.exportSymbols("ACMEPACKET-SMI", acmepacketExperiment=acmepacketExperiment, acmepacketAgentCapability=acmepacketAgentCapability, acmepacketConfig=acmepacketConfig, acmepacketModules=acmepacketModules, acmepacket=acmepacket, acmepacketMgmt=acmepacketMgmt, PYSNMP_MODULE_ID=acmepacket)
