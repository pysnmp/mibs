#
# PySNMP MIB module JDSU-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/jds/JDSU-SMI-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:05:01 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Integer32, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, IpAddress, Counter64, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Integer32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "IpAddress", "Counter64", "Gauge32", "enterprises")
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
mibBuilder.exportSymbols("JDSU-SMI-MIB", jdsuOtu=jdsuOtu, jdsuLabManufacturingTest=jdsuLabManufacturingTest, jdsuDataIPTest=jdsuDataIPTest, jdsuCableNetworkTest=jdsuCableNetworkTest, jdsuNetworkEnterpriseTest=jdsuNetworkEnterpriseTest, jdsuWirelessTest=jdsuWirelessTest, PYSNMP_MODULE_ID=jdsuRoot, jdsuRoot=jdsuRoot, jdsuDigitalVideoTest=jdsuDigitalVideoTest, jdsuRemoteFiberTest=jdsuRemoteFiberTest, jdsuAccessNetworkTest=jdsuAccessNetworkTest, jdsuOnmsi=jdsuOnmsi, jdsuStorageProtocolTest=jdsuStorageProtocolTest, jdsuServiceAssurance=jdsuServiceAssurance, jdsuMetroNetworkTest=jdsuMetroNetworkTest, jdsuFiberFieldTestSystems=jdsuFiberFieldTestSystems)
