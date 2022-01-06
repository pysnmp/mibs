#
# PySNMP MIB module ATM-FORUM-SRVC-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ATM-FORUM-SRVC-REG
# Produced by pysmi-1.1.8 at Thu Jan  6 19:59:48 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
atmForumAdmin, atmForumUni = mibBuilder.importSymbols("ATM-FORUM-TC-MIB", "atmForumAdmin", "atmForumUni")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, Unsigned32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Counter32, iso, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Gauge32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class AtmAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
atmfSrvcRegistryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 8))
atmfSrvcRegTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 5))
atmfSrvcRegLecs = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 5, 1))
atmfSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 353, 2, 8, 1), )
if mibBuilder.loadTexts: atmfSrvcRegTable.setStatus('mandatory')
atmfSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1), ).setIndexNames((0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegPort"), (0, "ATM-FORUM-SRVC-REG", "atmfSrvcRegServiceID"), (0, "ATM-FORUM-SRVC-REG", "atmfSrvcAddressIndex"))
if mibBuilder.loadTexts: atmfSrvcRegEntry.setStatus('mandatory')
atmfSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: atmfSrvcRegPort.setStatus('mandatory')
atmfSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: atmfSrvcRegServiceID.setStatus('mandatory')
atmfSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 3), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmfSrvcRegATMAddress.setStatus('mandatory')
atmfSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 2, 8, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: atmfSrvcRegAddressIndex.setStatus('mandatory')
mibBuilder.exportSymbols("ATM-FORUM-SRVC-REG", atmfSrvcRegTable=atmfSrvcRegTable, atmfSrvcRegServiceID=atmfSrvcRegServiceID, atmfSrvcRegTypes=atmfSrvcRegTypes, AtmAddress=AtmAddress, atmfSrvcRegATMAddress=atmfSrvcRegATMAddress, atmfSrvcRegAddressIndex=atmfSrvcRegAddressIndex, atmfSrvcRegPort=atmfSrvcRegPort, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup, atmfSrvcRegEntry=atmfSrvcRegEntry, atmfSrvcRegLecs=atmfSrvcRegLecs)
