#
# PySNMP MIB module DLINKSW-SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-SAFEGUARD-ENGINE-MIB
# Source digest sha256:360bbe479a6459e67dea6d1d3d3a9b0084d2f5f2340e9ca0f50afe37478239bb
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dCpuProtectMIBObjects, = mibBuilder.importSymbols("DLINKSW-CPU-PROTECT-MIB", "dCpuProtectMIBObjects")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
dlinkSwSafeguardEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1))
dlinkSwSafeguardEngineMIB.setRevisions(('2012-06-27 00:00',))
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setLastUpdated('2012-06-27 00:00')
if mibBuilder.loadTexts: dlinkSwSafeguardEngineMIB.setOrganization('D-Link Corp.')
dSafeguardEngineMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0))
dSafeguardEngineMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1))
dSafeguardEngineMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2))
dSafeguardEngineState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineState.setStatus('current')
dSafeguardEngineRiseThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(50)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineRiseThresh.setStatus('current')
dSafeguardEngineFallThresh = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 100)).clone(20)).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineFallThresh.setStatus('current')
dSafeguardEngineCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("exhausted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dSafeguardEngineCurrentMode.setStatus('current')
dSafeguardEngineNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSafeguardEngineNotifEnable.setStatus('current')
dSafeguardChgToExhausted = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToExhausted.setStatus('current')
dSafeguardChgToNormal = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 0, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if mibBuilder.loadTexts: dSafeguardChgToNormal.setStatus('current')
dSafeguardEngineCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1))
dSafeguardEngineCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 1, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngNotifEnableGroup"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineCompliance = dSafeguardEngineCompliance.setStatus('current')
dSafeguardEngineGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2))
dSafeguardEngineGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 1)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineState"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineRiseThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineFallThresh"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineCurrentMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineGroup = dSafeguardEngineGroup.setStatus('current')
dSafeguardEngNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 2)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardEngineNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngNotifEnableGroup = dSafeguardEngNotifEnableGroup.setStatus('current')
dSafeguardEngineNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 19, 1, 1, 2, 2, 3)).setObjects(("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToExhausted"), ("DLINKSW-SAFEGUARD-ENGINE-MIB", "dSafeguardChgToNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSafeguardEngineNotifGroup = dSafeguardEngineNotifGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-SAFEGUARD-ENGINE-MIB", PYSNMP_MODULE_ID=dlinkSwSafeguardEngineMIB, dSafeguardChgToExhausted=dSafeguardChgToExhausted, dSafeguardChgToNormal=dSafeguardChgToNormal, dSafeguardEngNotifEnableGroup=dSafeguardEngNotifEnableGroup, dSafeguardEngineCompliance=dSafeguardEngineCompliance, dSafeguardEngineCompliances=dSafeguardEngineCompliances, dSafeguardEngineCurrentMode=dSafeguardEngineCurrentMode, dSafeguardEngineFallThresh=dSafeguardEngineFallThresh, dSafeguardEngineGroup=dSafeguardEngineGroup, dSafeguardEngineGroups=dSafeguardEngineGroups, dSafeguardEngineMIBConformance=dSafeguardEngineMIBConformance, dSafeguardEngineMIBNotif=dSafeguardEngineMIBNotif, dSafeguardEngineMIBObjects=dSafeguardEngineMIBObjects, dSafeguardEngineNotifEnable=dSafeguardEngineNotifEnable, dSafeguardEngineNotifGroup=dSafeguardEngineNotifGroup, dSafeguardEngineRiseThresh=dSafeguardEngineRiseThresh, dSafeguardEngineState=dSafeguardEngineState, dlinkSwSafeguardEngineMIB=dlinkSwSafeguardEngineMIB)
