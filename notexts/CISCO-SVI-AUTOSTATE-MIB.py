#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SVI-AUTOSTATE-MIB
# Source digest sha256:cf1d1e07f46a1da26700ae1ead2d522c12ada3dc8aaabace333be4b7cec30ad9
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSVIAutostateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 376))
ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setLastUpdated('2004-04-06 00:00')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setOrganization('Cisco Systems, Inc.')
ciscoSVIAutostateMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 0))
ciscoSVIAutostateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1))
ciscoSVIAutostateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2))
csaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1))
csaInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2))
csaFeatureEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaFeatureEnable.setStatus('current')
csaTrackedVlansLow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansLow.setStatus('current')
csaTrackedVlansHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansHigh.setStatus('current')
csaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: csaIfConfigTable.setStatus('current')
csaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csaIfConfigEntry.setStatus('current')
csaInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("exclude", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaInterfaceMode.setStatus('current')
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVIAutostateGroup"), ("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVITrackedVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
ciscoSVIAutostateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"), ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVIAutostateGroup = ciscoSVIAutostateGroup.setStatus('current')
ciscoSVITrackedVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"), ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVITrackedVlanGroup = ciscoSVITrackedVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-MIB", PYSNMP_MODULE_ID=ciscoSVIAutostateMIB, ciscoSVIAutostateGroup=ciscoSVIAutostateGroup, ciscoSVIAutostateMIB=ciscoSVIAutostateMIB, ciscoSVIAutostateMIBConformance=ciscoSVIAutostateMIBConformance, ciscoSVIAutostateMIBNotifs=ciscoSVIAutostateMIBNotifs, ciscoSVIAutostateMIBObjects=ciscoSVIAutostateMIBObjects, ciscoSVITrackedVlanGroup=ciscoSVITrackedVlanGroup, csaFeatureEnable=csaFeatureEnable, csaGlobal=csaGlobal, csaIfConfigEntry=csaIfConfigEntry, csaIfConfigTable=csaIfConfigTable, csaInterface=csaInterface, csaInterfaceMode=csaInterfaceMode, csaMIBCompliance=csaMIBCompliance, csaMIBCompliances=csaMIBCompliances, csaMIBGroups=csaMIBGroups, csaTrackedVlansHigh=csaTrackedVlansHigh, csaTrackedVlansLow=csaTrackedVlansLow)
