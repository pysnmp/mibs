#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.12 at Sat Jul  6 01:10:59 2024
# On host fv-az1532-138 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, TimeTicks, Unsigned32, Counter32, MibIdentifier, Counter64, IpAddress, NotificationType, Gauge32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "Gauge32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jdsuRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 35873))
jdsuRoot.setRevisions(('2010-06-08 09:53', '2014-01-22 08:51',))
if mibBuilder.loadTexts: jdsuRoot.setLastUpdated('201006080953Z')
if mibBuilder.loadTexts: jdsuRoot.setOrganization('JDSU')
jdsuAccessNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 1))
jdsuCableNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 2))
jdsuDataIPTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 3))
jdsuDigitalVideoTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 4))
jdsuFiberFieldTestSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5))
jdsuRemoteFiberTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1))
jdsuOnmsi = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1, 1))
jdsuOtu = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 5, 1, 2))
jdsuLabManufacturingTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 6))
jdsuMetroNetworkTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 7))
jdsuNetworkEnterpriseTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 8))
jdsuServiceAssurance = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 9))
jdsuStorageProtocolTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 10))
jdsuWirelessTest = MibIdentifier((1, 3, 6, 1, 4, 1, 35873, 11))
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuCableNetworkTest=jdsuCableNetworkTest, jdsuRoot=jdsuRoot, jdsuDataIPTest=jdsuDataIPTest, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems, PYSNMP_MODULE_ID=jdsuRoot, jdsuWirelessTest=jdsuWirelessTest, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuOnmsi=jdsuOnmsi, jdsuServiceAssurance=jdsuServiceAssurance, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuOtu=jdsuOtu)
