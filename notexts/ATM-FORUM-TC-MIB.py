#
# PySNMP MIB module ATM-FORUM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/atmforum/ATM-FORUM-TC-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:10:43 2023
# On host fv-az879-766 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, MibIdentifier, ObjectIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Counter32, Gauge32, Unsigned32, enterprises, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibIdentifier", "ObjectIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "Unsigned32", "enterprises", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ATM-FORUM-TC-MIB", atmfSrvcRegTypes=atmfSrvcRegTypes, atmfClpTaggingScr=atmfClpTaggingScr, ClnpAddress=ClnpAddress, AtmAddress=AtmAddress, atmfAtmLayerGroup=atmfAtmLayerGroup, atmfVccAbrGroup=atmfVccAbrGroup, atmfSonetSTS12c=atmfSonetSTS12c, atmf4B5B=atmf4B5B, atmfE3=atmfE3, atmfPhysicalGroup=atmfPhysicalGroup, atmfMediaStp=atmfMediaStp, atmForumUni=atmForumUni, atmfClpNoTaggingNoScr=atmfClpNoTaggingNoScr, atmfSonetSTS3c=atmfSonetSTS3c, atmfE1=atmfE1, atmfMediaSingleMode=atmfMediaSingleMode, atmfMediaTypes=atmfMediaTypes, atmfAtmStatsGroup=atmfAtmStatsGroup, atmfMediaUtp=atmfMediaUtp, atmfNoDescriptor=atmfNoDescriptor, TruthValue=TruthValue, atmfAddressRegistrationAdminGroup=atmfAddressRegistrationAdminGroup, atmf8B10B=atmf8B10B, atmfDs3=atmfDs3, atmfClpNoTaggingMcr=atmfClpNoTaggingMcr, atmfVpcGroup=atmfVpcGroup, atmForum=atmForum, atmfNoClpNoScr=atmfNoClpNoScr, atmfClpNoTaggingScr=atmfClpNoTaggingScr, AtmServiceCategory=AtmServiceCategory, atmfMediaCoaxCable=atmfMediaCoaxCable, atmfNoClpScr=atmfNoClpScr, atmfVccGroup=atmfVccGroup, atmfUnknownType=atmfUnknownType, atmForumAdmin=atmForumAdmin, atmfT1=atmfT1, atmfAddressGroup=atmfAddressGroup, atmfNetPrefixGroup=atmfNetPrefixGroup, atmfTransmissionTypes=atmfTransmissionTypes, atmfSrvcRegistryGroup=atmfSrvcRegistryGroup, atmfPeakRate=atmfPeakRate, atmfClpTaggingNoScr=atmfClpTaggingNoScr, atmfVpcAbrGroup=atmfVpcAbrGroup, NetPrefix=NetPrefix, atmfMediaMultiMode=atmfMediaMultiMode, atmfMediaUnknownType=atmfMediaUnknownType, atmfTrafficDescrTypes=atmfTrafficDescrTypes)
