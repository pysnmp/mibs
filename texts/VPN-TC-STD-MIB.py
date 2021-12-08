#
# PySNMP MIB module VPN-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VPN-TC-STD-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:19:02 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, Counter32, NotificationType, Gauge32, IpAddress, iso, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "Counter32", "NotificationType", "Gauge32", "IpAddress", "iso", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vpnTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 129))
vpnTcMIB.setRevisions(('2005-11-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vpnTcMIB.setRevisionsDescriptions(('Initial version, published as RFC 4265.',))
if mibBuilder.loadTexts: vpnTcMIB.setLastUpdated('200511150000Z')
if mibBuilder.loadTexts: vpnTcMIB.setOrganization('Layer 3 Virtual Private Networks (L3VPN) Working Group.')
if mibBuilder.loadTexts: vpnTcMIB.setContactInfo('Benson Schliesser\n         bensons@savvis.net\n\n         Thomas D. Nadeau\n         tnadeau@cisco.com\n\n         This TC MIB is a product of the PPVPN\n         http://www.ietf.org/html.charters/ppvpn-charter.html\n         and subsequently the L3VPN\n         http://www.ietf.org/html.charters/l3vpn-charter.html\n         working groups.\n\n         Comments and discussion should be directed to\n         l3vpn@ietf.org')
if mibBuilder.loadTexts: vpnTcMIB.setDescription('This MIB contains TCs for VPNs.\n\n         Copyright (C) The Internet Society (2005).  This version\n         of this MIB module is part of RFC 4265;  see the RFC\n         itself for full legal notices.')
class VPNId(TextualConvention, OctetString):
    reference = "Fox, B. and Gleeson, B., 'Virtual Private Networks\n         Identifier', RFC 2685, September 1999."
    description = 'The purpose of a VPN-ID is to uniquely identify a VPN.\n         The Global VPN Identifier format is:\n         3 octet VPN Authority, Organizationally Unique Identifier\n         followed by 4 octet VPN index identifying VPN according\n         to OUI'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class VPNIdOrZero(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the\n         VPNId textual convention that defines a non-zero-length\n         OCTET STRING to identify a physical entity.  This extension\n         permits the additional value of a zero-length OCTET STRING.\n\n         The semantics of the value zero-length OCTET STRING are\n         object-specific and must therefore be defined\n         as part of the description of any object that uses this\n         syntax.  Examples of usage of this extension are\n         situations where none or all VPN IDs need to be\n         referenced.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(7, 7), )
mibBuilder.exportSymbols("VPN-TC-STD-MIB", PYSNMP_MODULE_ID=vpnTcMIB, vpnTcMIB=vpnTcMIB, VPNIdOrZero=VPNIdOrZero, VPNId=VPNId)
