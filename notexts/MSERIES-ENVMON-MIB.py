#
# PySNMP MIB module MSERIES-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ENVMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 15:03:17 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, ModuleIdentity, Bits, Counter64, Integer32, MibIdentifier, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ModuleIdentity", "Bits", "Counter64", "Integer32", "MibIdentifier", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MSERIES-ENVMON-MIB", smartEnvMonGroups=smartEnvMonGroups, smartEnvMonTemperatureEntry=smartEnvMonTemperatureEntry, smartEnvMonTemperatureIndex=smartEnvMonTemperatureIndex, smartEnvMonBasicComplV1=smartEnvMonBasicComplV1, smartEnvMonTemperatureDescr=smartEnvMonTemperatureDescr, PYSNMP_MODULE_ID=smartEnvMon, smartEnvMonTemperatureValue=smartEnvMonTemperatureValue, smartEnvMon=smartEnvMon, smartEnvMonCompliances=smartEnvMonCompliances, smartEnvMonMIBConformance=smartEnvMonMIBConformance, smartEnvMonTemperatureTable=smartEnvMonTemperatureTable, smartEnvMonTemperatureGroupV1=smartEnvMonTemperatureGroupV1, smartEnvMonObjects=smartEnvMonObjects)
