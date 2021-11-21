#
# PySNMP MIB module VPN-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VPN-TC-STD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:40:08 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, IpAddress, Unsigned32, ObjectIdentity, mib_2, Integer32, NotificationType, iso, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "IpAddress", "Unsigned32", "ObjectIdentity", "mib-2", "Integer32", "NotificationType", "iso", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vpnTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 129))
vpnTcMIB.setRevisions(('2005-11-15 00:00',))
if mibBuilder.loadTexts: vpnTcMIB.setLastUpdated('200511150000Z')
if mibBuilder.loadTexts: vpnTcMIB.setOrganization('Layer 3 Virtual Private Networks (L3VPN) Working Group.')
class VPNId(TextualConvention, OctetString):
    reference = "Fox, B. and Gleeson, B., 'Virtual Private Networks Identifier', RFC 2685, September 1999."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class VPNIdOrZero(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(7, 7), )
mibBuilder.exportSymbols("VPN-TC-STD-MIB", PYSNMP_MODULE_ID=vpnTcMIB, VPNId=VPNId, VPNIdOrZero=VPNIdOrZero, vpnTcMIB=vpnTcMIB)
