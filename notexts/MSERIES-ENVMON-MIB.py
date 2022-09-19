#
# PySNMP MIB module MSERIES-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ENVMON-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 07:36:31 2022
# On host fv-az215-626 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, ModuleIdentity, Gauge32, IpAddress, NotificationType, Counter32, Unsigned32, iso, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Gauge32", "IpAddress", "NotificationType", "Counter32", "Unsigned32", "iso", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartEnvMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 4))
smartEnvMon.setRevisions(('2014-02-15 10:34',))
if mibBuilder.loadTexts: smartEnvMon.setLastUpdated('201402151034Z')
if mibBuilder.loadTexts: smartEnvMon.setOrganization('SmartOptics')
smartEnvMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1))
smartEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2))
smartEnvMonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1))
smartEnvMonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2))
smartEnvMonTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1), )
if mibBuilder.loadTexts: smartEnvMonTemperatureTable.setStatus('current')
smartEnvMonTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1), ).setIndexNames((0, "MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"))
if mibBuilder.loadTexts: smartEnvMonTemperatureEntry.setStatus('current')
smartEnvMonTemperatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureIndex.setStatus('current')
smartEnvMonTemperatureDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureDescr.setStatus('current')
smartEnvMonTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 3), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureValue.setStatus('current')
smartEnvMonTemperatureGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureDescr"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonTemperatureGroupV1 = smartEnvMonTemperatureGroupV1.setStatus('current')
smartEnvMonBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonBasicComplV1 = smartEnvMonBasicComplV1.setStatus('current')
mibBuilder.exportSymbols("MSERIES-ENVMON-MIB", smartEnvMonTemperatureTable=smartEnvMonTemperatureTable, smartEnvMonMIBConformance=smartEnvMonMIBConformance, smartEnvMon=smartEnvMon, smartEnvMonTemperatureGroupV1=smartEnvMonTemperatureGroupV1, smartEnvMonTemperatureIndex=smartEnvMonTemperatureIndex, smartEnvMonObjects=smartEnvMonObjects, PYSNMP_MODULE_ID=smartEnvMon, smartEnvMonTemperatureDescr=smartEnvMonTemperatureDescr, smartEnvMonGroups=smartEnvMonGroups, smartEnvMonTemperatureValue=smartEnvMonTemperatureValue, smartEnvMonCompliances=smartEnvMonCompliances, smartEnvMonTemperatureEntry=smartEnvMonTemperatureEntry, smartEnvMonBasicComplV1=smartEnvMonBasicComplV1)
