#
# PySNMP MIB module DIFFSERV-DSCP-TC (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/DIFFSERV-DSCP-TC
# Produced by pysmi-1.1.12 at Thu Sep 26 02:09:57 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, iso, Counter32, Counter64, mib_2, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "iso", "Counter32", "Counter64", "mib-2", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier")
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
mibBuilder.exportSymbols("DIFFSERV-DSCP-TC", PYSNMP_MODULE_ID=diffServDSCPTC, DscpOrAny=DscpOrAny, Dscp=Dscp, diffServDSCPTC=diffServDSCPTC)
