#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB
# Source digest sha256:e98492f50487c4deb7bbe035a569e9238dfa5435c661b9834467bffe75758db1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappDot11ClientCCXTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 611))
ciscoLwappDot11ClientCCXTextualConventions.setRevisions(('2007-03-22 00:00', '2007-02-22 00:00', '2007-02-19 00:00', '2007-01-30 00:00',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setLastUpdated('2007-03-22 00:00')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setOrganization('Cisco Systems Inc.')
class CiscoLwappDot11ClientReqStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("initiate", 1), ("inProgress", 2), ("success", 3), ("failure", 4), ("requestNotProcessedByClient", 5))

class CiscoLwappDot11ClientSSId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CiscoLwappDot11ClientAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("none", 0), ("preSharedKey", 1), ("eap", 2), ("unknown", 255))

class CiscoLwappDot11ClientEAPMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("leap", 0), ("eapFast", 1), ("eapTls", 2), ("eapTtls", 3), ("peap0EapMschap2", 4), ("peap1EapGtc", 5), ("eapMd5", 6), ("eapSim", 7), ("preSharedKey", 8), ("unknown", 255))

class CiscoLwappDot11ClientKeyMgmtMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 255))
    namedValues = NamedValues(("none", 0), ("staticWep", 1), ("dynamicWep", 2), ("wpa", 3), ("wpaCckm", 4), ("wpa2", 5), ("wpa2Cckm", 6), ("cckm", 7), ("unknown", 255))

class CiscoLwappDot11ClientEncryptionMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("ckip", 4), ("aesCcmp", 5), ("unknown", 255))

class CiscoLwappDot11ClientCredentialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("localSaved", 0), ("manuallyPrompted", 1), ("hostOsLogin", 2), ("unknown", 255))

class CiscoLwappDot11ClientPowerSaveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 255))
    namedValues = NamedValues(("awake", 0), ("normal", 1), ("maxPower", 2), ("uApsd", 3), ("sApsd", 4), ("unknown", 255))

class CiscoLwappDot11ClientTxPowerMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("automatic", 1))

class CiscoLwappDot11ClientRadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unused", 0), ("fhss", 1), ("dsss", 2), ("irBaseband", 3), ("oFdm", 4), ("highRateDsss", 5), ("erp", 6), ("draft11n2point4Ghz", 7), ("draft11n5Ghz", 8))

class CiscoLwappDot11ClientDataRates(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("mhz1", 0), ("mhz2", 1), ("mhz5point5", 2), ("mhz6", 3), ("mhz9", 4), ("mhz11", 5), ("mhz12", 6), ("mhz18", 7), ("mhz24", 8), ("mhz36", 9), ("mhz48", 10), ("mhz54", 11))

mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB", CiscoLwappDot11ClientAuthMethod=CiscoLwappDot11ClientAuthMethod, CiscoLwappDot11ClientCredentialType=CiscoLwappDot11ClientCredentialType, CiscoLwappDot11ClientDataRates=CiscoLwappDot11ClientDataRates, CiscoLwappDot11ClientEAPMethod=CiscoLwappDot11ClientEAPMethod, CiscoLwappDot11ClientEncryptionMethod=CiscoLwappDot11ClientEncryptionMethod, CiscoLwappDot11ClientKeyMgmtMethod=CiscoLwappDot11ClientKeyMgmtMethod, CiscoLwappDot11ClientPowerSaveMode=CiscoLwappDot11ClientPowerSaveMode, CiscoLwappDot11ClientRadioType=CiscoLwappDot11ClientRadioType, CiscoLwappDot11ClientReqStatus=CiscoLwappDot11ClientReqStatus, CiscoLwappDot11ClientSSId=CiscoLwappDot11ClientSSId, CiscoLwappDot11ClientTxPowerMode=CiscoLwappDot11ClientTxPowerMode, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCCXTextualConventions, ciscoLwappDot11ClientCCXTextualConventions=ciscoLwappDot11ClientCCXTextualConventions)
