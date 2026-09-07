#
# PySNMP MIB module CISCO-MGX82XX-PXM-CLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-MGX82XX-PXM-CLOCK-MIB
# Source digest sha256:c0b7af08fcc68b017f8976a0be1125d11ae662280354fd86baa1831cb0c81bed
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cardSpecific, = mibBuilder.importSymbols("BASIS-MIB", "cardSpecific")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxPxmClockMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 72))
ciscoMgx82xxPxmClockMIB.setRevisions(('2003-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setRevisionsDescriptions(('Initial version of the MIB.\n\n        The content of this MIB was originally available\n        in CISCO-WAN-AXIPOP-MIB defined using SMIv1.\n        The applicable objects from CISCO-WAN-AXIPOP-MIB\n        are defined using SMIv2 in this MIB. Also the\n        descriptions of some of the objects have been \n        modified.',))
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setLastUpdated('2003-05-27 00:00')
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMgx82xxPxmClockMIB.setDescription('The MIB module to describe the clock configuration\n        in Processor Switch Module(PXM) in MGX82xx product.\n \n        Back cards supported for PXM1:\n         PXM-UI     : T1 Clock port, E1 Clock Port\n         PXM-UI-S3  : External Clock1 for T1/E1 Clock input.')
class CmpClockConnectorType(TextualConvention, Integer32):
    description = 'Represents the connector type for the clock\n        device.\n\n        rj45Type(1): RJ-45 Connector. This is for T1/E1 clock\n                     input.\n        smbType (2): SMB Connector. This is for E1 clock input.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rj45Type", 1), ("smbType", 2))

class CmpClockSourceType(TextualConvention, Integer32):
    description = 'This object identifies the source of the\n        Mux Clock on PXM card.\n\n        pxmInbandClock1 (1),\n        pxmInbandClock2 (5): clock is derived from physical line\n\n        pxmServiceModuleClock1(2),\n        pxmServiceModuleClock2(6): clock is derived from service module.\n\n        pxmTopSRMClock         (3),\n        pxmBottomSRMClock      (7): clock is derived from SRM module.\n\n        pxmExternalClock(4),\n        pxmExternalClock2(9)      :clock is derived from the port.\n\n        pxmInternalOscillator  (8): clock is derived from internal\n                                     oscillator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("pxmInbandClock1", 1), ("pxmServiceModuleClock1", 2), ("pxmTopSRMClock", 3), ("pxmExternalClock", 4), ("pxmInbandClock2", 5), ("pxmServiceModuleClock2", 6), ("pxmBottomSRMClock", 7), ("pxmInternalOscillator", 8), ("pxmExternalClock2", 9))

class CmpCurrentClock(TextualConvention, Integer32):
    description = 'This TEXTUAL Convention represents the clock source currently \n        selected for PXM card.\n\n        primary(1): The primary clock source is described by\n                    pxmPrimaryMuxClockSource\n\n        secondary(2): The secondary clock source is described by\n                      pxmSecondaryMuxClockSource.\n        intOscillator(3): Current clock is internal oscillator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("primary", 1), ("secondary", 2), ("intOscillator", 3))

class CmpClockExistence(TextualConvention, Integer32):
    description = 'This TEXTUAL Convention represents the existence of\n        the clock source.\n\n        clkNotPresent (1): The T1/E1 external clock not present.\n        clkPresent    (2): The T1/E1 external clock present.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("clkNotPresent", 1), ("clkPresent", 2))

class CmpClockImpedance(TextualConvention, Integer32):
    description = 'This Textual Convention provides the impedance on\n        external clock input on PXM-UI-S3 back card.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ohms75", 1), ("ohms100", 2), ("ohms120", 3))

pxmClockConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 3, 16))
pxmPrimaryMuxClockSource = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 1), CmpClockSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimaryMuxClockSource.setStatus('current')
if mibBuilder.loadTexts: pxmPrimaryMuxClockSource.setDescription('This object identifies the source of the\n        Primary Mux Clock for PXM card.')
pxmPrimaryInbandClockSourceLineNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimaryInbandClockSourceLineNumber.setStatus('current')
if mibBuilder.loadTexts: pxmPrimaryInbandClockSourceLineNumber.setDescription('This object indicates the inband line number.\n        This is applicable when pxmPrimaryMuxClockSource is \n        pxmInbandClock1(1) or pxmServiceModuleClock2 (5).')
pxmPrimarySMClockSourceSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPrimarySMClockSourceSlotNumber.setStatus('current')
if mibBuilder.loadTexts: pxmPrimarySMClockSourceSlotNumber.setDescription('This object indicates the service module slot number.\n        This is applicable when pxmPrimaryMuxClockSource is\n        pxmServiceModuleClock1(2) or pxmServiceModuleClock2(6).')
pxmSecondaryMuxClockSource = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 4), CmpClockSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondaryMuxClockSource.setStatus('current')
if mibBuilder.loadTexts: pxmSecondaryMuxClockSource.setDescription('This object identifies the source of the\n        Secondary Mux Clock for PXM card.')
pxmSecondaryInbandClockSourceLineNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondaryInbandClockSourceLineNumber.setStatus('current')
if mibBuilder.loadTexts: pxmSecondaryInbandClockSourceLineNumber.setDescription('This object indicates the inband line number.\n        This is applicable when pxmSecondaryMuxClockSource is \n        pxmInbandClock1(1) or pxmServiceModuleClock2 (5).')
pxmSecondarySMClockSourceSlotNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmSecondarySMClockSourceSlotNumber.setStatus('current')
if mibBuilder.loadTexts: pxmSecondarySMClockSourceSlotNumber.setDescription('This object indicates the service module slot number.\n        This is applicable when pxmSecondaryMuxClockSource is\n        pxmServiceModuleClock1(2) or pxmServiceModuleClock2(6).')
pxmCurrentClock = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 7), CmpCurrentClock()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmCurrentClock.setStatus('current')
if mibBuilder.loadTexts: pxmCurrentClock.setDescription('This object represents the clock source currently \n        selected for PXM card.\n\n        primary(1): The primary clock source is described by\n                    pxmPrimaryMuxClockSource\n        secondary(2): The secondary clock source is described by\n                      pxmSecondaryMuxClockSource.\n        intOscillator(3): Current clock is internal oscillator.')
pxmPreviousClock = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 8), CmpCurrentClock()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmPreviousClock.setStatus('current')
if mibBuilder.loadTexts: pxmPreviousClock.setDescription('This object represents the clock source previously \n        selected for PXM card.')
pxmExtClockPresent = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 9), CmpClockExistence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClockPresent.setStatus('current')
if mibBuilder.loadTexts: pxmExtClockPresent.setDescription('Status of External T1/E1 Clock on PXM card.')
pxmExtClkSrcImpedance = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 10), CmpClockImpedance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClkSrcImpedance.setStatus('current')
if mibBuilder.loadTexts: pxmExtClkSrcImpedance.setDescription('Impedance on external clock input for PXM card.')
pxmExtClkConnectorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 11), CmpClockConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClkConnectorType.setStatus('current')
if mibBuilder.loadTexts: pxmExtClkConnectorType.setDescription('This object describes the type of connector available\n        for connecting the external clock source to the PXM.')
pxmClkStratumLevel = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("stratumUnknown", 1), ("stratumLevel1", 2), ("stratumLevel2", 3), ("stratumLevel3E", 4), ("stratumLevel3", 5), ("stratumLevel4", 6), ("stratumLevel4E", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmClkStratumLevel.setStatus('current')
if mibBuilder.loadTexts: pxmClkStratumLevel.setDescription('This object describes the lowest stratum level\n        provided by the interface the external clock source to\n        the PXM back card.')
pxmClkErrReason = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("goodClk", 1), ("unknownReason", 2), ("noClkSignal", 3), ("freqTooHigh", 4), ("freqTooLow", 5), ("excessiveJitter", 6), ("missingCard", 7), ("missingLogicalIf", 8), ("noClock", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmClkErrReason.setStatus('current')
if mibBuilder.loadTexts: pxmClkErrReason.setDescription('This object gives more information about clock \n        status.\n        The possible values are :\n\n         goodClk(1)         : Clock is good\n         unkownReason(2)    : reason not known\n         noClkSignal(3)     : Loss of signal(LOS) on clock source\n         freqTooHigh(4)     : frequency drifted too high\n         freqTooLow(5)      : frequency drifted too low\n         excessiveJitter(6) : jitter has exceeded the tolerance\n         missingCard    (7) : no clock hardware found\n         missingLogicalIf(8): Logical Interface missing\n                              or not operational\n         noClock         (9): No clock.')
pxmExtClock2Present = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 14), CmpClockExistence()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClock2Present.setStatus('current')
if mibBuilder.loadTexts: pxmExtClock2Present.setDescription('This object indicates the status of external T1/E1 \n        Clock on port 2 of PXMUI-S3 back card.')
pxmExtClk2SrcImpedance = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 15), CmpClockImpedance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClk2SrcImpedance.setStatus('current')
if mibBuilder.loadTexts: pxmExtClk2SrcImpedance.setDescription('This object provides the impedance on external clock \n       input on port 2 of PXMUI-S3 back card.')
pxmExtClk2ConnectorType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 3, 16, 16), CmpClockConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmExtClk2ConnectorType.setStatus('current')
if mibBuilder.loadTexts: pxmExtClk2ConnectorType.setDescription('This object describes the type of connector \n       available for connecting the external clock source \n       to the port 2 of PXM-UI-S3 back card of PXM.')
cmpClockMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2))
cmpClockMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1))
cmpClockMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2))
cmpClockCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 2, 1)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpPrimaryClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpSecondaryClockInfoGroup"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "cmpExtClockInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpClockCompliance = cmpClockCompliance.setStatus('current')
if mibBuilder.loadTexts: cmpClockCompliance.setDescription('The compliance statement for objects related\n        to PXM Clock mib.')
cmpClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 1)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmCurrentClock"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPreviousClock"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkStratumLevel"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmClkErrReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpClockInfoGroup = cmpClockInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cmpClockInfoGroup.setDescription('The collection of objects which are used for\n          providing information on PXM Clock configuration.')
cmpPrimaryClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 2)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryMuxClockSource"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimaryInbandClockSourceLineNumber"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmPrimarySMClockSourceSlotNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpPrimaryClockInfoGroup = cmpPrimaryClockInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cmpPrimaryClockInfoGroup.setDescription('The collection of objects which are used for\n          providing information on Primary Clock configuration.')
cmpSecondaryClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 3)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryMuxClockSource"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondaryInbandClockSourceLineNumber"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmSecondarySMClockSourceSlotNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpSecondaryClockInfoGroup = cmpSecondaryClockInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cmpSecondaryClockInfoGroup.setDescription('The collection of objects which are used for\n          providing information on Secondary Clock configuration.')
cmpExtClockInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 72, 2, 1, 4)).setObjects(("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClockPresent"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkSrcImpedance"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClkConnectorType"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClock2Present"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2SrcImpedance"), ("CISCO-MGX82XX-PXM-CLOCK-MIB", "pxmExtClk2ConnectorType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmpExtClockInfoGroup = cmpExtClockInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cmpExtClockInfoGroup.setDescription('The collection of objects which are used for\n          providing general information on PXM Clock \n          configuration.')
mibBuilder.exportSymbols("CISCO-MGX82XX-PXM-CLOCK-MIB", CmpClockConnectorType=CmpClockConnectorType, CmpClockExistence=CmpClockExistence, CmpClockImpedance=CmpClockImpedance, CmpClockSourceType=CmpClockSourceType, CmpCurrentClock=CmpCurrentClock, PYSNMP_MODULE_ID=ciscoMgx82xxPxmClockMIB, ciscoMgx82xxPxmClockMIB=ciscoMgx82xxPxmClockMIB, cmpClockCompliance=cmpClockCompliance, cmpClockInfoGroup=cmpClockInfoGroup, cmpClockMIBCompliances=cmpClockMIBCompliances, cmpClockMIBConformance=cmpClockMIBConformance, cmpClockMIBGroups=cmpClockMIBGroups, cmpExtClockInfoGroup=cmpExtClockInfoGroup, cmpPrimaryClockInfoGroup=cmpPrimaryClockInfoGroup, cmpSecondaryClockInfoGroup=cmpSecondaryClockInfoGroup, pxmClkErrReason=pxmClkErrReason, pxmClkStratumLevel=pxmClkStratumLevel, pxmClockConfig=pxmClockConfig, pxmCurrentClock=pxmCurrentClock, pxmExtClk2ConnectorType=pxmExtClk2ConnectorType, pxmExtClk2SrcImpedance=pxmExtClk2SrcImpedance, pxmExtClkConnectorType=pxmExtClkConnectorType, pxmExtClkSrcImpedance=pxmExtClkSrcImpedance, pxmExtClock2Present=pxmExtClock2Present, pxmExtClockPresent=pxmExtClockPresent, pxmPreviousClock=pxmPreviousClock, pxmPrimaryInbandClockSourceLineNumber=pxmPrimaryInbandClockSourceLineNumber, pxmPrimaryMuxClockSource=pxmPrimaryMuxClockSource, pxmPrimarySMClockSourceSlotNumber=pxmPrimarySMClockSourceSlotNumber, pxmSecondaryInbandClockSourceLineNumber=pxmSecondaryInbandClockSourceLineNumber, pxmSecondaryMuxClockSource=pxmSecondaryMuxClockSource, pxmSecondarySMClockSourceSlotNumber=pxmSecondarySMClockSourceSlotNumber)
