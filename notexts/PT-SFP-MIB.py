#
# PySNMP MIB module PT-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-SFP-MIB
# Produced by pysmi-1.1.8 at Thu Feb  9 12:01:13 2023
# On host fv-az173-80 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalEntry, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, iso, Counter64, IpAddress, TimeTicks, Bits, ObjectIdentity, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter64", "IpAddress", "TimeTicks", "Bits", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ptSFP = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 6))
ptSFP.setRevisions(('2016-05-22 10:30',))
if mibBuilder.loadTexts: ptSFP.setLastUpdated('201605221030Z')
if mibBuilder.loadTexts: ptSFP.setOrganization('Ericsson')
ptSFPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2))
class PortInterfaceTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55))
    namedValues = NamedValues(("eNONE", 1), ("eUNKNOWN", 2), ("e100BASELX10", 5), ("e100BASEFX", 7), ("e1000BASET", 8), ("e1000BASEZX", 10), ("e1000BASELX10", 11), ("eS11", 12), ("eS11E", 13), ("eL11", 14), ("eL12", 15), ("eS41", 16), ("eL41", 17), ("eL42", 18), ("eL42CWDM32DB", 19), ("eS161", 20), ("eL161", 21), ("eL162", 22), ("eL162CWDM32DB", 23), ("eL12CWDM28DB", 24), ("e1000BASESX", 25), ("e1000BASECWDM32DB", 26), ("e1000BASECWDM28DB", 27), ("eL12CWDM32DB", 29), ("e10GBASELRLW", 30), ("e10GBASEEREW", 31), ("e10GBASEZpRZpW", 32), ("eL42CWDM28DB", 33), ("eL162CWDM28DB", 34), ("eMULTIRATECWDM28DB", 35), ("eMULTIRATECWDM32DB", 36), ("eMULTIRATES11S41", 37), ("e100BASEBX10U", 38), ("e100BASEBX10D", 39), ("e1000BASEBX10U", 40), ("e1000BASEBX10D", 41), ("e10GBASESX", 42), ("e10GBASELH", 43), ("eSTM1SFWD", 44), ("eSTM1SFWU", 45), ("eSTM4SFWD", 46), ("eSTM4SFWU", 47), ("e1000BASELX", 48), ("e10GBASESRSW", 49), ("e1000BASETFIXED", 50), ("e1000BASEBX20U", 51), ("e1000BASEBX20D", 52), ("e10GBASEDWDM", 53), ("eDWDMSFPHP", 54), ("eUNRECOGNIZEDSFP", 55))

class InstallStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("eEMPTY", 1), ("eNOTINSTALLED", 2), ("eINSTALLEDANDNOTPROVISIONED", 3), ("eINSTALLEDANDPROVISIONED", 4), ("eUNAVAILABLE", 5), ("eUNKNOWN", 6))

class WaveLengthTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53))
    namedValues = NamedValues(("eNA", 1), ("eUNKNOWN", 2), ("e1471", 3), ("e1491", 4), ("e1511", 5), ("e1531", 6), ("e1551", 7), ("e1571", 8), ("e1591", 9), ("e1611", 10), ("eNOTPROVISIONED", 11), ("e1311", 12), ("e1560d6", 13), ("e1559d8", 14), ("e1559d0", 15), ("e1558d2", 16), ("e1557d4", 17), ("e1556d6", 18), ("e1555d8", 19), ("e1554d9", 20), ("e1554d1", 21), ("e1553d3", 22), ("e1552d5", 23), ("e1551d7", 24), ("e1550d9", 25), ("e1550d1", 26), ("e1549d3", 27), ("e1548d5", 28), ("e1547d7", 29), ("e1546d9", 30), ("e1546d1", 31), ("e1545d3", 32), ("e1544d5", 33), ("e1543d7", 34), ("e1542d9", 35), ("e1542d1", 36), ("e1541d4", 37), ("e1540d6", 38), ("e1539d8", 39), ("e1539d0", 40), ("e1538d2", 41), ("e1537d4", 42), ("e1536d6", 43), ("e1535d8", 44), ("e1535d0", 45), ("e1534d3", 46), ("e1533d5", 47), ("e1532d7", 48), ("e1531d9", 49), ("e1531d1", 50), ("e1530d3", 51), ("e1529d6", 52), ("e850", 53))

class ConnectorTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("eUNKNOWNORUNSPECIFIED", 1), ("eSC", 2), ("eFIBERCHANNELSTYLE1COPPER", 3), ("eFIBERCHANNELSTYLE2COPPER", 4), ("eBNCTNC", 5), ("eFIBERCHANNELCOAXIALHEADERS", 6), ("eFIBERJACK", 7), ("eLC", 8), ("eMTRT", 9), ("eMU", 10), ("eSG", 11), ("eOPTICALPIGTAIL", 12), ("eRESERVED", 13), ("eHSSDCII", 14), ("eCOPPERPIGTAIL", 15), ("eVENDORSPECIFIC", 16))

ptSFPTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1), )
if mibBuilder.loadTexts: ptSFPTable.setStatus('current')
ptSFPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1), )
entPhysicalEntry.registerAugmentions(("PT-SFP-MIB", "ptSFPEntry"))
ptSFPEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: ptSFPEntry.setStatus('current')
installedSFP = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 1), PortInterfaceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSFP.setStatus('current')
installState = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 2), InstallStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installState.setStatus('current')
vendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
vendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorOui.setStatus('current')
vendorPn = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorPn.setStatus('current')
vendorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorRev.setStatus('current')
vendorSn = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorSn.setStatus('current')
saleableEntityCode = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saleableEntityCode.setStatus('current')
connectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 9), ConnectorTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectorType.setStatus('current')
installedWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 10), WaveLengthTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedWavelength.setStatus('current')
levelRx = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: levelRx.setStatus('current')
rxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxPower.setStatus('current')
txPower = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
brNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brNominal.setStatus('current')
length9m1km = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length9m1km.setStatus('current')
length9m100m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length9m100m.setStatus('current')
length50m10m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length50m10m.setStatus('current')
length62m10m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length62m10m.setStatus('current')
lengthCopper1m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lengthCopper1m.setStatus('current')
temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
vcc = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcc.setStatus('current')
biasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biasCurrent.setStatus('current')
ptSFPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 1))
ptSFPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 2))
ptSFPFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 1, 1)).setObjects(("PT-SFP-MIB", "ptSFPCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptSFPFullCompliance = ptSFPFullCompliance.setStatus('current')
ptSFPCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 2, 1)).setObjects(("PT-SFP-MIB", "installedSFP"), ("PT-SFP-MIB", "installState"), ("PT-SFP-MIB", "installedWavelength"), ("PT-SFP-MIB", "levelRx"), ("PT-SFP-MIB", "vendorName"), ("PT-SFP-MIB", "vendorOui"), ("PT-SFP-MIB", "vendorPn"), ("PT-SFP-MIB", "vendorRev"), ("PT-SFP-MIB", "connectorType"), ("PT-SFP-MIB", "brNominal"), ("PT-SFP-MIB", "length9m1km"), ("PT-SFP-MIB", "length9m100m"), ("PT-SFP-MIB", "length50m10m"), ("PT-SFP-MIB", "length62m10m"), ("PT-SFP-MIB", "lengthCopper1m"), ("PT-SFP-MIB", "saleableEntityCode"), ("PT-SFP-MIB", "vendorSn"), ("PT-SFP-MIB", "rxPower"), ("PT-SFP-MIB", "txPower"), ("PT-SFP-MIB", "temperature"), ("PT-SFP-MIB", "vcc"), ("PT-SFP-MIB", "biasCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptSFPCompleteGroup = ptSFPCompleteGroup.setStatus('current')
mibBuilder.exportSymbols("PT-SFP-MIB", ptSFPCompliances=ptSFPCompliances, length62m10m=length62m10m, vcc=vcc, saleableEntityCode=saleableEntityCode, vendorOui=vendorOui, ptSFPConformance=ptSFPConformance, connectorType=connectorType, levelRx=levelRx, ptSFPTable=ptSFPTable, lengthCopper1m=lengthCopper1m, brNominal=brNominal, ptSFPCompleteGroup=ptSFPCompleteGroup, ptSFPFullCompliance=ptSFPFullCompliance, vendorRev=vendorRev, vendorSn=vendorSn, length50m10m=length50m10m, installState=installState, installedWavelength=installedWavelength, InstallStateTC=InstallStateTC, PortInterfaceTC=PortInterfaceTC, vendorName=vendorName, biasCurrent=biasCurrent, ptSFPGroups=ptSFPGroups, ConnectorTypeTC=ConnectorTypeTC, installedSFP=installedSFP, ptSFP=ptSFP, rxPower=rxPower, WaveLengthTC=WaveLengthTC, length9m100m=length9m100m, temperature=temperature, PYSNMP_MODULE_ID=ptSFP, txPower=txPower, ptSFPEntry=ptSFPEntry, vendorPn=vendorPn, length9m1km=length9m1km)
