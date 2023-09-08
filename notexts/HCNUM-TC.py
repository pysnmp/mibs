#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HCNUM-TC
# Produced by pysmi-1.1.8 at Fri Sep  8 07:54:59 2023
# On host fv-az887-856 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, mib_2, ModuleIdentity, ObjectIdentity, IpAddress, Counter64, TimeTicks, Bits, iso, NotificationType, Integer32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "mib-2", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter64", "TimeTicks", "Bits", "iso", "NotificationType", "Integer32", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
class CounterBasedGauge64(TextualConvention, Counter64):
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", PYSNMP_MODULE_ID=hcnumTC, hcnumTC=hcnumTC, ZeroBasedCounter64=ZeroBasedCounter64, CounterBasedGauge64=CounterBasedGauge64)
