#
# PySNMP MIB module DIFFSERV-DSCP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DIFFSERV-DSCP-TC
# Produced by pysmi-1.1.10 at Mon Oct 30 02:11:40 2023
# On host fv-az879-766 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, mib_2, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "mib-2", "Counter32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
diffServDSCPTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 96))
diffServDSCPTC.setRevisions(('2002-05-09 00:00',))
if mibBuilder.loadTexts: diffServDSCPTC.setLastUpdated('200205090000Z')
if mibBuilder.loadTexts: diffServDSCPTC.setOrganization('IETF Differentiated Services WG')
class Dscp(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 63)

class DscpOrAny(TextualConvention, Integer32):
    reference = 'RFC 2474, RFC 2780'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 63), )
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", diffServDSCPTC=diffServDSCPTC, Dscp=Dscp, DscpOrAny=DscpOrAny, PYSNMP_MODULE_ID=diffServDSCPTC)
