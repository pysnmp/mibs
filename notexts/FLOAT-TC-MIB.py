#
# PySNMP MIB module FLOAT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/FLOAT-TC-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:43:33 2021
# On host fv-az135-192 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, mib_2, Counter32, IpAddress, MibIdentifier, Counter64, Gauge32, NotificationType, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "mib-2", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "NotificationType", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
floatTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 201))
floatTcMIB.setRevisions(('2011-07-27 00:00',))
if mibBuilder.loadTexts: floatTcMIB.setLastUpdated('201107270000Z')
if mibBuilder.loadTexts: floatTcMIB.setOrganization('IETF OPSAWG Working Group')
class Float32TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic, Standard 754-2008'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class Float64TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic, Standard 754-2008'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Float128TC(TextualConvention, OctetString):
    reference = 'IEEE Standard for Floating-Point Arithmetic, Standard 754-2008'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

mibBuilder.exportSymbols("FLOAT-TC-MIB", floatTcMIB=floatTcMIB, PYSNMP_MODULE_ID=floatTcMIB, Float32TC=Float32TC, Float128TC=Float128TC, Float64TC=Float64TC)
