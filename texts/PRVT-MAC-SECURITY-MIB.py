#
# PySNMP MIB module PRVT-MAC-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MAC-SECURITY-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:22 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Bits, Gauge32, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Bits", "Gauge32", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "iso")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
prvtMacSecurityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 109))
prvtMacSecurityMIB.setRevisions(('2010-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtMacSecurityMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: prvtMacSecurityMIB.setLastUpdated('201003260000Z')
if mibBuilder.loadTexts: prvtMacSecurityMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtMacSecurityMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtMacSecurityMIB.setDescription('The MIB module for managing port MAC security.')
class PrvtMacSecLrnProfileNameType(TextualConvention, OctetString):
    description = 'The name of a learning profile.'
    status = 'current'
    displayHint = '30t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 30)

class PrvtMacSecWatermarkActionType(TextualConvention, Integer32):
    description = 'Action to perform upon reaching the watermark MAC count value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4))
    namedValues = NamedValues(("log", 3), ("trap", 4))

class PrvtMacSecSecurityActionType(TextualConvention, Integer32):
    description = 'Action to perform upon reaching the maximum MAC count value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("operationalShutdown", 1), ("trap", 2))

class PrvtMacSecPolicyType(TextualConvention, Integer32):
    description = 'Type of policy a MAC security profile may have.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portSecurity", 1), ("portLimit", 2))

class PrvtMacSecEntryStateType(TextualConvention, Integer32):
    description = 'The state of a port with regards to MAC count.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noViolation", 1), ("watermarkReached", 2), ("maxMacCountReached", 3), ("errorState", 4))

prvtMacSecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0))
prvtMacSecObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1))
prvtMacSecLrnProfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1), )
if mibBuilder.loadTexts: prvtMacSecLrnProfTable.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfTable.setDescription('The table of learning profiles.\n         A learning profile specifies the thresholds, and actions to take with regards to the number of MAC addresses learned.')
prvtMacSecLrnProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1), ).setIndexNames((0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecLrnProfName"))
if mibBuilder.loadTexts: prvtMacSecLrnProfEntry.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfEntry.setDescription('An entry belonging to prvtMacSecLrnProfTable.')
prvtMacSecLrnProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 1), PrvtMacSecLrnProfileNameType())
if mibBuilder.loadTexts: prvtMacSecLrnProfName.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfName.setDescription('The name uniquely identifying the learning profile.')
prvtMacSecLrnProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfRowStatus.setDescription('The RowStatus for this instance.')
prvtMacSecLrnProfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 3), PrvtMacSecPolicyType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfPolicy.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfPolicy.setDescription('The type of MAC security policy that this learning profile follows.')
prvtMacSecLrnProfMaxMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfMaxMacCount.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfMaxMacCount.setDescription('Maximum allowed number of MAC addresses to be learned.\n         This value should be greater than or equal to the watermark MAC count, prvtMacSecLrnProfWatermarkCount.')
prvtMacSecLrnProfIgnoreFiltered = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfIgnoreFiltered.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfIgnoreFiltered.setDescription('When the violation limit is reached, do not learn violating MACs as filtered, but simply ignore them.')
prvtMacSecLrnProfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 6), PrvtMacSecSecurityActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfAction.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfAction.setDescription('The action to perform upon reaching the prvtMacSecLrnProfMaxMacCount value.')
prvtMacSecLrnProfWatermarkAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 7), PrvtMacSecWatermarkActionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkAction.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkAction.setDescription('The action to perform upon reaching the prvtMacSecLrnProfWatermarkCount value.')
prvtMacSecLrnProfWatermarkCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkCount.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecLrnProfWatermarkCount.setDescription('Sets the watermark at which the action specified in prvtMacSecLrnProfWatermarkAction will be taken.\n         This value should be less than the maximum MAC count, prvtMacSecLrnProfMaxMacCount.')
prvtMacSecIfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2), )
if mibBuilder.loadTexts: prvtMacSecIfTable.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfTable.setDescription('The table of profiles that have been assigned to each interface.')
prvtMacSecIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1), ).setIndexNames((0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: prvtMacSecIfEntry.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfEntry.setDescription('An entry belonging to prvtMacSecIfTable.')
prvtMacSecIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtMacSecIfName.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfName.setDescription('Interface name.')
prvtMacSecIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfRowStatus.setDescription('The RowStatus for this instance.')
prvtMacSecIfProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 3), PrvtMacSecLrnProfileNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMacSecIfProfile.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfProfile.setDescription('The name of a learning profile from prvtMacSecLrnProfTable.')
prvtMacSecIfCurrMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMacSecIfCurrMacCount.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfCurrMacCount.setDescription('The current MAC count for this entry.')
prvtMacSecIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 1, 2, 1, 5), PrvtMacSecEntryStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMacSecIfState.setStatus('current')
if mibBuilder.loadTexts: prvtMacSecIfState.setDescription('The current state of this entry.')
portSecurityWmarkViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0, 1)).setObjects(("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: portSecurityWmarkViolation.setStatus('current')
if mibBuilder.loadTexts: portSecurityWmarkViolation.setDescription('')
portSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 738, 10, 5, 109, 0, 2)).setObjects(("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"))
if mibBuilder.loadTexts: portSecurityViolation.setStatus('current')
if mibBuilder.loadTexts: portSecurityViolation.setDescription('')
mibBuilder.exportSymbols("PRVT-MAC-SECURITY-MIB", prvtMacSecIfName=prvtMacSecIfName, prvtMacSecurityMIB=prvtMacSecurityMIB, prvtMacSecLrnProfPolicy=prvtMacSecLrnProfPolicy, PrvtMacSecSecurityActionType=PrvtMacSecSecurityActionType, prvtMacSecObjects=prvtMacSecObjects, prvtMacSecIfProfile=prvtMacSecIfProfile, prvtMacSecLrnProfIgnoreFiltered=prvtMacSecLrnProfIgnoreFiltered, prvtMacSecLrnProfEntry=prvtMacSecLrnProfEntry, prvtMacSecIfRowStatus=prvtMacSecIfRowStatus, portSecurityWmarkViolation=portSecurityWmarkViolation, prvtMacSecIfCurrMacCount=prvtMacSecIfCurrMacCount, PrvtMacSecEntryStateType=PrvtMacSecEntryStateType, prvtMacSecLrnProfAction=prvtMacSecLrnProfAction, PrvtMacSecWatermarkActionType=PrvtMacSecWatermarkActionType, prvtMacSecIfState=prvtMacSecIfState, prvtMacSecLrnProfWatermarkCount=prvtMacSecLrnProfWatermarkCount, prvtMacSecLrnProfTable=prvtMacSecLrnProfTable, PrvtMacSecPolicyType=PrvtMacSecPolicyType, prvtMacSecLrnProfMaxMacCount=prvtMacSecLrnProfMaxMacCount, portSecurityViolation=portSecurityViolation, prvtMacSecIfTable=prvtMacSecIfTable, PrvtMacSecLrnProfileNameType=PrvtMacSecLrnProfileNameType, prvtMacSecLrnProfName=prvtMacSecLrnProfName, prvtMacSecLrnProfRowStatus=prvtMacSecLrnProfRowStatus, PYSNMP_MODULE_ID=prvtMacSecurityMIB, prvtMacSecIfEntry=prvtMacSecIfEntry, prvtMacSecNotifications=prvtMacSecNotifications, prvtMacSecLrnProfWatermarkAction=prvtMacSecLrnProfWatermarkAction)
