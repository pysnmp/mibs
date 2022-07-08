#
# PySNMP MIB module DIFFSERV-DSCP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DIFFSERV-DSCP-TC
# Produced by pysmi-1.1.8 at Fri Jul  8 08:49:21 2022
# On host fv-az42-349 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Integer32, Counter32, MibIdentifier, TimeTicks, NotificationType, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Bits, Unsigned32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "Counter32", "MibIdentifier", "TimeTicks", "NotificationType", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Bits", "Unsigned32", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", PYSNMP_MODULE_ID=diffServDSCPTC, Dscp=Dscp, diffServDSCPTC=diffServDSCPTC, DscpOrAny=DscpOrAny)
