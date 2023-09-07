#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 11:57:03 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, MibIdentifier, Counter32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, mib_2, Unsigned32, TimeTicks, Gauge32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "mib-2", "Unsigned32", "TimeTicks", "Gauge32", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))
ianaAddressFamilyNumbers.setRevisions(('2014-09-02 00:00', '2013-09-25 00:00', '2013-07-16 00:00', '2013-06-26 00:00', '2013-06-18 00:00', '2002-03-14 00:00', '2000-09-08 00:00', '2000-03-01 00:00', '2000-02-04 00:00', '1999-08-26 00:00',))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setLastUpdated('201409020000Z')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
class AddressFamilyNumbers(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 65535))
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("mplsTpSectionEndpointIdentifier", 26), ("mplsTpLspEndpointIdentifier", 27), ("mplsTpPseudowireEndpointIdentifier", 28), ("eigrpCommonServiceFamily", 16384), ("eigrpIpv4ServiceFamily", 16385), ("eigrpIpv6ServiceFamily", 16386), ("lispCanonicalAddressFormat", 16387), ("bgpLs", 16388), ("fortyeightBitMac", 16389), ("sixtyfourBitMac", 16390), ("oui", 16391), ("mac24", 16392), ("mac40", 16393), ("ipv664", 16394), ("rBridgePortID", 16395), ("trillNickname", 16396), ("reserved", 65535))

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", ianaAddressFamilyNumbers=ianaAddressFamilyNumbers, AddressFamilyNumbers=AddressFamilyNumbers, PYSNMP_MODULE_ID=ianaAddressFamilyNumbers)
