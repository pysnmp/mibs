#
# PySNMP MIB module PRVT-MAC-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MAC-SECURITY-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 17:25:01 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, TimeTicks, ObjectIdentity, Counter32, Integer32, iso, IpAddress, Counter64, Bits, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "TimeTicks", "ObjectIdentity", "Counter32", "Integer32", "iso", "IpAddress", "Counter64", "Bits", "Unsigned32", "MibIdentifier")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
prvtMacSecurityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 109))
prvtMacSecurityMIB.setRevisions(('2010-03-26 00:00',))
if mibBuilder.loadTexts: prvtMacSecurityMIB.setLastUpdated('201003260000Z')
if mibBuilder.loadTexts: prvtMacSecurityMIB.setOrganization('BATM Advanced Communication')
class PrvtMacSecLrnProfileNameType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '30t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 30)

class PrvtMacSecWatermarkActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4))
    namedValues = NamedValues(("log", 3), ("trap", 4))

class PrvtMacSecSecurityActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("operationalShutdown", 1), ("trap", 2))

class PrvtMacSecPolicyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portSecurity", 1), ("portLimit", 2))

class PrvtMacSecEntryStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noViolation", 1), ("watermarkReached", 2), ("maxMacCountReached", 3), ("errorState", 4))

prvtMacSecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0))
prvtMacSecObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1))
prvtMacSecLrnProfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1), )
if mibBuilder.loadTexts: prvtMacSecLrnProfTable.setStatus('current')
prvtMacSecLrnProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1), ).setIndexNames((0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecLrnProfName"))
if mibBuilder.loadTexts: prvtMacSecLrnProfEntry.setStatus('current')
prvtMacSecLrnProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 1), PrvtMacSecLrnProfileNameType())
if mibBuilder.loadTexts: prvtMacSecLrnProfName.setStatus('current')
prvtMacSecLrnProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfRowStatus.setStatus('current')
prvtMacSecLrnProfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 3), PrvtMacSecPolicyType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfPolicy.setStatus('current')
prvtMacSecLrnProfMaxMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfMaxMacCount.setStatus('current')
prvtMacSecLrnProfIgnoreFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfIgnoreFiltered.setStatus('current')
prvtMacSecLrnProfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 6), PrvtMacSecSecurityActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfAction.setStatus('current')
prvtMacSecLrnProfWatermarkAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 7), PrvtMacSecWatermarkActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkAction.setStatus('current')
prvtMacSecLrnProfWatermarkCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkCount.setStatus('current')
prvtMacSecIfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2), )
if mibBuilder.loadTexts: prvtMacSecIfTable.setStatus('current')
prvtMacSecIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1), ).setIndexNames((0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: prvtMacSecIfEntry.setStatus('current')
prvtMacSecIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtMacSecIfName.setStatus('current')
prvtMacSecIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecIfRowStatus.setStatus('current')
prvtMacSecIfProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 3), PrvtMacSecLrnProfileNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecIfProfile.setStatus('current')
prvtMacSecIfCurrMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMacSecIfCurrMacCount.setStatus('current')
prvtMacSecIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 5), PrvtMacSecEntryStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMacSecIfState.setStatus('current')
portSecurityWmarkViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0, 1)).setObjects(("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: portSecurityWmarkViolation.setStatus('current')
portSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0, 2)).setObjects(("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: portSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("PRVT-MAC-SECURITY-MIB", prvtMacSecIfName=prvtMacSecIfName, PrvtMacSecSecurityActionType=PrvtMacSecSecurityActionType, prvtMacSecLrnProfName=prvtMacSecLrnProfName, prvtMacSecLrnProfWatermarkAction=prvtMacSecLrnProfWatermarkAction, PrvtMacSecEntryStateType=PrvtMacSecEntryStateType, PYSNMP_MODULE_ID=prvtMacSecurityMIB, PrvtMacSecWatermarkActionType=PrvtMacSecWatermarkActionType, portSecurityWmarkViolation=portSecurityWmarkViolation, prvtMacSecIfTable=prvtMacSecIfTable, prvtMacSecLrnProfTable=prvtMacSecLrnProfTable, prvtMacSecLrnProfRowStatus=prvtMacSecLrnProfRowStatus, prvtMacSecLrnProfPolicy=prvtMacSecLrnProfPolicy, prvtMacSecIfProfile=prvtMacSecIfProfile, prvtMacSecLrnProfAction=prvtMacSecLrnProfAction, PrvtMacSecPolicyType=PrvtMacSecPolicyType, prvtMacSecLrnProfWatermarkCount=prvtMacSecLrnProfWatermarkCount, prvtMacSecLrnProfMaxMacCount=prvtMacSecLrnProfMaxMacCount, prvtMacSecNotifications=prvtMacSecNotifications, prvtMacSecLrnProfEntry=prvtMacSecLrnProfEntry, prvtMacSecIfEntry=prvtMacSecIfEntry, prvtMacSecIfRowStatus=prvtMacSecIfRowStatus, prvtMacSecurityMIB=prvtMacSecurityMIB, prvtMacSecIfCurrMacCount=prvtMacSecIfCurrMacCount, portSecurityViolation=portSecurityViolation, PrvtMacSecLrnProfileNameType=PrvtMacSecLrnProfileNameType, prvtMacSecLrnProfIgnoreFiltered=prvtMacSecLrnProfIgnoreFiltered, prvtMacSecObjects=prvtMacSecObjects, prvtMacSecIfState=prvtMacSecIfState)
