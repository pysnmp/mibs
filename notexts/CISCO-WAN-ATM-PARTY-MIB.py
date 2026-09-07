#
# PySNMP MIB module CISCO-WAN-ATM-PARTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-WAN-ATM-PARTY-MIB
# Source digest sha256:1c751f1b2fb67edcdf6a64d03eeecd456834218bec6dc208974b7cca27822a35
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
ciscoWanAtmPartyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99998))
ciscoWanAtmPartyMIB.setRevisions(('2002-06-17 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setLastUpdated('2002-06-17 00:00')
if mibBuilder.loadTexts: ciscoWanAtmPartyMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanAtmPartyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 0))
ciscoWanAtmPartyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1))
cwapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1))
ciscoWanAtmPartyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2))
class WanPartyAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WanPartyOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("fail", 2))

class WanNsapAtmAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

cwapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapConfigTable.setStatus('current')
cwapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVpi"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapRootVci"), (0, "CISCO-WAN-ATM-PARTY-MIB", "cwapReference"))
if mibBuilder.loadTexts: cwapConfigEntry.setStatus('current')
cwapRootVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapRootVpi.setStatus('current')
cwapRootVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapRootVci.setStatus('current')
cwapReference = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cwapReference.setStatus('current')
cwapNSAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 4), WanNsapAtmAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapNSAPAddress.setStatus('current')
cwapVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVpi.setStatus('current')
cwapVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapVci.setStatus('current')
cwapReroute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapReroute.setStatus('current')
cwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 8), WanPartyAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapAdminStatus.setStatus('current')
cwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 9), WanPartyOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapOperStatus.setStatus('current')
cwapIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapIdentifier.setStatus('current')
cwapUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapUploadCounter.setStatus('current')
cwapRootPhysicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwapRootPhysicalId.setStatus('current')
cwapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99998, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwapRowStatus.setStatus('current')
ciscoWanAtmPartyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1))
ciscoWanAtmPartyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2))
ciscoWanAtmPartyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "ciscoWanAtmPartyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyMIBCompliance = ciscoWanAtmPartyMIBCompliance.setStatus('current')
ciscoWanAtmPartyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99998, 2, 2, 2)).setObjects(("CISCO-WAN-ATM-PARTY-MIB", "cwapNSAPAddress"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVpi"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapVci"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapAdminStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapOperStatus"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapReroute"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapIdentifier"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapUploadCounter"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRootPhysicalId"), ("CISCO-WAN-ATM-PARTY-MIB", "cwapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanAtmPartyGroup = ciscoWanAtmPartyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-PARTY-MIB", PYSNMP_MODULE_ID=ciscoWanAtmPartyMIB, WanNsapAtmAddress=WanNsapAtmAddress, WanPartyAdminStatus=WanPartyAdminStatus, WanPartyOperStatus=WanPartyOperStatus, ciscoWanAtmPartyGroup=ciscoWanAtmPartyGroup, ciscoWanAtmPartyMIB=ciscoWanAtmPartyMIB, ciscoWanAtmPartyMIBCompliance=ciscoWanAtmPartyMIBCompliance, ciscoWanAtmPartyMIBCompliances=ciscoWanAtmPartyMIBCompliances, ciscoWanAtmPartyMIBConform=ciscoWanAtmPartyMIBConform, ciscoWanAtmPartyMIBGroups=ciscoWanAtmPartyMIBGroups, ciscoWanAtmPartyMIBNotifs=ciscoWanAtmPartyMIBNotifs, ciscoWanAtmPartyMIBObjects=ciscoWanAtmPartyMIBObjects, cwapAdminStatus=cwapAdminStatus, cwapConfig=cwapConfig, cwapConfigEntry=cwapConfigEntry, cwapConfigTable=cwapConfigTable, cwapIdentifier=cwapIdentifier, cwapNSAPAddress=cwapNSAPAddress, cwapOperStatus=cwapOperStatus, cwapReference=cwapReference, cwapReroute=cwapReroute, cwapRootPhysicalId=cwapRootPhysicalId, cwapRootVci=cwapRootVci, cwapRootVpi=cwapRootVpi, cwapRowStatus=cwapRowStatus, cwapUploadCounter=cwapUploadCounter, cwapVci=cwapVci, cwapVpi=cwapVpi)
