#
# PySNMP MIB module CISCO-SDWAN-OMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SDWAN-OMP-MIB
# Source digest sha256:51c368b28922d8059a1d93071abc2ea87e0f244cf21d229a17f9aa2b244f3881
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanOmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1003))
ciscoSdwanOmpMIB.setRevisions(('2021-03-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setRevisionsDescriptions(('Cisco SDWAN OMP Revision 0',))
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setLastUpdated('2021-03-03 00:00')
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setContactInfo('Cisco Systems,\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            Email: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSdwanOmpMIB.setDescription('This module defines the data model for OMP')
class NotificationSeverity(TextualConvention, Integer32):
    description = 'Netconf notification severity level'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3))

class OperState(TextualConvention, Integer32):
    description = 'Operational state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("up", 0), ("down", 1))

class PeerState(TextualConvention, Integer32):
    description = 'OMP peer state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("invalid", 0), ("init", 1), ("handshake", 2), ("up", 3), ("down", 4), ("init-in-gr", 5), ("down-in-gr", 6), ("handshake-in-gr", 7))

class OmpPolicyState(TextualConvention, Integer32):
    description = 'OMP policy state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("add", 0), ("delete", 1))

class InetAddressIP(TextualConvention, OctetString):
    description = 'confd:inetAddressIP'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
ciscoSdwanOmpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0))
ciscoSdwanOmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 1))
ciscoSdwanOmpMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2))
ciscoSdwanOmpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3))
netconfNotificationSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 2), NotificationSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: netconfNotificationSeverity.setStatus('current')
if mibBuilder.loadTexts: netconfNotificationSeverity.setDescription('Netconf notification severity level')
ciscoSdwanOmpNumberOfVsmarts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpNumberOfVsmarts.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpNumberOfVsmarts.setDescription('Number of vsmarts')
ciscoSdwanOmpNewState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 4), OperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpNewState.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpNewState.setDescription('OMP new state')
ciscoSdwanOmpPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 5), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPeer.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpPeer.setDescription('OMP peer')
ciscoSdwanOmpPeerNewState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 6), PeerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPeerNewState.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpPeerNewState.setDescription('Peer state')
ciscoSdwanOmpPolicy = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 7), OmpPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpPolicy.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpPolicy.setDescription('OMP policy state')
ciscoSdwanOmpVsmartPeer = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 1003, 2, 8), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoSdwanOmpVsmartPeer.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpVsmartPeer.setDescription('Peer vsmart')
ciscoSdwanOmpOmpNumberOfVsmartsChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpNumberOfVsmartsChange.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpOmpNumberOfVsmartsChange.setDescription('Cisco SDWAN trap from omp')
ciscoSdwanOmpOmpStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 2)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpOmpStateChange.setDescription('Cisco SDWAN trap from omp')
ciscoSdwanOmpOmpPeerStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 3)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPeerStateChange.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPeerStateChange.setDescription('Cisco SDWAN trap from omp')
ciscoSdwanOmpOmpPolicy = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 1003, 0, 4)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPolicy.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpOmpPolicy.setDescription('Cisco SDWAN trap from omp')
ciscoSdwanOmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1))
ciscoSdwanOmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2))
ciscoSdwanOmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 1, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifObjsGroup"), ("CISCO-SDWAN-OMP-MIB", "cSdwanOmpNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanOmpMIBCompliance = ciscoSdwanOmpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanOmpMIBCompliance.setDescription('The compliance statement for the SNMP entities\n         that implement the ciscoSdwanOmpMIB module.')
cSdwanOmpNotifObjsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 1)).setObjects(("CISCO-SDWAN-OMP-MIB", "netconfNotificationSeverity"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNumberOfVsmarts"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpNewState"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeer"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPeerNewState"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpPolicy"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpVsmartPeer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanOmpNotifObjsGroup = cSdwanOmpNotifObjsGroup.setStatus('current')
if mibBuilder.loadTexts: cSdwanOmpNotifObjsGroup.setDescription('This is a collection of objects of\n                                 OMP notification objects.')
cSdwanOmpNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 1003, 3, 2, 2)).setObjects(("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpNumberOfVsmartsChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpStateChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPeerStateChange"), ("CISCO-SDWAN-OMP-MIB", "ciscoSdwanOmpOmpPolicy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanOmpNotifsGroup = cSdwanOmpNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: cSdwanOmpNotifsGroup.setDescription('This is a collection of OMP notifications.')
mibBuilder.exportSymbols("CISCO-SDWAN-OMP-MIB", InetAddressIP=InetAddressIP, NotificationSeverity=NotificationSeverity, OmpPolicyState=OmpPolicyState, OperState=OperState, PYSNMP_MODULE_ID=ciscoSdwanOmpMIB, PeerState=PeerState, cSdwanOmpNotifObjsGroup=cSdwanOmpNotifObjsGroup, cSdwanOmpNotifsGroup=cSdwanOmpNotifsGroup, ciscoSdwanOmpMIB=ciscoSdwanOmpMIB, ciscoSdwanOmpMIBCompliance=ciscoSdwanOmpMIBCompliance, ciscoSdwanOmpMIBCompliances=ciscoSdwanOmpMIBCompliances, ciscoSdwanOmpMIBConform=ciscoSdwanOmpMIBConform, ciscoSdwanOmpMIBGroups=ciscoSdwanOmpMIBGroups, ciscoSdwanOmpMIBNotifObjects=ciscoSdwanOmpMIBNotifObjects, ciscoSdwanOmpMIBNotifs=ciscoSdwanOmpMIBNotifs, ciscoSdwanOmpMIBObjects=ciscoSdwanOmpMIBObjects, ciscoSdwanOmpNewState=ciscoSdwanOmpNewState, ciscoSdwanOmpNumberOfVsmarts=ciscoSdwanOmpNumberOfVsmarts, ciscoSdwanOmpOmpNumberOfVsmartsChange=ciscoSdwanOmpOmpNumberOfVsmartsChange, ciscoSdwanOmpOmpPeerStateChange=ciscoSdwanOmpOmpPeerStateChange, ciscoSdwanOmpOmpPolicy=ciscoSdwanOmpOmpPolicy, ciscoSdwanOmpOmpStateChange=ciscoSdwanOmpOmpStateChange, ciscoSdwanOmpPeer=ciscoSdwanOmpPeer, ciscoSdwanOmpPeerNewState=ciscoSdwanOmpPeerNewState, ciscoSdwanOmpPolicy=ciscoSdwanOmpPolicy, ciscoSdwanOmpVsmartPeer=ciscoSdwanOmpVsmartPeer, netconfNotificationSeverity=netconfNotificationSeverity)
