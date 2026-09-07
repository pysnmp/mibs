#
# PySNMP MIB module CISCO-IF-CALL-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IF-CALL-SERVICE-MIB
# Source digest sha256:6ff3f469047e45c795f9a9771f2b3b0e9ea67572c229b2129b3a7f372c98b254
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
BulkConfigResult, ConfigIterator = mibBuilder.importSymbols("CISCO-TC", "BulkConfigResult", "ConfigIterator")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfCallServiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9968))
ciscoIfCallServiceMIB.setRevisions(('2003-04-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setRevisionsDescriptions(('Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setLastUpdated('2003-04-25 00:00')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setContactInfo('       Cisco Systems\n                    Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setDescription('The MIB is used to manage call service state\n           for interfaces on media gateway. \n          ')
ciscoIfCallServiceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 0))
ciscoIfCallServiceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1))
ciscoIfCallServiceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2))
cicServiceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1))
class CIfCallServiceOperState(TextualConvention, Integer32):
    description = 'This Textual Convention defines the call connection related \n         service state of an interface. The possible service states are:\n\n          inService:\n\t      An interface is ready for call connection setup. \n\n          outOfService:\n              The interface is in Out-Of-Service state.\n              All calls will be destroyed on this interface by Call\n              Agent. \n              A call service state change message with FORCED method  \n              is sent to Call Agent.\n              No new connections are allowed on the interface.\n\n          oosPending:\n              The interface is in Out-Of-Service state.\n              All existing calls will not be affected on this \n              interface. \n              A call service state change message with GRACEFUL method\n              is sent to Call Agent.\n              No new connections are allowed.     \n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2), ("oosPending", 3))

class CIfCallServiceAdminState(TextualConvention, Integer32):
    description = 'This Textual Convention defines the service administrative \n         state of an interface. The possible service administrative \n         states are as follows:\n\n          inService: \n              The interface would be restored to in-service status \n              and a call service state change with method RESTART  \n              message will be sent to Call Agent\n             \n          forcefulOutOfService: \n              The interface would be in Out-Of-Service state.\n              Any existing connections on the interface will \n              deleted.\n              A call service state change message with FORCED method \n              will be sent to Call Agent.\n              New connections would be blocked.           \n\n          gracefulOutOfService: \n              The interface would be in Out-Of-Service state.\n              Any existing connections on the interface are not \n              affected.\n              A call service state change message with GRACEFUL \n              method will be sent to Call Agent.\n              New connections would be blocked.      \n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("forcedOutOfService", 2), ("gracefulOutOfService", 3))

cicServiceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cicServiceTable.setStatus('current')
if mibBuilder.loadTexts: cicServiceTable.setDescription('This table defines the parameters related to the\n         call service state administration for the \n         interfaces on media gateway. The possible interfaces  \n         include channelized sonet interface, DS1 interface, \n         etc..\n        ')
cicServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cicServiceEntry.setStatus('current')
if mibBuilder.loadTexts: cicServiceEntry.setDescription('An entry containing service administration information \n         applicable to a particular interface. \n        ')
cicServiceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 1), CIfCallServiceOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceOperState.setStatus('current')
if mibBuilder.loadTexts: cicServiceOperState.setDescription("This object indicates the current operating state of \n         the service in the interface.\n\n         The entry in this table is also in ifTable(the index of this\n         table is ifIndex). The 'cicServiceOperState' of the entry is  \n         not only dependent on the 'cicServiceAdminState', it is also\n         dependent on the 'ifOperStatus' of ifTable. \n         The following is the relationship between \n         'cicServiceAdminState' and 'ifOperStatus':\n\n         cicServiceOperState     cicServiceAdminState   ifOperStatus\n         ----------------       -----------------     ------------\n         inService              inService              up\n         outOfService           forcefulOutOfService   up\n         oosPending             gracefulOutOfService   up\n         outOfService           inService              down\n         outOfService           forcefulOutOfService   down\n         outOfService           gracefulOutOfService   down\n        ")
cicServiceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 2), CIfCallServiceAdminState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceAdminState.setStatus('current')
if mibBuilder.loadTexts: cicServiceAdminState.setDescription("This object is used to change the desired service state \n         of the interface. The operational service state of the\n         interface is indicated by 'cicServiceOperState'.\n        ")
cicServiceGraceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceGraceTime.setStatus('current')
if mibBuilder.loadTexts: cicServiceGraceTime.setDescription("This object specifies the amount of time before the \n         existing call connections been gracefully shutdown in \n         the interface when 'cicServiceAdminState' \n         is set to 'gracefulOutOfService'.\n\n         This object is not applicable if 'cicServiceAdminState'\n         is set to 'forcefulOutOfService'.\n\n         The value of 0 specifies that the service on the interface\n         will not be put outOfService until the call connection over \n         the interface is terminated.\n        ")
cicServiceRepetition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 4), ConfigIterator().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepetition.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepetition.setDescription('This object is used to change service state to multiple\n         interfaces by repeatedly applying the writable \n         objects of cicServiceTable specified in the same \n         SNMP PDU starting from the row specified by the instance \n         value in INDEX for the number of rows specified in this \n         object.\n\n         The order of operation is iterated through the logical\n         order of the interface. Whether the iteration will\n         be applied across the physical boundary or not is depends\n         upon the system implementation.\n\n         The GET operation on this object will always return 1.')
cicServiceRepeatOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepeatOwner.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepeatOwner.setDescription("This object is used for error checking of the operation\n         specified in 'cicServiceRepetition'.\n\n         The value of this object is set by the SNMP manager\n         with its own identifier at the same time as issuing the bulk\n         operation by setting 'cicServiceRepetition'. This object and\n         'cicServiceRepetition' need to be in the same SNMP SET PDU.\n\n         Later on, the SNMP manager should check the value of this\n         object, if it is same as the name previously set, then\n         the value of 'cicServiceRepeatResult' indicates the result \n         of the bulk operation initiated by this SNMP manager.\n         In the case that a SNMP manager do multi bulk operation,\n         it is recommended that the SNMP manager choose to set this \n         value to its IP Address so as to be unique.\n        ")
cicServiceRepeatResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 6), BulkConfigResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceRepeatResult.setStatus('current')
if mibBuilder.loadTexts: cicServiceRepeatResult.setDescription("This object is used for error checking of the operation\n         specified in cicServiceRepetition.\n\n         This object indicates the result of the bulk operation\n         initiated by the SNMP manager specified in the value of\n         'cicServiceRepeatOwner'.\n        ")
cicServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1))
cicServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2))
cicServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceCompliance = cicServiceCompliance.setStatus('current')
if mibBuilder.loadTexts: cicServiceCompliance.setDescription('The compliance statement for interfaces which implement the\n         CISCO-IF-CALL-SERVICE-MIB.')
cicServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceOperState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceAdminState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGraceTime"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepetition"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatOwner"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceGroup = cicServiceGroup.setStatus('current')
if mibBuilder.loadTexts: cicServiceGroup.setDescription('A collection of objects for managing per interface basis \n         call service state information.\n        ')
mibBuilder.exportSymbols("CISCO-IF-CALL-SERVICE-MIB", CIfCallServiceAdminState=CIfCallServiceAdminState, CIfCallServiceOperState=CIfCallServiceOperState, PYSNMP_MODULE_ID=ciscoIfCallServiceMIB, cicServiceAdminState=cicServiceAdminState, cicServiceCompliance=cicServiceCompliance, cicServiceCompliances=cicServiceCompliances, cicServiceConfig=cicServiceConfig, cicServiceEntry=cicServiceEntry, cicServiceGraceTime=cicServiceGraceTime, cicServiceGroup=cicServiceGroup, cicServiceGroups=cicServiceGroups, cicServiceOperState=cicServiceOperState, cicServiceRepeatOwner=cicServiceRepeatOwner, cicServiceRepeatResult=cicServiceRepeatResult, cicServiceRepetition=cicServiceRepetition, cicServiceTable=cicServiceTable, ciscoIfCallServiceMIB=ciscoIfCallServiceMIB, ciscoIfCallServiceMIBConformance=ciscoIfCallServiceMIBConformance, ciscoIfCallServiceMIBNotifs=ciscoIfCallServiceMIBNotifs, ciscoIfCallServiceMIBObjects=ciscoIfCallServiceMIBObjects)
