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

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setRevisionsDescriptions(('Added 2 more radio types to CiscoLwappDot11ClientRadioType.', 'Reverted some of the enum names to be in line with the CCXV5\n        spec.', 'Incorporated review comments.', 'Initial version of this  mib module.',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setLastUpdated('2007-03-22 00:00')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setContactInfo('Cisco Systems,\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientCCXTextualConventions.setDescription("This module defines the textual conventions used\n        throughout the Cisco enterprise MIBs designed for\n        implementation on Central Controllers (CC) that\n        terminate the Light Weight Access Point Protocol\n        tunnel from Light-weight LWAPP Access Points, \n        specifically for the functions of the Cisco Client \n        Extensions (CCX) program.\n\n        This MIB provides textual conventions used in the\n        configuration and status information mibs\n        about the CCX clients that the controller is aware of.\n\n\n                 GLOSSARY\n\n        Light Weight Access Point Protocol ( LWAPP )\n\n        This is a generic protocol that defines the\n        communication between the Access Points and the\n        Central Controller.\n\n        Mobile Node ( MN )\n\n        A roaming 802.11 wireless device in a wireless\n        network associated with an access point. Mobile Node,\n        Mobile Station(Ms) and client are used\n        interchangeably.\n\n        Cisco Client eXtentions (CCX)\n        The Cisco Client Extensions (CCX) Program is a \n        program of working through silicon providers to \n        embed Cisco client technology in wireless client \n        reference designs, and to promote compliant and \n        interoperable third-party clients with Cisco's \n        infrastructure, thus further driving wireless adoption \n        in the market.  \n\n        Extensible Authentication Protocol (EAP) \n\n        The Extensible Authentication Protocol (EAP) is an \n        Internet Engineering Task Force (IETF) standard that \n        provides an infrastructure for network access clients and \n        authentication servers to host plug-in modules for current\n        and future authentication methods and technologies.\n\n        Wired Equivalent Privacy (WEP) \n\n        A security method defined by 802.11. WEP uses a  \n        symmetric key stream cipher called RC4 to encrypt the data\n        packets. \n\n\n\n        REFERENCE\n\n        [1] Part 11 Wireless LAN Medium Access Control ( MAC )\n        and Physical Layer ( PHY ) Specifications.\n\n        [2] Draft-obara-capwap-lwapp-00.txt, IETF Light \n        Weight Access Point Protocol. \n\n        [3] Cisco Compatible Extensions for WLAN Devices\n        Version 5.0.11")
class CiscoLwappDot11ClientReqStatus(TextualConvention, Integer32):
    description = 'This field indicates the status of current request.The values\n        used can be one of the following:\n\n            initiate - this will be used to trigger a request to get \n            some parameters from a CCX client.\n\n            inProgress - this indicates that the request to get the \n            details from the client is still in progress.\n\n            success - indicates that the query was executed \n            successfully. \n\n            failed -  this indicates that the request to get some \n            parameters from a CCX client failed.\n\n            requestNotProcessedByClient - indicates that the CCX client\n            did not honour this request.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("initiate", 1), ("inProgress", 2), ("success", 3), ("failure", 4), ("requestNotProcessedByClient", 5))

class CiscoLwappDot11ClientSSId(TextualConvention, OctetString):
    description = 'This represents the Service Set Identifier assigned\n        to WLAN.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class CiscoLwappDot11ClientAuthMethod(TextualConvention, Integer32):
    description = 'This is the authentication method used by the client.\n        The possible values are:\n           none - this indicates that no authentication method is\n           used\n\n           preSharedKey - this refers to the method of using pre\n           shared key for authentication\n\n           eap - this is Extensible Authentication Protocol \n\n           unknown - this indicates an authentication protocol other\n           than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("none", 0), ("preSharedKey", 1), ("eap", 2), ("unknown", 255))

class CiscoLwappDot11ClientEAPMethod(TextualConvention, Integer32):
    description = 'This identifies the Extensible Authentication Protocol(EAP)\n        method used. The possible values are:\n\n           leap - this is Lightweight Extensible Authentication \n           Protocol\n\n           eapFast - this is Extensible Authentication \n           Protocol with Flexible Authentication via Secure Tunneling\n\n           eapTls - this is Extensible Authentication\n           Protocol with Transport Layer Security\n\n           eapTtls - this is Extensible Authentication Protocol with\n           Tunneled Transport Layer Security\n\n           peap0EapMschap2 - this refers to Protected Extensible \n           Authentication Protocol Version 0 with Microsoft \n           Challenge Handshake Authentication Protocol version 2\n\n           peap1EapGtc - this refers to Protected Extensible \n           Authentication Protocol Version 1 with Generic Token Card\n\n           eapMd5 - this is Extensible Authentication Protocol with\n           Message-Digest algorithm 5\n\n           eapSim - this is Extensible Authentication Protocol using \n           the Global System for Mobile Communications (GSM) \n           Subscriber Identity Module (SIM)\n\n           preSharedKey - this refers to the method of using pre\n           shared key for authentication\n\n           unknown - this indicates an EAP method other\n           than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 255))
    namedValues = NamedValues(("leap", 0), ("eapFast", 1), ("eapTls", 2), ("eapTtls", 3), ("peap0EapMschap2", 4), ("peap1EapGtc", 5), ("eapMd5", 6), ("eapSim", 7), ("preSharedKey", 8), ("unknown", 255))

class CiscoLwappDot11ClientKeyMgmtMethod(TextualConvention, Integer32):
    description = 'This is the key management method used by the client.\n        The possible values are:\n\n           staticWep - this is Wired Equivalent Privacy with a static\n           key defined\n\n           dynamicWep - this is Wired Equivalent Privacy with a \n           dynamic key\n\n           wpa - this indicates wifi protected access\n\n           wpaCckm - this is wifi protected access with \n           Cisco Centralized Key Management\n\n           wpa2 - this indicates version 2 of wifi protected access\n\n           wpa2Cckm - this is wifi protected access  \n           version 2 with Cisco Centralized Key Management\n\n           cckm - this indicates Cisco Centralized Key \n           Management\n\n           unknown - this indicates a key management method other\n           than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 255))
    namedValues = NamedValues(("none", 0), ("staticWep", 1), ("dynamicWep", 2), ("wpa", 3), ("wpaCckm", 4), ("wpa2", 5), ("wpa2Cckm", 6), ("cckm", 7), ("unknown", 255))

class CiscoLwappDot11ClientEncryptionMethod(TextualConvention, Integer32):
    description = 'This is the encryption method used  by the client.\n        The possible values are:\n\n           none - no encryption is used\n\n           wep40 - this is Wired Equivalent Privacy with a 40 bit \n           secret key\n\n           wep104 - this is Wired Equivalent Privacy with a 104 bit\n           secret key\n\n           tkip - this indicates Temporal Key Integrity\n           Protocol\n\n           ckip - this is Cisco Key Integrity Protocol\n\n           aesCcmp - this is Advanced Encryption Standard \n           - Counter Mode Cipher Block Chaining-Message Authentication \n           Code Protocol\n\n           unknown - this indicates an encryption method other\n           than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("none", 0), ("wep40", 1), ("wep104", 2), ("tkip", 3), ("ckip", 4), ("aesCcmp", 5), ("unknown", 255))

class CiscoLwappDot11ClientCredentialType(TextualConvention, Integer32):
    description = "This indicates how the 802.11 credentials are configured for\n        the client.\n        The possible values are:\n\n           localSaved - credentials are locally saved\n\n           manuallyPrompted - client is prompted for the credentials\n\n           hostOsLogin - this means the host operating system's login\n           credentials will be used\n\n           unknown - this indicates a credential method other\n           than the ones defined above"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("localSaved", 0), ("manuallyPrompted", 1), ("hostOsLogin", 2), ("unknown", 255))

class CiscoLwappDot11ClientPowerSaveMode(TextualConvention, Integer32):
    description = 'This is the type of power save mode configured on the\n        client. The possible values are:\n\n           awake - this indicates that the client is constantly awake\n\n           normal - this indicates normal power save mode\n\n           maxPower - this indicates maximum power save mode\n\n           uApsd - this indicates Unsolicited Automatic  \n           Power Save Delivery\n\n           sApsd - this indicates Solicited Automatic Power  \n           Save Delivery\n\n           unknown - this indicates a power save mode other\n           than the ones defined above'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 255))
    namedValues = NamedValues(("awake", 0), ("normal", 1), ("maxPower", 2), ("uApsd", 3), ("sApsd", 4), ("unknown", 255))

class CiscoLwappDot11ClientTxPowerMode(TextualConvention, Integer32):
    description = 'This field identifies the transmit power mode of the\n        client. The possible values are:\n\n           fixed - this indicates that the client is operating at a\n           fixed power mode\n\n           automatic - this indicates that the client power will be\n           determined automatically'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fixed", 0), ("automatic", 1))

class CiscoLwappDot11ClientRadioType(TextualConvention, Integer32):
    description = 'This is the radio type of the client. The possible values\n        are:\n            unused - this is currently a reserved radio type and is \n            not used\n\n            fhss - this is Frequency-hopping spread spectrum based\n            radio\n\n            dsss - this is Direct Sequence spread spectrum based\n            radio\n\n            infraRedBaseband - this is infrared baseband based radio\n\n            oFdm - this is orthogonal frequency division \n            multiplexing based radio\n\n            highRateDsss - this is high rate direct sequence spread \n            spectrum based radio\n\n            erp - this indicates effective radiated power based radio\n\n            draft11n2point4Ghz - this indicates a 2.4 Ghz band radio\n            as defined in draft 802.11n\n\n            draft11n5Ghz - this indicates a 5 Ghz band radio\n            as defined in draft 802.11n'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unused", 0), ("fhss", 1), ("dsss", 2), ("irBaseband", 3), ("oFdm", 4), ("highRateDsss", 5), ("erp", 6), ("draft11n2point4Ghz", 7), ("draft11n5Ghz", 8))

class CiscoLwappDot11ClientDataRates(TextualConvention, Bits):
    description = 'This field indicates the data rates supported by a\n        client.  If a data rate is supported by a client, the \n        corresponding bit is set to 1 else it is \n        set to 0.  The different data rates (in Mhz) are 1, 2,\n        5.5, 6, 9, 11, 12, 18, 24, 36, 48, 54.'
    status = 'current'
    namedValues = NamedValues(("mhz1", 0), ("mhz2", 1), ("mhz5point5", 2), ("mhz6", 3), ("mhz9", 4), ("mhz11", 5), ("mhz12", 6), ("mhz18", 7), ("mhz24", 8), ("mhz36", 9), ("mhz48", 10), ("mhz54", 11))

mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CCX-TC-MIB", CiscoLwappDot11ClientAuthMethod=CiscoLwappDot11ClientAuthMethod, CiscoLwappDot11ClientCredentialType=CiscoLwappDot11ClientCredentialType, CiscoLwappDot11ClientDataRates=CiscoLwappDot11ClientDataRates, CiscoLwappDot11ClientEAPMethod=CiscoLwappDot11ClientEAPMethod, CiscoLwappDot11ClientEncryptionMethod=CiscoLwappDot11ClientEncryptionMethod, CiscoLwappDot11ClientKeyMgmtMethod=CiscoLwappDot11ClientKeyMgmtMethod, CiscoLwappDot11ClientPowerSaveMode=CiscoLwappDot11ClientPowerSaveMode, CiscoLwappDot11ClientRadioType=CiscoLwappDot11ClientRadioType, CiscoLwappDot11ClientReqStatus=CiscoLwappDot11ClientReqStatus, CiscoLwappDot11ClientSSId=CiscoLwappDot11ClientSSId, CiscoLwappDot11ClientTxPowerMode=CiscoLwappDot11ClientTxPowerMode, PYSNMP_MODULE_ID=ciscoLwappDot11ClientCCXTextualConventions, ciscoLwappDot11ClientCCXTextualConventions=ciscoLwappDot11ClientCCXTextualConventions)
