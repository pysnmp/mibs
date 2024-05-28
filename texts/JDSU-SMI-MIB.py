#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:37:15 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, NotificationType, Integer32, IpAddress, MibIdentifier, enterprises, Bits, Gauge32, TimeTicks, Unsigned32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "MibIdentifier", "enterprises", "Bits", "Gauge32", "TimeTicks", "Unsigned32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuServiceAssurance=jdsuServiceAssurance, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuCableNetworkTest=jdsuCableNetworkTest, jdsuWirelessTest=jdsuWirelessTest, PYSNMP_MODULE_ID=jdsuRoot, jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems, jdsuOtu=jdsuOtu, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuOnmsi=jdsuOnmsi, jdsuRoot=jdsuRoot, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuDataIPTest=jdsuDataIPTest)
