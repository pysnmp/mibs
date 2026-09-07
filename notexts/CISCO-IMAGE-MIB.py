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
if mibBuilder.loadTexts: ciscoImageMIB.setLastUpdated('1995-08-15 00:00')
if mibBuilder.loadTexts: ciscoImageMIB.setOrganization('Cisco Systems, Inc.')
ciscoImageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 1))
ciscoImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoImageTable.setStatus('current')
ciscoImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-IMAGE-MIB", "ciscoImageIndex"))
if mibBuilder.loadTexts: ciscoImageEntry.setStatus('current')
ciscoImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoImageIndex.setStatus('current')
ciscoImageString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageString.setStatus('current')
ciscoImageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2))
ciscoImageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1))
ciscoImageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2))
ciscoImageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCompliance = ciscoImageMIBCompliance.setStatus('current')
ciscoImageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBGroup = ciscoImageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-MIB", PYSNMP_MODULE_ID=ciscoImageMIB, ciscoImageEntry=ciscoImageEntry, ciscoImageIndex=ciscoImageIndex, ciscoImageMIB=ciscoImageMIB, ciscoImageMIBCompliance=ciscoImageMIBCompliance, ciscoImageMIBCompliances=ciscoImageMIBCompliances, ciscoImageMIBConformance=ciscoImageMIBConformance, ciscoImageMIBGroup=ciscoImageMIBGroup, ciscoImageMIBGroups=ciscoImageMIBGroups, ciscoImageMIBObjects=ciscoImageMIBObjects, ciscoImageString=ciscoImageString, ciscoImageTable=ciscoImageTable)
