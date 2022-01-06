#
# PySNMP MIB module DMTF-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DMTF-MONITOR-MIB
# Produced by pysmi-1.1.8 at Thu Jan  6 19:59:48 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dmiEventSubSystem, dmiCompId, dmiEventAssociatedGroup, DmiString, dmiEventSystem, dmiEventSeverity, dmiEventDateTime, dmiEventStateKey = mibBuilder.importSymbols("DMTF-DMI-MIB", "dmiEventSubSystem", "dmiCompId", "dmiEventAssociatedGroup", "DmiString", "dmiEventSystem", "dmiEventSeverity", "dmiEventDateTime", "dmiEventStateKey")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, IpAddress, Unsigned32, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, MibIdentifier, Counter32, iso, Gauge32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "IpAddress", "Unsigned32", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Counter32", "iso", "Gauge32", "NotificationType", "Bits")
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
mibBuilder.exportSymbols("DMTF-MONITOR-MIB", horizontalResolution=horizontalResolution, DmiInteger=DmiInteger, assetTag=assetTag, minimumMonitorRefreshRate=minimumMonitorRefreshRate, verticalScanMode=verticalScanMode, dmtfMonitorAdditionalInformationsEntry=dmtfMonitorAdditionalInformationsEntry, monitorPrimaryUserPhone=monitorPrimaryUserPhone, monitorPrimaryUserName=monitorPrimaryUserName, PYSNMP_MODULE_ID=dmtfMonitorMIF, DmiCompId=DmiCompId, DmiCounter=DmiCounter, DmiOctetstring=DmiOctetstring, dmtfStdMifs=dmtfStdMifs, dmtfMonitorAdditionalInformationsTable=dmtfMonitorAdditionalInformationsTable, verticalResolution=verticalResolution, monitorLocation=monitorLocation, dmtfDynOids=dmtfDynOids, dmtfMonitorResolutionsTable=dmtfMonitorResolutionsTable, dmtfMonitorMIF=dmtfMonitorMIF, refreshRate=refreshRate, DmiGroupId=DmiGroupId, dmtfMonitorResolutionsState=dmtfMonitorResolutionsState, DmiGauge=DmiGauge, dmtfMonitorResolutionsEntry=dmtfMonitorResolutionsEntry, maximumMonitorRefreshRate=maximumMonitorRefreshRate, dmtf=dmtf, DmiCounter64=DmiCounter64, monitorResolutionIndex=monitorResolutionIndex)
