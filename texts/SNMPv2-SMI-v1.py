#
# PySNMP MIB module SNMPv2-SMI-v1 (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/SNMPv2-SMI-v1
# Produced by pysmi-1.1.12 at Thu Nov 28 02:57:21 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, IpAddress, iso, Integer32, Counter64, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "IpAddress", "iso", "Integer32", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Counter_32(Counter32):
    pass

class Gauge_32(Gauge32):
    pass

class Integer_32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class Unsigned_32(Gauge32):
    pass

internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
security = MibIdentifier((1, 3, 6, 1, 5))
snmpV2 = MibIdentifier((1, 3, 6, 1, 6))
snmpDomains = MibIdentifier((1, 3, 6, 1, 6, 1))
snmpProxys = MibIdentifier((1, 3, 6, 1, 6, 2))
snmpModules = MibIdentifier((1, 3, 6, 1, 6, 3))
mibBuilder.exportSymbols("SNMPv2-SMI-v1", snmpModules=snmpModules, Integer_32=Integer_32, Unsigned_32=Unsigned_32, Counter_32=Counter_32, Gauge_32=Gauge_32, private=private, experimental=experimental, snmpV2=snmpV2, snmpDomains=snmpDomains, directory=directory, mgmt=mgmt, internet=internet, enterprises=enterprises, security=security, snmpProxys=snmpProxys)
