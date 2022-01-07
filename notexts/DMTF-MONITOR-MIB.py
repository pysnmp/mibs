#
# PySNMP MIB module DMTF-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DMTF-MONITOR-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:05:00 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
dmiEventSystem, dmiEventSubSystem, dmiEventStateKey, dmiEventDateTime, dmiCompId, dmiEventSeverity, dmiEventAssociatedGroup, DmiString = mibBuilder.importSymbols("DMTF-DMI-MIB", "dmiEventSystem", "dmiEventSubSystem", "dmiEventStateKey", "dmiEventDateTime", "dmiCompId", "dmiEventSeverity", "dmiEventAssociatedGroup", "DmiString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, enterprises, iso, IpAddress, Bits, Integer32, NotificationType, TimeTicks, Gauge32, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "enterprises", "iso", "IpAddress", "Bits", "Integer32", "NotificationType", "TimeTicks", "Gauge32", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("DMTF-MONITOR-MIB", dmtfMonitorResolutionsEntry=dmtfMonitorResolutionsEntry, DmiGauge=DmiGauge, dmtfMonitorMIF=dmtfMonitorMIF, assetTag=assetTag, PYSNMP_MODULE_ID=dmtfMonitorMIF, dmtf=dmtf, monitorResolutionIndex=monitorResolutionIndex, DmiInteger=DmiInteger, DmiCompId=DmiCompId, DmiCounter64=DmiCounter64, dmtfMonitorAdditionalInformationsEntry=dmtfMonitorAdditionalInformationsEntry, DmiGroupId=DmiGroupId, monitorLocation=monitorLocation, verticalScanMode=verticalScanMode, horizontalResolution=horizontalResolution, dmtfStdMifs=dmtfStdMifs, monitorPrimaryUserName=monitorPrimaryUserName, dmtfDynOids=dmtfDynOids, dmtfMonitorResolutionsState=dmtfMonitorResolutionsState, maximumMonitorRefreshRate=maximumMonitorRefreshRate, minimumMonitorRefreshRate=minimumMonitorRefreshRate, refreshRate=refreshRate, dmtfMonitorAdditionalInformationsTable=dmtfMonitorAdditionalInformationsTable, verticalResolution=verticalResolution, monitorPrimaryUserPhone=monitorPrimaryUserPhone, DmiOctetstring=DmiOctetstring, DmiCounter=DmiCounter, dmtfMonitorResolutionsTable=dmtfMonitorResolutionsTable)
