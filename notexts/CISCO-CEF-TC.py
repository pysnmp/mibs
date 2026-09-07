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
if mibBuilder.loadTexts: ciscoCefTextualConventions.setLastUpdated('2005-09-30 00:00')
if mibBuilder.loadTexts: ciscoCefTextualConventions.setOrganization('Cisco Systems, Inc.')
class CefIpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class CefAdjLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2), ("mpls", 3), ("raw", 4), ("unknown", 5))

class CefAdjacencySource(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("atom", 0), ("linkRawAdj", 1), ("ipPseudowireAdj", 2), ("arp", 3), ("p2pAdj", 4), ("frMap", 5), ("atmPVC", 6), ("atmSVC", 7), ("atmTVC", 8), ("nbma", 9), ("mpoa", 10), ("atmBundle", 11), ("lec", 12), ("nhrp", 13), ("ipv6ND", 14), ("cmcc", 15), ("ipv6SixtoFourTunnel", 16), ("ipv6IsaTapTunnel", 17), ("ipv6AutoTunnel", 18), ("fibLc", 19), ("virtual", 20), ("multicast", 21), ("unknown", 22))

class CefPathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("receive", 1), ("connectedPrefix", 2), ("attachedPrefix", 3), ("attachedHost", 4), ("attachedNexthop", 5), ("recursiveNexthop", 6), ("adjacencyPrefix", 7), ("specialPrefix", 8), ("unknown", 9))

class CefPrefixSearchState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("running", 1), ("matchFound", 2), ("noMatchFound", 3))

class CefForwardingElementSpecialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("illegal", 1), ("punt", 2), ("drop", 3), ("discard", 4), ("null", 5), ("glean", 6), ("unresolved", 7), ("noRoute", 8), ("none", 9))

class CefMplsLabelList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CefAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CefOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class CefFailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("mallocFailure", 2), ("hwFailure", 3), ("keepaliveFailure", 4), ("noMsgBuffer", 5), ("invalidMsgSize", 6), ("internalError", 7))

class CefCCType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("lcDetect", 1), ("scanFibLcRp", 2), ("scanFibRpLc", 3), ("scanRibFib", 4), ("scanFibRib", 5), ("scanFibHwSw", 6), ("scanFibSwHw", 7), ("fullScanRibFib", 8), ("fullScanFibRib", 9), ("fullScanFibRpLc", 10), ("fullScanFibLcRp", 11), ("fullScanFibHwSw", 12), ("fullScanFibSwHw", 13))

class CefCCAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccActionStart", 1), ("ccActionAbort", 2), ("ccActionNone", 3))

class CefCCStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ccStatusIdle", 1), ("ccStatusRunning", 2), ("ccStatusDone", 3))

mibBuilder.exportSymbols("CISCO-CEF-TC", CefAdjLinkType=CefAdjLinkType, CefAdjacencySource=CefAdjacencySource, CefAdminStatus=CefAdminStatus, CefCCAction=CefCCAction, CefCCStatus=CefCCStatus, CefCCType=CefCCType, CefFailureReason=CefFailureReason, CefForwardingElementSpecialType=CefForwardingElementSpecialType, CefIpVersion=CefIpVersion, CefMplsLabelList=CefMplsLabelList, CefOperStatus=CefOperStatus, CefPathType=CefPathType, CefPrefixSearchState=CefPrefixSearchState, PYSNMP_MODULE_ID=ciscoCefTextualConventions, ciscoCefTextualConventions=ciscoCefTextualConventions)
