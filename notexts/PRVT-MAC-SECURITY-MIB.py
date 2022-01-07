#
# PySNMP MIB module PRVT-MAC-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MAC-SECURITY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 18:06:34 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, NotificationType, Bits, TimeTicks, ObjectIdentity, IpAddress, Counter32, MibIdentifier, Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "NotificationType", "Bits", "TimeTicks", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("PRVT-MAC-SECURITY-MIB", prvtMacSecIfEntry=prvtMacSecIfEntry, prvtMacSecIfState=prvtMacSecIfState, portSecurityViolation=portSecurityViolation, prvtMacSecLrnProfPolicy=prvtMacSecLrnProfPolicy, prvtMacSecNotifications=prvtMacSecNotifications, prvtMacSecLrnProfMaxMacCount=prvtMacSecLrnProfMaxMacCount, PrvtMacSecPolicyType=PrvtMacSecPolicyType, prvtMacSecLrnProfWatermarkAction=prvtMacSecLrnProfWatermarkAction, PrvtMacSecEntryStateType=PrvtMacSecEntryStateType, prvtMacSecObjects=prvtMacSecObjects, PrvtMacSecSecurityActionType=PrvtMacSecSecurityActionType, prvtMacSecLrnProfEntry=prvtMacSecLrnProfEntry, prvtMacSecLrnProfWatermarkCount=prvtMacSecLrnProfWatermarkCount, prvtMacSecIfRowStatus=prvtMacSecIfRowStatus, prvtMacSecLrnProfName=prvtMacSecLrnProfName, prvtMacSecurityMIB=prvtMacSecurityMIB, prvtMacSecLrnProfTable=prvtMacSecLrnProfTable, portSecurityWmarkViolation=portSecurityWmarkViolation, prvtMacSecIfTable=prvtMacSecIfTable, PYSNMP_MODULE_ID=prvtMacSecurityMIB, prvtMacSecIfProfile=prvtMacSecIfProfile, prvtMacSecLrnProfRowStatus=prvtMacSecLrnProfRowStatus, prvtMacSecLrnProfIgnoreFiltered=prvtMacSecLrnProfIgnoreFiltered, PrvtMacSecLrnProfileNameType=PrvtMacSecLrnProfileNameType, prvtMacSecIfName=prvtMacSecIfName, prvtMacSecLrnProfAction=prvtMacSecLrnProfAction, prvtMacSecIfCurrMacCount=prvtMacSecIfCurrMacCount, PrvtMacSecWatermarkActionType=PrvtMacSecWatermarkActionType)
