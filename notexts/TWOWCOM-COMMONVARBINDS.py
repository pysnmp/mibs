#
# PySNMP MIB module TWOWCOM-COMMONVARBINDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-COMMONVARBINDS
# Produced by pysmi-1.1.12 at Tue May 28 12:02:28 2024
# On host fv-az1490-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, Counter64, Unsigned32, Integer32, ModuleIdentity, Bits, MibIdentifier, Counter32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "Integer32", "ModuleIdentity", "Bits", "MibIdentifier", "Counter32", "iso", "NotificationType")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
twowcom, = mibBuilder.importSymbols("TWOWCOM-SMI", "twowcom")
commonVarbinds = ModuleIdentity((1, 3, 6, 1, 4, 1, 21529, 11, 1))
commonVarbinds.setRevisions(('2011-05-26 12:00', '2010-02-17 16:00', '2009-02-06 13:30', '2008-04-28 15:17', '2008-03-26 15:36', '2007-04-26 08:52', '2006-10-26 16:13',))
if mibBuilder.loadTexts: commonVarbinds.setLastUpdated('201105261200Z')
if mibBuilder.loadTexts: commonVarbinds.setOrganization('2wcom GmbH')
class Integer32d(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class Integer32d1(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class Integer32d2(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class Integer32d3(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class Integer32h(TextualConvention, Integer32):
    reference = 'Interger32 hex'
    status = 'current'
    displayHint = 'x'

class ValidFlag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class ActiveNotActive(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notActive", 0), ("active", 1))

class SelectOnOff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("on", 1), ("off", 2))

class FaultOK(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fault", 1), ("ok", 2))

class SelectYesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FloatString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d1dEE1a1d1d'

class Unsigned16x(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = '4x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

common = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 11))
commonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21529, 11, 1, 1)).setObjects(("TWOWCOM-COMMONVARBINDS", "eventTimeStamp"), ("TWOWCOM-COMMONVARBINDS", "eventPriority"), ("TWOWCOM-COMMONVARBINDS", "eventCounter"), ("TWOWCOM-COMMONVARBINDS", "mibRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    commonGroup = commonGroup.setStatus('current')
eventTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
eventPriority = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPriority.setStatus('current')
eventCounter = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCounter.setStatus('current')
mibRelease = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibRelease.setStatus('current')
mibBuilder.exportSymbols("TWOWCOM-COMMONVARBINDS", FloatString=FloatString, FaultOK=FaultOK, Integer32d2=Integer32d2, common=common, Integer32d3=Integer32d3, eventPriority=eventPriority, SelectOnOff=SelectOnOff, ValidFlag=ValidFlag, Unsigned16x=Unsigned16x, Integer32d=Integer32d, eventCounter=eventCounter, mibRelease=mibRelease, SelectYesNo=SelectYesNo, ActiveNotActive=ActiveNotActive, Integer32h=Integer32h, eventTimeStamp=eventTimeStamp, Integer32d1=Integer32d1, commonGroup=commonGroup, commonVarbinds=commonVarbinds, PYSNMP_MODULE_ID=commonVarbinds)
