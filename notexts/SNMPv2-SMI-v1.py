#
# PySNMP MIB module SNMPv2-SMI-v1 (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/SNMPv2-SMI-v1
# Produced by pysmi-1.1.12 at Tue Sep 17 13:28:23 2024
# On host fv-az883-167 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, IpAddress, Counter64, TimeTicks, Integer32, NotificationType, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "iso", "Gauge32")
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
mibBuilder.exportSymbols("SNMPv2-SMI-v1", directory=directory, Unsigned_32=Unsigned_32, snmpDomains=snmpDomains, mgmt=mgmt, private=private, Counter_32=Counter_32, Gauge_32=Gauge_32, internet=internet, enterprises=enterprises, security=security, snmpProxys=snmpProxys, snmpModules=snmpModules, experimental=experimental, Integer_32=Integer_32, snmpV2=snmpV2)
