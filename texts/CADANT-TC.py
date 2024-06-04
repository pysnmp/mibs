#
# PySNMP MIB module CADANT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/CADANT-TC-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:02:50 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
cadant, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadant")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Gauge32, ModuleIdentity, IpAddress, Integer32, Counter32, NotificationType, iso, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "Counter32", "NotificationType", "iso", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cadTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 0))
cadTextualConventions.setRevisions(('2009-10-15 00:00', '2009-09-14 00:00', '2009-08-28 00:00', '2008-10-23 00:00', '2008-08-06 00:00', '2007-11-05 00:00', '2007-06-25 00:00', '2006-10-16 00:00', '2006-08-23 00:00', '2006-07-27 00:00', '2006-07-27 00:00', '2005-12-02 00:00', '2005-08-30 00:00', '2005-09-23 00:00', '2005-08-31 00:00', '2004-11-12 00:00', '2004-09-15 00:00', '2004-03-09 00:00', '2003-12-18 00:00', '2003-08-20 00:00', '2003-06-08 00:00', '2003-05-08 00:00', '2003-04-21 00:00', '2003-04-04 00:00', '2003-04-01 00:00', '2003-03-31 00:00', '2003-03-17 00:00', '2002-11-01 00:00', '2002-10-25 00:00', '2002-10-16 00:00', '2002-09-25 00:00', '2001-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cadTextualConventions.setRevisionsDescriptions(('Add CadCpeDeviceTypes.', 'Add ipv6-access-list(5) to CadAclType.', 'Add CadCpeDeviceTypes.', 'Remove superGreedy(4) from FlowActivityState.', 'Add support for 16D CAM PIC types.', 'Add support for port flow control.', 'Add support for EUI IPv6 addresses.', 'Add new card subtype rcardhcp to represent the HCP on the RCM.', 'Add new card type dmm(15) and new card subtype dcard0d12u(35), dmm16m16p4iu(36) and dmm16m(37).', 'This MIB modules contains textual conventions that are\n       shared among two or more Cadant MIBs.', 'This MIB modules contains textual conventions that are\n       shared among two or more Cadant MIBs.', 'Add support from scheduling types from DISMAN-SCHEDULE-MIB.', 'Added support for RCM ports.', 'Remove SshSession and SshConnectionState. Add SshService, \n         SshAuthMethod, SshMacAlg, SshCipherType, and SshMacAlg.', 'Added another ACL type to support embedded remarks.', 'Added OUIAddress', 'Add support for CAR feature.', 'Add cadIfDirection', 'Add port type to support logical uchannels.', 'Add type to support start-stop and stop-only accounting.', 'Add additional port types to support gbic detection.', 'Add serverType for INET service support.', 'Add cadExtAclCondition for IPSec/IKE support.', 'Fixed comment for FlowActivityState', 'Rename AuthenticationMethod as AAAmethod.', 'Add premilinary pic support and card reset action', 'Add card detail support.', 'Add diskVolume support.', 'Remove enable authentication method type.', 'Change SshCipher to bitmask.', 'Align card subtypes and types.', 'Created.',))
if mibBuilder.loadTexts: cadTextualConventions.setLastUpdated('200910150000Z')
if mibBuilder.loadTexts: cadTextualConventions.setOrganization('Arris International Inc')
if mibBuilder.loadTexts: cadTextualConventions.setContactInfo('Arris Technical Support\n         Phone: +1 630 281 3000\n         Email: support@arrisi.com')
if mibBuilder.loadTexts: cadTextualConventions.setDescription('This MIB module contains the textual conventions that are shared\n         among multiple ARRIS MIBs.')
class ShelfId(TextualConvention, Integer32):
    description = 'Uniquely identifies the shelf. Number of 99 indicate an invalid ShelfId.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardId(TextualConvention, Integer32):
    description = 'Uniquely identifies the individual Circuit Pack. \n         Number of 99 indicates an invalid CardId.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardSubId(TextualConvention, Integer32):
    description = 'Uniquely identifies an entity on the circuit pack.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1)

class PortId(TextualConvention, Integer32):
    description = 'Uniquely identifies the port. Number of 99 indicates an invalid PortId. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardType(TextualConvention, Integer32):
    description = 'Enumeration of generic Card Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 98, 99))
    namedValues = NamedValues(("dcard", 1), ("ecard", 2), ("fcard", 3), ("mcard", 4), ("rcard", 6), ("fanA", 7), ("fanB", 8), ("fanC", 9), ("fanD", 10), ("powerA", 11), ("powerB", 12), ("discdriveA", 13), ("discdriveB", 14), ("dmm", 15), ("unknown", 98), ("invalid", 99))

class CardSubType(TextualConvention, Integer32):
    description = 'Enumeration of more specific current Card Type.\n         For cards with only one subtype, the type and subtype\n         should be identical.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 40, 98, 99))
    namedValues = NamedValues(("dcardiu1d8u", 1), ("ecard4e", 2), ("fcard", 3), ("mcard", 4), ("rcard", 6), ("fanA", 7), ("fanB", 8), ("fanC", 9), ("fanD", 10), ("powerA", 11), ("powerB", 12), ("discdriveA", 13), ("discdriveB", 14), ("dcard1d8u", 20), ("dcard2d8u", 21), ("dcardiu2d8u", 22), ("dcardiu2d12u", 23), ("ecard8e", 30), ("ecard4oc3", 31), ("ecard7oc3", 32), ("ecard1oc12", 33), ("ecard1gig", 34), ("dcard0d12u", 35), ("dmm16m16p4iu", 36), ("dmm16m", 37), ("rcardhcp", 40), ("unknown", 98), ("invalid", 99))

class PortType(TextualConvention, Integer32):
    description = 'Enumeration of current Port Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99))
    namedValues = NamedValues(("dport", 1), ("uport", 2), ("eport10BaseT", 3), ("eport100BaseT", 4), ("macport", 5), ("mport", 6), ("eport1000BaseT", 7), ("uchannel", 8), ("eport10000BaseT", 9), ("dportMac", 10), ("invalid", 99))

class MacChlPortType(TextualConvention, Integer32):
    description = 'Enumeration of current Port Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 8, 99))
    namedValues = NamedValues(("dport", 1), ("uchannel", 8), ("invalid", 99))

class PortMode(TextualConvention, Integer32):
    description = 'mode settings for a network port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 99))
    namedValues = NamedValues(("autoNegotiate", 1), ("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("fullDuplex1000Mpbs", 6), ("halfDuplex1000Mpbs", 7), ("fullDuplex10000Mpbs", 8), ("invalid", 99))

class PortDetectedMode(TextualConvention, Integer32):
    description = 'detected mode settings for a network port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 98, 99))
    namedValues = NamedValues(("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("sfpFullDuplex1000BaseT", 9), ("sfpHalfDuplex1000BaseT", 10), ("sfpFullDuplex100BaseT", 11), ("sfpHalfDuplex100BaseT", 12), ("sfpFullDuplex10BaseT", 13), ("sfpHalfDuplex10BaseT", 14), ("sfpFullDuplex1000BaseSX", 15), ("sfpFullDuplex1000BaseLX", 16), ("sfpFullDuplex1000BaseLH", 17), ("sfpFullDuplex1000BaseLXLH", 18), ("sfpFullDuplex1000BaseZX", 19), ("sfpFullDuplex1000BaseCWDM", 20), ("sfpFullDuplex1000BaseDWDM", 21), ("xfpFullDuplex10GBaseSR", 22), ("xfpFullDuplex10GBaseLRM", 23), ("xfpFullDuplex10GBaseLR", 24), ("xfpFullDuplex10GBaseER", 25), ("xfpFullDuplex10GBaseZR", 26), ("xfpFullDuplex10GBaseLX4", 27), ("unknown", 98), ("invalid", 99))

class FlowControlMode(TextualConvention, Integer32):
    description = 'flow control settings for a network port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 98, 99))
    namedValues = NamedValues(("on", 1), ("off", 2), ("desired", 3), ("unknown", 98), ("invalid", 99))

class AdminState(TextualConvention, Integer32):
    description = 'The administrative or the desired states of the element and are set by the EMS.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrimaryState(TextualConvention, Integer32):
    description = 'The operational state\n\t IS(1): The element is operable and available for use\n\t OOS(2): The element/resource is inoperable and unable to provide service\n\t UNEQ(3): The element/resource is unequiped.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class SecondaryState(TextualConvention, Integer32):
    description = 'For each PrimaryState, there might be an associated secondary state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notapplicable", 0), ("manual", 1), ("fault", 2), ("diagnostic", 3), ("overload", 4), ("normal", 5), ("degrade", 6), ("initializing", 7), ("swdownload", 8), ("firmwarepump", 9))

class UnknownState(TextualConvention, Integer32):
    description = 'Similar to TMN representation of the Unknown Status. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("known", 0), ("unknown", 1))

class DuplexStatus(TextualConvention, Integer32):
    description = 'not applicable to all components '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notapplicable", 0), ("active", 1), ("standby", 2), ("simplex", 3), ("protected", 4))

class MacPortId(TextualConvention, Integer32):
    description = 'A valid unique identifier for a MAC port in a C4 CMTS system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 448)

class MacPortIdWithInvalid(TextualConvention, Integer32):
    description = 'Identifier for a MAC port in a C4 CMTS system.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 449)

class EqActionType(TextualConvention, Integer32):
    description = 'not applicable to all components '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notapplicable", 0), ("initialize", 1), ("switch", 2), ("remove", 3), ("restorecond", 4), ("restoreuncd", 5), ("systemreset", 6), ("cardreset", 7))

class OverloadStatus(TextualConvention, Integer32):
    description = 'Three levels indicating how much work the card is doing.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("yellow", 2), ("red", 3))

class DiskVolumeUsageLevel(TextualConvention, Integer32):
    description = 'Describe the disk volume usage level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("minor", 2), ("major", 3), ("critical", 4))

class CadBridgeGroupId(TextualConvention, Integer32):
    description = 'Uniquely identifies the bridge group.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(33, 255)

class CadBridgePortType(TextualConvention, Integer32):
    description = 'Type of traffic allowed on a bridge port.  \n\t Ethernet ports allow any type of traffic.\n\t RF ports can be sub divided for CM traffic,\n\t authorized CPE traffic, and unauthorized CPE\n\t traffic.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cm", 1), ("cpeauth", 2), ("cpeunauth", 3), ("any", 4), ("none", 5))

class VlanId(TextualConvention, Integer32):
    description = 'The unique identifier for a Virtual LAN. A value of 1000000 indicates unknown VLAN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000000)

class FlowActivityState(TextualConvention, Integer32):
    description = "Flow Activity State describes the recent bandwidth utilization history \n\t of a service flow relative to its Service Level Agreement. A flow that is \n\t operating below its Tmin is said to be 'needy'. A flow that is operating\n\t above Tmin but below Tmid is said to be 'normal'. A flow that is operating\n\t above Tmid but below Tmax is said to be 'greedy'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("needy", 1), ("normal", 2), ("greedy", 3))

class InetAddressIPv4or6(TextualConvention, OctetString):
    reference = 'InetAddress from INET-ADDRESS-MIB, RFC2851'
    description = 'This TEXTUAL-CONVENTION is similar to InetAddress as defined\n          in the INET-ADDRESS-MIB. However, InetAddressIPv4or6 does not\n          allow DNS addresses and its address type, either IPv4 or IPv6,\n          can be readily determined from its length alone. If the\n          address is an IPv4 address, then the length will be exactly\n          4 bytes. If the address is an IPv6 address, then the length\n          will be either 16 or 20 bytes.\n\n          If the length if 0, then the address is empty or null.\n\n          If the length is 4:\n            octets   contents         encoding\n             1-4     IP address       network-byte order\n\n          If the length is 8:\n            octets   contents         encoding\n             1-8     EUI IPv6 address network-byte order\n\n          If the length is 16:\n            octets   contents         encoding\n             1-16    IPv6 address     network-byte order\n\n          If the length is 20:\n            octets   contents         encoding\n             1-16    IPv6 address     network-byte order\n            17-20    scope identifier network-byte order\n\n          The scope identifier (bytes 17-20) MUST NOT be present\n          for global IPv6 addresses. For non-global IPv6 addresses\n          (e.g. link-local or site-local addresses), the scope\n          identifier MUST always be present. It contains a link\n          identifier for link-local and a site identifier for\n          site-local IPv6 addresses.\n\n          The scope identifier MUST disambiguate identical address\n          values. For link-local addresses, the scope identifier will\n          typically be the interface index (ifIndex as defined in the\n          IF-MIB, RFC 2233) of the interface on which the address is\n          configured.\n\n          The scope identifier may contain the special value 0\n          which refers to the default scope. The default scope\n          may be used in cases where the valid scope identifier\n          is not known (e.g., a management application needs to\n          write a site-local InetAddressIPv6 address without\n          knowing the site identifier value). The default scope\n          SHOULD NOT be used as an easy way out in cases where\n          the scope identifier for a non-global IPv6 is known.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
class LineType(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the type line connections\n         available on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("console", 1), ("vty", 2))

class AAAmethod(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the type of AAA\n         methods available on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("none", 1), ("line", 2), ("local", 4), ("group", 5))

class SshService(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the SSH service types\n         available in SSH on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("terminal", 1), ("sftp", 2))

class SshAuthMethod(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the authentication method available in SSH\n         on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("password", 1), ("public-key", 2))

class SshCipher(TextualConvention, Bits):
    description = 'This TEXTUAL-CONVENTION describes the ciphers available in SSH\n         on the C4.'
    status = 'current'
    namedValues = NamedValues(("other", 0), ("threedes", 1), ("arcfour", 2), ("blowfish", 3), ("cast", 4), ("aes", 5))

class SshCipherType(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the specific cipher type\n         on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("threedes", 2), ("arcfour", 3), ("blowfish", 4), ("cast128", 5), ("aes128", 6), ("aes192", 7), ("aes256", 8), ("des", 9), ("rc4", 10))

class SshMacAlg(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the MAC algorithm available in SSH\n         on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("hmac-sha1", 2))

class SshProtocol(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the SSH protocol versions \n         available in SSH on the C4.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ssh1", 1), ("ssh2", 2), ("ssh1ssh2", 3))

class CadDouble(TextualConvention, Counter64):
    description = 'This type is used to express and display 64-bit, double-precision \n         floating-point values.'
    status = 'current'
    displayHint = 'd-10'

class FirmwareSource(TextualConvention, Integer32):
    description = 'This type describes the initial source of the firmware running on\n\t a card.  Committed and transient indicate the card flash device and\n\t the downloaded image, respectively.  Boot1 and Boot2 indicate which\n\t of the resident boot images was used to boot the card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("committed", 1), ("transient", 2), ("boot1", 3), ("boot2", 4), ("unknown", 5))

class PicType(TextualConvention, Integer32):
    description = 'This type describes the PIC attached to the backplane behind a a card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 98, 99))
    namedValues = NamedValues(("cameven", 1), ("camevensp1to1", 2), ("camevensp2to1", 3), ("camevensp4to1", 4), ("camevensp8to1", 5), ("camodd", 6), ("camoddsp1to1", 7), ("camoddsp2to1", 8), ("camoddsp4to1", 9), ("camoddsp8to1", 10), ("camspare", 11), ("nam", 12), ("scm", 13), ("cam16d", 14), ("cam16dspare", 15), ("unknown", 98), ("invalid", 99))

class CadExtAclCondition(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the condition of Extended ACLs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("na", 0), ("eq", 1), ("ne", 2), ("lt", 3), ("le", 4), ("gt", 5), ("ge", 6), ("range", 7))

class ServerType(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the INET services available on the SCM.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("telnet", 1), ("ftp", 2), ("snmp", 3), ("syslog", 4), ("radius", 5), ("tacacs", 6), ("other", 7))

class AccountingType(TextualConvention, Integer32):
    description = 'This TEXTUAL-CONVENTION describes the different types of accounting services.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("start-stop", 1), ("stop-only", 2))

class CadIfDirection(TextualConvention, Integer32):
    description = 'A direction of flow on an interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class CadIpPort(TextualConvention, Integer32):
    description = 'The port of an IP packet.\n\t The value -1 indicates that this field is not used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(-1, -1), )
class CadIpTos(TextualConvention, Integer32):
    description = 'The type-of-service of an IP packet.\n         The value 0 indicates that this field is not used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CadIpTosMask(TextualConvention, Integer32):
    description = 'The allowed type-of-service mask of an IP packet. 30 is used\n         when the 4 bit TOS is specified.  224 is used when the 3 bit\n         precedence is specified, and 254 is used when the entire 7\n         bit TOS is specified.  A value of 0 indicates that the TOS field \n         is not used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(224, 224), ValueRangeConstraint(254, 254), )
class CadProtocolType(TextualConvention, Integer32):
    description = 'The protocol type an IP packet (8 bits). 0 is IP, 1 is ICMP, \n         2 is IGMP, 6 is TCP 17 is UDP.  See RFC-1700 for complete list.\n         The value -1 indicates an invalid/unused protocol type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 255), ValueRangeConstraint(-1, -1), )
class CadTcpFlags(TextualConvention, Bits):
    description = 'The values available in the flags portion of the TCP header.'
    status = 'current'
    namedValues = NamedValues(("urg", 0), ("ack", 1), ("push", 2), ("rst", 3), ("syn", 4), ("fin", 5))

class CadAclType(TextualConvention, Integer32):
    description = 'The type of ACL this ACE is part of.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("std-access-list", 1), ("ext-access-list", 2), ("rate-limit-access-list", 3), ("remark", 4), ("ipv6-access-list", 5))

class CadAclString(TextualConvention, OctetString):
    description = 'The name of the ACL this ACE is part of.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class OUIAddress(TextualConvention, OctetString):
    description = "Represents the first three(3), most significant bytes of\n\t an 802 MAC address represented in the `canonical' order\n\t defined by IEEE 802.1a, i.e., as if it were transmitted\n\t least significant bit first, even though 802.5 (in contrast\n\t to other 802.x protocols) requires MAC addresses to be\n\t transmitted most significant bit first."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class SchedWeekDay(TextualConvention, Bits):
    description = 'The set of weekdays on which the scheduled action should\n         take place.  Setting multiple bits will include several\n         weekdays in the set of possible weekdays for this schedule.\n         Setting all bits will cause the scheduler to ignore the\n         weekday.'
    status = 'current'
    namedValues = NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6))

class SchedMonth(TextualConvention, Bits):
    description = 'The set of months during which the scheduled action should\n         take place.  Setting multiple bits will include several\n         months in the set of possible months for this schedule.\n\n         Setting all bits will cause the scheduler to ignore the\n         month.'
    status = 'current'
    namedValues = NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11))

class SchedDay(TextualConvention, Bits):
    description = "The set of days in a month on which a scheduled action\n         should take place.  There are two sets of bits one can\n         use to define the day within a month:\n\n         Enumerations starting with the letter 'd' indicate a\n         day in a month relative to the first day of a month.\n         The first day of the month can therefore be specified\n         by setting the bit d1(0) and d31(30) means the last\n         day of a month with 31 days.\n\n         Enumerations starting with the letter 'r' indicate a\n         day in a month in reverse order, relative to the last\n         day of a month.  The last day in the month can therefore\n         be specified by setting the bit r1(31) and r31(61) means\n         the first day of a month with 31 days.\n\n         Setting multiple bits will include several days in the set\n         of possible days for this schedule.  Setting all bits will\n         cause the scheduler to ignore the day within a month.\n\n         Setting all bits starting with the letter 'd' or the\n         letter 'r' will also cause the scheduler to ignore the\n         day within a month."
    status = 'current'
    namedValues = NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61))

class SchedHour(TextualConvention, Bits):
    description = 'The set of hours within a day during which the scheduled\n         action should take place.'
    status = 'current'
    namedValues = NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23))

class SchedMinute(TextualConvention, Bits):
    description = 'The set of minutes within an hour when the scheduled action\n         should take place.'
    status = 'current'
    namedValues = NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59))

class CadCpeDeviceTypes(TextualConvention, Bits):
    description = 'CPE Device types.'
    status = 'current'
    namedValues = NamedValues(("cable-modem", 0), ("cpe", 1), ("ps", 2), ("mta", 3), ("stb", 4), ("tea", 5), ("erouter", 6), ("dva", 7), ("sg", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("reserved31", 31))

mibBuilder.exportSymbols("CADANT-TC", SshProtocol=SshProtocol, ServerType=ServerType, CadBridgePortType=CadBridgePortType, SchedDay=SchedDay, OverloadStatus=OverloadStatus, SchedMonth=SchedMonth, CadTcpFlags=CadTcpFlags, CadDouble=CadDouble, PortDetectedMode=PortDetectedMode, ShelfId=ShelfId, AccountingType=AccountingType, SchedMinute=SchedMinute, SecondaryState=SecondaryState, CardType=CardType, UnknownState=UnknownState, CadAclType=CadAclType, CadCpeDeviceTypes=CadCpeDeviceTypes, CadIpTosMask=CadIpTosMask, VlanId=VlanId, PortMode=PortMode, CardSubId=CardSubId, FlowControlMode=FlowControlMode, FirmwareSource=FirmwareSource, MacPortId=MacPortId, AAAmethod=AAAmethod, SshService=SshService, OUIAddress=OUIAddress, EqActionType=EqActionType, SshCipher=SshCipher, cadTextualConventions=cadTextualConventions, CadExtAclCondition=CadExtAclCondition, CadAclString=CadAclString, CadIfDirection=CadIfDirection, PYSNMP_MODULE_ID=cadTextualConventions, MacChlPortType=MacChlPortType, CadIpTos=CadIpTos, CadProtocolType=CadProtocolType, CardId=CardId, CadIpPort=CadIpPort, SshMacAlg=SshMacAlg, SchedWeekDay=SchedWeekDay, PortType=PortType, DuplexStatus=DuplexStatus, FlowActivityState=FlowActivityState, AdminState=AdminState, SchedHour=SchedHour, MacPortIdWithInvalid=MacPortIdWithInvalid, CadBridgeGroupId=CadBridgeGroupId, InetAddressIPv4or6=InetAddressIPv4or6, PrimaryState=PrimaryState, DiskVolumeUsageLevel=DiskVolumeUsageLevel, LineType=LineType, PicType=PicType, CardSubType=CardSubType, PortId=PortId, SshCipherType=SshCipherType, SshAuthMethod=SshAuthMethod)
