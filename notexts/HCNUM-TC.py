#
# PySNMP MIB module HCNUM-TC (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/HCNUM-TC
# Produced by pysmi-1.1.12 at Mon Sep 16 14:50:45 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, MibIdentifier, iso, ObjectIdentity, TimeTicks, Integer32, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter64, Bits, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibIdentifier", "iso", "ObjectIdentity", "TimeTicks", "Integer32", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter64", "Bits", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcnumTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 78))
hcnumTC.setRevisions(('2000-06-08 00:00',))
if mibBuilder.loadTexts: hcnumTC.setLastUpdated('200006080000Z')
if mibBuilder.loadTexts: hcnumTC.setOrganization('IETF OPS Area')
class CounterBasedGauge64(TextualConvention, Counter64):
    status = 'current'

class ZeroBasedCounter64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("HCNUM-TC", ZeroBasedCounter64=ZeroBasedCounter64, hcnumTC=hcnumTC, CounterBasedGauge64=CounterBasedGauge64, PYSNMP_MODULE_ID=hcnumTC)
