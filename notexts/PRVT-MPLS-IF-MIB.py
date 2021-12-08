#
# PySNMP MIB module PRVT-MPLS-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MPLS-IF-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:20:48 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Counter64, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Integer32, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Integer32", "Counter32", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
prvtMplsIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6))
prvtMplsIfMIB.setRevisions(('2011-08-05 00:00', '2010-04-28 00:00',))
if mibBuilder.loadTexts: prvtMplsIfMIB.setLastUpdated('201108050000Z')
if mibBuilder.loadTexts: prvtMplsIfMIB.setOrganization('BATM Advanced Communication')
class PrvtMplsIpAddressMask(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class EgressLabelUsageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("global", 0), ("implicitNull", 1), ("explicitNull", 2))

prvtMplsIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1))
prvtMplsIfaceObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1))
prvtMplsIfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1), )
if mibBuilder.loadTexts: prvtMplsIfaceTable.setStatus('current')
prvtMplsIfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtMplsIfaceEntry.setStatus('current')
ifaceMplsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsRowStatus.setStatus('current')
ifaceMplsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsEnable.setStatus('current')
ifaceMplsPHPEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsPHPEnable.setStatus('current')
ifaceMplsLdpHelloHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsLdpHelloHoldTimer.setStatus('current')
ifaceMplsLdpKeepaliveHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsLdpKeepaliveHoldTimer.setStatus('current')
ifaceMplsRsvpEgrLabelUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 7), EgressLabelUsageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsRsvpEgrLabelUsage.setStatus('current')
ifaceMplsLdpEgrLabelUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 8), EgressLabelUsageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsLdpEgrLabelUsage.setStatus('current')
ifaceMplsSignalCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 1, 1, 1, 9), Bits().clone(namedValues=NamedValues(("sigCapsRsvp", 0), ("sigCapsLdp", 1), ("sigCapsData", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifaceMplsSignalCapabilities.setStatus('current')
prvtMplsRouteObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2))
prvtMplsRouteProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 1), )
if mibBuilder.loadTexts: prvtMplsRouteProtocolTable.setStatus('current')
prvtMplsRouteProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 1, 1), ).setIndexNames((0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteProtocolDirection"), (0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteProtocolType"))
if mibBuilder.loadTexts: prvtMplsRouteProtocolEntry.setStatus('current')
prvtMplsRouteProtocolDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2))))
if mibBuilder.loadTexts: prvtMplsRouteProtocolDirection.setStatus('current')
prvtMplsRouteProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("bgp", 1), ("connected", 2), ("isisl1", 3), ("isisl2", 4), ("kernel", 5), ("ospf", 6), ("rip", 7), ("static", 8))))
if mibBuilder.loadTexts: prvtMplsRouteProtocolType.setStatus('current')
prvtMplsRouteProtocolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsRouteProtocolRowStatus.setStatus('current')
prvtMplsRouteAddressTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 2), )
if mibBuilder.loadTexts: prvtMplsRouteAddressTable.setStatus('current')
prvtMplsRouteAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 2, 1), ).setIndexNames((0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteProtocolDirection"), (0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteAddressIpAddrMask"))
if mibBuilder.loadTexts: prvtMplsRouteAddressEntry.setStatus('current')
prvtMplsRouteAddressIpAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 2, 1, 2), PrvtMplsIpAddressMask())
if mibBuilder.loadTexts: prvtMplsRouteAddressIpAddrMask.setStatus('current')
prvtMplsRouteAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 6, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsRouteAddressRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-MPLS-IF-MIB", prvtMplsIfaceObjs=prvtMplsIfaceObjs, prvtMplsRouteProtocolTable=prvtMplsRouteProtocolTable, ifaceMplsLdpHelloHoldTimer=ifaceMplsLdpHelloHoldTimer, prvtMplsRouteProtocolEntry=prvtMplsRouteProtocolEntry, ifaceMplsRowStatus=ifaceMplsRowStatus, prvtMplsRouteProtocolType=prvtMplsRouteProtocolType, prvtMplsRouteObjs=prvtMplsRouteObjs, prvtMplsIfaceEntry=prvtMplsIfaceEntry, ifaceMplsLdpKeepaliveHoldTimer=ifaceMplsLdpKeepaliveHoldTimer, ifaceMplsEnable=ifaceMplsEnable, prvtMplsIfaceTable=prvtMplsIfaceTable, prvtMplsIfMIB=prvtMplsIfMIB, prvtMplsRouteProtocolDirection=prvtMplsRouteProtocolDirection, prvtMplsRouteAddressTable=prvtMplsRouteAddressTable, ifaceMplsLdpEgrLabelUsage=ifaceMplsLdpEgrLabelUsage, ifaceMplsPHPEnable=ifaceMplsPHPEnable, prvtMplsIfMIBObjects=prvtMplsIfMIBObjects, prvtMplsRouteAddressIpAddrMask=prvtMplsRouteAddressIpAddrMask, prvtMplsRouteAddressRowStatus=prvtMplsRouteAddressRowStatus, EgressLabelUsageType=EgressLabelUsageType, prvtMplsRouteProtocolRowStatus=prvtMplsRouteProtocolRowStatus, PrvtMplsIpAddressMask=PrvtMplsIpAddressMask, ifaceMplsRsvpEgrLabelUsage=ifaceMplsRsvpEgrLabelUsage, PYSNMP_MODULE_ID=prvtMplsIfMIB, prvtMplsRouteAddressEntry=prvtMplsRouteAddressEntry, ifaceMplsSignalCapabilities=ifaceMplsSignalCapabilities)
