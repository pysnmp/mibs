#
# PySNMP MIB module WISI-TANGRAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-TANGRAM-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:12:56 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Counter32, Gauge32, NotificationType, iso, ObjectIdentity, Unsigned32, TimeTicks, MibIdentifier, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Counter32", "Gauge32", "NotificationType", "iso", "ObjectIdentity", "Unsigned32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tangram, = mibBuilder.importSymbols("WISI-ROOT-MIB", "tangram")
tangramMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 0))
tangramMIB.setRevisions(('2016-09-08 00:00', '2014-04-29 00:00', '2012-12-06 09:00', '2012-10-31 00:00', '2011-12-13 00:00', '2011-04-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tangramMIB.setRevisionsDescriptions(('Fixed parse warnings. Updated contact information.', "Add oid 'gtTS'.", 'Fixed compile errors.', 'Changes: Initial Chameleon support.', 'Changes: Updated MIBs to revision 12 for GT22ex.', 'Initial Version',))
if mibBuilder.loadTexts: tangramMIB.setLastUpdated('201609080000Z')
if mibBuilder.loadTexts: tangramMIB.setOrganization('WISI Communications GmbH & Co. KG')
if mibBuilder.loadTexts: tangramMIB.setContactInfo('https://wisiconnect.tv/')
if mibBuilder.loadTexts: tangramMIB.setDescription('This MIB comprises all base OIDs of Tangram-related MIBs.')
gtUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1))
gtGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4))
gtGenericNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0))
gtGenericObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1))
gtGenericNotifyUsertrap = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0, 1))
if mibBuilder.loadTexts: gtGenericNotifyUsertrap.setStatus('current')
if mibBuilder.loadTexts: gtGenericNotifyUsertrap.setDescription('The gtGenericNotifyUsertrap notification is raised by a user event.')
gtGenericObjectUsertrap = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtGenericObjectUsertrap.setStatus('current')
if mibBuilder.loadTexts: gtGenericObjectUsertrap.setDescription('The gtGenericObjectUsertrap contain the latest data sent with a user event.')
gtStandards = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4))
gtIP = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 1))
gtRF = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 3))
gtDVB = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 4))
gtTS = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 5))
gtProcessing = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 6))
class FloatingPoint(TextualConvention, OctetString):
    description = "\n\t\tFloatingPoint provides a way of representing non-integer\n\t\tnumbers in SNMP. Numbers are represented as a string of\n\t\tASCII characters in the natural way. So for example, '3',\n\t\t'3.142' and '0.3142E1' are all valid numbers.\n\n\t\tThe syntax for the string is as follows.  [] enclose an\n\t\toptional element, | is the separator for a set of\n\t\talternatives.  () enclose syntax which is to be viewed\n\t\tas a unit.\n\n\t\tFloatingPoint ::= [Sign]\n\t\t(Float1 | Float2 | DigitSequence)\n\t\t[ExponentPart]\n\n\t\tFloat1        ::= DigitSequence '.' [DigitSequence]\n\t\tFloat2        ::= '.' DigitSequence\n\t\tDigitSequence ::= Digit [DigitSequence]\n\n\t\tExponentPart  ::= ('e' | 'E') [Sign] DigitSequence\n\n\t\tDigit         ::= '0'..'9'\n\t\tSign          ::= '+' | '-'\n\t\t"
    status = 'current'
    displayHint = '63a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

mibBuilder.exportSymbols("WISI-TANGRAM-MIB", gtGenericNotifyUsertrap=gtGenericNotifyUsertrap, gtGenericObjectUsertrap=gtGenericObjectUsertrap, gtStandards=gtStandards, FloatingPoint=FloatingPoint, gtGeneric=gtGeneric, tangramMIB=tangramMIB, PYSNMP_MODULE_ID=tangramMIB, gtGenericObjects=gtGenericObjects, gtRF=gtRF, gtTS=gtTS, gtIP=gtIP, gtDVB=gtDVB, gtProcessing=gtProcessing, gtUnit=gtUnit, gtGenericNotifications=gtGenericNotifications)
