#
# PySNMP MIB module CISCO-DOT11-ANTENNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-DOT11-ANTENNA-MIB
# Source digest sha256:5e40fe8f894f8230001f907bf91e011fcab1be24a6cd484848f98f4b1eae6231
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
ciscoDot11AntennaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 384))
ciscoDot11AntennaMIB.setRevisions(('2016-02-15 00:00', '2003-12-08 00:00',))
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setLastUpdated('2016-02-15 00:00')
if mibBuilder.loadTexts: ciscoDot11AntennaMIB.setOrganization('Cisco System Inc.')
cDot11AntennaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1))
cDot11AntennaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1))
cDot11AntennaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cDot11AntennaTable.setStatus('current')
cDot11AntennaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cDot11AntennaEntry.setStatus('current')
cDot11AntennaIsGainConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaIsGainConfigured.setStatus('current')
cDot11AntennaResultantGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 384, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11AntennaResultantGain.setStatus('current')
cDot11AntennaMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2))
cDot11AntennaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1))
cDot11AntennaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2))
cDot11AntennaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 1, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaMIBCompliance = cDot11AntennaMIBCompliance.setStatus('current')
cDot11AntennaGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 384, 2, 2, 1)).setObjects(("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaIsGainConfigured"), ("CISCO-DOT11-ANTENNA-MIB", "cDot11AntennaResultantGain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11AntennaGlobalGroup = cDot11AntennaGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-ANTENNA-MIB", PYSNMP_MODULE_ID=ciscoDot11AntennaMIB, cDot11AntennaEntry=cDot11AntennaEntry, cDot11AntennaGlobal=cDot11AntennaGlobal, cDot11AntennaGlobalGroup=cDot11AntennaGlobalGroup, cDot11AntennaIsGainConfigured=cDot11AntennaIsGainConfigured, cDot11AntennaMIBCompliance=cDot11AntennaMIBCompliance, cDot11AntennaMIBCompliances=cDot11AntennaMIBCompliances, cDot11AntennaMIBConform=cDot11AntennaMIBConform, cDot11AntennaMIBGroups=cDot11AntennaMIBGroups, cDot11AntennaMIBObjects=cDot11AntennaMIBObjects, cDot11AntennaResultantGain=cDot11AntennaResultantGain, cDot11AntennaTable=cDot11AntennaTable, ciscoDot11AntennaMIB=ciscoDot11AntennaMIB)
