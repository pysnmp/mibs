#
# PySNMP MIB module JUNIPER-WX-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-WX-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:22 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
jnxWxModules, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-REG", "jnxWxModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Unsigned32, Bits, Counter32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Unsigned32", "Bits", "Counter32", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxWxGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 2))
jnxWxGlobalTcModule.setRevisions(('2006-06-08 18:00', '2005-05-09 10:10', '2004-03-15 14:00', '2003-06-26 20:00', '2002-11-07 19:00', '2001-07-29 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxWxGlobalTcModule.setRevisionsDescriptions(('\n\t\t\tUpdate contact and MIB with Juniper information\n\t\t\tAdd wxc590 and wx60 chassis type.', '\n\t\t\tAdd wxc250 chassis type.', '\n\t\t\tAdd wx100 chassis type.', '\n\t\t\tAdd wx80 chassis type.', '\n\t\t\tAdd wx20 chassis type.', '\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module JUNIPER-WX-GLOBAL-TC.',))
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setOrganization('Juniper Networks, Inc')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tJuniper Networks, Inc.\n\t\t\t\t\t1194 North Mathilda Avenue\n\t\t\t\t\tSunnyvale, CA  94089\n\n\t\t\t\t\t+1 888-314-JTAC\n\t\t\t\t\tsupport@juniper.net')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setDescription("\n\t\t\tA MIB module containing textual conventions\n\t\t\tfor Juniper Networks' enterprise MIB modules.\n\t\t\tThese textual conventions are used across all WX products.")
class TcAppName(TextualConvention, OctetString):
    description = "\n\t\t\tRepresents the name of an application.\n\n\t\t\tThis has all the restrictions of the DisplayString textual\n\t\t\tconvention with the following additional ones:\n\n\t\t\t- Only the following characters/character ranges are allowed:\n\t\t\t\t0-9\n\t\t\t\tA-Z\n\t\t\t\ta-z\n\t\t\t\t:./#$&_-+()'\n\t\t\t\t<space>\n\n\t\t\tAny object defined using this syntax may not exceed 64\n\t\t\tcharacters in length."
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcQosIdentifier(TextualConvention, OctetString):
    description = "\n\t\t\tRepresents the name of a QoS class, a tunnel or\n\t\t\ta tunnel ip address encoded as a string.\n\n\t\t\tThis has all the restrictions of the DisplayString textual\n\t\t\tconvention with the following additional ones:\n\n\t\t\t- Only the following characters/character ranges are allowed:\n\t\t\t\t0-9\n\t\t\t\tA-Z\n\t\t\t\ta-z\n\t\t\t\t:./#$&_-+()'\n\t\t\t\t<space>\n\n\t\t\tAny object defined using this syntax may not exceed 24\n\t\t\tcharacters in length."
    status = 'current'
    displayHint = '24a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 24)

class TcChassisType(TextualConvention, Integer32):
    description = '\n\t\t\tEnumerates all possible chassis types for WX devices.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("jnxWxOther", 1), ("jnxWx50", 2), ("jnxWx20", 3), ("jnxWx80", 4), ("jnxWx100", 5), ("jnxWxc500", 6), ("jnxWx15", 7), ("jnxWxc250", 8), ("jnxWx100V3", 9), ("jnxWx60", 10), ("jnxWxc590", 11), ("jnxIsm200Wxc", 12), ("jnxWxc1800", 13), ("jnxWxc2600", 14), ("jnxWxc3400", 15))

mibBuilder.exportSymbols("JUNIPER-WX-GLOBAL-TC", TcAppName=TcAppName, TcQosIdentifier=TcQosIdentifier, PYSNMP_MODULE_ID=jnxWxGlobalTcModule, TcChassisType=TcChassisType, jnxWxGlobalTcModule=jnxWxGlobalTcModule)
