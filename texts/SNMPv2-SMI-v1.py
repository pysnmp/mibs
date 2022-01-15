#
# PySNMP MIB module SNMPv2-SMI-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMPv2-SMI-v1
# Produced by pysmi-1.1.8 at Sat Jan 15 04:27:53 2022
# On host fv-az83-73 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, iso, IpAddress, Bits, NotificationType, Counter64, Gauge32, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "iso", "IpAddress", "Bits", "NotificationType", "Counter64", "Gauge32", "Integer32", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SNMPv2-SMI-v1", experimental=experimental, snmpModules=snmpModules, Counter_32=Counter_32, Gauge_32=Gauge_32, snmpProxys=snmpProxys, Integer_32=Integer_32, private=private, internet=internet, snmpV2=snmpV2, security=security, enterprises=enterprises, snmpDomains=snmpDomains, mgmt=mgmt, directory=directory, Unsigned_32=Unsigned_32)
