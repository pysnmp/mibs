#
# PySNMP MIB module CISCO-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-AAA-CLIENT-MIB
# Source digest sha256:d39a8e0a284a9106ac31d5e6437cee7c26b2e281af5af07ba1bed2cbeb28b375
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 158))
ciscoAAAClientMIB.setRevisions(('2001-11-19 00:00', '2001-05-10 00:00',))
if mibBuilder.loadTexts: ciscoAAAClientMIB.setLastUpdated('2001-11-19 00:00')
if mibBuilder.loadTexts: ciscoAAAClientMIB.setOrganization('Cisco Systems, Inc.')
class SessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("http", 3))

class AuthenMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("tacacs", 1), ("radius", 2), ("kerberos", 3), ("local", 4))

class LoginMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("login", 1), ("enable", 2))

cacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1))
cacPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1))
cacLoginConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2))
cacPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cacPriorityTable.setStatus('current')
cacPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacSession"), (0, "CISCO-AAA-CLIENT-MIB", "cacAuthen"), (0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"))
if mibBuilder.loadTexts: cacPriorityEntry.setStatus('current')
cacSession = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 1), SessionType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cacSession.setStatus('current')
cacAuthen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 2), AuthenMethod()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cacAuthen.setStatus('current')
cacLoginMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 3), LoginMode()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cacLoginMode.setStatus('current')
cacEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacEnable.setStatus('current')
cacPriorityNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cacPriorityNumber.setStatus('current')
cacPrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacPrimaryMethod.setStatus('current')
cacLoginConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cacLoginConfigTable.setStatus('current')
cacLoginConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-AAA-CLIENT-MIB", "cacLoginMode"), (0, "CISCO-AAA-CLIENT-MIB", "cacSession"))
if mibBuilder.loadTexts: cacLoginConfigEntry.setStatus('current')
cacMaxLoginAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 10), )).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacMaxLoginAttempt.setStatus('current')
cacLockoutPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 600), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriod.setStatus('deprecated')
cacLockoutPeriodExt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 158, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 43200), )).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cacLockoutPeriodExt.setStatus('current')
cacMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 2))
cacMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3))
cacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1))
cacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2))
cacMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance = cacMIBCompliance.setStatus('deprecated')
cacMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 1, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacPriorityGroup"), ("CISCO-AAA-CLIENT-MIB", "cacLoginConfigGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacMIBCompliance2 = cacMIBCompliance2.setStatus('current')
cacPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 1)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacEnable"), ("CISCO-AAA-CLIENT-MIB", "cacPriorityNumber"), ("CISCO-AAA-CLIENT-MIB", "cacPrimaryMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacPriorityGroup = cacPriorityGroup.setStatus('current')
cacLoginConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 2)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroup = cacLoginConfigGroup.setStatus('deprecated')
cacLoginConfigGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 158, 3, 2, 3)).setObjects(("CISCO-AAA-CLIENT-MIB", "cacMaxLoginAttempt"), ("CISCO-AAA-CLIENT-MIB", "cacLockoutPeriodExt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cacLoginConfigGroupRev1 = cacLoginConfigGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-MIB", AuthenMethod=AuthenMethod, LoginMode=LoginMode, PYSNMP_MODULE_ID=ciscoAAAClientMIB, SessionType=SessionType, cacAuthen=cacAuthen, cacEnable=cacEnable, cacLockoutPeriod=cacLockoutPeriod, cacLockoutPeriodExt=cacLockoutPeriodExt, cacLoginConfig=cacLoginConfig, cacLoginConfigEntry=cacLoginConfigEntry, cacLoginConfigGroup=cacLoginConfigGroup, cacLoginConfigGroupRev1=cacLoginConfigGroupRev1, cacLoginConfigTable=cacLoginConfigTable, cacLoginMode=cacLoginMode, cacMIBCompliance2=cacMIBCompliance2, cacMIBCompliance=cacMIBCompliance, cacMIBCompliances=cacMIBCompliances, cacMIBConformance=cacMIBConformance, cacMIBGroups=cacMIBGroups, cacMIBNotifications=cacMIBNotifications, cacMIBObjects=cacMIBObjects, cacMaxLoginAttempt=cacMaxLoginAttempt, cacPrimaryMethod=cacPrimaryMethod, cacPriority=cacPriority, cacPriorityEntry=cacPriorityEntry, cacPriorityGroup=cacPriorityGroup, cacPriorityNumber=cacPriorityNumber, cacPriorityTable=cacPriorityTable, cacSession=cacSession, ciscoAAAClientMIB=ciscoAAAClientMIB)
