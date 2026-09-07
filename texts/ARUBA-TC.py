#
# PySNMP MIB module ARUBA-TC (http://snmplabs.com/pysmi)
# ASN.1 source ARUBA-TC
# Source digest sha256:db4eab5875fed7a4fe84a0b8b31fa2d56592a1362ac10d38e165c02491af856b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class ArubaEnableValue(TextualConvention, Integer32):
    description = 'Represents a Flag which is either Enabled or Disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ArubaFrameType(TextualConvention, Integer32):
    description = 'Represents the Frame type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("associateRequest", 0), ("associateResponse", 1), ("reassociateRequest", 2), ("reassociateResponse", 3), ("probeRequest", 4), ("probeResponse", 5), ("beacon", 8), ("atim", 9), ("disassociate", 10), ("auth", 11), ("deauth", 12))

class ArubaPhyType(TextualConvention, Integer32):
    description = " Represents the PHY-type of the access point or client.  Wired clients will\r\n\t\t  show 'wired' in user MIB entries.\r\n\t\t"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 3), ("dot11ag", 4), ("wired", 5))

class ArubaHTMode(TextualConvention, Integer32):
    description = ' Represents the HT status of the access point or client.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("none", 1), ("ht20", 2), ("ht40", 3), ("vht20", 4), ("vht40", 5), ("vht80", 6), ("vht160", 7), ("vht80plus80", 8), ("he20", 9), ("he40", 10), ("he80", 11), ("he160", 12), ("he80plus80", 13))

class ArubaHTExtChannel(TextualConvention, Integer32):
    description = ' Represents the extension channel offset relative to the current channel.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("above", 2), ("below", 3), ("eighty", 4), ("onesixty", 5))

class ArubaMonEncryptionType(TextualConvention, Integer32):
    description = ' Represents the encryption type supported by the access point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("open", 0), ("wep", 1), ("wpa", 2), ("wpa2", 3), ("wpa3", 4))

class ArubaMonEncryptionCipher(TextualConvention, Integer32):
    description = ' Represents the WPA encryption cipher supported by the access point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("aesccmp", 4), ("other", 5), ("gcm256", 6))

class ArubaMonAuthAlgorithm(TextualConvention, Integer32):
    description = ' Represents the WPA authentication algorithm supported by the access point.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("psk", 1), ("dot1x", 2), ("ftdot1x", 3), ("ftpsk", 4), ("dot1x256", 5), ("psk256", 6), ("tdls", 7), ("sae", 8), ("ftsae", 9), ("other", 10), ("suiteb", 11), ("owe", 12))

class ArubaSwitchRole(TextualConvention, Integer32):
    description = ' Represents the role of the controller'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("master", 1), ("local", 2), ("backupmaster", 3), ("standalone", 4))

class ArubaSupportStatus(TextualConvention, Integer32):
    description = ' Represents if a feature is supported or unsupported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unsupported", 1), ("supported", 2))

class ArubaActiveState(TextualConvention, Integer32):
    description = ' Represents if a feature is active or inactive.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class ArubaACLDomain(TextualConvention, Integer32):
    description = ' Represents both the source and destination to which an ACL rule will\r\n\t\t  be applied.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("alias", 1), ("any", 2), ("user", 3), ("host", 4), ("network", 5))

class ArubaACLNetworkServiceType(TextualConvention, Integer32):
    description = ' Represents the network service in an ACL Rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("alias", 1), ("any", 2), ("tcp", 3), ("udp", 4), ("protocol", 5))

class ArubaACLAction(TextualConvention, Integer32):
    description = ' Represents the Actions in an ACL rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("deny", 1), ("permit", 2), ("srcNAT", 3), ("dstNAT", 4), ("redirect", 5))

class ArubaDaysOfWeek(TextualConvention, Integer32):
    description = ' Represents the Actions in an ACL rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("sun", 1), ("mon", 2), ("tue", 3), ("wed", 4), ("thu", 5), ("fri", 6), ("sat", 7))

class ArubaAuthenticationMethods(TextualConvention, Integer32):
    description = ' Authentication Method.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 7, 15, 16, 17, 28, 255))
    namedValues = NamedValues(("none", 0), ("web", 1), ("mac", 2), ("vpn", 3), ("dot1x", 4), ("kerberos", 5), ("secureId", 7), ("pubcookie", 15), ("xSec", 16), ("xSecMachine", 17), ("via-vpn", 28), ("other", 255))

class ArubaSubAuthenticationMethods(TextualConvention, Integer32):
    description = ' Sub Authentication Method (e.g. EAP type).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("authPAP", 1), ("authCHAP", 2), ("authMSCHAP", 3), ("authMSCHAPv2", 4), ("eapTLS", 5), ("eapTTLS", 6), ("eapLEAP", 7), ("eapMD5", 8), ("eapPEAP", 9))

class ArubaEncryptionType(TextualConvention, Integer32):
    description = ' Encryption Method.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22))
    namedValues = NamedValues(("none", 0), ("static-wep", 1), ("dynamic-wep", 2), ("wpa-psk-tkip", 3), ("wpa-tkip", 4), ("wpa-psk-aes", 5), ("wpa-aes", 6), ("wpa2-psk-tkip", 7), ("wpa2-tkip", 8), ("wpa2-psk-aes", 9), ("wpa2-aes", 10), ("xSec", 11), ("bSec-128", 12), ("bSec-256", 13), ("aes-128-cmac", 14), ("unknown", 15), ("ft-psk", 16), ("ft-8021x", 17), ("wpa3-cnsa", 18), ("owe-aes", 20), ("wpa3-sae-aes", 21), ("wpa3-aes-gcmp-256", 22))

class ArubaUserForwardMode(TextualConvention, Integer32):
    description = ' User Forwarding Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("tunnel-encrypted", 0), ("bridge", 1), ("tunnel-decrypted", 2), ("split-tunnel", 3))

class ArubaRogueApType(TextualConvention, Integer32):
    description = 'Represents the Rogue AP Type. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("valid", 1), ("interfering", 2), ("unsecure", 3), ("dos", 4), ("unknown", 5), ("knownInterfering", 6), ("suspectedUnsecure", 7))

class ArubaAPMatchType(TextualConvention, Integer32):
    description = 'Represents the match type of a suspected rogue AP. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("configuredWiredMac", 1), ("ethernetWiredMac", 2), ("apWiredMac", 3), ("externalWiredMac", 4), ("manual", 5), ("baseBSSIDOverride", 6), ("mms", 7), ("ethernetGatewayWiredMac", 8), ("classificationDisabled", 9), ("apBSSID", 10), ("propagatedEthernetWiredMac", 11), ("apRule", 12), ("systemWiredMac", 13), ("systemGatewayMac", 14))

class ArubaAPMatchMethod(TextualConvention, Integer32):
    description = 'Represents the match method of a suspected rogue AP. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 0), ("exactMatch", 1), ("plusOneMatch", 2), ("minusOneMatch", 3), ("ouiMatch", 4))

class ArubaStationType(TextualConvention, Integer32):
    description = 'Represents the station type. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("valid", 1), ("interfering", 2), ("dos", 3))

class ArubaEncryptionMethods(TextualConvention, Bits):
    description = ' Represents the Actions in an ACL rule.'
    status = 'current'
    namedValues = NamedValues(("disabled", 0), ("static-wep", 1), ("dynamic-wep", 2), ("static-wpa", 3), ("dynamic-wpa", 4), ("wpa2-psk-aes", 5), ("wpa2-8021x-aes", 6), ("wpa2PreAuth", 7), ("xsec", 8), ("wpa-psk-aes", 9), ("wpa-aes", 10), ("wpa2-psk-tkip", 11), ("wpa2-8021x-tkip", 12), ("bSec-128", 13), ("bSec-256", 14), ("owe-aes", 16), ("wpa3-sae-aes", 17), ("wpa3-cnsa", 18), ("wpa3-aes-ccm-128", 19), ("mpsk-aes", 21), ("wpa3-aes-gcm-256", 22))

class ArubaHashAlgorithms(TextualConvention, Integer32):
    description = ' Represents the Actions in an ACL rule.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class ArubaVlanValidRange(TextualConvention, Integer32):
    description = 'Represents the Valid Vlan Id Range.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4095)

class ArubaPortMode(TextualConvention, Integer32):
    description = 'Represents the controller port mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("access", 1), ("dot1q", 2))

class ArubaDot1dState(TextualConvention, Integer32):
    description = 'Represents the controller port spanning tree state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 1), ("blocked", 2), ("listening", 3), ("learning", 4), ("forwarding", 5))

class ArubaAPDot1dState(TextualConvention, Integer32):
    description = 'Represents the AP port spanning tree state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notAvailable", 1), ("off", 2), ("disabled", 3), ("listening", 4), ("learning", 5), ("forwarding", 6), ("blocking", 7))

class ArubaPoeState(TextualConvention, Integer32):
    description = 'Represents the POE mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("enabledCisco", 3), ("notAvailable", 4))

class ArubaCardType(TextualConvention, Integer32):
    description = '\r\n\t\tType of the hardware module.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))
    namedValues = NamedValues(("lc1", 1), ("lc2", 2), ("sc1", 3), ("sc2", 4), ("sw2400", 5), ("sw800", 6), ("sw200", 7), ("m3mk1", 8), ("sw3200", 9), ("sw3400", 10), ("sw3600", 11), ("sw650", 12), ("sw651", 13), ("reserved1", 14), ("reserved2", 15), ("sw620", 16), ("sw7210", 17), ("sw7220", 18), ("sw7240", 19), ("sw3500", 20), ("sw2500", 21), ("sw1500", 22), ("sw7010", 23), ("sw7005", 24), ("sw7030", 25), ("sw7205", 26), ("sw7024", 27), ("sw7024xm", 28))

class ArubaESIServerMode(TextualConvention, Integer32):
    description = '\r\n\t\tThe mode of the ESI server.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("bridged", 1), ("routed", 2), ("nat", 3))

class ArubaESIServerStatus(TextualConvention, Integer32):
    description = '\r\n\t\tThe status of the ESI server.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ArubaIfType(TextualConvention, Integer32):
    description = '\r\n\t\tThe type of interface referred to by the value of ifIndex.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("tunnel", 3), ("loopback", 4))

class ArubaVoipProtocolType(TextualConvention, Integer32):
    description = '\r\n\t\tThe type of VoIP protocols supported.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 9, 11, 13, 15))
    namedValues = NamedValues(("sccp", 1), ("svp", 2), ("vocera", 3), ("sip", 9), ("ua", 11), ("h323", 13), ("unknown", 15))

class ArubaAccessPointMode(TextualConvention, Integer32):
    description = '\r\n\t\tThe mode of the access point.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("airMonitor", 1), ("accessPoint", 2), ("accessPointAndMonitor", 3), ("meshPortal", 4), ("meshPoint", 5), ("rfprotectSensor", 6), ("spectrumSensor", 7))

class ArubaAuthServerType(TextualConvention, Integer32):
    description = '\r\n\t\tThe type of the auth server.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("internaldb", 1), ("radius", 2), ("ldap", 3), ("kerberos", 4), ("tacacs", 5))

class ArubaAddressType(TextualConvention, Integer32):
    description = '\r\n\t\tAddress Type.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("srcAddress", 1), ("dstAddress", 2), ("bssid", 3))

class ArubaBlackListReason(TextualConvention, Integer32):
    description = '\r\n\t\tBlack List Reason.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 100))
    namedValues = NamedValues(("userDefined", 1), ("mitmAttack", 2), ("authFailure", 3), ("pingFlood", 4), ("sessionFlood", 5), ("synFlood", 6), ("sessionBlacklist", 7), ("ipSpoofing", 8), ("esiBlacklist", 9), ("other", 100))

class ArubaDBType(TextualConvention, Integer32):
    description = '\r\n\t\tDataBase Type.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mssql", 1), ("mysql", 2))

class ArubaVrrpState(TextualConvention, Integer32):
    description = '\r\n\t\tDataBase Type.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("initialize", 1), ("backup", 2), ("master", 3))

class ArubaOperStateValue(TextualConvention, Integer32):
    description = 'Represents Operational state of an interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3))

class ArubaAntennaSetting(TextualConvention, Integer32):
    description = 'Represents the status of the external antenna.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notPresent", 1), ("enabled", 2), ("disabled", 3))

class ArubaAPStatus(TextualConvention, Integer32):
    description = '\r\n\t\tThe status of the access point.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class ArubaPortSpeed(TextualConvention, Integer32):
    description = '\r\n\t\tPort Speed.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("speed10Mbps", 1), ("speed100Mbps", 2), ("speed1000Mbps", 3), ("speedAuto", 4), ("speed10Gbps", 5), ("speed2Point5Gbps", 6), ("speed5Gbps", 7), ("speed40Gbps", 8))

class ArubaPortDuplex(TextualConvention, Integer32):
    description = '\r\n\t\tPort Duplexity.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("half", 1), ("full", 2), ("auto", 3))

class ArubaPortType(TextualConvention, Integer32):
    description = '\r\n\t\tPort Type.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fastethernet", 1), ("gigabitethernet", 2), ("xgigabitethernet", 3), ("twogigabitethernet", 4), ("fivegigabitethernet", 5))

class ArubaEnet1Mode(TextualConvention, Integer32):
    description = ' Represents the Mode of the Ethernet port on the Access Point'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("activeStandby", 1), ("tunnel", 2), ("bridge", 3), ("notApplicable", 4), ("split", 5))

class ArubaUnprovisionedStatus(TextualConvention, Integer32):
    description = ' Represents whether the AP is provisioned or not.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

class ArubaMonitorMode(TextualConvention, Integer32):
    description = ' Represents whether the AP has any radios dedicated to monitoring.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("all", 1), ("none", 2), ("mixed", 3))

class ArubaConfigurationState(TextualConvention, Integer32):
    description = 'Configuration Transfer Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("error", 2))

class ArubaConfigurationChangeType(TextualConvention, Integer32):
    description = 'Configuration Change Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("create", 1), ("delete", 2), ("modify", 3))

class ArubaCallStates(TextualConvention, Integer32):
    description = '\r\n\t\tThe Call state.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("idle", 0), ("initiated", 1), ("connecting", 2), ("delivered", 3), ("connected", 4), ("offered", 5), ("alerting", 6), ("releasing", 7), ("cancelling", 8), ("challenging", 9), ("transient", 10), ("blockwait", 11), ("succ", 12), ("fail", 13), ("aborted", 14), ("blocked", 15))

class ArubaVoipProtocol(TextualConvention, Integer32):
    description = '\r\n\t\t  VoIP protocol used\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 9, 11, 13))
    namedValues = NamedValues(("sccp", 1), ("svp", 2), ("vocera", 3), ("sip", 9), ("ua", 11), ("h323", 13))

class ArubaVoipRegState(TextualConvention, Integer32):
    description = '\r\n\t\t  VoIP registered state\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("registering", 1), ("unregistering", 2), ("challenge", 3), ("registered", 4), ("unregistered", 5))

class ArubaVoiceCdrDirection(TextualConvention, Integer32):
    description = '\r\n\t\t  VoIP CDR direction\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("og", 0), ("ic", 1))

class ArubaVoiceCacBit(TextualConvention, Bits):
    description = '\r\n\t\t\tVoice CAC bit flags\r\n\t\t'
    status = 'current'
    namedValues = NamedValues(("cacActiveLoadBalancing", 0), ("cacHighCapThresholdReached", 1), ("cacHandRsrvThresholdReached", 2), ("cacPeakCapacityReached", 3))

class ArubaMeshRole(TextualConvention, Integer32):
    description = '\r\n\t\t  Mesh role\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nonmesh", 0), ("point", 1), ("portal", 2))

class ArubaHTRate(TextualConvention, Integer32):
    description = 'Represents HT rate'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("unknown", 0), ("ht6dot5", 1), ("ht13", 2), ("ht13dot5", 3), ("ht15", 4), ("ht19dot5", 5), ("ht26", 6), ("ht27", 7), ("ht30", 8), ("ht39", 9), ("ht40dot5", 10), ("ht45", 11), ("ht52", 12), ("ht54", 13), ("ht58dot5", 14), ("ht60", 15), ("ht65", 16), ("ht78", 17), ("ht81", 18), ("ht90", 19), ("ht104", 20), ("ht108", 21), ("ht117", 22), ("ht120", 23), ("ht121dot5", 24), ("ht130", 25), ("ht135", 26), ("ht150", 27), ("ht162", 28), ("ht180", 29), ("ht216", 30), ("ht240", 31), ("ht243", 32), ("ht270", 33), ("ht300", 34))

class ArubaARMChangeReason(TextualConvention, Integer32):
    description = '\r\n\t\tThe reason for ARM or AirMatch based change.\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("radarDetected", 1), ("radarCleared", 2), ("txHang", 3), ("txHangClear", 4), ("fortyMhzIntol", 5), ("cancel40mhzIntol", 6), ("fortyMhzAlign", 7), ("armInterference", 8), ("armInvalidCh", 9), ("armErrorThresh", 10), ("armNoiseThresh", 11), ("armEmptyCh", 12), ("armRogueCont", 13), ("armDecreasePower", 14), ("armIncreasePower", 15), ("armTurnOffRadio", 16), ("armTurnOnRadio", 17), ("armChannelQualityThresh", 18), ("armDynamicBW", 19), ("armInterferenceCCA", 20), ("airmatchNoise", 21), ("airmatchSolver", 22), ("airmatchFreeze", 23), ("airmatchUnfreeze", 24), ("random", 25), ("airmatchInit", 26), ("unknown", 27), ("airmatchNoiseCleared", 28), ("airmatchRogueCont", 29))

class ArubaAPMasterStatus(TextualConvention, Integer32):
    description = '\r\n\t\t  AP status as seen by the master controller\r\n          (used to indicate a status change).\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("move", 3))

class ArubaDot3azStatus(TextualConvention, Bits):
    description = ' Represents the state of Energy Efficient Ethernet (802.3az).'
    status = 'current'
    namedValues = NamedValues(("disabled", 0), ("unsupported", 1), ("eee100BaseTX", 2), ("eee1000BaseT", 3), ("eee10GBaseT", 4), ("eee1000BaseKX", 5), ("eee10GBaseKX4", 6), ("eee10GBaseKR", 7))

class ArubaDot3bzStatus(TextualConvention, Integer32):
    description = ' Represents the state of 802.3bz.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unsupported", 0), ("no", 1), ("yes", 2))

class ArubaThresholdResourceType(TextualConvention, Integer32):
    description = ' Represents the Threshold Resource Types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dataPathCpu", 0), ("controlPathCpu", 1), ("controlPathMemory", 2), ("totalTunnelCapacity", 3), ("userCapacity", 4), ("noofAps", 5), ("noofLocals", 6), ("noofVaps", 7))

class ArubaStackState(TextualConvention, Integer32):
    description = 'The state of the stack element in the stack.\r\n\r\n        primary   - the stack element is in primary state.\r\n        secondary - the stack element is in secondary state.\r\n        linecard  - the stack element is in linecard state.\r\n        away      - the stack element is in inactive state.\r\n\r\n        primary, secondary and linecard implies active state of the stack\r\n        element.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primary", 1), ("secondary", 2), ("linecard", 3), ("away", 4))

class ArubaStackChangeEvent(TextualConvention, Integer32):
    description = 'Used to specify the event which caused change in topology in stack.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("primarySlotChanged", 2), ("secondarySlotChanged", 3), ("lineCardSlotChanged", 4), ("roleChanged", 5), ("priorityChanged", 6), ("versionMismatch", 7), ("slotExceeded", 8))

class ArubaStackIfTopoJoined(TextualConvention, Integer32):
    description = 'Used to specify whether an interface has joined the stacking\r\n        topology or left the topology.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("connected", 1), ("disconnected", 2))

class InterfaceIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each interface or\r\n            interface sub-layer in the managed system.  It is\r\n            recommended that values are assigned contiguously starting\r\n            from 1.  The value for each interface sub-layer must remain\r\n            constant at least from one re-initialization of the entity's\r\n            network management system to the next re-initialization."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ArubaIfState(TextualConvention, Integer32):
    description = 'Used to specify the state of an interface.\r\n\r\n        linkUp   - Operational state of this interface is up.\r\n        linkDown - Operational state of this interface is down.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("linkUp", 1), ("linkDown", 2))

class ArubaIfStateChangeReason(TextualConvention, Integer32):
    description = "Used to specify the reason for interface state change.\r\n\r\n        admin       - User has explicitly issued 'shutdown' or 'no shutdown'\r\n                      configuration from CLI on this interface.\r\n        loopProtect - If ifState of an interface changes to linkDown, then\r\n                      it is used to specify that a loop has been detected on\r\n                      this interface by loop protect mechanism.\r\n                      If ifState of an interface changes to linkUp, then\r\n                      it is used to specify that loop-protect error has been\r\n                      cleared out on this interface through port auto-recovery\r\n                      mechanism or through explicit clear error-recovery\r\n                      command.\r\n        macLimit    - If ifState of an interface changes to linkDown, then\r\n                      it is used to specify that number of learnt MACs on this\r\n                      interface exceeds the limit configured.\r\n                      If ifState of an interface changes to linkUp, then it is\r\n                      used to specify that mac-limit error has been cleared out\r\n                      on this interface through port auto-recovery mechanism or\r\n                      through explicit clear error-recovery command.\r\n        raGuard     - If ifState of an interface changes to linkDown, then it\r\n                      is used to specify that invalid router advertisement has\r\n                      been identified on this interface, resulting shutting\r\n                      down of this interface.\r\n                      If ifState of an interface changes to linkUp, then it is\r\n                      used to specify that raGuard error has been cleared out on\r\n                      this interface through port auto-recovery mechanism or\r\n                      through explicit clear error-recovery command.\r\n        bpduGuard   - If ifState of an interface changes to linkDown, then it\r\n                      is used to specify that BPDU is received on this interface\r\n                      resulting shutting down of this interface.\r\n                      If ifState of an interface changes to linkUp, then it is\r\n                      used to specify that BPDU Guard error has been cleared out\r\n                      on this interface through port auto-recovery mechanism or\r\n                      through explicit clear error-recovery command."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("admin", 1), ("loopProtect", 2), ("macLimit", 3), ("raGuard", 4), ("bpduGuard", 5))

class ArubaAPUplinkType(TextualConvention, Integer32):
    description = '\r\n          AP uplink type\r\n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ethernet", 1), ("usb", 2), ("pppoe", 3), ("wifi", 4))

class ArubaAPUplinkChangeReason(TextualConvention, Integer32):
    description = 'Used to specify the reason for AP uplink change.\r\n\r\n        linkFailure - The uplink went down\r\n        vpnFailure  - VPN tunnel could not be sustained using the uplink\r\n        preemption  - The uplink was pre-empted by a higher-priority uplink'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("linkFailure", 1), ("vpnFailure", 2), ("preemption", 3))

class ArubaPortalServerDownReason(TextualConvention, Integer32):
    description = 'Used to specify the reason for Portal server down.\r\n\r\n        connectFail - Connect Portal server fail'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("connectFail", 1))

class ArubaHaRole(TextualConvention, Integer32):
    description = ' Represents the HA role of the Aruba controller'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("dual", 0), ("active", 1), ("standby", 2), ("disabled", 3))

class ArubaHaConnectivityStatus(TextualConvention, Integer32):
    description = ' Represents the HA standby connectivity status of the Access Point'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("haSuccess", 0), ("haNetUnreach", 1), ("haCpUnreach", 2), ("haImageMissMatch", 3), ("haApDenied", 4), ("haHbtFailure", 5), ("haInvalidHelloResponse", 6), ("haStandbyTunnelDown", 7))

class ArubaFlexRadioMode(TextualConvention, Integer32):
    description = '\r\n\t\t  Flex Radio Operating Mode\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("single2GHzBand", 0), ("single5GHzBand", 1), ("dual2GHzplus5GHzBand", 2), ("unknown", 3), ("notApplicable", 4))

class ArubaDual5GMode(TextualConvention, Integer32):
    description = '\r\n\t\t  Dual 5GHz Operating Mode\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("unknown", 2), ("notApplicable", 3))

class ArubaSplit5GMode(TextualConvention, Integer32):
    description = '\r\n\t\t  Split 5GHz Operating Mode\r\n\t\t'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("unknown", 2), ("notApplicable", 3))

mibBuilder.exportSymbols("ARUBA-TC", ArubaACLAction=ArubaACLAction, ArubaACLDomain=ArubaACLDomain, ArubaACLNetworkServiceType=ArubaACLNetworkServiceType, ArubaAPDot1dState=ArubaAPDot1dState, ArubaAPMasterStatus=ArubaAPMasterStatus, ArubaAPMatchMethod=ArubaAPMatchMethod, ArubaAPMatchType=ArubaAPMatchType, ArubaAPStatus=ArubaAPStatus, ArubaAPUplinkChangeReason=ArubaAPUplinkChangeReason, ArubaAPUplinkType=ArubaAPUplinkType, ArubaARMChangeReason=ArubaARMChangeReason, ArubaAccessPointMode=ArubaAccessPointMode, ArubaActiveState=ArubaActiveState, ArubaAddressType=ArubaAddressType, ArubaAntennaSetting=ArubaAntennaSetting, ArubaAuthServerType=ArubaAuthServerType, ArubaAuthenticationMethods=ArubaAuthenticationMethods, ArubaBlackListReason=ArubaBlackListReason, ArubaCallStates=ArubaCallStates, ArubaCardType=ArubaCardType, ArubaConfigurationChangeType=ArubaConfigurationChangeType, ArubaConfigurationState=ArubaConfigurationState, ArubaDBType=ArubaDBType, ArubaDaysOfWeek=ArubaDaysOfWeek, ArubaDot1dState=ArubaDot1dState, ArubaDot3azStatus=ArubaDot3azStatus, ArubaDot3bzStatus=ArubaDot3bzStatus, ArubaDual5GMode=ArubaDual5GMode, ArubaESIServerMode=ArubaESIServerMode, ArubaESIServerStatus=ArubaESIServerStatus, ArubaEnableValue=ArubaEnableValue, ArubaEncryptionMethods=ArubaEncryptionMethods, ArubaEncryptionType=ArubaEncryptionType, ArubaEnet1Mode=ArubaEnet1Mode, ArubaFlexRadioMode=ArubaFlexRadioMode, ArubaFrameType=ArubaFrameType, ArubaHTExtChannel=ArubaHTExtChannel, ArubaHTMode=ArubaHTMode, ArubaHTRate=ArubaHTRate, ArubaHaConnectivityStatus=ArubaHaConnectivityStatus, ArubaHaRole=ArubaHaRole, ArubaHashAlgorithms=ArubaHashAlgorithms, ArubaIfState=ArubaIfState, ArubaIfStateChangeReason=ArubaIfStateChangeReason, ArubaIfType=ArubaIfType, ArubaMeshRole=ArubaMeshRole, ArubaMonAuthAlgorithm=ArubaMonAuthAlgorithm, ArubaMonEncryptionCipher=ArubaMonEncryptionCipher, ArubaMonEncryptionType=ArubaMonEncryptionType, ArubaMonitorMode=ArubaMonitorMode, ArubaOperStateValue=ArubaOperStateValue, ArubaPhyType=ArubaPhyType, ArubaPoeState=ArubaPoeState, ArubaPortDuplex=ArubaPortDuplex, ArubaPortMode=ArubaPortMode, ArubaPortSpeed=ArubaPortSpeed, ArubaPortType=ArubaPortType, ArubaPortalServerDownReason=ArubaPortalServerDownReason, ArubaRogueApType=ArubaRogueApType, ArubaSplit5GMode=ArubaSplit5GMode, ArubaStackChangeEvent=ArubaStackChangeEvent, ArubaStackIfTopoJoined=ArubaStackIfTopoJoined, ArubaStackState=ArubaStackState, ArubaStationType=ArubaStationType, ArubaSubAuthenticationMethods=ArubaSubAuthenticationMethods, ArubaSupportStatus=ArubaSupportStatus, ArubaSwitchRole=ArubaSwitchRole, ArubaThresholdResourceType=ArubaThresholdResourceType, ArubaUnprovisionedStatus=ArubaUnprovisionedStatus, ArubaUserForwardMode=ArubaUserForwardMode, ArubaVlanValidRange=ArubaVlanValidRange, ArubaVoiceCacBit=ArubaVoiceCacBit, ArubaVoiceCdrDirection=ArubaVoiceCdrDirection, ArubaVoipProtocol=ArubaVoipProtocol, ArubaVoipProtocolType=ArubaVoipProtocolType, ArubaVoipRegState=ArubaVoipRegState, ArubaVrrpState=ArubaVrrpState, InterfaceIndex=InterfaceIndex)
