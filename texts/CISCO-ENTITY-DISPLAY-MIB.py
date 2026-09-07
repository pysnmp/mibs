#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-DISPLAY-MIB
# Source digest sha256:0f1a951921eed33471d02e8b878f44e220cbde165747a62614f8f5e5ab12f8b5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoEntityDisplayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 344))
ciscoEntityDisplayMIB.setRevisions(('2009-10-05 00:00', '2003-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setRevisionsDescriptions(("Added the enumeration 'greenAndAmber' to\n        CDisplayColor TEXTUAL-CONVENTION.\n        Added support for ceDisplayBeaconGroup.", 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setLastUpdated('2009-10-05 00:00')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-displaymib@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setDescription('This MIB module provides information about the\n        status of display devices such as Light Emitting\n        Diodes (LEDs) and alphanumeric displays present\n        on the physical entities contained by the managed\n        system.')
class CDisplayType(TextualConvention, Integer32):
    description = 'An integer value that indicates the type of\n        display device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("led", 1), ("alphanumeric", 2))

class CDisplayColor(TextualConvention, Integer32):
    description = "An integer value that describes the color of the\n        display.\n\n        'greenAndAmber'    - Indicates that the display color\n                             toggles between green and amber."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("white", 2), ("red", 3), ("green", 4), ("yellow", 5), ("amber", 6), ("blue", 7), ("greenAndAmber", 8))

class CDisplayState(TextualConvention, Integer32):
    description = 'An integer value that describes the state of the\n        display.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("blinking", 4))

ciscoEntityDisplayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 1))
ceDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceDisplayTable.setStatus('current')
if mibBuilder.loadTexts: ceDisplayTable.setDescription('This table provides information about the display\n        devices on the physical entities in the managed\n        system and their current display status.')
ceDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayEntry.setStatus('current')
if mibBuilder.loadTexts: ceDisplayEntry.setDescription('An entry in the ceDisplayTable that provides\n        information about an LED or an alphanumeric display\n        in the system including its current display status.')
ceDisplayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceDisplayIndex.setStatus('current')
if mibBuilder.loadTexts: ceDisplayIndex.setDescription('An arbitrary index that uniquely identifies an LED or\n        an alphanumeric display on the physical entity\n        identified by entPhysicalIndex.')
ceDisplayType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 2), CDisplayType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayType.setStatus('current')
if mibBuilder.loadTexts: ceDisplayType.setDescription('This object indicates the type of display described\n        in this entry. i.e. whether it is an LED display or\n        an alphanumeric display.')
ceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayName.setStatus('current')
if mibBuilder.loadTexts: ceDisplayName.setDescription('This object provides a human-readable string which is\n        the name for the display device specified in this entry.')
ceDisplayState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 4), CDisplayState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayState.setStatus('current')
if mibBuilder.loadTexts: ceDisplayState.setDescription('This object indicates the current display state for\n        the display specified in this entry.')
ceDisplayColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 5), CDisplayColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayColor.setStatus('current')
if mibBuilder.loadTexts: ceDisplayColor.setDescription("This object indicates the color currently seen on\n        the display specified in this entry. If the display\n        specified by this entry is an alphanumeric display,\n        i.e. ceDisplayType is of type 'alphanumeric' then,\n        color may not apply and the agent may choose to\n        indicate this by setting this object to 'unknown'.")
ceDisplayText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayText.setStatus('current')
if mibBuilder.loadTexts: ceDisplayText.setDescription("This object provides a human-readable string which is\n        the text currently displayed in the alphanumeric display\n        specified in this entry. If the display specified by\n        this entry is an LED, i.e. ceDisplayType is of type 'led'\n        then, this object would be an empty string.")
ceDisplayBeaconTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ceDisplayBeaconTable.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconTable.setDescription('This table provides functionality to manage\n        beacon display devices in the managed system.')
ceDisplayBeaconEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setDescription('An entry containing management information of\n        beacon functionality of a particular beacon \n        display device.\n\n        Only those display devices, as specified by \n        entPhysicalIndex in ENTITY-MIB, that support \n        beacon functionality will be populated in this \n        table.')
ceDisplayBeaconEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setDescription("This object specifies if the beacon functionality is\n        administratively enabled for this display device.\n\n        'true'    - beacon functionality is administratively \n                    enabled\n        'false'   - beacon functionality is administratively \n                    disabled.")
ceDisplayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2))
ceDisplayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1))
ceDisplayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2))
ceDisplayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance = ceDisplayMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ceDisplayMIBCompliance.setDescription('The compliance statement for entities that implement the\n        CISCO-ENTITY-DISPLAY-MIB.\n\n        This compliance statement is deprecated and superceded by\n        ceDisplayMIBCompliance2.')
ceDisplayMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance2 = ceDisplayMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: ceDisplayMIBCompliance2.setDescription('The compliance statement for entities that implement the\n        CISCO-ENTITY-DISPLAY-MIB.')
ceDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayType"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayName"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayGroup = ceDisplayGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayGroup.setDescription('A collection of managed objects that provide information\n        about a display in the system including its current state.')
ceDisplayLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayLEDGroup = ceDisplayLEDGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayLEDGroup.setDescription('A collection of objects relevant to LED display.')
ceDisplayAlphaNumericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 3)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayAlphaNumericGroup = ceDisplayAlphaNumericGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayAlphaNumericGroup.setDescription('A collection of objects relevant to alphanumeric display.')
ceDisplayBeaconGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 4)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayBeaconGroup = ceDisplayBeaconGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconGroup.setDescription('A collection of objects relevant to beacon\n        functionality.')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-MIB", CDisplayColor=CDisplayColor, CDisplayState=CDisplayState, CDisplayType=CDisplayType, PYSNMP_MODULE_ID=ciscoEntityDisplayMIB, ceDisplayAlphaNumericGroup=ceDisplayAlphaNumericGroup, ceDisplayBeaconEnabled=ceDisplayBeaconEnabled, ceDisplayBeaconEntry=ceDisplayBeaconEntry, ceDisplayBeaconGroup=ceDisplayBeaconGroup, ceDisplayBeaconTable=ceDisplayBeaconTable, ceDisplayColor=ceDisplayColor, ceDisplayEntry=ceDisplayEntry, ceDisplayGroup=ceDisplayGroup, ceDisplayIndex=ceDisplayIndex, ceDisplayLEDGroup=ceDisplayLEDGroup, ceDisplayMIBCompliance2=ceDisplayMIBCompliance2, ceDisplayMIBCompliance=ceDisplayMIBCompliance, ceDisplayMIBCompliances=ceDisplayMIBCompliances, ceDisplayMIBConformance=ceDisplayMIBConformance, ceDisplayMIBGroups=ceDisplayMIBGroups, ceDisplayName=ceDisplayName, ceDisplayState=ceDisplayState, ceDisplayTable=ceDisplayTable, ceDisplayText=ceDisplayText, ceDisplayType=ceDisplayType, ciscoEntityDisplayMIB=ciscoEntityDisplayMIB, ciscoEntityDisplayMIBObjects=ciscoEntityDisplayMIBObjects)
