#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:10:37 2024
# On host fv-az1121-719 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, iso, ModuleIdentity, Bits, Unsigned32, Integer32, IpAddress, NotificationType, Counter32, enterprises, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "iso", "ModuleIdentity", "Bits", "Unsigned32", "Integer32", "IpAddress", "NotificationType", "Counter32", "enterprises", "Counter64", "ObjectIdentity")
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
mibBuilder.exportSymbols("JDSU-SMI-MIB", PYSNMP_MODULE_ID=jdsuRoot, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuDataIPTest=jdsuDataIPTest, jdsuWirelessTest=jdsuWirelessTest, jdsuOtu=jdsuOtu, jdsuRoot=jdsuRoot, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuOnmsi=jdsuOnmsi, jdsuCableNetworkTest=jdsuCableNetworkTest, jdsuServiceAssurance=jdsuServiceAssurance, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuStorageProtocolTest=jdsuStorageProtocolTest)
