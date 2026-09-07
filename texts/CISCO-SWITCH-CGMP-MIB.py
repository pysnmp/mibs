#
# PySNMP MIB module CISCO-SWITCH-CGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SWITCH-CGMP-MIB
# Source digest sha256:6ed7bc6c5d9e84a7f5fbf30c77bb4111864f6bb5a5a7ea0a6de28e1849e5b175
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
ciscoSwitchCgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 101))
ciscoSwitchCgmpMIB.setRevisions(('1998-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setLastUpdated('1998-05-07 00:00')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setOrganization('Cisco Systems, Inc')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                Email: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setDescription('Switch-side Cisco Group Management Protocol MIB for  \n                 Layer 2 Switch devices.')
ciscoSwitchCgmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1))
sCgmpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1))
class SCgmpVlanIndex(TextualConvention, Integer32):
    description = 'The VLAN-id of a VLAN on either ISL trunk, 802.1q trunk\n             or port-based VLAN implementations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1023)

sCgmpEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpEnable.setStatus('current')
if mibBuilder.loadTexts: sCgmpEnable.setDescription('This variable allows user to enable or disable Cisco\n                 Group Management Protocol (CGMP).')
sCgmpFastLeaveEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setStatus('current')
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setDescription('This variable allows user to enable or disable Cisco\n                 Group Management Protocol (CGMP) Fast Leave processing.')
sCgmpRouterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 6000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setDescription('Multicast routers that support CGMP will send CGMP\n                 join message to advertise themselves to switches within\n                 a network. A switch that receives a CGMP message will save\n                 the information and set a timer equal to this router hold\n                 time. When the router hold time expires, the switch will\n                 remove the Router entry from CGMP. The default value \n                 is 300 seconds.')
sCgmpRouterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: sCgmpRouterTable.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterTable.setDescription('List of Router entries present on the switch.')
sCgmpRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterVlanIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterMacAddress"))
if mibBuilder.loadTexts: sCgmpRouterEntry.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterEntry.setDescription("Entry containing multicast router information for\n                a particular router. These entries are created when a\n                router sends a CGMP join for itself on a particular\n                vlan. Entries may be removed when a router entry's\n                sCgmpRouterHoldTime expires, or when explicitly \n                removed by a user.")
sCgmpRouterVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 1), SCgmpVlanIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setDescription('An index value that uniquely identifies the \n                vlan on which the router identified by this router entry\n                is located. This value may be the same as used in the \n                CISCO-VLAN-MEMBERSHIP-MIB and the CISCO-VTP-MIB for\n                the same given vlan, if VTP is present and in use\n                on the switch.')
sCgmpRouterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 3), MacAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setDescription('An 802 MAC Address in canonical format. This is the \n                MAC address of the router itself.')
sCgmpRouterEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setDescription('This object is used by a management station to\n                 delete the row entry in sCgmpRouterTable following \n                 the RowStatus textual convention. The managment\n                 station may remove this entry by setting destroy (6).\n                 Entries may not be created. Entries removed may \n                 reappear in normal CGMP operation when the router\n                 sends another self join.')
ciscoSwitchCgmpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3))
ciscoSwitchCgmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1))
ciscoSwitchCgmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2))
ciscoSwitchCgmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCgmpMIBCompliance = ciscoSwitchCgmpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIBCompliance.setDescription('The compliance statement for switches implementing\n                the Cisco Group Management Protocol')
sCgmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpFastLeaveEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterHoldTime"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sCgmpGroup = sCgmpGroup.setStatus('current')
if mibBuilder.loadTexts: sCgmpGroup.setDescription('Switch-side Cisco Group Management Protocol.')
mibBuilder.exportSymbols("CISCO-SWITCH-CGMP-MIB", PYSNMP_MODULE_ID=ciscoSwitchCgmpMIB, SCgmpVlanIndex=SCgmpVlanIndex, ciscoSwitchCgmpMIB=ciscoSwitchCgmpMIB, ciscoSwitchCgmpMIBCompliance=ciscoSwitchCgmpMIBCompliance, ciscoSwitchCgmpMIBCompliances=ciscoSwitchCgmpMIBCompliances, ciscoSwitchCgmpMIBConformance=ciscoSwitchCgmpMIBConformance, ciscoSwitchCgmpMIBGroups=ciscoSwitchCgmpMIBGroups, ciscoSwitchCgmpMIBObjects=ciscoSwitchCgmpMIBObjects, sCgmpEnable=sCgmpEnable, sCgmpFastLeaveEnable=sCgmpFastLeaveEnable, sCgmpGroup=sCgmpGroup, sCgmpInfo=sCgmpInfo, sCgmpRouterEntry=sCgmpRouterEntry, sCgmpRouterEntryStatus=sCgmpRouterEntryStatus, sCgmpRouterHoldTime=sCgmpRouterHoldTime, sCgmpRouterMacAddress=sCgmpRouterMacAddress, sCgmpRouterTable=sCgmpRouterTable, sCgmpRouterVlanIndex=sCgmpRouterVlanIndex)
