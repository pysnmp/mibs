#
# PySNMP MIB module CISCO-IMAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IMAGE-MIB
# Source digest sha256:3d2bacc298d72b6924a17e4b115b98253a91fd00c46412134b5e69b220fc9ed1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 25))
ciscoImageMIB.setRevisions(('1995-08-15 00:00', '1995-01-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImageMIB.setRevisionsDescriptions(('Specify a correct (non-negative) range for an index\n        object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImageMIB.setLastUpdated('1995-08-15 00:00')
if mibBuilder.loadTexts: ciscoImageMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImageMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageMIB.setDescription('Router image MIB which identify the capabilities\n        and characteristics of the image')
ciscoImageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 1))
ciscoImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoImageTable.setStatus('current')
if mibBuilder.loadTexts: ciscoImageTable.setDescription('A table provides content information describing the\n        executing IOS image.')
ciscoImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IMAGE-MIB", "ciscoImageIndex"))
if mibBuilder.loadTexts: ciscoImageEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoImageEntry.setDescription('A image characteristic string entry.')
ciscoImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoImageIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoImageIndex.setDescription('A sequence number for each string stored\n        in the IOS image.')
ciscoImageString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageString.setStatus('current')
if mibBuilder.loadTexts: ciscoImageString.setDescription('The string of this entry.')
ciscoImageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2))
ciscoImageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1))
ciscoImageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2))
ciscoImageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCompliance = ciscoImageMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBCompliance.setDescription('The compliance statement for entities which implement\n        the Cisco Image MIB')
ciscoImageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBGroup = ciscoImageMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBGroup.setDescription('A collection of objects providing IOS image characteristics')
mibBuilder.exportSymbols("CISCO-IMAGE-MIB", PYSNMP_MODULE_ID=ciscoImageMIB, ciscoImageEntry=ciscoImageEntry, ciscoImageIndex=ciscoImageIndex, ciscoImageMIB=ciscoImageMIB, ciscoImageMIBCompliance=ciscoImageMIBCompliance, ciscoImageMIBCompliances=ciscoImageMIBCompliances, ciscoImageMIBConformance=ciscoImageMIBConformance, ciscoImageMIBGroup=ciscoImageMIBGroup, ciscoImageMIBGroups=ciscoImageMIBGroups, ciscoImageMIBObjects=ciscoImageMIBObjects, ciscoImageString=ciscoImageString, ciscoImageTable=ciscoImageTable)
