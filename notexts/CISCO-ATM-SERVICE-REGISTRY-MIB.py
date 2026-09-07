#
# PySNMP MIB module CISCO-ATM-SERVICE-REGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-SERVICE-REGISTRY-MIB
# Source digest sha256:897e694926dcf4158d0c9b0d0bdac39ebd1bef7e2de44412e14a11d18326a1b7
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmServiceRegistryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 50))
ciscoAtmServiceRegistryMIB.setRevisions(('1996-02-04 00:00',))
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setLastUpdated('1996-02-21 00:00')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmServiceRegistryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 1))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

asrSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegTable.setStatus('current')
asrSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegPort"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegServiceID"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegAddressIndex"))
if mibBuilder.loadTexts: asrSrvcRegEntry.setStatus('current')
asrSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegPort.setStatus('current')
asrSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegServiceID.setStatus('current')
asrSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 3), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setStatus('current')
asrSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 4), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setStatus('current')
asrSrvcRegParm1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegParm1.setStatus('current')
asrSrvcRegRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setStatus('current')
asrSrvcRegMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3))
asrSrvcRegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1))
asrSrvcRegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2))
asrSrvcRegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBCompliance = asrSrvcRegMIBCompliance.setStatus('current')
asrSrvcRegMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegATMAddress"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegParm1"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBGroup = asrSrvcRegMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SERVICE-REGISTRY-MIB", AtmAddr=AtmAddr, InterfaceIndexOrZero=InterfaceIndexOrZero, PYSNMP_MODULE_ID=ciscoAtmServiceRegistryMIB, asrSrvcRegATMAddress=asrSrvcRegATMAddress, asrSrvcRegAddressIndex=asrSrvcRegAddressIndex, asrSrvcRegEntry=asrSrvcRegEntry, asrSrvcRegMIBCompliance=asrSrvcRegMIBCompliance, asrSrvcRegMIBCompliances=asrSrvcRegMIBCompliances, asrSrvcRegMIBConformance=asrSrvcRegMIBConformance, asrSrvcRegMIBGroup=asrSrvcRegMIBGroup, asrSrvcRegMIBGroups=asrSrvcRegMIBGroups, asrSrvcRegParm1=asrSrvcRegParm1, asrSrvcRegPort=asrSrvcRegPort, asrSrvcRegRowStatus=asrSrvcRegRowStatus, asrSrvcRegServiceID=asrSrvcRegServiceID, asrSrvcRegTable=asrSrvcRegTable, ciscoAtmServiceRegistryMIB=ciscoAtmServiceRegistryMIB, ciscoAtmServiceRegistryMIBObjects=ciscoAtmServiceRegistryMIBObjects)
