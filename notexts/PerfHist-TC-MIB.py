#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:00:07 2024
# On host fv-az888-540 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, TimeTicks, Bits, Counter64, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, mib_2, MibIdentifier, Counter32, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "TimeTicks", "Bits", "Counter64", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "mib-2", "MibIdentifier", "Counter32", "NotificationType", "Integer32", "ObjectIdentity")
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

mibBuilder.exportSymbols("PerfHist-TC-MIB", PYSNMP_MODULE_ID=perfHistTCMIB, PerfIntervalCount=PerfIntervalCount, PerfCurrentCount=PerfCurrentCount, PerfTotalCount=PerfTotalCount, perfHistTCMIB=perfHistTCMIB)
