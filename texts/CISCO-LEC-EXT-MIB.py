#
# PySNMP MIB module CISCO-LEC-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-LEC-EXT-MIB
# Source digest sha256:58f72b7a3f1d53447027598aef26e49ff387741303b23e5742f6f258d55182cb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
lecConfigEntry, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "lecConfigEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLecExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 77))
ciscoLecExtMIB.setRevisions(('1997-05-09 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLecExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLecExtMIB.setLastUpdated('1997-05-09 12:30')
if mibBuilder.loadTexts: ciscoLecExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLecExtMIB.setContactInfo('       Cisco Systems\n                           Customer Service\n\n                   Postal: 170 W Tasman Drive\n                           San Jose, CA  95134\n                           USA\n\n                      Tel: +1 800 553-NETS\n\n                   E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoLecExtMIB.setDescription("This MIB module is a Cisco extension to the ATM\n                Forum's LANE Client MIB.")
ciscoLecExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1))
cLecExtVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1))
cLecToVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cLecToVlanTable.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanTable.setDescription('An extension to the lecConfig table in the\n                LAN-EMULATION-CLIENT-MIB that identifies which VLAN a\n                LEC is associated with.')
cLecToVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
lecConfigEntry.registerAugmentions(("CISCO-LEC-EXT-MIB", "cLecToVlanEntry"))
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLecToVlanEntry.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanEntry.setDescription(' Each entry in this table shows the correlation\n                between a LAN Emulation client and the VLAN that it\n                extends.')
cLecToVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1, 1), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLecToVlanId.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanId.setDescription(' The VLAN ID of the VLAN to which the specified LEC\n                is attributed.')
ciscoLecExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2))
ciscoLecExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2, 0))
ciscoLecExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3))
ciscoLecExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1))
ciscoLecExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2))
ciscoLecExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1, 1)).setObjects(("CISCO-LEC-EXT-MIB", "ciscoLecExtVlanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtMIBCompliance = ciscoLecExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtMIBCompliance.setDescription('This module should be implemented by all Cisco\n                 devices supporting ATM LAN Emulation Clients.')
ciscoLecExtVlanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2, 1)).setObjects(("CISCO-LEC-EXT-MIB", "cLecToVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtVlanMIBGroup = ciscoLecExtVlanMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtVlanMIBGroup.setDescription('A collection of objects related to identifying\n                a LANE Client associated VLAN information.')
mibBuilder.exportSymbols("CISCO-LEC-EXT-MIB", PYSNMP_MODULE_ID=ciscoLecExtMIB, cLecExtVlan=cLecExtVlan, cLecToVlanEntry=cLecToVlanEntry, cLecToVlanId=cLecToVlanId, cLecToVlanTable=cLecToVlanTable, ciscoLecExtMIB=ciscoLecExtMIB, ciscoLecExtMIBCompliance=ciscoLecExtMIBCompliance, ciscoLecExtMIBCompliances=ciscoLecExtMIBCompliances, ciscoLecExtMIBConformance=ciscoLecExtMIBConformance, ciscoLecExtMIBGroups=ciscoLecExtMIBGroups, ciscoLecExtMIBNotificationPrefix=ciscoLecExtMIBNotificationPrefix, ciscoLecExtMIBNotifications=ciscoLecExtMIBNotifications, ciscoLecExtMIBObjects=ciscoLecExtMIBObjects, ciscoLecExtVlanMIBGroup=ciscoLecExtVlanMIBGroup)
