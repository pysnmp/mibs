#
# PySNMP MIB module CISCO-CEF-TC (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-CEF-TC
# Source digest sha256:dadd94c86f68de099508dc70e6076ce9650b37f3f56f79694655f810d63355b5
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCefTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 493))
ciscoCefTextualConventions.setRevisions(('2005-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCefTextualConventions.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCefTextualConventions.setLastUpdated('2005-09-30 00:00')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setContactInfo('Postal: Cisco Systems, Inc.\n          170 West Tasman Drive\n          San Jose, CA 95134-1706\n          USA\n\n          Tel: +1 800 553-NETS\n\n          E-mail: cs-cef@cisco.com')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setDescription('This MIB module defines Textual Conventions and\n          OBJECT-IDENTITIES for use in documents defining\n          management information base (MIBs) modules for \n          managing Cisco Express Forwarding (CEF).')
class CefIpVersion(TextualConvention, Integer32):
    description = 'The version of CEF IP forwarding.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class CefAdjLinkType(TextualConvention, Integer32):
    description = 'Link type for the adjacency. The adjacency link type \n          identifies protocol stack on neighbour device which will \n          process packets fed through adjacency.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("mpls", 3), ("raw", 4), ("unknown", 5))

class CefAdjacencySource(TextualConvention, Bits):
    description = "The mechanism by which the adjacency is learned.\n          As the mechanism of learning the adjacency can be\n          multiple (e.g. 'arp' and 'atmPVC'), hence the \n          value of this object represents the bit mask of\n          adjacency sources."
    status = 'current'
    namedValues = NamedValues(("atom", 0), ("linkRawAdj", 1), ("ipPseudowireAdj", 2), ("arp", 3), ("p2pAdj", 4), ("frMap", 5), ("atmPVC", 6), ("atmSVC", 7), ("atmTVC", 8), ("nbma", 9), ("mpoa", 10), ("atmBundle", 11), ("lec", 12), ("nhrp", 13), ("ipv6ND", 14), ("cmcc", 15), ("ipv6SixtoFourTunnel", 16), ("ipv6IsaTapTunnel", 17), ("ipv6AutoTunnel", 18), ("fibLc", 19), ("virtual", 20), ("multicast", 21), ("unknown", 22))

class CefPathType(TextualConvention, Integer32):
    description = 'Type of the CEF Path.\n           receive(1)          : path for the address\n                                 configured on any of the\n                                 interface in the device.\n\n           connectedPrefix(2)  : connected prefix path\n\n           attachedPrefix(3)   : attached prefix path\n\n           attachedHost(4)     : attached host path \n\n           attachedNexthop(5)  : attached next hop path\n\n           recursiveNexthop(6) : recursive next hop path\n\n           adjacencyPrefix(7)  : adjacency prefix path\n\n           specialPrefix(8)    : special prefix path\n\n           unknown(9):         : unknown  path\n         .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("receive", 1), ("connectedPrefix", 2), ("attachedPrefix", 3), ("attachedHost", 4), ("attachedNexthop", 5), ("recursiveNexthop", 6), ("adjacencyPrefix", 7), ("specialPrefix", 8), ("unknown", 9))

class CefPrefixSearchState(TextualConvention, Integer32):
    description = 'The state of prefix search operation. \n          The description of each state is given below:\n\n            running(1)      : this state signifies that a prefix \n                              search request is running.\n\n            matchFound(2)   : this state signifies that a prefix \n                              search request is completed and a prefix\n                              match has been found.\n\n            noMatchFound(3) : this state signifies that a prefix \n                              search request is completed and a prefix\n                              match has not been found.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("running", 1), ("matchFound", 2), ("noMatchFound", 3))

class CefForwardingElementSpecialType(TextualConvention, Integer32):
    description = 'Type of special forwarding element \n\n           illegal(1)   : illegal special forwarding element.\n                          the packet will be dropped.\n\n           punt(2)      : the packet will be punted to the\n                          next switching path\n\n           drop(3)      : not supported for Destination IP to next hop\n                          interface and the packet will be dropped\n\n           discard(4)   : the packet is for Destination IP through\n                          next hop interface and it will be discarded\n\n           null(5)      : the packet is for Destination IP to null0,\n                          it will be dropped\n\n           glean(6)     : an attempt will be made to complete the\n                          encapsulation string through address \n                          resolution\n\n           unResolved(7): unresolved forwarding element.\n                          the packet will be dropped unconditionally. \n\n           noRoute(8)   : no route forwarding element.\n                          This forwarding element will result\n                          in rate limited punts to the next\n                          switching path(to generate ICMP \n                          no route message) \n\n           none(9)      : not a special forwarding element and\n                          the value of this object should be\n                          ignored \n\n\n          '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("illegal", 1), ("punt", 2), ("drop", 3), ("discard", 4), ("null", 5), ("glean", 6), ("unresolved", 7), ("noRoute", 8), ("none", 9))

class CefMplsLabelList(TextualConvention, OctetString):
    description = "This contains a list of MPLS Labels, \n\t  each separated by the ';' (semi-colon) character.  \n\n          MPLS Label values are in accordance with the\n          MplsLabel TEXTUAL-CONVENTION defined in the\n          MPLS-TC-MIB.\n\n\t  The following is en example containing two MPLS labels: \n\t    \n\t     4294;100\n     \t\t\t\t\n          An empty string value for this object indicates\n          no MPLS Labels in this list. \n\t "
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CefAdminStatus(TextualConvention, Integer32):
    description = 'Admin status of CEF. The admin status of CEF\n          may differ from the oper status of CEF depending\n          upon the success of the admin operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CefOperStatus(TextualConvention, Integer32):
    description = 'Operational status of CEF.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CefFailureReason(TextualConvention, Integer32):
    description = 'Reason of CEF Failure:\n\n            none(1)                : no failure \n\n            mallocFailure(2)       : memory allocation failed for CEF\n\n            hwFailure(3)           : hardware interface failure \n                                     for CEF\n    \n            keepaliveFailure(4)    : keepalive was not received from \n                                     the CEF peer entity\n\n            noMsgBuffer(5)         : message buffers were exhausted \n                                     while preparing IPC message to be \n                                     sent to the CEF peer entity\n\n            invalidMsgSize(6)      : IPC message was received with \n                                     invalid size from the\n                                     CEF peer entity\n\n            internalError(7)       : Some other internal error was \n                                     detected for CEF\n           '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("mallocFailure", 2), ("hwFailure", 3), ("keepaliveFailure", 4), ("noMsgBuffer", 5), ("invalidMsgSize", 6), ("internalError", 7))

class CefCCType(TextualConvention, Integer32):
    description = 'Type of the consistency checker.\n\n        lcDetect         : This is an active consistency checker\n                           which is triggered when a packet cannot \n                           be forwarded because the prefix is not\n                           in the forwarding table. It Detects \n                           missing prefixes on the linecard CEF \n                           database by sending the missing prefixes \n                           to the RP.\n                      \n        scanFibLcRp      : This is an passive consistency checker\n                           which performs a passive scan check of\n                           the table on the line card.\n\n                           This consistency checker operates on \n                           the line card by examining the FIB table \n                           for a configurable time period and sending \n                           the next n prefixes to the RP. \n\n        scanFibRpLc      : This is an passive consistency checker\n                           which performs a passive scan check of\n                           RP by examining the FIB table for \n                           a configurable period and\n                           sending the next n prefixes to the \n                           line card. \n\n        scanRibFib       : This is an passive consistency checker\n                           which compares routing information base \n                           (RIB) to the FIB table at a configurable\n                           interval and provides the number of \n                           entries missing from the FIB table. \n\n        scanFibRib       : This is an passive consistency checker\n                           which compares FIB Tables to the \n                           routing information base (RIB) \n                           at a configurable interval and provides \n                           the number of entries missing from the \n                           FIB table. \n\n        scanFibHwSw      : This is an passive consistency checker\n                           which compares FIB Tables in hardware\n                           to the FIB Tables in RP.\n\n        scanFibSwHw      : This is an passive consistency checker\n                           which compares FIB Tables in RP\n                           to the FIB Tables in hardware.\n\n        fullScanRibFib   : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the entire routing \n                           information base (RIB) to the FIB table\n                           and provide the number of entries missing\n                            from the FIB Table.\n \n        fullScanFibRib   : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the FIB table to the \n                           routing information base (RIB)\n                           and provide the number of entries missing\n                           from the FIB Table.\n\n        fullScanFibRpLc  : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the RP FIB Table \n                           with FIB Table on each LC and report \n                           inconsistencies.\n                        \n        fullScanFibLcRp  : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the Fib Table on LC \n                           with FIB table on RP and report \n                           inconsistencies.\n\n        fullScanFibHwSw  : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the Fib Table in \n                           hardware with FIB table in RP and report \n                           inconsistencies.\n\n        fullScanFibSwHw  : This is an active consistency checker\n                           which is triggered by Management Station \n                           request. It compares the Fib Table in RP \n                           with FIB table in hardware and report \n                           inconsistencies.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("lcDetect", 1), ("scanFibLcRp", 2), ("scanFibRpLc", 3), ("scanRibFib", 4), ("scanFibRib", 5), ("scanFibHwSw", 6), ("scanFibSwHw", 7), ("fullScanRibFib", 8), ("fullScanFibRib", 9), ("fullScanFibRpLc", 10), ("fullScanFibLcRp", 11), ("fullScanFibHwSw", 12), ("fullScanFibSwHw", 13))

class CefCCAction(TextualConvention, Integer32):
    description = 'The action to be performed for the consistency\n          checkers.\n          \n            ccActionStart(1)   :  start the Consistency checker\n                                  operation.\n  \n            ccActionAbort(2)   :  abort the Consistency checker \n                                  operation. After aborting, the \n                                  active process must recover. \n                                  This can take some time, and \n                                  during this period, the scan \n                                  cannot be restarted.\n\n            ccActionNone(3)    :  no operation is being performed \n                                  on consistency checkers.\n\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccActionStart", 1), ("ccActionAbort", 2), ("ccActionNone", 3))

class CefCCStatus(TextualConvention, Integer32):
    description = 'The status of consistency checker operation. \n          The description of each state is given below:\n\n            ccStatusIdle(1)    :  this state signifies that\n                                  no consistency checker request\n                                  is being performed.\n  \n            ccStatusRunning(2) :  this state signifies that \n                                  consistency checker request is \n                                  in progress.\n\n            ccStatusDone(3)     : this state signifies that \n                                  consistency checker request is \n                                  over. \n                                \n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccStatusIdle", 1), ("ccStatusRunning", 2), ("ccStatusDone", 3))

mibBuilder.exportSymbols("CISCO-CEF-TC", CefAdjLinkType=CefAdjLinkType, CefAdjacencySource=CefAdjacencySource, CefAdminStatus=CefAdminStatus, CefCCAction=CefCCAction, CefCCStatus=CefCCStatus, CefCCType=CefCCType, CefFailureReason=CefFailureReason, CefForwardingElementSpecialType=CefForwardingElementSpecialType, CefIpVersion=CefIpVersion, CefMplsLabelList=CefMplsLabelList, CefOperStatus=CefOperStatus, CefPathType=CefPathType, CefPrefixSearchState=CefPrefixSearchState, PYSNMP_MODULE_ID=ciscoCefTextualConventions, ciscoCefTextualConventions=ciscoCefTextualConventions)
