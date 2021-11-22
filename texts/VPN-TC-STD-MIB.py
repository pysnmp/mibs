#
# PySNMP MIB module VPN-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VPN-TC-STD-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:21:33 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, mib_2, Bits, Unsigned32, iso, IpAddress, TimeTicks, Counter32, MibIdentifier, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "mib-2", "Bits", "Unsigned32", "iso", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("VPN-TC-STD-MIB", vpnTcMIB=vpnTcMIB, VPNId=VPNId, VPNIdOrZero=VPNIdOrZero, PYSNMP_MODULE_ID=vpnTcMIB)
