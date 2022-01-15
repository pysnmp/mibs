#
# PySNMP MIB module DMTF-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DMTF-MONITOR-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:06:47 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
dmiEventAssociatedGroup, dmiEventStateKey, dmiEventSystem, DmiString, dmiCompId, dmiEventSeverity, dmiEventDateTime, dmiEventSubSystem = mibBuilder.importSymbols("DMTF-DMI-MIB", "dmiEventAssociatedGroup", "dmiEventStateKey", "dmiEventSystem", "DmiString", "dmiCompId", "dmiEventSeverity", "dmiEventDateTime", "dmiEventSubSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, enterprises, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ModuleIdentity, Bits, Counter64, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiCounter(Counter32):
    pass

class DmiCounter64(Counter64):
    pass

class DmiGauge(Gauge32):
    pass

class DmiInteger(Integer32):
    pass

class DmiOctetstring(OctetString):
    pass

class DmiCompId(Integer32):
    pass

class DmiGroupId(Integer32):
    pass

dmtf = MibIdentifier((1, 3, 6, 1, 4, 1, 412))
dmtfStdMifs = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 2))
dmtfDynOids = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 3))
dmtfMonitorMIF = ModuleIdentity((1, 3, 6, 1, 4, 1, 412, 2, 6))
if mibBuilder.loadTexts: dmtfMonitorMIF.setLastUpdated('9710221800Z')
if mibBuilder.loadTexts: dmtfMonitorMIF.setOrganization('Desktop Management Task Force')
dmtfMonitorAdditionalInformationsTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 6, 1), )
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsTable.setStatus('current')
dmtfMonitorAdditionalInformationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1), ).setIndexNames((0, "DMTF-MONITOR-MIB", "DmiCompId"), (0, "DMTF-MONITOR-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dmtfMonitorAdditionalInformationsEntry.setStatus('current')
assetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 1), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: assetTag.setStatus('current')
monitorLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 2), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorLocation.setStatus('current')
monitorPrimaryUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 3), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorPrimaryUserName.setStatus('current')
monitorPrimaryUserPhone = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 4), DmiString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monitorPrimaryUserPhone.setStatus('current')
dmtfMonitorResolutionsTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 6, 2), )
if mibBuilder.loadTexts: dmtfMonitorResolutionsTable.setStatus('current')
dmtfMonitorResolutionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1), ).setIndexNames((0, "DMTF-MONITOR-MIB", "DmiCompId"), (0, "DMTF-MONITOR-MIB", "DmiGroupId"), (0, "DMTF-MONITOR-MIB", "monitorResolutionIndex"))
if mibBuilder.loadTexts: dmtfMonitorResolutionsEntry.setStatus('current')
dmtfMonitorResolutionsState = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dmtfMonitorResolutionsState.setStatus('current')
monitorResolutionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monitorResolutionIndex.setStatus('current')
horizontalResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 2), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: horizontalResolution.setStatus('current')
verticalResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: verticalResolution.setStatus('current')
refreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 4), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: refreshRate.setStatus('current')
verticalScanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("unsupported", 3), ("notInterlaced", 4), ("interlaced", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: verticalScanMode.setStatus('current')
minimumMonitorRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 6), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: minimumMonitorRefreshRate.setStatus('current')
maximumMonitorRefreshRate = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 7), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maximumMonitorRefreshRate.setStatus('current')
mibBuilder.exportSymbols("DMTF-MONITOR-MIB", DmiGauge=DmiGauge, verticalScanMode=verticalScanMode, monitorResolutionIndex=monitorResolutionIndex, dmtfMonitorAdditionalInformationsEntry=dmtfMonitorAdditionalInformationsEntry, dmtfMonitorResolutionsEntry=dmtfMonitorResolutionsEntry, DmiOctetstring=DmiOctetstring, DmiInteger=DmiInteger, refreshRate=refreshRate, DmiCounter64=DmiCounter64, verticalResolution=verticalResolution, monitorPrimaryUserName=monitorPrimaryUserName, minimumMonitorRefreshRate=minimumMonitorRefreshRate, monitorPrimaryUserPhone=monitorPrimaryUserPhone, dmtfMonitorResolutionsTable=dmtfMonitorResolutionsTable, DmiCounter=DmiCounter, DmiGroupId=DmiGroupId, dmtfMonitorMIF=dmtfMonitorMIF, maximumMonitorRefreshRate=maximumMonitorRefreshRate, dmtfMonitorAdditionalInformationsTable=dmtfMonitorAdditionalInformationsTable, DmiCompId=DmiCompId, dmtf=dmtf, PYSNMP_MODULE_ID=dmtfMonitorMIF, dmtfDynOids=dmtfDynOids, assetTag=assetTag, dmtfMonitorResolutionsState=dmtfMonitorResolutionsState, dmtfStdMifs=dmtfStdMifs, horizontalResolution=horizontalResolution, monitorLocation=monitorLocation)
