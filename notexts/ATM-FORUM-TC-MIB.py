#
# PySNMP MIB module ATM-FORUM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-TC-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:13:58 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Unsigned32, MibIdentifier, Bits, Counter64, TimeTicks, Counter32, IpAddress, NotificationType, Gauge32, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "TimeTicks", "Counter32", "IpAddress", "NotificationType", "Gauge32", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
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
mibBuilder.exportSymbols("ATM-FORUM-TC-MIB", atmfMediaTypes=atmfMediaTypes, atmfE3=atmfE3, atmfNoClpScr=atmfNoClpScr, atmfClpNoTaggingMcr=atmfClpNoTaggingMcr, NetPrefix=NetPrefix, atmfSrvcRegTypes=atmfSrvcRegTypes, atmfVpcGroup=atmfVpcGroup, atmfClpTaggingNoScr=atmfClpTaggingNoScr, atmfClpNoTaggingScr=atmfClpNoTaggingScr, atmForumUni=atmForumUni, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup, atmfVccAbrGroup=atmfVccAbrGroup, TruthValue=TruthValue, atmfVccGroup=atmfVccGroup, atmf8B10B=atmf8B10B, atmfNetPrefixGroup=atmfNetPrefixGroup, AtmAddress=AtmAddress, atmfSonetSTS3c=atmfSonetSTS3c, atmf4B5B=atmf4B5B, atmfT1=atmfT1, atmfE1=atmfE1, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfClpNoTaggingNoScr=atmfClpNoTaggingNoScr, atmfVpcAbrGroup=atmfVpcAbrGroup, atmfMediaUtp=atmfMediaUtp, atmfUnknownType=atmfUnknownType, atmfMediaMultiMode=atmfMediaMultiMode, atmfTransmissionTypes=atmfTransmissionTypes, atmfMediaUnknownType=atmfMediaUnknownType, atmfPeakRate=atmfPeakRate, atmfClpTaggingScr=atmfClpTaggingScr, atmfNoClpNoScr=atmfNoClpNoScr, AtmServiceCategory=AtmServiceCategory, atmfMediaCoaxCable=atmfMediaCoaxCable, atmfSonetSTS12c=atmfSonetSTS12c, atmfPhysicalGroup=atmfPhysicalGroup, atmfMediaSingleMode=atmfMediaSingleMode, ClnpAddress=ClnpAddress, atmfNoDescriptor=atmfNoDescriptor, atmfAddressRegistrationAdminGroup=atmfAddressRegistrationAdminGroup, atmForumAdmin=atmForumAdmin, atmfAddressGroup=atmfAddressGroup, atmfDs3=atmfDs3, atmForum=atmForum, atmfTrafficDescrTypes=atmfTrafficDescrTypes, atmfMediaStp=atmfMediaStp, atmfAtmLayerGroup=atmfAtmLayerGroup)
