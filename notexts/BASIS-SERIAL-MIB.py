#
# PySNMP MIB module BASIS-SERIAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source BASIS-SERIAL-MIB
# Source digest sha256:e4e33240f90575febcf5c5204f8da8f6d3ed63bb1e018b776650559951a328c6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
basisLines, = mibBuilder.importSymbols("BASIS-MIB", "basisLines")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basisSerialMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 69))
basisSerialMIB.setRevisions(('2003-05-03 00:00',))
if mibBuilder.loadTexts: basisSerialMIB.setLastUpdated('2003-05-03 00:00')
if mibBuilder.loadTexts: basisSerialMIB.setOrganization('Cisco Systems, Inc.')
serialInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 4, 1))
serialPortNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNumOfValidEntries.setStatus('current')
serialInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: serialInterfaceTable.setStatus('current')
serialInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "BASIS-SERIAL-MIB", "serialPortNum"))
if mibBuilder.loadTexts: serialInterfaceEntry.setStatus('current')
serialPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortNum.setStatus('current')
serialPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("main", 1), ("debug", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialPortType.setStatus('current')
serialPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortEnable.setStatus('current')
serialPortbps = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bps9600", 1), ("bps2400", 2), ("bps19200", 3))).clone('bps9600')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: serialPortbps.setStatus('current')
basisSerialMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2))
basisSerialMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1))
basisSerialMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2))
basisSerialCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2, 1)).setObjects(("BASIS-SERIAL-MIB", "basisSerialConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialCompliance = basisSerialCompliance.setStatus('current')
basisSerialConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1, 1)).setObjects(("BASIS-SERIAL-MIB", "serialPortNumOfValidEntries"), ("BASIS-SERIAL-MIB", "serialPortNum"), ("BASIS-SERIAL-MIB", "serialPortType"), ("BASIS-SERIAL-MIB", "serialPortEnable"), ("BASIS-SERIAL-MIB", "serialPortbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basisSerialConfGroup = basisSerialConfGroup.setStatus('current')
mibBuilder.exportSymbols("BASIS-SERIAL-MIB", PYSNMP_MODULE_ID=basisSerialMIB, basisSerialCompliance=basisSerialCompliance, basisSerialConfGroup=basisSerialConfGroup, basisSerialMIB=basisSerialMIB, basisSerialMIBCompliances=basisSerialMIBCompliances, basisSerialMIBConformance=basisSerialMIBConformance, basisSerialMIBGroups=basisSerialMIBGroups, serialInterface=serialInterface, serialInterfaceEntry=serialInterfaceEntry, serialInterfaceTable=serialInterfaceTable, serialPortEnable=serialPortEnable, serialPortNum=serialPortNum, serialPortNumOfValidEntries=serialPortNumOfValidEntries, serialPortType=serialPortType, serialPortbps=serialPortbps)
