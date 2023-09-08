#
# PySNMP MIB module MSERIES-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ENVMON-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 07:44:31 2023
# On host fv-az437-489 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, MibIdentifier, Counter64, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, NotificationType, Unsigned32, IpAddress, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "Counter64", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Unsigned32", "IpAddress", "Gauge32", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartEnvMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826, 1, 4))
smartEnvMon.setRevisions(('2014-02-15 10:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartEnvMon.setRevisionsDescriptions(('The initial revision of the MSERIES Enviroment Monitor MIB.',))
if mibBuilder.loadTexts: smartEnvMon.setLastUpdated('201402151034Z')
if mibBuilder.loadTexts: smartEnvMon.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartEnvMon.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartEnvMon.setDescription('This is the enterprise specific Enviroment Monitor MIB for SmartOptics M-Series.')
smartEnvMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1))
smartEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2))
smartEnvMonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1))
smartEnvMonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2))
smartEnvMonTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1), )
if mibBuilder.loadTexts: smartEnvMonTemperatureTable.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureTable.setDescription('This table contains one row per temperature sensor.')
smartEnvMonTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1), ).setIndexNames((0, "MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"))
if mibBuilder.loadTexts: smartEnvMonTemperatureEntry.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureEntry.setDescription('Information about a particular temperature sensor.')
smartEnvMonTemperatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureIndex.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureIndex.setDescription('An unique index for each temperature sensor.')
smartEnvMonTemperatureDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureDescr.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureDescr.setDescription('The name of the temperature sensor.')
smartEnvMonTemperatureValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 3), Integer32()).setUnits('degrees Celsius').setMaxAccess("readonly")
if mibBuilder.loadTexts: smartEnvMonTemperatureValue.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureValue.setDescription('The temperature in Celsius measured by the sensor.')
smartEnvMonTemperatureGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureDescr"), ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonTemperatureGroupV1 = smartEnvMonTemperatureGroupV1.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonTemperatureGroupV1.setDescription('The EnvMon Temperatue MIB objects v1.')
smartEnvMonBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2, 1)).setObjects(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smartEnvMonBasicComplV1 = smartEnvMonBasicComplV1.setStatus('current')
if mibBuilder.loadTexts: smartEnvMonBasicComplV1.setDescription('Basic implementation requirements for the ENVMON MIB.')
mibBuilder.exportSymbols("MSERIES-ENVMON-MIB", smartEnvMonTemperatureGroupV1=smartEnvMonTemperatureGroupV1, smartEnvMonTemperatureValue=smartEnvMonTemperatureValue, smartEnvMonObjects=smartEnvMonObjects, smartEnvMonCompliances=smartEnvMonCompliances, smartEnvMonTemperatureDescr=smartEnvMonTemperatureDescr, smartEnvMonGroups=smartEnvMonGroups, smartEnvMonTemperatureEntry=smartEnvMonTemperatureEntry, smartEnvMonTemperatureIndex=smartEnvMonTemperatureIndex, smartEnvMon=smartEnvMon, PYSNMP_MODULE_ID=smartEnvMon, smartEnvMonBasicComplV1=smartEnvMonBasicComplV1, smartEnvMonMIBConformance=smartEnvMonMIBConformance, smartEnvMonTemperatureTable=smartEnvMonTemperatureTable)
