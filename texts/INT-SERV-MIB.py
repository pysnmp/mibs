#
# PySNMP MIB module INT-SERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/INT-SERV-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:24:18 2021
# On host fv-az135-680 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter64, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Counter32, Gauge32, Bits, mib_2, Unsigned32, ModuleIdentity, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Counter32", "Gauge32", "Bits", "mib-2", "Unsigned32", "ModuleIdentity", "Integer32", "MibIdentifier")
DisplayString, RowStatus, TextualConvention, TruthValue, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue", "TestAndIncr")
intSrv = ModuleIdentity((1, 3, 6, 1, 2, 1, 52))
if mibBuilder.loadTexts: intSrv.setLastUpdated('9710030642Z')
if mibBuilder.loadTexts: intSrv.setOrganization('IETF Integrated Services Working Group')
if mibBuilder.loadTexts: intSrv.setContactInfo('       Fred Baker\n       Postal: Cisco Systems\n               519 Lado Drive\n               Santa Barbara, California 93111\n       Tel:    +1 805 681 0115\n       E-Mail: fred@cisco.com\n\n               John Krawczyk\n       Postal: ArrowPoint Communications\n               235 Littleton Road\n               Westford, Massachusetts 01886\n       Tel:    +1 508 692 5875\n       E-Mail: jjk@tiac.net')
if mibBuilder.loadTexts: intSrv.setDescription('The MIB module to describe the Integrated Services\n       Protocol')
intSrvObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 1))
intSrvGenObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 2))
intSrvNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 3))
intSrvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4))
class SessionNumber(TextualConvention, Integer32):
    description = 'The Session  Number  convention  is  used  for\n           numbers  identifying  sessions or saved PATH or\n           RESV information. It is a number in  the  range\n           returned  by  a TestAndIncr variable, having no\n           protocol meaning whatsoever but serving instead\n           as simple identifier.\n\n           The alternative was a very complex instance  or\n           instance object that became unwieldy.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Protocol(TextualConvention, Integer32):
    description = 'The value of the IP Protocol field  of  an  IP\n           Datagram  Header.  This identifies the protocol\n           layer above IP.  For example, the  value  6  is\n           used  for TCP and the value 17 is used for UDP.\n           The values of this field are defined in the As-\n           signed Numbers RFC.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class SessionType(TextualConvention, Integer32):
    description = "The value of the C-Type field of a Session ob-\n           ject,  as  defined  in  the RSVP specification.\n           This value  determines  the  lengths  of  octet\n           strings  and use of certain objects such as the\n           'port' variables. If the C-Type  calls  for  an\n           IP6  address, one would expect all source, des-\n           tination, and next/previous hop addresses to be\n           16  bytes long, and for the ports to be UDP/TCP\n           port numbers, for example."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class Port(TextualConvention, OctetString):
    description = 'The value of the UDP or TCP Source or Destina-\n           tion  Port field, a virtual destination port or\n           generalized port identifier used with the IPSEC\n           Authentication Header or Encapsulating Security\n           Payload, or other session discriminator.  If it\n           is  not  used, the value should be of length 0.\n           This pair, when coupled with the  IP  Addresses\n           of the source and destination system and the IP\n           protocol  field,  uniquely  identifies  a  data\n           stream.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 4)

class MessageSize(TextualConvention, Integer32):
    description = 'The size of a message in bytes. This  is  used\n           to  specify  the  minimum and maximum size of a\n           message along an integrated services route.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BitRate(TextualConvention, Integer32):
    description = 'The rate, in bits/second, that data  may  move\n           in  the context.  Applicable contexts minimally\n           include the speed of an  interface  or  virtual\n           circuit, the data rate of a (potentially aggre-\n           gated) data flow, or the data rate to be  allo-\n           cated for use by a flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class BurstSize(TextualConvention, Integer32):
    description = 'The number of octets of IP Data, including  IP\n           Headers, that a stream may send without concern\n           for policing.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class QosService(TextualConvention, Integer32):
    description = 'The class of service in use by a flow.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 5))
    namedValues = NamedValues(("bestEffort", 1), ("guaranteedDelay", 2), ("controlledLoad", 5))

intSrvIfAttribTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 1), )
if mibBuilder.loadTexts: intSrvIfAttribTable.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribTable.setDescription("The reservable attributes of the system's  in-\n           terfaces.")
intSrvIfAttribEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvIfAttribEntry.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribEntry.setDescription('The reservable attributes of  a  given  inter-\n           face.')
intSrvIfAttribAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 1), BitRate()).setUnits('Bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBits.setDescription('The number of bits/second currently  allocated\n           to reserved sessions on the interface.')
intSrvIfAttribMaxAllocatedBits = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 2), BitRate()).setUnits('Bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribMaxAllocatedBits.setDescription('The maximum number of bits/second that may  be\n           allocated  to  reserved  sessions on the inter-\n           face.')
intSrvIfAttribAllocatedBuffer = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 3), BurstSize()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribAllocatedBuffer.setDescription('The amount of buffer space  required  to  hold\n           the simultaneous burst of all reserved flows on\n           the interface.')
intSrvIfAttribFlows = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvIfAttribFlows.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribFlows.setDescription('The number of reserved flows currently  active\n           on  this  interface.  A flow can be created ei-\n           ther from a reservation protocol (such as  RSVP\n           or ST-II) or via configuration information.')
intSrvIfAttribPropagationDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 5), Integer32()).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribPropagationDelay.setDescription('The amount of propagation delay that this  in-\n           terface  introduces  in addition to that intro-\n           diced by bit propagation delays.')
intSrvIfAttribStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvIfAttribStatus.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribStatus.setDescription("'active' on interfaces that are configured for\n           RSVP.")
intSrvFlowTable = MibTable((1, 3, 6, 1, 2, 1, 52, 1, 2), )
if mibBuilder.loadTexts: intSrvFlowTable.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowTable.setDescription("Information describing the reserved flows  us-\n           ing the system's interfaces.")
intSrvFlowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 1, 2, 1), ).setIndexNames((0, "INT-SERV-MIB", "intSrvFlowNumber"))
if mibBuilder.loadTexts: intSrvFlowEntry.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowEntry.setDescription('Information describing the use of a given  in-\n           terface   by   a   given   flow.   The  counter\n           intSrvFlowPoliced starts counting  at  the  in-\n           stallation of the flow.')
intSrvFlowNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 1), SessionNumber())
if mibBuilder.loadTexts: intSrvFlowNumber.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowNumber.setDescription('The number of this flow.  This is for SNMP In-\n           dexing purposes only and has no relation to any\n           protocol value.')
intSrvFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 2), SessionType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowType.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowType.setDescription('The type of session (IP4, IP6, IP6  with  flow\n           information, etc).')
intSrvFlowOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("rsvp", 2), ("management", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOwner.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowOwner.setDescription('The process that installed this  flow  in  the\n           queue policy database.')
intSrvFlowDestAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestAddr.setDescription("The destination address used by all senders in\n           this  session.   This object may not be changed\n           when the value of the RowStatus object is  'ac-\n           tive'.")
intSrvFlowSenderAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowSenderAddr.setDescription("The source address of the sender  selected  by\n           this  reservation.  The value of all zeroes in-\n           dicates 'all senders'.  This object may not  be\n           changed  when the value of the RowStatus object\n           is 'active'.")
intSrvFlowDestAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestAddrLength.setDescription("The length of the destination address in bits.\n           This  is  the CIDR Prefix Length, which for IP4\n           hosts and multicast addresses is 32 bits.  This\n           object may not be changed when the value of the\n           RowStatus object is 'active'.")
intSrvFlowSenderAddrLength = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowSenderAddrLength.setDescription("The length of the sender's  address  in  bits.\n           This  is  the CIDR Prefix Length, which for IP4\n           hosts and multicast addresses is 32 bits.  This\n           object may not be changed when the value of the\n           RowStatus object is 'active'.")
intSrvFlowProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 8), Protocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowProtocol.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowProtocol.setDescription("The IP Protocol used by a session.   This  ob-\n           ject  may  not be changed when the value of the\n           RowStatus object is 'active'.")
intSrvFlowDestPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 9), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDestPort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDestPort.setDescription("The UDP or TCP port number used as a  destina-\n           tion  port for all senders in this session.  If\n           the  IP   protocol   in   use,   specified   by\n           intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH),\n           this  represents  a  virtual  destination  port\n           number.   A value of zero indicates that the IP\n           protocol in use does not have ports.  This  ob-\n           ject  may  not be changed when the value of the\n           RowStatus object is 'active'.")
intSrvFlowPort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 10), Port()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowPort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowPort.setDescription("The UDP or TCP port number used  as  a  source\n           port  for  this sender in this session.  If the\n           IP    protocol    in    use,    specified    by\n           intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH),\n           this represents a generalized  port  identifier\n           (GPI).   A  value of zero indicates that the IP\n           protocol in use does not have ports.  This  ob-\n           ject  may  not be changed when the value of the\n           RowStatus object is 'active'.")
intSrvFlowFlowId = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowFlowId.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowFlowId.setDescription('The flow ID that  this  sender  is  using,  if\n           this  is  an IPv6 session.')
intSrvFlowInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 12), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowInterface.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowInterface.setDescription('The ifIndex value of the  interface  on  which\n           this reservation exists.')
intSrvFlowIfAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowIfAddr.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowIfAddr.setDescription('The IP Address on the ifEntry  on  which  this\n           reservation  exists.  This is present primarily\n           to support those interfaces which layer  multi-\n           ple IP Addresses on the interface.')
intSrvFlowRate = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 14), BitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowRate.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowRate.setDescription("The Reserved Rate of the sender's data stream.\n           If this is a Controlled Load service flow, this\n           rate is derived from the Tspec  rate  parameter\n           (r).   If  this  is  a Guaranteed service flow,\n           this rate is derived from  the  Rspec  clearing\n           rate parameter (R).")
intSrvFlowBurst = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 15), BurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowBurst.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowBurst.setDescription("The size of the largest  burst  expected  from\n           the sender at a time.\n\n           If this is less than  the  sender's  advertised\n           burst  size, the receiver is asking the network\n           to provide flow pacing  beyond  what  would  be\n           provided  under normal circumstances. Such pac-\n           ing is at the network's option.")
intSrvFlowWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowWeight.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowWeight.setDescription('The weight used  to  prioritize  the  traffic.\n           Note  that the interpretation of this object is\n           implementation-specific,   as   implementations\n           vary in their use of weighting procedures.')
intSrvFlowQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowQueue.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowQueue.setDescription('The number of the queue used by this  traffic.\n           Note  that the interpretation of this object is\n           implementation-specific,   as   implementations\n           vary in their use of queue identifiers.')
intSrvFlowMinTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 18), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMinTU.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowMinTU.setDescription('The minimum message size for  this  flow.  The\n           policing  algorithm will treat smaller messages\n           as though they are this size.')
intSrvFlowMaxTU = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 19), MessageSize()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowMaxTU.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowMaxTU.setDescription('The maximum datagram size for this  flow  that\n           will conform to the traffic specification. This\n           value cannot exceed the MTU of the interface.')
intSrvFlowBestEffort = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowBestEffort.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowBestEffort.setDescription('The number of packets that  were  remanded  to\n           best effort service.')
intSrvFlowPoliced = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowPoliced.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowPoliced.setDescription("The number of packets policed since the incep-\n           tion of the flow's service.")
intSrvFlowDiscard = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowDiscard.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowDiscard.setDescription("If 'true', the flow  is  to  incur  loss  when\n           traffic is policed.  If 'false', policed traff-\n           ic is treated as best effort traffic.")
intSrvFlowService = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 23), QosService()).setMaxAccess("readonly")
if mibBuilder.loadTexts: intSrvFlowService.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowService.setDescription('The QoS service being applied to this flow.')
intSrvFlowOrder = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowOrder.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowOrder.setDescription('In the event of ambiguity, the order in  which\n           the  classifier  should  make  its comparisons.\n           The row with intSrvFlowOrder=0 is tried  first,\n           and  comparisons  proceed  in  the order of in-\n           creasing value.  Non-serial implementations  of\n           the classifier should emulate this behavior.')
intSrvFlowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 1, 2, 1, 25), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvFlowStatus.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowStatus.setDescription("'active' for all active  flows.   This  object\n           may be used to install static classifier infor-\n           mation, delete classifier information,  or  au-\n           thorize such.")
intSrvFlowNewIndex = MibScalar((1, 3, 6, 1, 2, 1, 52, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: intSrvFlowNewIndex.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowNewIndex.setDescription("This  object  is  used  to  assign  values  to\n           intSrvFlowNumber  as described in 'Textual Con-\n           ventions  for  SNMPv2'.   The  network  manager\n           reads  the  object,  and  then writes the value\n           back in the SET that creates a new instance  of\n           intSrvFlowEntry.   If  the  SET  fails with the\n           code 'inconsistentValue', then the process must\n           be  repeated; If the SET succeeds, then the ob-\n           ject is incremented, and the  new  instance  is\n           created according to the manager's directions.")
intSrvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 2, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribGroup"), ("INT-SERV-MIB", "intSrvFlowsGroup"), ("INT-SERV-MIB", "intSrvGenObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvCompliance = intSrvCompliance.setStatus('current')
if mibBuilder.loadTexts: intSrvCompliance.setDescription('The compliance statement ')
intSrvIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 1)).setObjects(("INT-SERV-MIB", "intSrvIfAttribAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribMaxAllocatedBits"), ("INT-SERV-MIB", "intSrvIfAttribAllocatedBuffer"), ("INT-SERV-MIB", "intSrvIfAttribFlows"), ("INT-SERV-MIB", "intSrvIfAttribPropagationDelay"), ("INT-SERV-MIB", "intSrvIfAttribStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvIfAttribGroup = intSrvIfAttribGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvIfAttribGroup.setDescription('These objects are required  for  Systems  sup-\n           porting the Integrated Services Architecture.')
intSrvFlowsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 2)).setObjects(("INT-SERV-MIB", "intSrvFlowType"), ("INT-SERV-MIB", "intSrvFlowOwner"), ("INT-SERV-MIB", "intSrvFlowDestAddr"), ("INT-SERV-MIB", "intSrvFlowSenderAddr"), ("INT-SERV-MIB", "intSrvFlowDestAddrLength"), ("INT-SERV-MIB", "intSrvFlowSenderAddrLength"), ("INT-SERV-MIB", "intSrvFlowProtocol"), ("INT-SERV-MIB", "intSrvFlowDestPort"), ("INT-SERV-MIB", "intSrvFlowPort"), ("INT-SERV-MIB", "intSrvFlowFlowId"), ("INT-SERV-MIB", "intSrvFlowInterface"), ("INT-SERV-MIB", "intSrvFlowBestEffort"), ("INT-SERV-MIB", "intSrvFlowRate"), ("INT-SERV-MIB", "intSrvFlowBurst"), ("INT-SERV-MIB", "intSrvFlowWeight"), ("INT-SERV-MIB", "intSrvFlowQueue"), ("INT-SERV-MIB", "intSrvFlowMinTU"), ("INT-SERV-MIB", "intSrvFlowMaxTU"), ("INT-SERV-MIB", "intSrvFlowDiscard"), ("INT-SERV-MIB", "intSrvFlowPoliced"), ("INT-SERV-MIB", "intSrvFlowService"), ("INT-SERV-MIB", "intSrvFlowIfAddr"), ("INT-SERV-MIB", "intSrvFlowOrder"), ("INT-SERV-MIB", "intSrvFlowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvFlowsGroup = intSrvFlowsGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvFlowsGroup.setDescription('These objects are required  for  Systems  sup-\n           porting the Integrated Services Architecture.')
intSrvGenObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 1, 3)).setObjects(("INT-SERV-MIB", "intSrvFlowNewIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGenObjectsGroup = intSrvGenObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: intSrvGenObjectsGroup.setDescription('These objects are required  for  Systems  sup-\n           porting the Integrated Services Architecture.')
mibBuilder.exportSymbols("INT-SERV-MIB", Protocol=Protocol, intSrvFlowBestEffort=intSrvFlowBestEffort, intSrvFlowRate=intSrvFlowRate, intSrvFlowService=intSrvFlowService, intSrvFlowOrder=intSrvFlowOrder, intSrvFlowType=intSrvFlowType, intSrvGroups=intSrvGroups, intSrvIfAttribAllocatedBits=intSrvIfAttribAllocatedBits, intSrvGenObjects=intSrvGenObjects, intSrv=intSrv, intSrvGenObjectsGroup=intSrvGenObjectsGroup, intSrvFlowStatus=intSrvFlowStatus, intSrvFlowOwner=intSrvFlowOwner, intSrvFlowMinTU=intSrvFlowMinTU, SessionNumber=SessionNumber, intSrvIfAttribAllocatedBuffer=intSrvIfAttribAllocatedBuffer, BurstSize=BurstSize, intSrvCompliance=intSrvCompliance, intSrvFlowPort=intSrvFlowPort, BitRate=BitRate, intSrvFlowBurst=intSrvFlowBurst, intSrvFlowProtocol=intSrvFlowProtocol, intSrvFlowEntry=intSrvFlowEntry, intSrvFlowDestAddr=intSrvFlowDestAddr, intSrvFlowDestPort=intSrvFlowDestPort, intSrvIfAttribTable=intSrvIfAttribTable, intSrvIfAttribEntry=intSrvIfAttribEntry, intSrvIfAttribFlows=intSrvIfAttribFlows, intSrvFlowDestAddrLength=intSrvFlowDestAddrLength, intSrvFlowNewIndex=intSrvFlowNewIndex, intSrvFlowTable=intSrvFlowTable, intSrvFlowNumber=intSrvFlowNumber, MessageSize=MessageSize, SessionType=SessionType, intSrvCompliances=intSrvCompliances, intSrvObjects=intSrvObjects, intSrvNotifications=intSrvNotifications, PYSNMP_MODULE_ID=intSrv, intSrvIfAttribGroup=intSrvIfAttribGroup, intSrvFlowQueue=intSrvFlowQueue, intSrvFlowFlowId=intSrvFlowFlowId, intSrvFlowPoliced=intSrvFlowPoliced, intSrvFlowDiscard=intSrvFlowDiscard, intSrvFlowIfAddr=intSrvFlowIfAddr, intSrvFlowInterface=intSrvFlowInterface, intSrvFlowsGroup=intSrvFlowsGroup, intSrvIfAttribStatus=intSrvIfAttribStatus, intSrvFlowMaxTU=intSrvFlowMaxTU, intSrvFlowSenderAddr=intSrvFlowSenderAddr, Port=Port, intSrvConformance=intSrvConformance, intSrvIfAttribPropagationDelay=intSrvIfAttribPropagationDelay, intSrvFlowWeight=intSrvFlowWeight, intSrvIfAttribMaxAllocatedBits=intSrvIfAttribMaxAllocatedBits, QosService=QosService, intSrvFlowSenderAddrLength=intSrvFlowSenderAddrLength)
