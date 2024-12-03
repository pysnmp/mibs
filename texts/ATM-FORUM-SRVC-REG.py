#
# PySNMP MIB module ATM-FORUM-SRVC-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-SRVC-REG
# Produced by pysmi-1.1.12 at Tue Dec  3 09:48:55 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
atmForumUni, atmForumAdmin = mibBuilder.importSymbols("ATM-FORUM-TC-MIB", "atmForumUni", "atmForumAdmin")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Gauge32, ModuleIdentity, iso, Bits, NotificationType, ObjectIdentity, Unsigned32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "iso", "Bits", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class AtmAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
atmfSrvcRegistryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 8))
atmfSrvcRegTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 5))
atmfSrvcRegLecs = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 5, 1))
atmfSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 8, 1), )
if mibBuilder.loadTexts: atmfSrvcRegTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegTable.setDescription('The table implemented by the UNI Management Entity on the\n\t\tnetwork side of the ATM UNI port contains all of the\n\t\tservices that are available to the user-side of the UNI\n\t\tindexed by service identifier.')
atmfSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1), ).setIndexNames((0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegPort"), (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegServiceID"), (0, "ATM-FORUM-SRVC-REG", "atmfSrvcAddressIndex"))
if mibBuilder.loadTexts: atmfSrvcRegEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegEntry.setDescription('Information about a single service provider that is \n\t\tavailable to the user-side of the ATM UNI port.')
atmfSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: atmfSrvcRegPort.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegPort.setDescription('A unique value which identifies the UNI port for\n\t\t\twhich the service provider is available to the \n\t\t\tuser-side.  The value of 0 has the special meaning \n\t\t\tof identifying the local UNI.')
atmfSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: atmfSrvcRegServiceID.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegServiceID.setDescription('This is the service identifier which uniquely identifies\n\t\tthe type of service at the address provided in the table.')
atmfSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 3), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfSrvcRegATMAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegATMAddress.setDescription('This is the full address of the service.  The user-side\n\t\tATM UNI port may use this address to establish a connection\n\t\twith the service.')
atmfSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: atmfSrvcRegAddressIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmfSrvcRegAddressIndex.setDescription('An arbitrary integer to differentiate multiple rows\n            containing different ATM addresses for the same service\n            on the same port.')
mibBuilder.exportSymbols("ATM-FORUM-SRVC-REG", atmfSrvcRegEntry=atmfSrvcRegEntry, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup, atmfSrvcRegPort=atmfSrvcRegPort, atmfSrvcRegATMAddress=atmfSrvcRegATMAddress, atmfSrvcRegTypes=atmfSrvcRegTypes, atmfSrvcRegTable=atmfSrvcRegTable, atmfSrvcRegLecs=atmfSrvcRegLecs, atmfSrvcRegAddressIndex=atmfSrvcRegAddressIndex, AtmAddress=AtmAddress, atmfSrvcRegServiceID=atmfSrvcRegServiceID)
