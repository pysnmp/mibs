#
# PySNMP MIB module CISCO-WLAN-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WLAN-MAN-MIB
# Source digest sha256:77bbe8eb92be9564bfcd5ac354df62e09ac7f9a0172436673e6f171ecfe81eff
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoWlanManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 415))
ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWlanManMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWlanManMIB.setLastUpdated('2004-03-22 00:00')
if mibBuilder.loadTexts: ciscoWlanManMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoWlanManMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive,\n                        San Jose CA 95134-1706.\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                 Email: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoWlanManMIB.setDescription('This MIB module provides network management\n                and configuration support for IEEE 802.11\n                Wireless LAN devices.\n\n                          ACRONYMS\n\n                HTTP\n                    Hypertext Transfer Protocol.')
ciscoWlanManMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 0))
ciscoWlanManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1))
ciscoWlanManMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2))
cwmDeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1))
cwmNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2))
cwmHttpServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmHttpServerEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmHttpServerEnabled.setDescription("This object enables the HTTP Web server as follows:\n                    'true'  - HTTP Web server function is enabled,\n                    'false' - HTTP Web server function is disabled.")
cwmTelnetLoginEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setDescription("This object enables the telnet console login as \n                follows:                         \n                    'true'  - telnet console login is enabled,\n                    'false' - telnet console login is disabled.")
ciscoWlanManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1))
ciscoWlanManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2))
ciscoWlanManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmWirelessDeviceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanManMIBCompliance = ciscoWlanManMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWlanManMIBCompliance.setDescription('The compliance statement for the\n                ciscoWlanManMIB module.')
cwmWirelessDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"), ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWirelessDeviceGroup = cwmWirelessDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: cwmWirelessDeviceGroup.setDescription('Configuration for Wireless LAN Access Points\n                and bridges.')
mibBuilder.exportSymbols("CISCO-WLAN-MAN-MIB", PYSNMP_MODULE_ID=ciscoWlanManMIB, ciscoWlanManMIB=ciscoWlanManMIB, ciscoWlanManMIBCompliance=ciscoWlanManMIBCompliance, ciscoWlanManMIBCompliances=ciscoWlanManMIBCompliances, ciscoWlanManMIBConform=ciscoWlanManMIBConform, ciscoWlanManMIBGroups=ciscoWlanManMIBGroups, ciscoWlanManMIBNotifs=ciscoWlanManMIBNotifs, ciscoWlanManMIBObjects=ciscoWlanManMIBObjects, cwmDeviceConfig=cwmDeviceConfig, cwmHttpServerEnabled=cwmHttpServerEnabled, cwmNetworkConfig=cwmNetworkConfig, cwmTelnetLoginEnabled=cwmTelnetLoginEnabled, cwmWirelessDeviceGroup=cwmWirelessDeviceGroup)
