#
# PySNMP MIB module COLUBRIS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-TC.my
# Produced by pysmi-1.1.12 at Tue Jun  4 08:07:11 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
colubrisModules, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, TimeTicks, ObjectIdentity, ModuleIdentity, Gauge32, MibIdentifier, Counter64, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Gauge32", "MibIdentifier", "Counter64", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
colubrisTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 1))
if mibBuilder.loadTexts: colubrisTextualConventions.setLastUpdated('200710300000Z')
if mibBuilder.loadTexts: colubrisTextualConventions.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisTextualConventions.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisTextualConventions.setDescription('This module defines the Textual Conventions used in\n                    Colubris Networks enterprise MIBs.')
class ColubrisAuthenticationMode(TextualConvention, Integer32):
    description = 'Specifies the authentication mode to be used.\n\n                  local: The authentication is done locally from the\n                         device local database information.\n\n                  profile: An AAA profile is used in order to retrieve\n                           the authentication parameters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("profile", 2))

class ColubrisUsersAuthenticationMode(TextualConvention, Integer32):
    description = 'Specifies the authentication mode to be used.\n\n                   none: Users are not allowed to login.\n\n                   local: The authentication is done locally from the\n                          device local database information.\n\n                   profile: An AAA profile is used in order to retrieve\n                            the authentication parameters.\n\n                   localAndProfile: The authentication is done locally\n                                    first. If it fails an AAA profile\n                                    is used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("local", 1), ("profile", 2), ("localAndProfile", 3))

class ColubrisUsersAuthenticationType(TextualConvention, Integer32):
    description = 'Specifies the authentication type to be used.\n\n                   mac: Users authenticated using their MAC addresses.\n\n\t\t       ieee802dot1x: Users authenticated through 802.1x.\n\n\t\t       html: Users authenticated with html.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ieee802dot1x", 2), ("html", 3))

class ColubrisNotificationEnable(TextualConvention, Integer32):
    description = 'Specifies the generation of notification traps.\n                 \n                   enable: Enable the generation of the associated\n                           notification.\n\n                   disable: Disables the generation of the associated\n                            notification'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class ColubrisProfileIndex(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the AAA profile table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisProfileIndexOrZero(TextualConvention, Integer32):
    description = 'A profile index refers to an entry in the AAA profile table.\n                 When the special value Zero is specified, no AAA\n                 server profile is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisServerIndex(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the AAA server table.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisServerIndexOrZero(TextualConvention, Integer32):
    description = 'A server index refers to an entry in the AAA server table.\n                 When the special value Zero is specified, no AAA\n                 server is selected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisSSID(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined\n                 here and used throughout the Colubris proprietary MIBs. This\n\t\t specific textual convention is used for inputing SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class ColubrisSSIDOrNone(TextualConvention, OctetString):
    description = 'A generic service set identifier (SSID) convention is defined\n                 here and used throughout the Colubris proprietary MIBs. This\n\t\t specific textual convention is used when displaying SSIDs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class ColubrisSecurity(TextualConvention, Integer32):
    description = "An enumeration of the different Security modes allowed\n                 in the Colubris products.\n\n                 NOTE: 'unknown'- Could not identify the protection mode.\n                       'none'   - No wireless protection.\n                       'wep'    - WEP (static keys).\n                       'ieee802dot1x' - 802.1x no encryption.\n                       'ieee802dot1xWithWep' - 802.1x + WEP (dynamic keys).\n                       'wpa'    - 802.1x + TKIP + Key source AAA profile.\n                       'wpaPsk' - 802.1x + TKIP + Key Source Pre-Shared Key."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("none", 1), ("wep", 2), ("ieee802dot1x", 3), ("ieee802dot1xWithWep", 4), ("wpa", 5), ("wpaPsk", 6))

class ColubrisPriorityQueue(TextualConvention, Integer32):
    description = 'An enumeration of the different queues supported in the\n                 QOS and Bandwidth control feature of the Colubris products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("low", 1), ("normal", 2), ("high", 3), ("veryHigh", 4))

class ColubrisDataRate(TextualConvention, Integer32):
    description = 'An enumeration of the different data rates supported on a per\n                 VAP basis.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("rateLowestAvailable", 1), ("rate1Meg", 2), ("rate2Meg", 3), ("rate5dot5Meg", 4), ("rate6Meg", 5), ("rate9Meg", 6), ("rate11Meg", 7), ("rate12Meg", 8), ("rate18Meg", 9), ("rate24Meg", 10), ("rate36Meg", 11), ("rate48Meg", 12), ("rate54Meg", 13), ("rateHighestAvailable", 14))

class ColubrisRadioType(TextualConvention, Integer32):
    description = 'An enumeration of the different radio types used in\n                 the Colubris products.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))
    namedValues = NamedValues(("cm6", 1), ("cm9", 2), ("sunfish", 3), ("mb82", 5))

mibBuilder.exportSymbols("COLUBRIS-TC", ColubrisDataRate=ColubrisDataRate, ColubrisAuthenticationMode=ColubrisAuthenticationMode, ColubrisSSIDOrNone=ColubrisSSIDOrNone, ColubrisServerIndex=ColubrisServerIndex, ColubrisUsersAuthenticationType=ColubrisUsersAuthenticationType, ColubrisSSID=ColubrisSSID, ColubrisRadioType=ColubrisRadioType, ColubrisUsersAuthenticationMode=ColubrisUsersAuthenticationMode, ColubrisProfileIndexOrZero=ColubrisProfileIndexOrZero, ColubrisProfileIndex=ColubrisProfileIndex, colubrisTextualConventions=colubrisTextualConventions, ColubrisPriorityQueue=ColubrisPriorityQueue, ColubrisNotificationEnable=ColubrisNotificationEnable, ColubrisServerIndexOrZero=ColubrisServerIndexOrZero, ColubrisSecurity=ColubrisSecurity, PYSNMP_MODULE_ID=colubrisTextualConventions)
