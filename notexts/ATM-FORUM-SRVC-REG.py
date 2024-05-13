#
# PySNMP MIB module ATM-FORUM-SRVC-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-SRVC-REG
# Produced by pysmi-1.1.12 at Mon May 13 02:33:56 2024
# On host fv-az774-224 platform Linux version 6.5.0-1018-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
atmForumUni, atmForumAdmin = mibBuilder.importSymbols("ATM-FORUM-TC-MIB", "atmForumUni", "atmForumAdmin")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, ModuleIdentity, Counter64, Bits, Integer32, Gauge32, TimeTicks, IpAddress, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter64", "Bits", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ATM-FORUM-SRVC-REG", atmfSrvcRegEntry=atmfSrvcRegEntry, atmfSrvcRegPort=atmfSrvcRegPort, atmfSrvcRegServiceID=atmfSrvcRegServiceID, atmfSrvcRegTable=atmfSrvcRegTable, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup, atmfSrvcRegLecs=atmfSrvcRegLecs, AtmAddress=AtmAddress, atmfSrvcRegATMAddress=atmfSrvcRegATMAddress, atmfSrvcRegAddressIndex=atmfSrvcRegAddressIndex, atmfSrvcRegTypes=atmfSrvcRegTypes)
