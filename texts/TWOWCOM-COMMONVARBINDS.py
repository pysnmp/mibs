#
# PySNMP MIB module TWOWCOM-COMMONVARBINDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2wcom/TWOWCOM-COMMONVARBINDS
# Produced by pysmi-1.1.12 at Mon Oct  7 02:23:03 2024
# On host fv-az1986-495 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, ModuleIdentity, Gauge32, Integer32, IpAddress, TimeTicks, Counter32, MibIdentifier, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "ModuleIdentity", "Gauge32", "Integer32", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier", "ObjectIdentity", "NotificationType")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
twowcom, = mibBuilder.importSymbols("TWOWCOM-SMI", "twowcom")
commonVarbinds = ModuleIdentity((1, 3, 6, 1, 4, 1, 21529, 11, 1))
commonVarbinds.setRevisions(('2011-05-26 12:00', '2010-02-17 16:00', '2009-02-06 13:30', '2008-04-28 15:17', '2008-03-26 15:36', '2007-04-26 08:52', '2006-10-26 16:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: commonVarbinds.setRevisionsDescriptions(('Version 0.7\r\n\t\t\t\t- removed commonVarbindsCompliance (1.3.6.1.4.1.21529.11.1.10)', 'Version 0.6\r\n\t\t\t\t- new Textual convention: Unsigned16x', 'Version 0.5\r\n\t\t\t\t- new Textual convention: Integer32d3', "Version 0.4\r\n\t\t\t\t- syntax chanded in the textual convention 'ValidFlag' object: \r\n\t\t\t\t\told: 0 -> yes; 1 -> no\r\n\t\t\t\t\tnew: 0 -> undefined; 1 -> no; 2 -> yes", 'Version 0.3\r\n\t\t\t\t- new Textual convention: FloatString', 'Version 0.2\r\n\t\t\t\t- new Textual convention: SelectOnOff\r\n\t\t\t\t- new Textual convention: FaultOK', 'Version 0.1',))
if mibBuilder.loadTexts: commonVarbinds.setLastUpdated('201105261200Z')
if mibBuilder.loadTexts: commonVarbinds.setOrganization('2wcom GmbH')
if mibBuilder.loadTexts: commonVarbinds.setContactInfo('2wcom GmbH\r\n\t\t\t\tc/o Martin Hoppe\r\n\t\t\t\tLise-Meitner-Str. 4\r\n\t\t\t\t24941 Flensburg\r\n\t\t\t\tGermany\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\tTel: +49 461 662830-35\r\n\t\t\t\tFax: +49 461 662830-11\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\tWEB: www.2wcom.com')
if mibBuilder.loadTexts: commonVarbinds.setDescription('Description:\r\n\t\t\t\t\r\n\t\t\t\tCommon values')
class Integer32d(TextualConvention, Integer32):
    description = 'Interger32 dezimal mit keiner Nachkommastelle dargestellt.\r\n\t\t\t\tWert: 123      Darstellung:123'
    status = 'current'
    displayHint = 'd'

class Integer32d1(TextualConvention, Integer32):
    description = 'Interger32 dezimal mit einer Nachkommastelle dargestellt.\r\n\t\t\t\tWert: 123      Darstellung:12.3'
    status = 'current'
    displayHint = 'd-1'

class Integer32d2(TextualConvention, Integer32):
    description = 'Interger32 dezimal mit zwei Nachkommastellen dargestellt.\r\n\t\t\t\tWert: 123      Darstellung:1.23'
    status = 'current'
    displayHint = 'd-2'

class Integer32d3(TextualConvention, Integer32):
    description = 'Interger32 dezimal mit drei Nachkommastellen dargestellt.\r\n\t\t\t\tWert: 93200      Darstellung: 93.200'
    status = 'current'
    displayHint = 'd-3'

class Integer32h(TextualConvention, Integer32):
    reference = 'Interger32 hex'
    description = 'Wert in hex darstellen'
    status = 'current'
    displayHint = 'x'

class ValidFlag(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class ActiveNotActive(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("notActive", 0), ("active", 1))

class SelectOnOff(TextualConvention, Integer32):
    description = 'Description. On/Off selection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("on", 1), ("off", 2))

class FaultOK(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fault", 1), ("ok", 2))

class SelectYesNo(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FloatString(TextualConvention, OctetString):
    description = 'Description.'
    status = 'current'
    displayHint = '1d.1d1dEE1a1d1d'

class Unsigned16x(TextualConvention, Unsigned32):
    description = 'Description.'
    status = 'current'
    displayHint = '4x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

common = MibIdentifier((1, 3, 6, 1, 4, 1, 21529, 11))
commonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21529, 11, 1, 1)).setObjects(("TWOWCOM-COMMONVARBINDS", "eventTimeStamp"), ("TWOWCOM-COMMONVARBINDS", "eventPriority"), ("TWOWCOM-COMMONVARBINDS", "eventCounter"), ("TWOWCOM-COMMONVARBINDS", "mibRelease"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    commonGroup = commonGroup.setStatus('current')
if mibBuilder.loadTexts: commonGroup.setDescription('Description.')
eventTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
if mibBuilder.loadTexts: eventTimeStamp.setDescription('Description.')
eventPriority = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPriority.setStatus('current')
if mibBuilder.loadTexts: eventPriority.setDescription('Description.')
eventCounter = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCounter.setStatus('current')
if mibBuilder.loadTexts: eventCounter.setDescription('Description.')
mibRelease = MibScalar((1, 3, 6, 1, 4, 1, 21529, 11, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibRelease.setStatus('current')
if mibBuilder.loadTexts: mibRelease.setDescription('Description.')
mibBuilder.exportSymbols("TWOWCOM-COMMONVARBINDS", FaultOK=FaultOK, SelectYesNo=SelectYesNo, SelectOnOff=SelectOnOff, eventTimeStamp=eventTimeStamp, Integer32d=Integer32d, ActiveNotActive=ActiveNotActive, PYSNMP_MODULE_ID=commonVarbinds, Integer32d3=Integer32d3, FloatString=FloatString, Integer32h=Integer32h, common=common, ValidFlag=ValidFlag, mibRelease=mibRelease, Integer32d1=Integer32d1, eventPriority=eventPriority, eventCounter=eventCounter, commonGroup=commonGroup, Unsigned16x=Unsigned16x, Integer32d2=Integer32d2, commonVarbinds=commonVarbinds)
