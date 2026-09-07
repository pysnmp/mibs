#
# PySNMP MIB module CISCO-SUBSCRIBER-SESSION-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SUBSCRIBER-SESSION-TC-MIB
# Source digest sha256:197ff180969c0ea21eb43f0311b2bb01aeeb86d452bfb280740acb070457d071
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberSessionTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 785))
ciscoSubscriberSessionTcMIB.setRevisions(('2007-09-26 00:00',))
if mibBuilder.loadTexts: ciscoSubscriberSessionTcMIB.setLastUpdated('2012-01-27 00:00')
if mibBuilder.loadTexts: ciscoSubscriberSessionTcMIB.setOrganization('Cisco Systems, Inc.')
class SubSessionType(TextualConvention, Integer32):
    reference = "W. Simpson, 'The Point-to-Point Protocol (PPP)', RFC-1661, July 1994. R. Droms, 'Dynamic Host Configuration Protocol', RFC-2131, March 1997. A. Valencia, M. Littlewood, T. Kolar, 'Cisco Layer Two Forwarding Protocol (L2F)', RFC-2341, May 1998. L. Mamakos, K. Lidl, J. Evarts, D. Carrel, D. Simone, and R. Wheeler, 'A Method for Transmitting PPP Over Ethernet (PPPoE)', RFC-2516, February 1999. W. Townsley, A. Valencia, A. Rubens, G. Pall, G. Zorn, and B. Palter, 'Layer Two Tunneling Protocol (L2TP)', RFC-2661, August 1999. C. Rigney, S. Willens, A. Rubens, and W. Simpson, 'Remote Authentication Dial-In User Service (RADIUS)', RFC-2865, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("all", 1), ("other", 2), ("pppSubscriber", 3), ("pppoeSubscriber", 4), ("l2tpSubscriber", 5), ("l2fSubscriber", 6), ("ipInterfaceSubscriber", 7), ("ipPktSubscriber", 8), ("ipDhcpv4Subscriber", 9), ("ipRadiusSubscriber", 10), ("l2MacSubscriber", 11), ("l2Dhcpv4Subscriber", 12), ("l2RadiusSubscriber", 13))

class SubSessionTypes(TextualConvention, Bits):
    reference = "W. Simpson, 'The Point-to-Point Protocol (PPP)', RFC-1661, July 1994. R. Droms, 'Dynamic Host Configuration Protocol', RFC-2131, March 1997. A. Valencia, M. Littlewood, T. Kolar, 'Cisco Layer Two Forwarding Protocol (L2F)', RFC-2341, May 1998. L. Mamakos, K. Lidl, J. Evarts, D. Carrel, D. Simone, and R. Wheeler, 'A Method for Transmitting PPP Over Ethernet (PPPoE)', RFC-2516, February 1999. W. Townsley, A. Valencia, A. Rubens, G. Pall, G. Zorn, and B. Palter, 'Layer Two Tunneling Protocol (L2TP)', RFC-2661, August 1999. C. Rigney, S. Willens, A. Rubens, and W. Simpson, 'Remote Authentication Dial-In User Service (RADIUS)', RFC-2865, June 2000."
    status = 'current'
    namedValues = NamedValues(("pppSubscriber", 0), ("pppoeSubscriber", 1), ("l2tpSubscriber", 2), ("l2fSubscriber", 3), ("ipInterfaceSubscriber", 4), ("ipPktSubscriber", 5), ("ipDhcpv4Subscriber", 6), ("ipRadiusSubscriber", 7), ("l2MacSubscriber", 8), ("l2Dhcpv4Subscriber", 9), ("l2RadiusSubscriber", 10))

class SubSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("pending", 2), ("up", 3))

class SubSessionRedundancyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("other", 2), ("active", 3), ("standby", 4))

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-SESSION-TC-MIB", PYSNMP_MODULE_ID=ciscoSubscriberSessionTcMIB, SubSessionRedundancyMode=SubSessionRedundancyMode, SubSessionState=SubSessionState, SubSessionType=SubSessionType, SubSessionTypes=SubSessionTypes, ciscoSubscriberSessionTcMIB=ciscoSubscriberSessionTcMIB)
