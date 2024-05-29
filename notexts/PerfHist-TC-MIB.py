#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Wed May 29 08:07:29 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, mib_2, IpAddress, MibIdentifier, Integer32, NotificationType, Counter64, ModuleIdentity, Unsigned32, iso, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "mib-2", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "Counter64", "ModuleIdentity", "Unsigned32", "iso", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
perfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 58))
perfHistTCMIB.setRevisions(('2003-08-13 00:00', '1998-11-07 11:00',))
if mibBuilder.loadTexts: perfHistTCMIB.setLastUpdated('200308130000Z')
if mibBuilder.loadTexts: perfHistTCMIB.setOrganization('IETF AToM MIB WG')
class PerfCurrentCount(TextualConvention, Gauge32):
    status = 'current'

class PerfIntervalCount(TextualConvention, Gauge32):
    status = 'current'

class PerfTotalCount(TextualConvention, Gauge32):
    status = 'current'

mibBuilder.exportSymbols("PerfHist-TC-MIB", PYSNMP_MODULE_ID=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount, perfHistTCMIB=perfHistTCMIB, PerfCurrentCount=PerfCurrentCount, PerfTotalCount=PerfTotalCount)
