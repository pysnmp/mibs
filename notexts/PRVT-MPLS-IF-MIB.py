#
# PySNMP MIB module PRVT-MPLS-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-MPLS-IF-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:19:48 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, Unsigned32, IpAddress, iso, Counter32, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Unsigned32", "IpAddress", "iso", "Counter32", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity", "ModuleIdentity")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("PRVT-MPLS-IF-MIB", prvtMplsIfaceEntry=prvtMplsIfaceEntry, prvtMplsRouteProtocolDirection=prvtMplsRouteProtocolDirection, PYSNMP_MODULE_ID=prvtMplsIfMIB, prvtMplsIfaceTable=prvtMplsIfaceTable, ifaceMplsLdpKeepaliveHoldTimer=ifaceMplsLdpKeepaliveHoldTimer, ifaceMplsRsvpEgrLabelUsage=ifaceMplsRsvpEgrLabelUsage, prvtMplsRouteAddressIpAddrMask=prvtMplsRouteAddressIpAddrMask, prvtMplsRouteAddressEntry=prvtMplsRouteAddressEntry, prvtMplsRouteProtocolTable=prvtMplsRouteProtocolTable, EgressLabelUsageType=EgressLabelUsageType, prvtMplsRouteObjs=prvtMplsRouteObjs, prvtMplsRouteAddressTable=prvtMplsRouteAddressTable, prvtMplsIfaceObjs=prvtMplsIfaceObjs, PrvtMplsIpAddressMask=PrvtMplsIpAddressMask, ifaceMplsRowStatus=ifaceMplsRowStatus, prvtMplsRouteProtocolRowStatus=prvtMplsRouteProtocolRowStatus, prvtMplsIfMIB=prvtMplsIfMIB, ifaceMplsPHPEnable=ifaceMplsPHPEnable, ifaceMplsLdpEgrLabelUsage=ifaceMplsLdpEgrLabelUsage, prvtMplsRouteProtocolType=prvtMplsRouteProtocolType, ifaceMplsSignalCapabilities=ifaceMplsSignalCapabilities, prvtMplsIfMIBObjects=prvtMplsIfMIBObjects, prvtMplsRouteProtocolEntry=prvtMplsRouteProtocolEntry, ifaceMplsLdpHelloHoldTimer=ifaceMplsLdpHelloHoldTimer, ifaceMplsEnable=ifaceMplsEnable, prvtMplsRouteAddressRowStatus=prvtMplsRouteAddressRowStatus)
