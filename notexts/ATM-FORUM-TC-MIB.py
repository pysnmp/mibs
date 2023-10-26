#
# PySNMP MIB module ATM-FORUM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-TC-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 10:58:00 2023
# On host fv-az552-338 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, IpAddress, Bits, Gauge32, TimeTicks, Counter64, NotificationType, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "IpAddress", "Bits", "Gauge32", "TimeTicks", "Counter64", "NotificationType", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class TruthValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class ClnpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 21)

class AtmServiceCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6))

class AtmAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(20, 20), )
class NetPrefix(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), )
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1))
atmfTransmissionTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2))
atmfMediaTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3))
atmfTrafficDescrTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4))
atmfSrvcRegTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 5))
atmForumUni = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2))
atmfPhysicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 1))
atmfAtmLayerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 2))
atmfAtmStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 3))
atmfVpcGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 4))
atmfVccGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 5))
atmfAddressGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 6))
atmfNetPrefixGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 7))
atmfSrvcRegistryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 8))
atmfVpcAbrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 9))
atmfVccAbrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 10))
atmfAddressRegistrationAdminGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 2, 11))
atmfUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 1))
atmfSonetSTS3c = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 2))
atmfDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 3))
atmf4B5B = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 4))
atmf8B10B = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 5))
atmfSonetSTS12c = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 6))
atmfE3 = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 7))
atmfT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 8))
atmfE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 2, 9))
atmfMediaUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 1))
atmfMediaCoaxCable = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 2))
atmfMediaSingleMode = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 3))
atmfMediaMultiMode = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 4))
atmfMediaStp = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 5))
atmfMediaUtp = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 3, 6))
atmfNoDescriptor = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 1))
atmfPeakRate = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 2))
atmfNoClpNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 3))
atmfClpNoTaggingNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 4))
atmfClpTaggingNoScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 5))
atmfNoClpScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 6))
atmfClpNoTaggingScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 7))
atmfClpTaggingScr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 8))
atmfClpNoTaggingMcr = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 1, 4, 9))
mibBuilder.exportSymbols("ATM-FORUM-TC-MIB", atmfNoClpNoScr=atmfNoClpNoScr, atmfMediaUnknownType=atmfMediaUnknownType, atmfMediaTypes=atmfMediaTypes, atmf8B10B=atmf8B10B, atmfMediaSingleMode=atmfMediaSingleMode, atmf4B5B=atmf4B5B, atmfVpcAbrGroup=atmfVpcAbrGroup, atmfClpTaggingNoScr=atmfClpTaggingNoScr, atmfE1=atmfE1, atmfPhysicalGroup=atmfPhysicalGroup, atmfMediaMultiMode=atmfMediaMultiMode, NetPrefix=NetPrefix, ClnpAddress=ClnpAddress, atmfVpcGroup=atmfVpcGroup, atmfE3=atmfE3, atmForum=atmForum, atmfVccGroup=atmfVccGroup, atmfUnknownType=atmfUnknownType, atmForumUni=atmForumUni, atmfClpNoTaggingMcr=atmfClpNoTaggingMcr, atmfClpTaggingScr=atmfClpTaggingScr, atmfDs3=atmfDs3, atmfClpNoTaggingScr=atmfClpNoTaggingScr, atmfTransmissionTypes=atmfTransmissionTypes, atmfAddressGroup=atmfAddressGroup, atmfSonetSTS12c=atmfSonetSTS12c, atmfMediaUtp=atmfMediaUtp, AtmServiceCategory=AtmServiceCategory, atmForumAdmin=atmForumAdmin, atmfAddressRegistrationAdminGroup=atmfAddressRegistrationAdminGroup, atmfTrafficDescrTypes=atmfTrafficDescrTypes, atmfPeakRate=atmfPeakRate, atmfAtmLayerGroup=atmfAtmLayerGroup, atmfMediaCoaxCable=atmfMediaCoaxCable, atmfNetPrefixGroup=atmfNetPrefixGroup, atmfMediaStp=atmfMediaStp, atmfNoDescriptor=atmfNoDescriptor, atmfNoClpScr=atmfNoClpScr, atmfSonetSTS3c=atmfSonetSTS3c, atmfSrvcRegTypes=atmfSrvcRegTypes, atmfVccAbrGroup=atmfVccAbrGroup, AtmAddress=AtmAddress, TruthValue=TruthValue, atmfClpNoTaggingNoScr=atmfClpNoTaggingNoScr, atmfT1=atmfT1, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup)
