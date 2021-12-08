#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:56:21 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Counter32, Unsigned32, mib_2, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, IpAddress, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "Unsigned32", "mib-2", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6FlowLabelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 103))
ipv6FlowLabelMIB.setRevisions(('2003-08-28 00:00',))
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setLastUpdated('200308280000Z')
if mibBuilder.loadTexts: ipv6FlowLabelMIB.setOrganization('IETF Operations and Management Area')
class IPv6FlowLabel(TextualConvention, Integer32):
    reference = 'Internet Protocol, Version 6 (IPv6) specification, section 6. RFC 2460. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class IPv6FlowLabelOrAny(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1048575), )
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", ipv6FlowLabelMIB=ipv6FlowLabelMIB, IPv6FlowLabelOrAny=IPv6FlowLabelOrAny, PYSNMP_MODULE_ID=ipv6FlowLabelMIB, IPv6FlowLabel=IPv6FlowLabel)
