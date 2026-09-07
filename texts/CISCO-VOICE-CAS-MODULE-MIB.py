#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VOICE-CAS-MODULE-MIB
# Source digest sha256:dec0323657edf8a220ced6188f7cf142b1533773a5a6b32bea8ce514c96741b1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVoiceCasModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 389))
ciscoVoiceCasModuleMIB.setRevisions(('2004-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setRevisionsDescriptions(('Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setLastUpdated('2004-03-15 00:00')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setContactInfo('    Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setDescription('This MIB is used to support Programmable \n                 CAS signaling Bit configuration on modules\n                 that support voice traffic.\n\n                 This MIB will enable programming of the CAS\n                 bits in order to translate incoming/outgoing \n                 bit patterns from/to the TDM or packet side \n                 interface.\n                 \n                 Terminology:\n                 \n                 ABCD - Signaling bits describing off-hook,\n                        on-hook, idle, flash, etc events.\n\n                 DSP - Digital Signal Processing\n\n                 CAS - Channal Associated Signaling\n\n                 E&M - Ear and Mouth Protocol\n\n                 TDM - Time Division Multiplexed\n                ')
ciscoVoiceCasModuleNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 0))
ciscoVoiceCasModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1))
cvcmCasConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1))
class CvcmCasPatternBitPosition(TextualConvention, Bits):
    description = 'Defines the bit positions for the incoming\n         and outgoing ABCD bit patterns.\n         All positions need to be set to 0 or 1 in\n         order to have the correct pattern.\n\n         dBit : Position of the D bit in the \n                ABCD bit pattern\n         cBit : Position of the C bit in the \n                ABCD bit pattern\n         bBit : Position of the B bit in the\n                ABCD bit pattern\n         aBit : Position of the A bit in the\n                ABCD bit pattern\n        '
    status = 'current'
    namedValues = NamedValues(("dBit", 0), ("cBit", 1), ("bBit", 2), ("aBit", 3))

class CvcmCasBitAction(TextualConvention, Integer32):
    description = 'Defines the actions that can be performed on the\n         CAS ABCD bits.\n\n         casBitNoAction   : No action on the bit specifed. \n                            Maintain incoming bit value. \n         casBitSetToZero  : Set bit to zero\n         casBitSetToOne   : Set bit to one\n         casBitInvertBit  : Invert incoming bit\n         casBitInvertABit : Invert A bit and apply to the \n                            bit location specified\n         casBitInvertBBit : Invert B bit and apply to the \n                            bit location specified \n         casBitInvertCBit : Invert C bit and apply to the \n                            bit location specified \n         casBitInvertDBit : Invert D bit and apply to the \n                            bit location specified \n         casBitABit       : Apply A bit value to the bit \n                            location specified\n         casBitBBit       : Apply B bit value to the bit \n                            location specified\n         casBitCBit       : Apply C bit value to the bit \n                            location specified\n         casBitDBit       : Apply D bit value to the bit \n                            location specified\n       '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("casBitNoAction", 1), ("casBitSetToZero", 2), ("casBitSetToOne", 3), ("casBitInvertBit", 4), ("casBitInvertABit", 5), ("casBitInvertBBit", 6), ("casBitInvertCBit", 7), ("casBitInvertDBit", 8), ("casBitABit", 9), ("casBitBBit", 10), ("casBitCBit", 11), ("casBitDBit", 12))

cvcmABCDBitTemplateConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigTable.setDescription("This table is used to configure templates\n         on the module/card. These templates provide\n         mapping information between the incoming CAS \n         ABCD signaling bit patterns and the outgoing \n         ABCD signaling bit patterns. The outgoing \n         bit patterns are derived from the incoming \n         bit patterns by applying a set of actions to\n         each incoming bit.\n         \n         Thus, this table essentially contains \n         configuration information about CAS ABCD \n         signaling bits.\n\n         The ABCD bit carries signaling information\n         describing off-hook, on-hook event etc on a\n         T1 or E1. The pattern representations\n         differ in CAS variants on a T1 and E1.\n\n         For example:\n         On T1:\n         E&M protocol ABCD seized is 1100\n         On E1:\n         CAS-R2 signaling ABCD seized is 0001\n\n         This table is configured on a per module/ card \n         basis.\n\n         Further, one can have multiple different actions\n         performed on the different bits (A, B, C or D)\n         consecutively for the same incoming ABCD bit \n         index. However, a given bit position can only \n         have one action being performed on it for a given\n         incoming bit pattern.\n\n         For example, for a given incoming bit index, \n         one can define the 'A' bit to be set to 0, the 'B'\n         bit to be swapped with the 'C' bit, the 'C' bit to be \n         swapped with the 'B' bit and the 'D' bit to be inverted.\n         Thus, using this table, the user can create a template\n         with name (cvcmCasTemplateName) 'Template1' where for \n         incoming pattern (cvcmABCDIncomingPattern) '0000', \n         the action on the A bit (cvcmCasABitAction) is \n         'casBitSetToZero', the action on the B bit \n         (cvcmCasBBitAction) is 'casBitCBit', the action on the \n         C bit (cvcmCasCBitAction) is 'casBitBBit' and the action\n         on the D bit (cvcmCasDBitAction) is 'casBitInvertBit'.\n         This will create one entry in 'Template1' where the \n         resultant outgoing pattern (cvcmABCDOutgoingPattern)\n         will be '0001'.\n        ")
cvcmABCDBitTemplateConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmModuleIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDPatternIndex"))
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigEntry.setDescription('An entry in the table. Each entry consists of \n         user defined CAS ABCD bit information to configure\n         a transmit or received signaling channel on a DSP.\n        ')
cvcmModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcmModuleIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmModuleIndex.setDescription(" This object uniquely identifies the card/ module\n          where this table resides. It could be the slot\n          number of the module or be 1 where 'module' is \n          not applicable.\n        ")
cvcmCasTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcmCasTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmCasTemplateIndex.setDescription('This object will index into the template that \n         is configured in this table.\n        ')
cvcmABCDPatternIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcmABCDPatternIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDPatternIndex.setDescription('Will be used to index into a particular pattern\n         mapping in the template that is configured.\n         Since there are only 4 signaling bits (A, B, C, D),\n         there can only be (2^4) or 16 patterns per \n         template. \n        ')
cvcmModulePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 4), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmModulePhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: cvcmModulePhysicalIndex.setDescription('This object represents the entPhysicalIndex of \n         the module where this table is being configured. \n         If the entPhysicalTable is not supported on the \n         SNMP agent, then the value of this object will \n         be zero.\n        ')
cvcmCasTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasTemplateName.setStatus('current')
if mibBuilder.loadTexts: cvcmCasTemplateName.setDescription('This object identifies the name of the template\n         configured.\n         This object needs to be unique among all the\n         instances of the cvcmABCDBitTemplateConfigTable.\n         The SNMP agent will need to validate this value\n         for uniqueness.\n        ')
cvcmABCDIncomingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 6), CvcmCasPatternBitPosition()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmABCDIncomingPattern.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDIncomingPattern.setDescription("This object identifies the ABCD signaling bits\n         that are received by the module. The actions\n         specified in 'cvcmCasABitAction', 'cvcmCasBBitAction',\n         'cvcmCasCBitAction' and 'cvcmCasDBitAction' are applied\n         to this object.\n        ")
cvcmABCDOutgoingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 7), CvcmCasPatternBitPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmABCDOutgoingPattern.setStatus('current')
if mibBuilder.loadTexts: cvcmABCDOutgoingPattern.setDescription("This object identifies the ABCD signaling bits\n         defined by user, and downloaded to DSP signaling\n         channel. \n         This pattern is derived from the actions specified in \n         'cvcmCasABitAction', 'cvcmCasBBitAction', 'cvcmCasCBitAction' \n         and 'cvcmCasDBitAction'. \n         The same pattern can map to different \n         cvcmABCDIncomingPattern depending on the set of actions.\n         This pattern is mapped to input ABCD bit pattern \n         received and reported to the TDM or network side.\n        ")
cvcmCasABitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 8), CvcmCasBitAction().clone('casBitABit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasABitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasABitAction.setDescription("This object identifies the action on the \n         'A' bit of the incoming ABCD bit pattern\n         specified in cvcmABCDIncomingPattern.\n         For this object,\n         'cvcmInvertBit' is same as 'cvcmInvertABit',\n         'cvcmNoAction'  is same as 'cvcmABit'.\n        ")
cvcmCasBBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 9), CvcmCasBitAction().clone('casBitBBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBBitAction.setDescription("This object identifies the action on the \n         'B' bit of the incoming ABCD bit pattern\n         specified in cvcmABCDIncomingPattern.\n         For this object, \n         'cvcmInvertBit' is same as 'cvcmInvertBBit',\n         'cvcmNoAction'  is same as 'cvcmBBit'.\n        ")
cvcmCasCBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 10), CvcmCasBitAction().clone('casBitCBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasCBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasCBitAction.setDescription("This object identifies the action on the \n         'C' bit of the incoming ABCD bit pattern\n         specified in cvcmABCDIncomingPattern.\n         For this object,\n         'cvcmInvertBit' is same as 'cvcmInvertCBit',\n         'cvcmNoAction'  is same as 'cvcmCBit'.\n        ")
cvcmCasDBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 11), CvcmCasBitAction().clone('casBitDBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasDBitAction.setStatus('current')
if mibBuilder.loadTexts: cvcmCasDBitAction.setDescription("This object identifies the action on the \n         'D' bit of the incoming ABCD bit pattern\n         specified in cvcmABCDIncomingPattern.\n         For this object, \n         'cvcmInvertBit' is same as 'cvcmInvertDBit',\n         'cvcmNoAction'  is same as 'cvcmDBit'.\n        ")
cvcmCasBitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBitRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBitRowStatus.setDescription("An entry may be created using the 'createAndGo'\n         option.  When the row is successfully created, \n         the object will be set to 'active' by the agent. \n         An entry may be deleted by setting the object \n         to 'destroy'.\n        ")
cvcmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2))
cvcmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1))
cvcmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2))
ciscoVoiceCasModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCasModuleMIBCompliance = ciscoVoiceCasModuleMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIBCompliance.setDescription('Compliance statement for CISCO-VOICE-CAS-MODULE-MIB.')
cvcmCasBitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmModulePhysicalIndex"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateName"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDIncomingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDOutgoingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasABitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasCBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasDBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCasBitGroup = cvcmCasBitGroup.setStatus('current')
if mibBuilder.loadTexts: cvcmCasBitGroup.setDescription('A collection of objects used for configuring \n         DSP signaling channel.\n        ')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-MIB", CvcmCasBitAction=CvcmCasBitAction, CvcmCasPatternBitPosition=CvcmCasPatternBitPosition, PYSNMP_MODULE_ID=ciscoVoiceCasModuleMIB, ciscoVoiceCasModuleMIB=ciscoVoiceCasModuleMIB, ciscoVoiceCasModuleMIBCompliance=ciscoVoiceCasModuleMIBCompliance, ciscoVoiceCasModuleNotifs=ciscoVoiceCasModuleNotifs, ciscoVoiceCasModuleObjects=ciscoVoiceCasModuleObjects, cvcmABCDBitTemplateConfigEntry=cvcmABCDBitTemplateConfigEntry, cvcmABCDBitTemplateConfigTable=cvcmABCDBitTemplateConfigTable, cvcmABCDIncomingPattern=cvcmABCDIncomingPattern, cvcmABCDOutgoingPattern=cvcmABCDOutgoingPattern, cvcmABCDPatternIndex=cvcmABCDPatternIndex, cvcmCasABitAction=cvcmCasABitAction, cvcmCasBBitAction=cvcmCasBBitAction, cvcmCasBitGroup=cvcmCasBitGroup, cvcmCasBitRowStatus=cvcmCasBitRowStatus, cvcmCasCBitAction=cvcmCasCBitAction, cvcmCasConfig=cvcmCasConfig, cvcmCasDBitAction=cvcmCasDBitAction, cvcmCasTemplateIndex=cvcmCasTemplateIndex, cvcmCasTemplateName=cvcmCasTemplateName, cvcmMIBCompliances=cvcmMIBCompliances, cvcmMIBConformance=cvcmMIBConformance, cvcmMIBGroups=cvcmMIBGroups, cvcmModuleIndex=cvcmModuleIndex, cvcmModulePhysicalIndex=cvcmModulePhysicalIndex)
