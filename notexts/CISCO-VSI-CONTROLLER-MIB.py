#
# PySNMP MIB module CISCO-VSI-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-VSI-CONTROLLER-MIB
# Source digest sha256:fe6f33d9e18d84d98153debde8c539f27fe7c33739b24115967bbb0cda25c739
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoVSIControllerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 141))
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setLastUpdated('1999-06-08 00:00')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setOrganization('Cisco Systems, Inc.')
class CvcControllerShelfLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("internal", 1), ("external", 2))

class CvcControllerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("par", 1), ("pnni", 2), ("lsc", 3))

cvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1))
cvcConfController = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1))
cvcConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcConfTable.setStatus('current')
cvcConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerID"))
if mibBuilder.loadTexts: cvcConfEntry.setStatus('current')
cvcConfControllerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcConfControllerID.setStatus('current')
cvcConfControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 2), CvcControllerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerType.setStatus('current')
cvcConfControllerShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 3), CvcControllerShelfLocation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setStatus('current')
cvcConfControllerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerLocation.setStatus('current')
cvcConfControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerName.setStatus('current')
cvcConfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVpi.setStatus('current')
cvcConfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVci.setStatus('current')
cvcConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfRowStatus.setStatus('current')
cvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3))
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroup"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroupExternal"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
cvcConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerType"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerShelfLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerName"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroup = cvcConfGroup.setStatus('current')
cvcConfGroupExternal = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 2)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfVpi"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroupExternal = cvcConfGroupExternal.setStatus('current')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-MIB", CvcControllerShelfLocation=CvcControllerShelfLocation, CvcControllerType=CvcControllerType, PYSNMP_MODULE_ID=ciscoVSIControllerMIB, ciscoVSIControllerMIB=ciscoVSIControllerMIB, cvcConfController=cvcConfController, cvcConfControllerID=cvcConfControllerID, cvcConfControllerLocation=cvcConfControllerLocation, cvcConfControllerName=cvcConfControllerName, cvcConfControllerShelfLocation=cvcConfControllerShelfLocation, cvcConfControllerType=cvcConfControllerType, cvcConfEntry=cvcConfEntry, cvcConfGroup=cvcConfGroup, cvcConfGroupExternal=cvcConfGroupExternal, cvcConfRowStatus=cvcConfRowStatus, cvcConfTable=cvcConfTable, cvcConfVci=cvcConfVci, cvcConfVpi=cvcConfVpi, cvcMIBCompliance=cvcMIBCompliance, cvcMIBCompliances=cvcMIBCompliances, cvcMIBConformance=cvcMIBConformance, cvcMIBGroups=cvcMIBGroups, cvcMIBObjects=cvcMIBObjects)
