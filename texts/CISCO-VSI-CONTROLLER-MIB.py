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
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setContactInfo('Cisco Systems\n                Customer Service\n\n        Postal: 170 W Tasman Drive\n                San Jose, CA  95134\n                USA\n\n          Tel: +1 800 553-NETS\n\n     E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setDescription("This MIB module is used for configuring ATM Capable Switch \n     to be aware of VSI Controller information.\n\n     Terminolgies used:\n\n     VSI       - Virtual Switch Interface, a hardware-independent switch \n                 control protocol. This allows a Switch(node) to be \n\t\t controlled by a multiple controllers such as PNNI,LSC.\n\t\t These control planes can be internal or external to the\n\t         switch.The VSI interface defines the messages and associated\n\t         functions which allow communication between the controller \n\t\t and the switch.This interface is expected to support all \n\t\t types of connections (voice,data,frame relay,ATM) for PVCs,\n\t         SPVCs and SVCs.\n\n     VSI Master - software component which requests connections and receives\n                  switch generic information. This controls one or more VSI \n                  Slaves. This may run on the switch or a dedicated controller\n\t\t  platform. This is the master module.It performs the interface\n\t \t  to the higher layer networking software and handles all VSI\n\t\t  related functions.\n            \n     VSI Slave - software component which converts generic connection\n                 requests into hardware specific requests and hardware \n\t\t specific information into generic information.\n\t\t This runs on the switch.a A centralized slave has a single\n\t\t point of control for making connections and controlling \n\t\t interfaces, while a distributed slave allows for multiple\n\t\t slaves to coexist on the same switch.\n\n     Controller - Software ( and possibly hardware) which manages topology\n                  and network resources and performs VSI Master fucntion. \n\t\t  This performs source routing for ent-to-end SVCs, including\n\t\t  general call acceptance GCAC,setup calls with other \n\t\t  controllers.\n                  PNNI and MPLS are examples for the Controller.\n\n     Controller Shelf - A controller shelf is a switch containing atleast\n\t\t   one VSI Controller which is controlling a different \n\t\t   switch.It will also, typically, contain 'local' controllers\n\t\t   for itself.")
class CvcControllerShelfLocation(TextualConvention, Integer32):
    description = 'The location of the Controller Shelf. \n\n\t internal(1)  - controller resides on the same shelf\n\t                as the switch.\n\t external(2)  - controller resides on the external \n\t\t        platform. The controller shelf is\n\t\t        connected to the switch by an ATM link.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("internal", 1), ("external", 2))

class CvcControllerType(TextualConvention, Integer32):
    description = "The type of the controller which is a VSI Master.\n\t The Possible values are :\n\t     \n\t par(1) -  Portable Auto Route(PAR). This is a VSI Master controller\n\t           implementing Cisco Proprietary protocol for network\n\t           routing and topology in a Network containing only \n\t\t   Cisco Switches.\n\n\t pnni(2) - Private Network-to-Network Interface (PNNI) controller.\n\t\t   The PNNI protocol is used between private ATM Switches\n\t\t   and between groups of ATM switches. This protocol is \n\t\t   defined for distributing topology information between\n\t\t   switches and clusters of switches.\n\n\t lsc(3)  - Label Switch Controller(TSC).The LSC Implements MPLS\n\t           (Multi Protocol Label Switching) protocol. The LSC is \n\t\t   a router which is capable of controlling the operation\n\t\t   of a separate ATM switch so that the two of them \n                   together function as a single ATM-LSR(ATM Label Switch\n                   Router).\n\t\t   The LSC controls the operation of the ATM Switch\n\t\t   using a 'Switch Control Protocol', which allows the\n\t\t   LSC to setup and remove cross-connects on the ATM\n\t\t   switch, to discover the configuration and capabilities\n\t\t   of the controlled switch, and to gather statistics from\n\t\t   the controlled switch."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("par", 1), ("pnni", 2), ("lsc", 3))

cvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1))
cvcConfController = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1))
cvcConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcConfTable.setStatus('current')
if mibBuilder.loadTexts: cvcConfTable.setDescription('This table contains the entries for VSI Controllers.\n         This table is used for informing the VSI Slaves about\n         the existence of VSI Controllers and how the VSI slaves\n\t can reach the controller. The information in these entries\n\t are advertised to all the VSI Slaves using a system\n\t dependent implementation when an entry is created/activated.')
cvcConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerID"))
if mibBuilder.loadTexts: cvcConfEntry.setStatus('current')
if mibBuilder.loadTexts: cvcConfEntry.setDescription("An entry for a VSI Controller. \n         The entries in this table are created by setting the \n         cvcConfRowStatus object to 'createAndGo(4)'.\n\t The entries in this table are deleted by setting the\n\t cvcConfRowStatus object to 'destroy(6)'. The entries\n\t are can be created/modified/deleted through the Command\n\t Line Interface(CLI) also.")
cvcConfControllerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cvcConfControllerID.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerID.setDescription('This is the unique value for VSI Controller(VSI Master).\n         The VSI Slave uses this value in the message to identify \n         the VSI Master controller.')
cvcConfControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 2), CvcControllerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerType.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerType.setDescription("This object identifies the controller type.\n\t This object may not be modified if the associated\n\t cvcConfRowStatus is equal to 'active(1)'.")
cvcConfControllerShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 3), CvcControllerShelfLocation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setDescription('This identifies the location of the controller shelf.\n         This Object can be set only during row creation.')
cvcConfControllerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerLocation.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerLocation.setDescription("This identifies the location of the controller.\n         This object might contain the logical slot number\n         of the Module where the controller is running\n         on the same shelf as the switch.\n\t This object might contain the value of the interface \n         on the module where the controller is running on an\n         external shelf connected to the switch.\n\t This object may not be modified if the associated\n\t cvcConfRowStatus is equal to 'active(1)'.")
cvcConfControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerName.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerName.setDescription("This is the  name choosen by the user for the VSI Controller.\n        This object contains Octet string of length zero, if the user\n        does not set the value for this object.\n\tThis object may not be modified if the associated\n\tcvcConfRowStatus is equal to 'active(1)'.")
cvcConfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVpi.setStatus('current')
if mibBuilder.loadTexts: cvcConfVpi.setDescription("This is the Virtual Path Identifier(VPI) used for connecting to\n        the controller which is external to the switch. This object has\n        significance only if cvcConfControllerShelfLocation is 'external(2)'.\n\tThis object may not be modified if the associated\n\tcvcConfRowStatus is equal to 'active(1)'.")
cvcConfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVci.setStatus('current')
if mibBuilder.loadTexts: cvcConfVci.setDescription("This is the start value of Virtual Channel Identifier(VCI) used \n        for connecting to the controller which is external to the switch.\n        This object has significance only if cvcConfControllerShelfLocation \n        is 'external(2)'.\n\tThis object may not be modified if the associated\n\tcvcConfRowStatus is equal to 'active(1)'.")
cvcConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvcConfRowStatus.setDescription("This object is used for adding,deleting and modifying the\n        controller configuration. The row can be created by \n        setting this object to 'createAndGo(4)'.\n\tThe row can be deleted by setting this object to 'destroy(6)'.\n\tThe objects in the row can not be modified when this object \n        contains value 'active(1)'.")
cvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3))
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroup"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroupExternal"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvcMIBCompliance.setDescription('The Compliance statement for cisco VSI Controller group.')
cvcConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerType"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerShelfLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerName"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroup = cvcConfGroup.setStatus('current')
if mibBuilder.loadTexts: cvcConfGroup.setDescription('The objects related to configuring VSI controllers\n           running on the same shelf as the switch.\n          ')
cvcConfGroupExternal = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 2)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfVpi"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroupExternal = cvcConfGroupExternal.setStatus('current')
if mibBuilder.loadTexts: cvcConfGroupExternal.setDescription('The objects related to configuring VSI controllers\n           running on the shelf external to the switch. ')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-MIB", CvcControllerShelfLocation=CvcControllerShelfLocation, CvcControllerType=CvcControllerType, PYSNMP_MODULE_ID=ciscoVSIControllerMIB, ciscoVSIControllerMIB=ciscoVSIControllerMIB, cvcConfController=cvcConfController, cvcConfControllerID=cvcConfControllerID, cvcConfControllerLocation=cvcConfControllerLocation, cvcConfControllerName=cvcConfControllerName, cvcConfControllerShelfLocation=cvcConfControllerShelfLocation, cvcConfControllerType=cvcConfControllerType, cvcConfEntry=cvcConfEntry, cvcConfGroup=cvcConfGroup, cvcConfGroupExternal=cvcConfGroupExternal, cvcConfRowStatus=cvcConfRowStatus, cvcConfTable=cvcConfTable, cvcConfVci=cvcConfVci, cvcConfVpi=cvcConfVpi, cvcMIBCompliance=cvcMIBCompliance, cvcMIBCompliances=cvcMIBCompliances, cvcMIBConformance=cvcMIBConformance, cvcMIBGroups=cvcMIBGroups, cvcMIBObjects=cvcMIBObjects)
