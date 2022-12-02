#
# PySNMP MIB module SNMPv2-SMI-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMPv2-SMI-v1
# Produced by pysmi-1.1.8 at Fri Dec  2 17:06:48 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Bits, NotificationType, iso, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "NotificationType", "iso", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Integer32", "ObjectIdentity")
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
mibBuilder.exportSymbols("SNMPv2-SMI-v1", mgmt=mgmt, snmpModules=snmpModules, directory=directory, private=private, experimental=experimental, security=security, snmpProxys=snmpProxys, Gauge_32=Gauge_32, Counter_32=Counter_32, internet=internet, Integer_32=Integer_32, Unsigned_32=Unsigned_32, enterprises=enterprises, snmpV2=snmpV2, snmpDomains=snmpDomains)
