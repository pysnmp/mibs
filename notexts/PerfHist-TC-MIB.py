#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:37:40 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, Integer32, IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter64, Unsigned32, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter64", "Unsigned32", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "Bits")
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

mibBuilder.exportSymbols("PerfHist-TC-MIB", perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount, PerfIntervalCount=PerfIntervalCount, PYSNMP_MODULE_ID=perfHistTCMIB, PerfCurrentCount=PerfCurrentCount)
