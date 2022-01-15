#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ADSL-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:26 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
transmission, Counter64, Counter32, ObjectIdentity, TimeTicks, Gauge32, Integer32, MibIdentifier, NotificationType, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "transmission", "Counter64", "Counter32", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "MibIdentifier", "NotificationType", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adsltcmib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 94, 2))
adsltcmib.setRevisions(('1999-08-19 00:00',))
if mibBuilder.loadTexts: adsltcmib.setLastUpdated('9908190000Z')
if mibBuilder.loadTexts: adsltcmib.setOrganization('IETF ADSL MIB Working Group')
class AdslLineCodingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("dmt", 2), ("cap", 3), ("qam", 4))

class AdslPerfCurrDayCount(TextualConvention, Gauge32):
    status = 'current'

class AdslPerfPrevDayCount(TextualConvention, Gauge32):
    status = 'current'

class AdslPerfTimeElapsed(TextualConvention, Gauge32):
    status = 'current'

mibBuilder.exportSymbols("ADSL-TC-MIB", AdslPerfTimeElapsed=AdslPerfTimeElapsed, PYSNMP_MODULE_ID=adsltcmib, adsltcmib=adsltcmib, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslLineCodingType=AdslLineCodingType, AdslPerfCurrDayCount=AdslPerfCurrDayCount)
