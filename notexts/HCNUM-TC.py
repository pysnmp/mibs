#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HCNUM-TC
# Produced by pysmi-1.1.12 at Tue Dec  3 11:36:24 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, Bits, TimeTicks, ModuleIdentity, NotificationType, IpAddress, Integer32, MibIdentifier, ObjectIdentity, Gauge32, mib_2, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "Bits", "TimeTicks", "ModuleIdentity", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "ObjectIdentity", "Gauge32", "mib-2", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
class CounterBasedGauge64(TextualConvention, Counter64):
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", PYSNMP_MODULE_ID=hcnumTC, ZeroBasedCounter64=ZeroBasedCounter64, hcnumTC=hcnumTC, CounterBasedGauge64=CounterBasedGauge64)
