#
# PySNMP MIB module CISCO-ATM-CONN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-CONN-INFO-MIB
# Source digest sha256:1ef13ab0f546895463b5f1d960eeb2c26a813b3296d341cc002e02ea018ea4a4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmConnInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAtmConnInfoMIB.setRevisions(('2003-06-16 00:00',))
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setLastUpdated('2003-06-16 00:00')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setOrganization('Cisco Systems, Inc.')
caciMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
caciMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
caciAtmConnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
caciIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1))
caciP2pConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2))
caciP2pEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3))
caciP2pIntEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4))
caciP2mpConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5))
caciGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6))
class CaciGeneralConnEPCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2p", 1), ("caciP2mpR", 2), ("caciP2mpL", 3), ("caciP2mpPty", 4))

class CaciP2pConnCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSvcc", 1), ("caciP2pSvpc", 2), ("caciP2pSpvcD", 3), ("caciP2pSpvpD", 4), ("caciP2pSpvcR", 5), ("caciP2pSpvpR", 6))

class CaciP2pEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSpvcRPEP", 1), ("caciP2pSpvcRNPEP", 2), ("caciP2pSpvpRPEP", 3), ("caciP2pSpvpRNPEP", 4), ("caciP2pSpvcDEP", 5), ("caciP2pSpvpDEP", 6))

class CaciP2pIntEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2pSvccIntEP", 1), ("caciP2pSvpcIntEP", 2), ("caciP2pSpvcRIntEP", 3), ("caciP2pSpvpRIntEP", 4))

class CaciP2mpConnCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("caciP2mpSvcRoot", 1), ("caciP2mpSvcLeaf", 2), ("caciP2mpSvcParty", 3), ("caciP2mpSvpcRoot", 4), ("caciP2mpSvpcLeaf", 5), ("caciP2mpSvpcParty", 6), ("caciP2mpSpvcP", 7), ("caciP2mpSpvcNP", 8), ("caciP2mpSpvcAct", 9), ("caciP2mpSpvpP", 10), ("caciP2mpSpvpNP", 11), ("caciP2mpSpvpAct", 12), ("caciP2mpSpvcPaP", 13), ("caciP2mpSpvcPaAct", 14), ("caciP2mpSpvpPaP", 15), ("caciP2mpSpvpPaAct", 16))

class CaciATMEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciTotalSpvc", 1), ("caciP2pTotalInt", 2), ("caciTotalMaster", 3), ("caciTotalSlave", 4))

caciP2pTotalConfConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfConns.setStatus('current')
caciP2pMaxPossibleConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setStatus('current')
caciMaxPossibleEndpoints = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setStatus('current')
caciGenericEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciGenericEndpointTable.setStatus('current')
caciGenericEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciATMEndpointCategory"))
if mibBuilder.loadTexts: caciGenericEndpointEntry.setStatus('current')
caciATMEndpointCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 1), CaciATMEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciATMEndpointCategory.setStatus('current')
caciTotalEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciTotalEndpoints.setStatus('current')
caciConnInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciConnInfoTable.setStatus('current')
caciConnInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-CONN-INFO-MIB", "caciGeneralConnEPCategory"))
if mibBuilder.loadTexts: caciConnInfoEntry.setStatus('current')
caciGeneralConnEPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 1), CaciGeneralConnEPCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setStatus('current')
caciNumUsedConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciNumUsedConns.setStatus('current')
caciP2pConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pConnTable.setStatus('current')
caciP2pConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pConnectionCategory"))
if mibBuilder.loadTexts: caciP2pConnEntry.setStatus('current')
caciP2pConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 1), CaciP2pConnCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pConnectionCategory.setStatus('current')
caciP2pTotalConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConns.setStatus('current')
caciP2pEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pEndpointTable.setStatus('current')
caciP2pEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pEndptCategory"))
if mibBuilder.loadTexts: caciP2pEndpointEntry.setStatus('current')
caciP2pEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 1), CaciP2pEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pEndptCategory.setStatus('current')
caciP2pTotalConfEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setStatus('current')
caciP2pIntEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setStatus('current')
caciP2pIntEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pIntEndptCategory"))
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setStatus('current')
caciP2pIntEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 1), CaciP2pIntEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setStatus('current')
caciP2pTotalIntEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setStatus('current')
caciP2mpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2mpConnTable.setStatus('current')
caciP2mpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2mpConnectionCategory"))
if mibBuilder.loadTexts: caciP2mpConnEntry.setStatus('current')
caciP2mpConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 1), CaciP2mpConnCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setStatus('current')
caciP2mpTotalConfConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setStatus('current')
ciscoAtmConnInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAtmConnInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAtmConnInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAtmConnInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "ciscoConnInfoConfMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pIntEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2mpConnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmConnInfoMIBCompliance = ciscoAtmConnInfoMIBCompliance.setStatus('current')
ciscoConnInfoConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciNumUsedConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConnInfoConfMIBGroup = ciscoConnInfoConfMIBGroup.setStatus('current')
ciscoP2pConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pConnsMIBGroup = ciscoP2pConnsMIBGroup.setStatus('current')
ciscoP2pEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pEndpointsMIBGroup = ciscoP2pEndpointsMIBGroup.setStatus('current')
ciscoP2pIntEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalIntEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pIntEndpointsMIBGroup = ciscoP2pIntEndpointsMIBGroup.setStatus('current')
ciscoP2mpConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 5)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2mpTotalConfConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2mpConnsMIBGroup = ciscoP2mpConnsMIBGroup.setStatus('current')
ciscoTotalConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 6)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfConns"), ("CISCO-ATM-CONN-INFO-MIB", "caciP2pMaxPossibleConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalConnsMIBGroup = ciscoTotalConnsMIBGroup.setStatus('current')
ciscoTotalEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 7)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciMaxPossibleEndpoints"), ("CISCO-ATM-CONN-INFO-MIB", "caciTotalEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalEndpointsMIBGroup = ciscoTotalEndpointsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-CONN-INFO-MIB", CaciATMEndpointCategory=CaciATMEndpointCategory, CaciGeneralConnEPCategory=CaciGeneralConnEPCategory, CaciP2mpConnCategory=CaciP2mpConnCategory, CaciP2pConnCategory=CaciP2pConnCategory, CaciP2pEndpointCategory=CaciP2pEndpointCategory, CaciP2pIntEndpointCategory=CaciP2pIntEndpointCategory, PYSNMP_MODULE_ID=ciscoAtmConnInfoMIB, caciATMEndpointCategory=caciATMEndpointCategory, caciAtmConnInfo=caciAtmConnInfo, caciConnInfoEntry=caciConnInfoEntry, caciConnInfoTable=caciConnInfoTable, caciGeneralConnEPCategory=caciGeneralConnEPCategory, caciGeneric=caciGeneric, caciGenericEndpointEntry=caciGenericEndpointEntry, caciGenericEndpointTable=caciGenericEndpointTable, caciIfInfo=caciIfInfo, caciMIBNotifications=caciMIBNotifications, caciMIBObjects=caciMIBObjects, caciMaxPossibleEndpoints=caciMaxPossibleEndpoints, caciNumUsedConns=caciNumUsedConns, caciP2mpConnEntry=caciP2mpConnEntry, caciP2mpConnTable=caciP2mpConnTable, caciP2mpConnectionCategory=caciP2mpConnectionCategory, caciP2mpConns=caciP2mpConns, caciP2mpTotalConfConns=caciP2mpTotalConfConns, caciP2pConnEntry=caciP2pConnEntry, caciP2pConnTable=caciP2pConnTable, caciP2pConnectionCategory=caciP2pConnectionCategory, caciP2pConns=caciP2pConns, caciP2pEndpointEntry=caciP2pEndpointEntry, caciP2pEndpointTable=caciP2pEndpointTable, caciP2pEndpoints=caciP2pEndpoints, caciP2pEndptCategory=caciP2pEndptCategory, caciP2pIntEndpointEntry=caciP2pIntEndpointEntry, caciP2pIntEndpointTable=caciP2pIntEndpointTable, caciP2pIntEndpoints=caciP2pIntEndpoints, caciP2pIntEndptCategory=caciP2pIntEndptCategory, caciP2pMaxPossibleConns=caciP2pMaxPossibleConns, caciP2pTotalConfConns=caciP2pTotalConfConns, caciP2pTotalConfEndpoints=caciP2pTotalConfEndpoints, caciP2pTotalConns=caciP2pTotalConns, caciP2pTotalIntEndpoints=caciP2pTotalIntEndpoints, caciTotalEndpoints=caciTotalEndpoints, ciscoAtmConnInfoMIB=ciscoAtmConnInfoMIB, ciscoAtmConnInfoMIBCompliance=ciscoAtmConnInfoMIBCompliance, ciscoAtmConnInfoMIBCompliances=ciscoAtmConnInfoMIBCompliances, ciscoAtmConnInfoMIBConformance=ciscoAtmConnInfoMIBConformance, ciscoAtmConnInfoMIBGroups=ciscoAtmConnInfoMIBGroups, ciscoConnInfoConfMIBGroup=ciscoConnInfoConfMIBGroup, ciscoP2mpConnsMIBGroup=ciscoP2mpConnsMIBGroup, ciscoP2pConnsMIBGroup=ciscoP2pConnsMIBGroup, ciscoP2pEndpointsMIBGroup=ciscoP2pEndpointsMIBGroup, ciscoP2pIntEndpointsMIBGroup=ciscoP2pIntEndpointsMIBGroup, ciscoTotalConnsMIBGroup=ciscoTotalConnsMIBGroup, ciscoTotalEndpointsMIBGroup=ciscoTotalEndpointsMIBGroup)
