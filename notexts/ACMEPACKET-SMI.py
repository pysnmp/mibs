#
# PySNMP MIB module ACMEPACKET-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-SMI
# Produced by pysmi-1.1.12 at Thu Apr  4 13:41:45 2024
# On host fv-az984-576 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, Bits, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Integer32, TimeTicks, Counter32, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Integer32", "TimeTicks", "Counter32", "enterprises", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ACMEPACKET-SMI", acmepacket=acmepacket, acmepacketConfig=acmepacketConfig, acmepacketModules=acmepacketModules, PYSNMP_MODULE_ID=acmepacket, acmepacketMgmt=acmepacketMgmt, acmepacketExperiment=acmepacketExperiment, acmepacketAgentCapability=acmepacketAgentCapability)
