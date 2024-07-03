#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:05:35 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Bits, IpAddress, Counter64, Gauge32, Unsigned32, ObjectIdentity, Integer32, enterprises, iso, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "Integer32", "enterprises", "iso", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuRoot=jdsuRoot, jdsuServiceAssurance=jdsuServiceAssurance, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuOtu=jdsuOtu, jdsuCableNetworkTest=jdsuCableNetworkTest, PYSNMP_MODULE_ID=jdsuRoot, jdsuOnmsi=jdsuOnmsi, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuDataIPTest=jdsuDataIPTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuWirelessTest=jdsuWirelessTest, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuDigitalVideoTest=jdsuDigitalVideoTest)
