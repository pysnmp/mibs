#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ADSL-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:04:42 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, IpAddress, Bits, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, Counter64, transmission, Gauge32, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "IpAddress", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "Counter64", "transmission", "Gauge32", "NotificationType", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("ADSL-TC-MIB", AdslPerfCurrDayCount=AdslPerfCurrDayCount, adsltcmib=adsltcmib, AdslPerfTimeElapsed=AdslPerfTimeElapsed, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslLineCodingType=AdslLineCodingType, PYSNMP_MODULE_ID=adsltcmib)
