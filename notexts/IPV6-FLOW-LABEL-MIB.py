#
# PySNMP MIB module IPV6-FLOW-LABEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-FLOW-LABEL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:03:50 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, mib_2, Counter32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ModuleIdentity, TimeTicks, Gauge32, Counter64, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "mib-2", "Counter32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter64", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("IPV6-FLOW-LABEL-MIB", PYSNMP_MODULE_ID=ipv6FlowLabelMIB, ipv6FlowLabelMIB=ipv6FlowLabelMIB, IPv6FlowLabelOrAny=IPv6FlowLabelOrAny, IPv6FlowLabel=IPv6FlowLabel)
