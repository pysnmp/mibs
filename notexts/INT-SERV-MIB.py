#
# PySNMP MIB module INT-SERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/INT-SERV-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 19:41:12 2021
# On host fv-az83-233 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, mib_2, Counter32, Gauge32, Integer32, Unsigned32, Bits, MibIdentifier, ModuleIdentity, ObjectIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "mib-2", "Counter32", "Gauge32", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
TestAndIncr, DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TestAndIncr", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
intSrv = ModuleIdentity((1, 3, 6, 1, 2, 1, 52))
if mibBuilder.loadTexts: intSrv.setLastUpdated('9710030642Z')
if mibBuilder.loadTexts: intSrv.setOrganization('IETF Integrated Services Working Group')
intSrvObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 1))
intSrvGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 2))
intSrvNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 3))
intSrvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4))
class SessionNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Protocol(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class SessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class Port(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 4)

class MessageSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BitRate(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BurstSize(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class QosService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5))
    namedValues = NamedValues(("bestEffort", 1), ("guaranteedDelay", 2), ("controlledLoad", 5))

intSrvIfAttribTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 1), )
if mibBuilder.loadTexts: intSrvIfAttribTable.setStatus('current')
intSrvIfAttribEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvIfAttribEntry.setStatus('current')
intSrvIfAttribAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1), BitRate()).setUnits('Bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setStatus('current')
intSrvIfAttribMaxAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2), BitRate()).setUnits('Bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setStatus('current')
intSrvIfAttribAllocatedBuffer = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3), BurstSize()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setStatus('current')
intSrvIfAttribFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribFlows.setStatus('current')
intSrvIfAttribPropagationDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5), Integer32()).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setStatus('current')
intSrvIfAttribStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribStatus.setStatus('current')
intSrvFlowTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 2), )
if mibBuilder.loadTexts: intSrvFlowTable.setStatus('current')
intSrvFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 2, 1), ).setIndexNames((0, "INT-SERV-MIB", "intSrvFlowNumber"))
if mibBuilder.loadTexts: intSrvFlowEntry.setStatus('current')
intSrvFlowNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1), SessionNumber())
if mibBuilder.loadTexts: intSrvFlowNumber.setStatus('current')
intSrvFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2), SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowType.setStatus('current')
intSrvFlowOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rsvp", 2), ("management", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOwner.setStatus('current')
intSrvFlowDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddr.setStatus('current')
intSrvFlowSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setStatus('current')
intSrvFlowDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setStatus('current')
intSrvFlowSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setStatus('current')
intSrvFlowProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8), Protocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowProtocol.setStatus('current')
intSrvFlowDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestPort.setStatus('current')
intSrvFlowPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowPort.setStatus('current')
intSrvFlowFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowFlowId.setStatus('current')
intSrvFlowInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowInterface.setStatus('current')
intSrvFlowIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowIfAddr.setStatus('current')
intSrvFlowRate = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14), BitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowRate.setStatus('current')
intSrvFlowBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15), BurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowBurst.setStatus('current')
intSrvFlowWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowWeight.setStatus('current')
intSrvFlowQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowQueue.setStatus('current')
intSrvFlowMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMinTU.setStatus('current')
intSrvFlowMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMaxTU.setStatus('current')
intSrvFlowBestEffort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowBestEffort.setStatus('current')
intSrvFlowPoliced = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowPoliced.setStatus('current')
intSrvFlowDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDiscard.setStatus('current')
intSrvFlowService = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23), QosService()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowService.setStatus('current')
intSrvFlowOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOrder.setStatus('current')
intSrvFlowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowStatus.setStatus('current')
intSrvFlowNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 52, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intSrvFlowNewIndex.setStatus('current')
intSrvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 2, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribGroup"), ("INT-SERV-MIB", "intSrvFlowsGroup"), ("INT-SERV-MIB", "intSrvGenObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvCompliance = intSrvCompliance.setStatus('current')
intSrvIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribMaxAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribAllocatedBuffer"), ("INT-SERV-MIB", "intSrvIfAttribFlows"), ("INT-SERV-MIB", "intSrvIfAttribPropagationDelay"), ("INT-SERV-MIB", "intSrvIfAttribStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvIfAttribGroup = intSrvIfAttribGroup.setStatus('current')
intSrvFlowsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 2)).setObjects(("INT-SERV-MIB", "intSrvFlowType"), ("INT-SERV-MIB", "intSrvFlowOwner"), ("INT-SERV-MIB", "intSrvFlowDestAddr"), ("INT-SERV-MIB", "intSrvFlowSenderAddr"), ("INT-SERV-MIB", "intSrvFlowDestAddrLength"), ("INT-SERV-MIB", "intSrvFlowSenderAddrLength"), ("INT-SERV-MIB", "intSrvFlowProtocol"), ("INT-SERV-MIB", "intSrvFlowDestPort"), ("INT-SERV-MIB", "intSrvFlowPort"), ("INT-SERV-MIB", "intSrvFlowFlowId"), ("INT-SERV-MIB", "intSrvFlowInterface"), ("INT-SERV-MIB", "intSrvFlowBestEffort"), ("INT-SERV-MIB", "intSrvFlowRate"), ("INT-SERV-MIB", "intSrvFlowBurst"), ("INT-SERV-MIB", "intSrvFlowWeight"), ("INT-SERV-MIB", "intSrvFlowQueue"), ("INT-SERV-MIB", "intSrvFlowMinTU"), ("INT-SERV-MIB", "intSrvFlowMaxTU"), ("INT-SERV-MIB", "intSrvFlowDiscard"), ("INT-SERV-MIB", "intSrvFlowPoliced"), ("INT-SERV-MIB", "intSrvFlowService"), ("INT-SERV-MIB", "intSrvFlowIfAddr"), ("INT-SERV-MIB", "intSrvFlowOrder"), ("INT-SERV-MIB", "intSrvFlowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvFlowsGroup = intSrvFlowsGroup.setStatus('current')
intSrvGenObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 3)).setObjects(("INT-SERV-MIB", "intSrvFlowNewIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGenObjectsGroup = intSrvGenObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("INT-SERV-MIB", intSrvFlowDestPort=intSrvFlowDestPort, SessionType=SessionType, intSrvFlowRate=intSrvFlowRate, intSrvFlowPort=intSrvFlowPort, intSrvFlowOrder=intSrvFlowOrder, intSrvIfAttribStatus=intSrvIfAttribStatus, intSrvConformance=intSrvConformance, intSrvFlowDiscard=intSrvFlowDiscard, intSrvFlowDestAddrLength=intSrvFlowDestAddrLength, intSrvFlowService=intSrvFlowService, intSrvObjects=intSrvObjects, intSrvFlowType=intSrvFlowType, intSrvFlowSenderAddrLength=intSrvFlowSenderAddrLength, intSrvFlowProtocol=intSrvFlowProtocol, intSrvFlowMaxTU=intSrvFlowMaxTU, BurstSize=BurstSize, Port=Port, SessionNumber=SessionNumber, intSrvFlowMinTU=intSrvFlowMinTU, intSrvFlowDestAddr=intSrvFlowDestAddr, intSrvFlowStatus=intSrvFlowStatus, intSrvFlowQueue=intSrvFlowQueue, intSrvIfAttribAllocatedBits=intSrvIfAttribAllocatedBits, PYSNMP_MODULE_ID=intSrv, intSrvGenObjectsGroup=intSrvGenObjectsGroup, intSrvFlowWeight=intSrvFlowWeight, intSrvNotifications=intSrvNotifications, intSrvFlowIfAddr=intSrvFlowIfAddr, intSrvIfAttribFlows=intSrvIfAttribFlows, intSrvFlowBurst=intSrvFlowBurst, intSrvFlowOwner=intSrvFlowOwner, intSrvIfAttribMaxAllocatedBits=intSrvIfAttribMaxAllocatedBits, Protocol=Protocol, intSrvIfAttribEntry=intSrvIfAttribEntry, intSrvIfAttribPropagationDelay=intSrvIfAttribPropagationDelay, intSrvFlowInterface=intSrvFlowInterface, intSrvFlowNumber=intSrvFlowNumber, intSrvFlowBestEffort=intSrvFlowBestEffort, intSrvFlowNewIndex=intSrvFlowNewIndex, intSrvGroups=intSrvGroups, intSrvIfAttribGroup=intSrvIfAttribGroup, intSrvFlowsGroup=intSrvFlowsGroup, intSrvIfAttribAllocatedBuffer=intSrvIfAttribAllocatedBuffer, BitRate=BitRate, intSrvGenObjects=intSrvGenObjects, intSrvIfAttribTable=intSrvIfAttribTable, intSrvFlowSenderAddr=intSrvFlowSenderAddr, intSrvCompliances=intSrvCompliances, MessageSize=MessageSize, intSrvFlowPoliced=intSrvFlowPoliced, intSrvCompliance=intSrvCompliance, intSrvFlowEntry=intSrvFlowEntry, intSrvFlowFlowId=intSrvFlowFlowId, intSrvFlowTable=intSrvFlowTable, intSrv=intSrv, QosService=QosService)
