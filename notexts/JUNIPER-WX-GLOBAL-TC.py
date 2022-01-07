#
# PySNMP MIB module JUNIPER-WX-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-WX-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:15:43 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
jnxWxModules, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-REG", "jnxWxModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32, Unsigned32, Bits, ModuleIdentity, Counter32, IpAddress, MibIdentifier, Counter64, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32", "Unsigned32", "Bits", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxWxGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 2))
jnxWxGlobalTcModule.setRevisions(('2006-06-08 18:00', '2005-05-09 10:10', '2004-03-15 14:00', '2003-06-26 20:00', '2002-11-07 19:00', '2001-07-29 22:00',))
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: jnxWxGlobalTcModule.setOrganization('Juniper Networks, Inc')
class TcAppName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcQosIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '24a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 24)

class TcChassisType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("jnxWxOther", 1), ("jnxWx50", 2), ("jnxWx20", 3), ("jnxWx80", 4), ("jnxWx100", 5), ("jnxWxc500", 6), ("jnxWx15", 7), ("jnxWxc250", 8), ("jnxWx100V3", 9), ("jnxWx60", 10), ("jnxWxc590", 11), ("jnxIsm200Wxc", 12), ("jnxWxc1800", 13), ("jnxWxc2600", 14), ("jnxWxc3400", 15))

mibBuilder.exportSymbols("JUNIPER-WX-GLOBAL-TC", PYSNMP_MODULE_ID=jnxWxGlobalTcModule, TcChassisType=TcChassisType, TcAppName=TcAppName, jnxWxGlobalTcModule=jnxWxGlobalTcModule, TcQosIdentifier=TcQosIdentifier)
