#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HCNUM-TC
# Produced by pysmi-1.1.12 at Mon Jul  1 09:15:50 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, mib_2, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "mib-2", "Gauge32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
class CounterBasedGauge64(TextualConvention, Counter64):
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", CounterBasedGauge64=CounterBasedGauge64, ZeroBasedCounter64=ZeroBasedCounter64, PYSNMP_MODULE_ID=hcnumTC, hcnumTC=hcnumTC)
