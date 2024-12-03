#
# PySNMP MIB module FLOAT-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/FLOAT-TC-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:46:15 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, TimeTicks, Gauge32, Integer32, mib_2, MibIdentifier, iso, IpAddress, Bits, Counter32, Counter64, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "mib-2", "MibIdentifier", "iso", "IpAddress", "Bits", "Counter32", "Counter64", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("FLOAT-TC-MIB", Float64TC=Float64TC, Float32TC=Float32TC, floatTcMIB=floatTcMIB, PYSNMP_MODULE_ID=floatTcMIB, Float128TC=Float128TC)
