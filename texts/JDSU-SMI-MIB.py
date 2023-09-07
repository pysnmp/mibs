#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 10:18:43 2023
# On host fv-az627-713 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, Counter64, TimeTicks, iso, Gauge32, Bits, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Counter64", "TimeTicks", "iso", "Gauge32", "Bits", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jdsuRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 35873))
jdsuRoot.setRevisions(('2010-06-08 09:53', '2014-01-22 08:51',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jdsuRoot.setRevisionsDescriptions(('Initial version.', 'Add jdsuOtu.',))
if mibBuilder.loadTexts: jdsuRoot.setLastUpdated('201006080953Z')
if mibBuilder.loadTexts: jdsuRoot.setOrganization('JDSU')
if mibBuilder.loadTexts: jdsuRoot.setContactInfo("For product's contacts please see specific product's MIBs\r\n\t\tJDS Uniphase Corporation\r\n\t\t430 N. McCarthy Blvd.\r\n\t\tMilpitas, CA\r\n\t\t95035\r\n\t\tUSA")
if mibBuilder.loadTexts: jdsuRoot.setDescription('Corporate SMI root MIB')
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
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuWirelessTest=jdsuWirelessTest, jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuServiceAssurance=jdsuServiceAssurance, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuOnmsi=jdsuOnmsi, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuDataIPTest=jdsuDataIPTest, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuOtu=jdsuOtu, jdsuCableNetworkTest=jdsuCableNetworkTest, jdsuRoot=jdsuRoot, jdsuMetroNetworkTest=jdsuMetroNetworkTest, PYSNMP_MODULE_ID=jdsuRoot, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems)
