#
# PySNMP MIB module VPN-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/VPN-TC-STD-MIB
# Produced by pysmi-1.1.0 at Fri Nov 19 14:38:39 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, ModuleIdentity, MibIdentifier, iso, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Unsigned32, mib_2, ObjectIdentity, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ModuleIdentity", "MibIdentifier", "iso", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Unsigned32", "mib-2", "ObjectIdentity", "Gauge32", "IpAddress")
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
mibBuilder.exportSymbols("VPN-TC-STD-MIB", vpnTcMIB=vpnTcMIB, VPNIdOrZero=VPNIdOrZero, VPNId=VPNId, PYSNMP_MODULE_ID=vpnTcMIB)
