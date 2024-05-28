#
# PySNMP MIB module PT-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-SFP-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:34:27 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
entPhysicalEntry, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry")
pt, = mibBuilder.importSymbols("PT-MIB", "pt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, TimeTicks, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Integer32, ObjectIdentity, iso, ModuleIdentity, Bits, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Integer32", "ObjectIdentity", "iso", "ModuleIdentity", "Bits", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ptSFP = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2, 6))
ptSFP.setRevisions(('2016-05-22 10:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ptSFP.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: ptSFP.setLastUpdated('201605221030Z')
if mibBuilder.loadTexts: ptSFP.setOrganization('Ericsson')
if mibBuilder.loadTexts: ptSFP.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: ptSFP.setDescription('This is the MIB of PT SFP specifics. Most entries are read from the SFP itself according to SFF-8472')
ptSFPConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2))
class PortInterfaceTC(TextualConvention, Integer32):
    description = 'An integer which indicates the type of PORT_INTERFACE. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55))
    namedValues = NamedValues(("eNONE", 1), ("eUNKNOWN", 2), ("e100BASELX10", 5), ("e100BASEFX", 7), ("e1000BASET", 8), ("e1000BASEZX", 10), ("e1000BASELX10", 11), ("eS11", 12), ("eS11E", 13), ("eL11", 14), ("eL12", 15), ("eS41", 16), ("eL41", 17), ("eL42", 18), ("eL42CWDM32DB", 19), ("eS161", 20), ("eL161", 21), ("eL162", 22), ("eL162CWDM32DB", 23), ("eL12CWDM28DB", 24), ("e1000BASESX", 25), ("e1000BASECWDM32DB", 26), ("e1000BASECWDM28DB", 27), ("eL12CWDM32DB", 29), ("e10GBASELRLW", 30), ("e10GBASEEREW", 31), ("e10GBASEZpRZpW", 32), ("eL42CWDM28DB", 33), ("eL162CWDM28DB", 34), ("eMULTIRATECWDM28DB", 35), ("eMULTIRATECWDM32DB", 36), ("eMULTIRATES11S41", 37), ("e100BASEBX10U", 38), ("e100BASEBX10D", 39), ("e1000BASEBX10U", 40), ("e1000BASEBX10D", 41), ("e10GBASESX", 42), ("e10GBASELH", 43), ("eSTM1SFWD", 44), ("eSTM1SFWU", 45), ("eSTM4SFWD", 46), ("eSTM4SFWU", 47), ("e1000BASELX", 48), ("e10GBASESRSW", 49), ("e1000BASETFIXED", 50), ("e1000BASEBX20U", 51), ("e1000BASEBX20D", 52), ("e10GBASEDWDM", 53), ("eDWDMSFPHP", 54), ("eUNRECOGNIZEDSFP", 55))

class InstallStateTC(TextualConvention, Integer32):
    description = 'An integer which indicates the type of INSTALL_STATE.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("eEMPTY", 1), ("eNOTINSTALLED", 2), ("eINSTALLEDANDNOTPROVISIONED", 3), ("eINSTALLEDANDPROVISIONED", 4), ("eUNAVAILABLE", 5), ("eUNKNOWN", 6))

class WaveLengthTC(TextualConvention, Integer32):
    description = 'An integer which indicates the type of WAVELENGTH. d is for the decimal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53))
    namedValues = NamedValues(("eNA", 1), ("eUNKNOWN", 2), ("e1471", 3), ("e1491", 4), ("e1511", 5), ("e1531", 6), ("e1551", 7), ("e1571", 8), ("e1591", 9), ("e1611", 10), ("eNOTPROVISIONED", 11), ("e1311", 12), ("e1560d6", 13), ("e1559d8", 14), ("e1559d0", 15), ("e1558d2", 16), ("e1557d4", 17), ("e1556d6", 18), ("e1555d8", 19), ("e1554d9", 20), ("e1554d1", 21), ("e1553d3", 22), ("e1552d5", 23), ("e1551d7", 24), ("e1550d9", 25), ("e1550d1", 26), ("e1549d3", 27), ("e1548d5", 28), ("e1547d7", 29), ("e1546d9", 30), ("e1546d1", 31), ("e1545d3", 32), ("e1544d5", 33), ("e1543d7", 34), ("e1542d9", 35), ("e1542d1", 36), ("e1541d4", 37), ("e1540d6", 38), ("e1539d8", 39), ("e1539d0", 40), ("e1538d2", 41), ("e1537d4", 42), ("e1536d6", 43), ("e1535d8", 44), ("e1535d0", 45), ("e1534d3", 46), ("e1533d5", 47), ("e1532d7", 48), ("e1531d9", 49), ("e1531d1", 50), ("e1530d3", 51), ("e1529d6", 52), ("e850", 53))

class ConnectorTypeTC(TextualConvention, Integer32):
    description = 'An integer which indicates the type of CONNECTOR_TYPE according SFF-8024.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("eUNKNOWNORUNSPECIFIED", 1), ("eSC", 2), ("eFIBERCHANNELSTYLE1COPPER", 3), ("eFIBERCHANNELSTYLE2COPPER", 4), ("eBNCTNC", 5), ("eFIBERCHANNELCOAXIALHEADERS", 6), ("eFIBERJACK", 7), ("eLC", 8), ("eMTRT", 9), ("eMU", 10), ("eSG", 11), ("eOPTICALPIGTAIL", 12), ("eRESERVED", 13), ("eHSSDCII", 14), ("eCOPPERPIGTAIL", 15), ("eVENDORSPECIFIC", 16))

ptSFPTable = MibTable((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1), )
if mibBuilder.loadTexts: ptSFPTable.setStatus('current')
if mibBuilder.loadTexts: ptSFPTable.setDescription('An table of SFP Table entries.')
ptSFPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1), )
entPhysicalEntry.registerAugmentions(("PT-SFP-MIB", "ptSFPEntry"))
ptSFPEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: ptSFPEntry.setStatus('current')
if mibBuilder.loadTexts: ptSFPEntry.setDescription('An entry of PT SFP application.')
installedSFP = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 1), PortInterfaceTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedSFP.setStatus('current')
if mibBuilder.loadTexts: installedSFP.setDescription('Type of the inserted module, see textual convention')
installState = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 2), InstallStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installState.setStatus('current')
if mibBuilder.loadTexts: installState.setDescription('Status of the inserted module, see textual convention')
vendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
if mibBuilder.loadTexts: vendorName.setDescription('SFP vendor name as reported by the SFP')
vendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorOui.setStatus('current')
if mibBuilder.loadTexts: vendorOui.setDescription('SFP vendor IEEE company ID as reported by the SFP')
vendorPn = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorPn.setStatus('current')
if mibBuilder.loadTexts: vendorPn.setDescription('Part number provided by SFP vendor (ASCII) as reported by the SFP')
vendorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorRev.setStatus('current')
if mibBuilder.loadTexts: vendorRev.setDescription('Revision level for part number provided by vendor (ASCII) as reported by the SFP')
vendorSn = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorSn.setStatus('current')
if mibBuilder.loadTexts: vendorSn.setDescription('Serial number provided by vendor (ASCII) as reported by the SFP')
saleableEntityCode = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: saleableEntityCode.setStatus('current')
if mibBuilder.loadTexts: saleableEntityCode.setDescription("Propriety product name as reported by the SFP's Vendor Specific EEPROM")
connectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 9), ConnectorTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: connectorType.setStatus('current')
if mibBuilder.loadTexts: connectorType.setDescription('An integer which indicates the type of CONNECTOR_TYPE according SFF-8024. See also textual convention')
installedWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 10), WaveLengthTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedWavelength.setStatus('current')
if mibBuilder.loadTexts: installedWavelength.setDescription('An integer that in case of an optical SFP, is the laser wavelength in nm. See also textual convention.')
levelRx = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: levelRx.setStatus('current')
if mibBuilder.loadTexts: levelRx.setDescription('The input level in dBm (optical interfaces only). The value is an offset. The value 100 represents 0 dBm. The value 50 represents no signal.')
rxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxPower.setStatus('current')
if mibBuilder.loadTexts: rxPower.setDescription('The received light power, in dBm.')
txPower = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: txPower.setStatus('current')
if mibBuilder.loadTexts: txPower.setDescription('The transmit light power, in dBm.')
brNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brNominal.setStatus('current')
if mibBuilder.loadTexts: brNominal.setDescription('The nominal bit rate, in units of 100 Mbps.')
length9m1km = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length9m1km.setStatus('current')
if mibBuilder.loadTexts: length9m1km.setDescription('Link length supported for 9/125 um single fiber, units of 1 km')
length9m100m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length9m100m.setStatus('current')
if mibBuilder.loadTexts: length9m100m.setDescription('Link length supported for 9/125 um single fiber, units of 100 m')
length50m10m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length50m10m.setStatus('current')
if mibBuilder.loadTexts: length50m10m.setDescription('Link length supported for 50/125 um OM2 fiber, units of 10 m')
length62m10m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: length62m10m.setStatus('current')
if mibBuilder.loadTexts: length62m10m.setDescription('Link length supported for 62.5/125 um OM1 fiber, units of 10 m ')
lengthCopper1m = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lengthCopper1m.setStatus('current')
if mibBuilder.loadTexts: lengthCopper1m.setDescription('Link length supported for copper or direct attach cable, units of m ')
temperature = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('The SFP module temperature, in degree Celsius')
vcc = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcc.setStatus('current')
if mibBuilder.loadTexts: vcc.setDescription('The supply voltage of the interface module, in V.')
biasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biasCurrent.setStatus('current')
if mibBuilder.loadTexts: biasCurrent.setDescription('The bias current of the interface module, in mA.')
ptSFPCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 1))
ptSFPGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 2))
ptSFPFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 1, 1)).setObjects(("PT-SFP-MIB", "ptSFPCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptSFPFullCompliance = ptSFPFullCompliance.setStatus('current')
if mibBuilder.loadTexts: ptSFPFullCompliance.setDescription('The compliance statement for SNMP entities which implement everything.')
ptSFPCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 6, 2, 2, 1)).setObjects(("PT-SFP-MIB", "installedSFP"), ("PT-SFP-MIB", "installState"), ("PT-SFP-MIB", "installedWavelength"), ("PT-SFP-MIB", "levelRx"), ("PT-SFP-MIB", "vendorName"), ("PT-SFP-MIB", "vendorOui"), ("PT-SFP-MIB", "vendorPn"), ("PT-SFP-MIB", "vendorRev"), ("PT-SFP-MIB", "connectorType"), ("PT-SFP-MIB", "brNominal"), ("PT-SFP-MIB", "length9m1km"), ("PT-SFP-MIB", "length9m100m"), ("PT-SFP-MIB", "length50m10m"), ("PT-SFP-MIB", "length62m10m"), ("PT-SFP-MIB", "lengthCopper1m"), ("PT-SFP-MIB", "saleableEntityCode"), ("PT-SFP-MIB", "vendorSn"), ("PT-SFP-MIB", "rxPower"), ("PT-SFP-MIB", "txPower"), ("PT-SFP-MIB", "temperature"), ("PT-SFP-MIB", "vcc"), ("PT-SFP-MIB", "biasCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptSFPCompleteGroup = ptSFPCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: ptSFPCompleteGroup.setDescription('A collection of all current objects in this MIB module.')
mibBuilder.exportSymbols("PT-SFP-MIB", installedSFP=installedSFP, length9m100m=length9m100m, length50m10m=length50m10m, rxPower=rxPower, WaveLengthTC=WaveLengthTC, txPower=txPower, vendorOui=vendorOui, ptSFPTable=ptSFPTable, InstallStateTC=InstallStateTC, ptSFPEntry=ptSFPEntry, installedWavelength=installedWavelength, vendorName=vendorName, length62m10m=length62m10m, ptSFPCompleteGroup=ptSFPCompleteGroup, lengthCopper1m=lengthCopper1m, installState=installState, PYSNMP_MODULE_ID=ptSFP, brNominal=brNominal, vendorRev=vendorRev, levelRx=levelRx, vendorPn=vendorPn, ConnectorTypeTC=ConnectorTypeTC, temperature=temperature, vendorSn=vendorSn, ptSFPGroups=ptSFPGroups, ptSFPFullCompliance=ptSFPFullCompliance, PortInterfaceTC=PortInterfaceTC, ptSFP=ptSFP, saleableEntityCode=saleableEntityCode, length9m1km=length9m1km, connectorType=connectorType, ptSFPCompliances=ptSFPCompliances, ptSFPConformance=ptSFPConformance, biasCurrent=biasCurrent, vcc=vcc)
