#
# PySNMP MIB module OPENBSD-SNMPD-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SNMPD-CONF
# Produced by pysmi-1.1.12 at Wed Jul  3 09:59:36 2024
# On host fv-az530-296 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dBridge, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBridge")
hostResourcesMibModule, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hostResourcesMibModule")
ianaifType, = mibBuilder.importSymbols("IANAifType-MIB", "ianaifType")
ifMIB, = mibBuilder.importSymbols("IF-MIB", "ifMIB")
inetAddressMIB, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "inetAddressMIB")
ipForward, = mibBuilder.importSymbols("IP-FORWARD-MIB", "ipForward")
ipMIB, = mibBuilder.importSymbols("IP-MIB", "ipMIB")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
carpMIBObjects, = mibBuilder.importSymbols("OPENBSD-CARP-MIB", "carpMIBObjects")
memMIBObjects, = mibBuilder.importSymbols("OPENBSD-MEM-MIB", "memMIBObjects")
pfMIBObjects, = mibBuilder.importSymbols("OPENBSD-PF-MIB", "pfMIBObjects")
sensorsMIBObjects, = mibBuilder.importSymbols("OPENBSD-SENSORS-MIB", "sensorsMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpMIB, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpMIB")
TimeTicks, NotificationType, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, ObjectIdentity, Counter32, iso, Unsigned32, ModuleIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "ModuleIdentity", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
