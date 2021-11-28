#
# PySNMP MIB module ADSL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ADSL-TC-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 14:10:43 2021
# On host fv-az39-900 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, Gauge32, Bits, TimeTicks, iso, Counter32, ObjectIdentity, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Integer32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Gauge32", "Bits", "TimeTicks", "iso", "Counter32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Integer32", "Unsigned32", "NotificationType")
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

mibBuilder.exportSymbols("ADSL-TC-MIB", adsltcmib=adsltcmib, AdslPerfPrevDayCount=AdslPerfPrevDayCount, AdslLineCodingType=AdslLineCodingType, PYSNMP_MODULE_ID=adsltcmib, AdslPerfCurrDayCount=AdslPerfCurrDayCount, AdslPerfTimeElapsed=AdslPerfTimeElapsed)
