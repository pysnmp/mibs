#
# PySNMP MIB module ACMEPACKET-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-SMI
# Produced by pysmi-1.1.10 at Mon Oct 30 02:27:58 2023
# On host fv-az882-479 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32, TimeTicks, Bits, Counter32, MibIdentifier, NotificationType, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32", "TimeTicks", "Bits", "Counter32", "MibIdentifier", "NotificationType", "Unsigned32", "iso")
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
mibBuilder.exportSymbols("ACMEPACKET-SMI", acmepacketMgmt=acmepacketMgmt, PYSNMP_MODULE_ID=acmepacket, acmepacketModules=acmepacketModules, acmepacketConfig=acmepacketConfig, acmepacketAgentCapability=acmepacketAgentCapability, acmepacket=acmepacket, acmepacketExperiment=acmepacketExperiment)
