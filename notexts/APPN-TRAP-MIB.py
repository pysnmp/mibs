#
# PySNMP MIB module APPN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source APPN-TRAP-MIB
# Source digest sha256:57db80aaf6b7a3a8eaa1328cb24c980024cd92b1f36e7b42c09fc466d167954f
# Produced by pysmi-2.3.0
#
dlurDlusSessnStatus, = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
appnCompliances, appnGroups, appnIsInP2SFmdBytes, appnIsInP2SFmdPius, appnIsInP2SNonFmdBytes, appnIsInP2SNonFmdPius, appnIsInS2PFmdBytes, appnIsInS2PFmdPius, appnIsInS2PNonFmdBytes, appnIsInS2PNonFmdPius, appnIsInSessUpTime, appnLocalTgCpCpSession, appnLocalTgOperational, appnLsOperState, appnMIB, appnObjects, appnPortOperState = mibBuilder.importSymbols("APPN-MIB", "appnCompliances", "appnGroups", "appnIsInP2SFmdBytes", "appnIsInP2SFmdPius", "appnIsInP2SNonFmdBytes", "appnIsInP2SNonFmdPius", "appnIsInS2PFmdBytes", "appnIsInS2PFmdPius", "appnIsInS2PNonFmdBytes", "appnIsInS2PNonFmdPius", "appnIsInSessUpTime", "appnLocalTgCpCpSession", "appnLocalTgOperational", "appnLsOperState", "appnMIB", "appnObjects", "appnPortOperState")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
if mibBuilder.loadTexts: appnTrapMIB.setLastUpdated('1998-08-31 00:00')
if mibBuilder.loadTexts: appnTrapMIB.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(("APPN-MIB", "appnIsInP2SFmdPius"), ("APPN-MIB", "appnIsInS2PFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdPius"), ("APPN-MIB", "appnIsInS2PNonFmdPius"), ("APPN-MIB", "appnIsInP2SFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdBytes"), ("APPN-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-MIB", "appnIsInSessUpTime"))
if mibBuilder.loadTexts: appnIsrAccountingDataTrap.setStatus('current')
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgOperational"))
if mibBuilder.loadTexts: appnLocalTgOperStateChangeTrap.setStatus('current')
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgCpCpSession"))
if mibBuilder.loadTexts: appnLocalTgCpCpChangeTrap.setStatus('current')
appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-MIB", "appnPortOperState"))
if mibBuilder.loadTexts: appnPortOperStateChangeTrap.setStatus('current')
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(("APPN-TRAP-MIB", "appnLsTableChanges"), ("APPN-MIB", "appnLsOperState"))
if mibBuilder.loadTexts: appnLsOperStateChangeTrap.setStatus('current')
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(("APPN-TRAP-MIB", "dlurDlusTableChanges"), ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
if mibBuilder.loadTexts: dlurDlusStateChangeTrap.setStatus('current')
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().clone(namedValues=NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appnTrapControl.setStatus('current')
appnLocalTgTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLocalTgTableChanges.setStatus('current')
appnPortTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnPortTableChanges.setStatus('current')
appnLsTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLsTableChanges.setStatus('current')
dlurDlusTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlurDlusTableChanges.setStatus('current')
appnTrapMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)).setObjects(("APPN-TRAP-MIB", "appnTrapMibIsrNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibCompliance = appnTrapMibCompliance.setStatus('current')
appnTrapMibIsrNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibIsrNotifGroup = appnTrapMibIsrNotifGroup.setStatus('current')
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoConfGroup = appnTrapMibTopoConfGroup.setStatus('current')
appnTrapMibTopoNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoNotifGroup = appnTrapMibTopoNotifGroup.setStatus('current')
appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurConfGroup = appnTrapMibDlurConfGroup.setStatus('current')
appnTrapMibDlurNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurNotifGroup = appnTrapMibDlurNotifGroup.setStatus('current')
mibBuilder.exportSymbols("APPN-TRAP-MIB", PYSNMP_MODULE_ID=appnTrapMIB, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, appnLocalTgTableChanges=appnLocalTgTableChanges, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnLsTableChanges=appnLsTableChanges, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnPortTableChanges=appnPortTableChanges, appnTrapControl=appnTrapControl, appnTrapMIB=appnTrapMIB, appnTrapMibCompliance=appnTrapMibCompliance, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnTrapObjects=appnTrapObjects, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, dlurDlusTableChanges=dlurDlusTableChanges)
