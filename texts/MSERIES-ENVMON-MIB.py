#
# PySNMP MIB module MSERIES-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-ENVMON-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 08:48:59 2023
# On host fv-az566-171 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
mseries, = mibBuilder.importSymbols("MSERIES-MIB", "mseries")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Counter32, IpAddress, Unsigned32, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, iso, TimeTicks, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "IpAddress", "Unsigned32", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MSERIES-ENVMON-MIB", smartEnvMonTemperatureDescr=smartEnvMonTemperatureDescr, smartEnvMonMIBConformance=smartEnvMonMIBConformance, smartEnvMonTemperatureValue=smartEnvMonTemperatureValue, smartEnvMonTemperatureGroupV1=smartEnvMonTemperatureGroupV1, smartEnvMonGroups=smartEnvMonGroups, PYSNMP_MODULE_ID=smartEnvMon, smartEnvMonObjects=smartEnvMonObjects, smartEnvMonTemperatureTable=smartEnvMonTemperatureTable, smartEnvMon=smartEnvMon, smartEnvMonBasicComplV1=smartEnvMonBasicComplV1, smartEnvMonCompliances=smartEnvMonCompliances, smartEnvMonTemperatureIndex=smartEnvMonTemperatureIndex, smartEnvMonTemperatureEntry=smartEnvMonTemperatureEntry)
