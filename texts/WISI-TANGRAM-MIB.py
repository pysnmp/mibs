#
# PySNMP MIB module WISI-TANGRAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-TANGRAM-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 09:01:15 2024
# On host fv-az1149-759 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, MibIdentifier, Bits, ModuleIdentity, Gauge32, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "ModuleIdentity", "Gauge32", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Integer32", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("WISI-TANGRAM-MIB", gtGenericNotifications=gtGenericNotifications, gtDVB=gtDVB, gtIP=gtIP, gtGenericObjectUsertrap=gtGenericObjectUsertrap, gtRF=gtRF, FloatingPoint=FloatingPoint, gtStandards=gtStandards, gtProcessing=gtProcessing, gtGenericNotifyUsertrap=gtGenericNotifyUsertrap, gtTS=gtTS, tangramMIB=tangramMIB, PYSNMP_MODULE_ID=tangramMIB, gtGenericObjects=gtGenericObjects, gtGeneric=gtGeneric, gtUnit=gtUnit)
