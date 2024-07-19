#
# PySNMP MIB module IPO-PHONES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/IPO-PHONES-MIB.mib
# Produced by pysmi-1.1.12 at Fri Jul 19 09:59:25 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
IndexInteger, = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexInteger")
ipoGenMibs, ipoGTEventDevID, ipoGTEventEntityName, ipoGTEventSeverity, ipoGTEventStdSeverity, ipoGTEventDateTime = mibBuilder.importSymbols("IPO-MIB", "ipoGenMibs", "ipoGTEventDevID", "ipoGTEventEntityName", "ipoGTEventSeverity", "ipoGTEventStdSeverity", "ipoGTEventDateTime")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
Gauge32, ObjectIdentity, Counter32, Counter64, Integer32, Bits, ModuleIdentity, MibIdentifier, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "Integer32", "Bits", "ModuleIdentity", "MibIdentifier", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "TimeTicks")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
ipoPhonesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1))
ipoPhonesMIB.setRevisions(('2011-02-09 15:21', '2009-02-18 13:09', '2008-06-12 15:06', '2008-04-17 16:30', '2007-03-28 12:09', '2007-02-24 12:09', '2006-06-29 00:00', '2006-01-31 00:00', '2005-11-22 00:00', '2005-07-21 10:50', '2005-07-21 10:30', '2005-03-04 00:00', '2005-01-06 00:00', '2004-12-20 00:00', '2004-03-03 00:00', '2003-10-10 00:00',))
if mibBuilder.loadTexts: ipoPhonesMIB.setLastUpdated('201102091521Z')
if mibBuilder.loadTexts: ipoPhonesMIB.setOrganization('Avaya Inc.')
ipoPhonesMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0))
ipoPhonesMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1))
ipoPhonesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2))
class PhoneType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170))
    namedValues = NamedValues(("noPhone", 1), ("genericPhone", 2), ("potPhone", 3), ("dtPhone", 4), ("a4406Dplus", 5), ("a4412Dplus", 6), ("a4424Dplus", 7), ("a4424LDplus", 8), ("a9040TransTalk", 9), ("a6408Dplus", 10), ("a6416Dplus", 11), ("a6424Dplus", 12), ("a4606ip", 13), ("a4612ip", 14), ("a4624ip", 15), ("a4620ip", 16), ("a4602ip", 17), ("a2420", 18), ("a2010dt", 19), ("a2020dt", 20), ("a2030dt", 21), ("a2050dt", 22), ("act5", 23), ("att3", 24), ("att5", 25), ("a5420", 26), ("a5410", 27), ("a4601ip", 28), ("a4610ip", 29), ("ablf", 30), ("a2402", 31), ("a2410", 32), ("a5610ip", 33), ("a5620ip", 34), ("softIPPhone", 35), ("a5601ip", 36), ("a5602ip", 37), ("a4621ip", 38), ("a5621ip", 39), ("a4625ip", 40), ("a5402", 41), ("h323Phone", 42), ("sipPhone", 43), ("t3Compact", 44), ("t3Classic", 45), ("t3Comfort", 46), ("t3Phone", 47), ("t3compactIP", 48), ("t3classicIP", 49), ("t3comfortIP", 50), ("avayaSip", 51), ("admmPhone", 52), ("a9620ip", 53), ("a9630ip", 54), ("telecommuter", 55), ("mobiletwin", 56), ("a9640ip", 57), ("a9650ip", 58), ("a9610ip", 59), ("a1603ip", 60), ("a1608ip", 61), ("a1616ip", 62), ("a1703ip", 63), ("a1708ip", 64), ("a1716ip", 65), ("s60Sip", 66), ("sp320Sip", 67), ("sp601Sip", 68), ("a10ataSip", 69), ("pmataSip", 70), ("ip22Sip", 71), ("ip24Sip", 72), ("gxp2000Sip", 73), ("gxp2020Sip", 74), ("eyebeamSip", 75), ("a1403", 76), ("a1408", 77), ("a1416", 78), ("a1450", 79), ("ip28Sip", 80), ("phoneManagerIP", 81), ("a1503", 82), ("a1508", 83), ("a1516", 84), ("a1550", 85), ("a1603Lip", 86), ("a1608Lip", 87), ("a1616Lip", 88), ("softPhoneSip", 89), ("etr34d", 90), ("etr18d", 91), ("etr6d", 92), ("etr34", 93), ("etr18", 94), ("etr6", 95), ("etrpots", 96), ("doorphone1", 97), ("doorphone2", 98), ("bstT7316e", 99), ("a9620Sip", 100), ("a9630Sip", 101), ("a9640Sip", 102), ("a9650Sip", 103), ("a96xxSip", 104), ("a1603Sip", 105), ("a9404", 106), ("a9408", 107), ("a9504", 108), ("a9508", 109), ("a9608ip", 110), ("a9611ip", 111), ("a9621ip", 112), ("a9641ip", 113), ("a3720Admm", 114), ("a3725Admm", 115), ("a1010Sip", 116), ("a1040Sip", 117), ("a1120ESip", 118), ("a1140ESip", 119), ("a1220Sip", 120), ("a1230Sip", 121), ("a1692Sip", 122), ("pvvxSip", 123), ("gxv3140Sip", 124), ("a3740Admm", 125), ("a3749Admm", 126), ("bstT7316", 127), ("bstT7208", 128), ("bstM7208", 129), ("bstM7310", 130), ("bstM7310blf", 131), ("bstM7324", 132), ("bstM7100", 133), ("bstT7100", 134), ("bstT7000", 135), ("bstDectA", 136), ("bstDectB", 137), ("bstDectC", 138), ("bstDoorphone", 139), ("bstT7406", 140), ("bstT7406E", 141), ("bstM7310N", 142), ("bstAcu", 143), ("bstM7100N", 144), ("bstM7324N", 145), ("bstM7208N", 146), ("aB179Sip", 147), ("bstAta", 148), ("aA175Sip", 149), ("aOneXSip", 150), ("aFlareSip", 151), ("aD100", 152), ("aRadvisionXT1000", 153), ("aRadvisionXT1200", 154), ("aRadvisionXT4000", 155), ("aRadvisionXT4200", 156), ("aRadvisionXT5000", 157), ("aRadvisionXTPiccolo", 158), ("aRadvisionScopiaMCU", 159), ("aRadvisionScopiaVC240", 160), ("aOneXSipMobile", 161), ("aACCSServer", 162), ("aCIEServer", 163), ("aE129SIP", 164), ("aE159SIP", 165), ("aE169SIP", 166), ("aOneXMsiSIP", 167), ("aRadvisionXT240", 168), ("aWebRTCSIP", 169), ("softPhoneSipMac", 170))

ipoPhones = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1))
ipoPhonesNumber = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesNumber.setStatus('current')
ipoPhonesTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ipoPhonesTable.setStatus('current')
ipoPhonesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "IPO-PHONES-MIB", "ipoPhonesIndex"))
if mibBuilder.loadTexts: ipoPhonesEntry.setStatus('current')
ipoPhonesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1), IndexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesIndex.setStatus('current')
ipoPhonesExtID = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesExtID.setStatus('current')
ipoPhonesExtNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesExtNumber.setStatus('current')
ipoPhonesUserShort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesUserShort.setStatus('current')
ipoPhonesUserLong = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesUserLong.setStatus('current')
ipoPhonesType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 6), PhoneType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesType.setStatus('current')
ipoPhonesPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPort.setStatus('current')
ipoPhonesPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPortNumber.setStatus('current')
ipoPhonesModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesModuleNumber.setStatus('current')
ipoPhonesIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesIPAddress.setStatus('current')
ipoPhonesPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 11), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipoPhonesPhysAddress.setStatus('current')
ipoPhonesChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 1)).setObjects(("IPO-MIB", "ipoGTEventSeverity"), ("IPO-MIB", "ipoGTEventDateTime"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"))
if mibBuilder.loadTexts: ipoPhonesChangeEvent.setStatus('deprecated')
ipoPhonesChangeSvcEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 2)).setObjects(("IPO-MIB", "ipoGTEventStdSeverity"), ("IPO-MIB", "ipoGTEventDateTime"), ("IPO-MIB", "ipoGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"), ("IPO-MIB", "ipoGTEventEntityName"))
if mibBuilder.loadTexts: ipoPhonesChangeSvcEvent.setStatus('current')
ipoPhonesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1))
ipoPhonesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2))
ipoPhonesCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 1)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhonesNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesCompliance = ipoPhonesCompliance.setStatus('deprecated')
ipoPhonesv2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 2)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv2Compliance = ipoPhonesv2Compliance.setStatus('deprecated')
ipoPhonesv3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 3)).setObjects(("IPO-PHONES-MIB", "ipoPhonesGroup"), ("IPO-PHONES-MIB", "ipoPhones2Group"), ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv3Compliance = ipoPhonesv3Compliance.setStatus('current')
ipoPhonesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 1)).setObjects(("IPO-PHONES-MIB", "ipoPhonesNumber"), ("IPO-PHONES-MIB", "ipoPhonesIndex"), ("IPO-PHONES-MIB", "ipoPhonesExtID"), ("IPO-PHONES-MIB", "ipoPhonesExtNumber"), ("IPO-PHONES-MIB", "ipoPhonesUserShort"), ("IPO-PHONES-MIB", "ipoPhonesUserLong"), ("IPO-PHONES-MIB", "ipoPhonesType"), ("IPO-PHONES-MIB", "ipoPhonesPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesGroup = ipoPhonesGroup.setStatus('current')
ipoPhonesNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 2)).setObjects(("IPO-PHONES-MIB", "ipoPhonesChangeEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesNotificationsGroup = ipoPhonesNotificationsGroup.setStatus('deprecated')
ipoPhonesv2NotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 3)).setObjects(("IPO-PHONES-MIB", "ipoPhonesChangeSvcEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhonesv2NotificationsGroup = ipoPhonesv2NotificationsGroup.setStatus('current')
ipoPhones2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 4)).setObjects(("IPO-PHONES-MIB", "ipoPhonesPortNumber"), ("IPO-PHONES-MIB", "ipoPhonesModuleNumber"), ("IPO-PHONES-MIB", "ipoPhonesIPAddress"), ("IPO-PHONES-MIB", "ipoPhonesPhysAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipoPhones2Group = ipoPhones2Group.setStatus('current')
mibBuilder.exportSymbols("IPO-PHONES-MIB", ipoPhonesChangeSvcEvent=ipoPhonesChangeSvcEvent, ipoPhones=ipoPhones, ipoPhonesGroups=ipoPhonesGroups, ipoPhonesMIB=ipoPhonesMIB, ipoPhonesMibNotifications=ipoPhonesMibNotifications, ipoPhonesPort=ipoPhonesPort, ipoPhonesGroup=ipoPhonesGroup, ipoPhones2Group=ipoPhones2Group, ipoPhonesEntry=ipoPhonesEntry, ipoPhonesExtNumber=ipoPhonesExtNumber, PhoneType=PhoneType, ipoPhonesPhysAddress=ipoPhonesPhysAddress, ipoPhonesExtID=ipoPhonesExtID, ipoPhonesType=ipoPhonesType, ipoPhonesv2NotificationsGroup=ipoPhonesv2NotificationsGroup, PYSNMP_MODULE_ID=ipoPhonesMIB, ipoPhonesUserShort=ipoPhonesUserShort, ipoPhonesv2Compliance=ipoPhonesv2Compliance, ipoPhonesNotificationsGroup=ipoPhonesNotificationsGroup, ipoPhonesIPAddress=ipoPhonesIPAddress, ipoPhonesConformance=ipoPhonesConformance, ipoPhonesIndex=ipoPhonesIndex, ipoPhonesPortNumber=ipoPhonesPortNumber, ipoPhonesTable=ipoPhonesTable, ipoPhonesChangeEvent=ipoPhonesChangeEvent, ipoPhonesUserLong=ipoPhonesUserLong, ipoPhonesModuleNumber=ipoPhonesModuleNumber, ipoPhonesCompliance=ipoPhonesCompliance, ipoPhonesNumber=ipoPhonesNumber, ipoPhonesMibObjects=ipoPhonesMibObjects, ipoPhonesCompliances=ipoPhonesCompliances, ipoPhonesv3Compliance=ipoPhonesv3Compliance)
