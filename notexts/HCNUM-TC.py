#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HCNUM-TC
# Produced by pysmi-1.1.10 at Mon Oct 30 02:11:25 2023
# On host fv-az879-766 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, NotificationType, TimeTicks, Integer32, iso, Counter64, IpAddress, Unsigned32, Counter32, mib_2, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "iso", "Counter64", "IpAddress", "Unsigned32", "Counter32", "mib-2", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
class CounterBasedGauge64(TextualConvention, Counter64):
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", PYSNMP_MODULE_ID=hcnumTC, hcnumTC=hcnumTC, CounterBasedGauge64=CounterBasedGauge64, ZeroBasedCounter64=ZeroBasedCounter64)
