#
# PySNMP MIB module COLUBRIS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-TC.my
# Produced by pysmi-1.1.8 at Mon Jan 17 18:27:14 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisModules, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, IpAddress, NotificationType, Integer32, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, iso, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "IpAddress", "NotificationType", "Integer32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 4, 1))
if mibBuilder.loadTexts: colubrisTextualConventions.setLastUpdated('200710300000Z')
if mibBuilder.loadTexts: colubrisTextualConventions.setOrganization('Colubris Networks, Inc.')
class ColubrisAuthenticationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("profile", 2))

class ColubrisUsersAuthenticationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("local", 1), ("profile", 2), ("localAndProfile", 3))

class ColubrisUsersAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ieee802dot1x", 2), ("html", 3))

class ColubrisNotificationEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class ColubrisProfileIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisProfileIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisServerIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ColubrisServerIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ColubrisSSID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class ColubrisSSIDOrNone(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class ColubrisSecurity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("none", 1), ("wep", 2), ("ieee802dot1x", 3), ("ieee802dot1xWithWep", 4), ("wpa", 5), ("wpaPsk", 6))

class ColubrisPriorityQueue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("low", 1), ("normal", 2), ("high", 3), ("veryHigh", 4))

class ColubrisDataRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unknown", 0), ("rateLowestAvailable", 1), ("rate1Meg", 2), ("rate2Meg", 3), ("rate5dot5Meg", 4), ("rate6Meg", 5), ("rate9Meg", 6), ("rate11Meg", 7), ("rate12Meg", 8), ("rate18Meg", 9), ("rate24Meg", 10), ("rate36Meg", 11), ("rate48Meg", 12), ("rate54Meg", 13), ("rateHighestAvailable", 14))

class ColubrisRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))
    namedValues = NamedValues(("cm6", 1), ("cm9", 2), ("sunfish", 3), ("mb82", 5))

mibBuilder.exportSymbols("COLUBRIS-TC", PYSNMP_MODULE_ID=colubrisTextualConventions, ColubrisNotificationEnable=ColubrisNotificationEnable, ColubrisProfileIndex=ColubrisProfileIndex, ColubrisServerIndexOrZero=ColubrisServerIndexOrZero, ColubrisSSID=ColubrisSSID, colubrisTextualConventions=colubrisTextualConventions, ColubrisServerIndex=ColubrisServerIndex, ColubrisPriorityQueue=ColubrisPriorityQueue, ColubrisRadioType=ColubrisRadioType, ColubrisAuthenticationMode=ColubrisAuthenticationMode, ColubrisUsersAuthenticationMode=ColubrisUsersAuthenticationMode, ColubrisSSIDOrNone=ColubrisSSIDOrNone, ColubrisDataRate=ColubrisDataRate, ColubrisProfileIndexOrZero=ColubrisProfileIndexOrZero, ColubrisSecurity=ColubrisSecurity, ColubrisUsersAuthenticationType=ColubrisUsersAuthenticationType)
