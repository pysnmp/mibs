#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 16:24:44 2022
# On host fv-az126-328 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Gauge32, Counter32, Integer32, IpAddress, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, mib_2, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Gauge32", "Counter32", "Integer32", "IpAddress", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "mib-2", "Counter64", "ObjectIdentity")
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
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", IPv6FlowLabelOrAny=IPv6FlowLabelOrAny, PYSNMP_MODULE_ID=ipv6FlowLabelMIB, ipv6FlowLabelMIB=ipv6FlowLabelMIB, IPv6FlowLabel=IPv6FlowLabel)
