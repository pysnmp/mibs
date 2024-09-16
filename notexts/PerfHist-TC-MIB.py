#
# PySNMP MIB module PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/PerfHist-TC-MIB
# Produced by pysmi-1.1.12 at Mon Sep 16 14:52:03 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Gauge32, MibIdentifier, Counter64, NotificationType, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, mib_2, TimeTicks, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "mib-2", "TimeTicks", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("PerfHist-TC-MIB", PerfCurrentCount=PerfCurrentCount, PerfIntervalCount=PerfIntervalCount, PYSNMP_MODULE_ID=perfHistTCMIB, perfHistTCMIB=perfHistTCMIB, PerfTotalCount=PerfTotalCount)
