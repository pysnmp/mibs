#
# PySNMP MIB module FLOAT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/FLOAT-TC-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 10:08:58 2024
# On host fv-az1771-969 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, iso, TimeTicks, Counter64, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, Gauge32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "iso", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Gauge32", "ModuleIdentity", "Bits")
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

mibBuilder.exportSymbols("FLOAT-TC-MIB", PYSNMP_MODULE_ID=floatTcMIB, Float128TC=Float128TC, floatTcMIB=floatTcMIB, Float32TC=Float32TC, Float64TC=Float64TC)
